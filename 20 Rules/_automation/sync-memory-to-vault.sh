#!/bin/zsh
# Vault ingest — runs every 30 min via launchd com.aexgee.memory-vault-sync
#   1) Claude Code memory -> "30 Claude Memory" (Thai display names, self-healing)
#   2) Meeting-notes repo  -> "40 Meeting Notes"
#   3) Auto-commit the vault so every sync is recoverable (git rollback)
set -u

VAULT="$HOME/SecondBrain"
LOG="$HOME/Library/Logs/secondbrain-sync.log"
mkdir -p "$(dirname "$LOG")"

log() { print -r -- "$(date '+%F %T') $*" >>"$LOG"; }

log "=== sync start ==="

# 1) memory -> vault. The Python writes its own info lines to $LOG; here we only
#    capture stderr (crashes/tracebacks) so normal output isn't logged twice.
if /usr/bin/python3 "$HOME/bin/sync-memory-to-vault.py" 2>>"$LOG"; then
  log "memory sync ok"
else
  log "ERROR: memory sync failed (exit $?)"
fi

# 2) meeting-notes repo -> "40 Meeting Notes"
# Guarded rsync: only mirror-with-delete when the SOURCE actually has files,
# so a broken/empty git pull can never wipe the vault copy.
MN="$HOME/meeting-notes"
VMN="$VAULT/40 Meeting Notes"
mirror() {  # mirror <src> <dst>
  local src="$1" dst="$2"
  if [[ -d "$src" ]] && [[ -n "$(find "$src" -type f -print -quit 2>/dev/null)" ]]; then
    mkdir -p "$dst"
    /usr/bin/rsync -a --delete "$src/" "$dst/" && log "mirrored $src -> $dst"
  else
    log "SKIP mirror: source empty/missing ($src) — refusing --delete to protect vault"
  fi
}
if [[ -d "$MN/.git" ]]; then
  /usr/bin/git -C "$MN" pull --quiet --ff-only 2>>"$LOG" || log "WARN: meeting-notes git pull failed"
  mirror "$MN/notes" "$VMN/notes"
  mirror "$MN/quotations" "$VMN/quotations"
else
  log "SKIP meeting-notes: $MN/.git not found"
fi

# 3) auto-commit the vault (versioning + rollback). Skips cleanly when nothing changed.
if [[ -d "$VAULT/.git" ]]; then
  /usr/bin/git -C "$VAULT" add -A 2>>"$LOG"
  if ! /usr/bin/git -C "$VAULT" diff --cached --quiet 2>/dev/null; then
    /usr/bin/git -C "$VAULT" commit -q -m "auto-sync $(date '+%F %H:%M')" 2>>"$LOG" \
      && log "committed vault changes" || log "WARN: vault commit failed"
  else
    log "no vault changes to commit"
  fi

  # 4) push to off-machine backup (private GitHub). Pushes any unpushed commits, so
  #    a commit stranded by an earlier offline run gets flushed on the next sync.
  if /usr/bin/git -C "$VAULT" remote get-url origin >/dev/null 2>&1; then
    if [[ -n "$(/usr/bin/git -C "$VAULT" log '@{u}..HEAD' --oneline 2>/dev/null)" ]]; then
      if /usr/bin/git -C "$VAULT" push --quiet origin HEAD 2>>"$LOG"; then
        log "pushed to origin"
      else
        log "WARN: push failed (offline?) — commits safe locally, will retry next sync"
      fi
    else
      log "origin up to date"
    fi
  fi
fi

log "=== sync done ==="
