# Blazing Tails — Replit Import Notes

## What This Project Is
AI character pipeline — generates 84 unique AI model personas per month (12 models × 7 user groups = 1,008 characters/year). Outputs structured JSON per character.

## Stack Rules (non-negotiable)
- Python 3 only
- AI generation: claude-sonnet-4-6 via Anthropic API
- Output: JSON files in `characters/cycle-NNN/` format
- Deploy/hosting: Coolify self-hosted (never Vercel)
- Static frontend (if built): Cloudflare Pages

## Current State
- `generate_characters.py` — main generation script
- `README.md` — full spec (12 models, 7 groups, monthly cycle)
- `CPaintingServices-improvements.md` — unrelated file, can ignore

## Usage
```bash
python generate_characters.py --model "Claude Opus" --group "Creators" --cycle 1
# Output: characters/cycle-001/claude-opus-creators.json
```

## Improvements Roadmap
- [ ] Batch generation: run all 84 characters in one command (`--cycle N --all`)
- [ ] Add progress bar / cost estimate before full run
- [ ] Web UI to browse generated characters (static Cloudflare Pages)
- [ ] Character diff view: compare same model/group across cycles to show evolution
- [ ] Export to Notion database via API
- [ ] GitHub Action to auto-generate on 1st of each month

## Known Issues
- `CPaintingServices-improvements.md` in root is leftover from another project — safe to delete
