# dev-guides Memory

> AI Context File - Read this first for project state

## Last Updated
2026-02-04

## Current State
Active Development

Project initialized with full file structure. First guide (Oracle Free Server) is complete and published.

## What Exists
- `index.html` - Landing page with 4 guide cards (1 live, 3 placeholders)
- `assets/css/shared-styles.css` - Full design system (dark mode, components)
- `templates/guide-template.html` - Reusable blueprint for new guides
- `guides/oracle-free-server/index.html` - First complete guide
- `.github/workflows/deploy.yml` - Auto-deploy to GitHub Pages
- `README.md` - Repo documentation
- `FOLDER_STRUCTURE.txt` - Directory overview

## Key Decisions Made
1. **Design**: Premium dark mode, Indigo accent (#6366f1), Inter font, minimal/clean aesthetic
2. **Structure**: Each guide in `/guides/{slug}/index.html`
3. **Target Audience**: Indian devs, startups, technical founders
4. **Tone**: Practical, no-BS, professional (no emojis)
5. **CTA**: "DM me for consulting" on every page

## Next Steps
- [x] **UI REFACTOR (High Priority)**: Fix "Uncle's WhatsApp / Bollywood poster" vibe.
- [x] Push to GitHub and enable Pages.
- [ ] Replace placeholder social links (Twitter, email)

## Known Issues
- **Social links**: All social media handles in the code (e.g., footers) are placeholders or need verification against `@krishamaze`.
- **Infrastructure**: Verify that GitHub Pages is correctly pointed to the `main` branch output.

## Files to Ignore
- `scratch/` - Temp work
- `archive/` - Old versions
- `node_modules/` - If any build tools added later

## Quick Commands
```bash
# Preview locally
python -m http.server 8000

# Deploy (just push to main)
git add . && git commit -m "refactor: premium minimal UI" && git push
```

## Session Notes
### 2026-02-04: Project Created
- Generated complete file structure
- Created Oracle Free Server guide with Indian pricing context
- Set up GitHub Actions for auto-deploy
- Moved to PARA structure: `~/projects/1_PROJECTS/dev-guides/`

### 2026-02-04: UI Refactor Complete
Changes made to fix the "Uncle's WhatsApp / Bollywood poster" aesthetic:

**index.html**
- Removed ALL emojis (was: 17+ emojis scattered everywhere)
- Replaced emoji icons with clean SVG icons for guide cards
- Simplified hero section - cleaner headline, no badge emojis
- Removed flashy glow/gradient overlays
- Added proper logo mark (gradient "D" box) instead of emoji favicon
- Cleaner stats section with simpler styling

**shared-styles.css**
- Darker, more refined background colors (#09090b base)
- Reduced accent glow opacity (0.15 instead of 0.3)
- Removed aggressive card hover transforms
- Simplified button hover states (no glow effects)
- Tighter letter-spacing for headlines
- Removed unnecessary animation keyframes

**guides/oracle-free-server/index.html**
- Stripped all section emojis from headings
- Cleaner callout boxes (removed emoji titles like "💡 Real World math")
- Updated copy button text (no clipboard emoji)
- Consistent footer with main site

**Result**: Clean, minimal, premium dark-mode aesthetic. Professional without being boring.
