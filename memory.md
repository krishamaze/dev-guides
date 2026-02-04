# dev-guides Memory

> AI Context File - Read this first for project state

## Last Updated
2026-02-04

## Current State
🟢 **Active Development**

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
1. **Design**: Dark mode, Indigo accent (#6366f1), Inter font
2. **Structure**: Each guide in `/guides/{slug}/index.html`
3. **Target Audience**: Indian devs, startups, technical founders
4. **Tone**: Practical, no-BS, conversational with emojis
5. **CTA**: "DM me for consulting" on every page

## Next Steps
- [ ] **UI REFACTOR (High Priority)**: Fix "Uncle's WhatsApp / Bollywood poster" vibe.
- [ ] Push to GitHub and enable Pages
- [ ] Replace placeholder social links (Twitter, email)

## 🤖 Remote Agent Handover
**Mission**: Refactor `assets/css/shared-styles.css` and `index.html` to achieve a minimalist, high-end premium aesthetic.

**Critical Feedback**:
- Current vibe: "Uncle's WhatsApp forward discovered stickers" / "Early 2000s Bollywood poster".
- Overdose of emojis: 💰 📚 🇮🇳 ☁️ ⚡.
- Strategy: Ruthlessly simplify. Use professional typography, subtle gradients, and generous white space. Move away from "vibrant/loud" to "clean/minimal".

**Authority**: You have full permission to rewrite the CSS and restructure the HTML. "Do the needful."

## Files to Ignore
- `scratch/` - Temp work
- `archive/` - Old versions
- `node_modules/` - If any build tools added later

## Quick Commands
```bash
# Preview locally
python -m http.server 8000

# Deploy (just push to main)
git add . && git commit -m "Update" && git push
```

## Session Notes
### 2026-02-04: Project Created
- Generated complete file structure
- Created Oracle Free Server guide with Indian pricing context
- Set up GitHub Actions for auto-deploy
- Moved to PARA structure: `~/projects/1_PROJECTS/dev-guides/`
