# Project: Dev Guides

## Objective
Provide practical, no-BS technical guides for Indian developers and startups, focusing on high-value cost savings and efficiency on cloud infrastructure. The goal is to build a collection of 5+ guides that save significant time and money for solo developers and small teams.

## Tech Stack
- Languages: HTML5, CSS3 (Vanilla), JavaScript (Vanilla)
- Tools: GitHub Actions (Auto-deployment), `python -m http.server` (Local development)
- Storage: Static Web Hosting (GitHub Pages)

## Architecture
```
[Content Source] -> [Templates/Shared Styles] -> [Static Build (Local/CI)] -> [GitHub Actions] -> [GitHub Pages]
      |                                              |                             |                  |
   HTML Files                                  shared-styles.css            Auto-minify/Check        Public URL
```

## File Structure
```
/home/ubuntu/projects/1_PROJECTS/dev-guides/
├── index.html                           # Main landing page & guide hub
├── assets/
│   └── css/
│       └── shared-styles.css            # Global design system & tokens
├── templates/
│   └── guide-template.html              # Blueprint for new guide creation
├── guides/
│   └── oracle-free-server/
│       └── index.html                   # First published guide (Oracle Cloud)
├── .github/
│   └── workflows/
│       └── deploy.yml                   # CI/CD deployment pipeline
├── README.md                            # Project documentation
└── memory.md                            # AI Context & Session history
```

## Implementation Status
### Completed
- **Project Infrastructure**: Full file structure initialized with PARA-style organization.
- **Design System**: Refactored to a premium, minimal dark-mode aesthetic (Indigo accent, Inter font, minimal glow).
- **Oracle Guide**: First complete guide (Oracle Free Server) published with Indian-market context (pricing in INR, card troubleshooting).
- **Deployment Pipeline**: GitHub Actions set up and site pushed to GitHub Pages.
- **Git Sync**: Successfully pushed to `https://github.com/krishamaze/dev-guides.git`.

### Pending
- [ ] **Social Media Audit**: Update all links in `index.html` and guide subpages to correct production handles.
- [ ] **New Guides**: Create coming-soon guides (GitHub Actions, Cloudflare Free Stack, Telegram Bots).

## Key Technical Patterns
### Premium Minimal UI Design
```css
:root {
  --bg-primary: #09090b;
  --accent-primary: #6366f1;
  --accent-glow: rgba(99, 102, 241, 0.15);
  /* Refined tokens to avoid "Uncle's WhatsApp" aesthetic */
}
```
**Rationale**: High-quality dark mode was chosen over default light themes to appeal to technical founders and developers, using subtle radial gradients and Inter typography for a "SaaS-like" professional feel.

### Reusable Content Components
```html
<div class="callout callout-info">
    <div class="callout-title">Real World Math</div>
    <p>{Savings calculation for Indian context}</p>
</div>
```
**Rationale**: Standardized callout boxes ensure consistency across different guides while maintaining a professional tone (replacing previous emoji-heavy headers).

## Production Commands
```bash
# Preview the static site locally
python -m http.server 8000

# Deploy updates (once git is connected)
git add . && git commit -m "feat: publish oracle guide" && git push origin main
```

## Known Issues
- **Social links**: All social media handles in the code (e.g., footers) are placeholders or need verification against `@krishamaze`.
- **Custom Links**: Verify that the Threads link `@kris.na.27` is the correct handle as per user requirements.

## Next Session Priorities
1. **Social Media Audit**: Update all links in `index.html` and guide subpages to correct production handles.
2. **Content Expansion**: Start the "Cloudflare Free Stack" guide using the established template.
