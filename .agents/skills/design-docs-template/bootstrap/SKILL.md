---
name: docs-template-bootstrap
description: >-
  Bootstraps a new design-docs repository from the GitHub template (RFC, ADR,
  arc42, Starlight) and leaves agent skills inside the new repo. Day-zero
  scaffolding — the user should not clone templates by hand. Invoked via
  design-docs-template.
---

# bootstrap — new docs repo

**What:** Create a docs project from the GitHub template; rebrand site config; ensure agent skills are present in the new repo.  
**When:** Day zero — empty idea, new product docs, “scaffold the docs stack.”  
**Not:** Writing architecture content; that comes after day-one pointers.

## Promise

The human installs **only this skill**, then runs bootstrap. You create the full repo (including `.cursor` / `.claude` / `.agents` skills). Do **not** ask them to clone the template manually.

## Process

### 1. Collect inputs

Ask only what is missing (one batch):

- **Project name** (folder + GitHub repo name)
- **Parent directory** (default: current workspace parent, or `~/Projects`)
- **Visibility** (`private` default)
- **GitHub owner** (user or org; default: authenticated `gh` user)
- **Site `base` path** (default: `/<repo-name>`)
- **Create GitHub remote?** (default **yes** — required for the polished path)
- **Template flavour** if not obvious:
  - `alessandroros/design-docs-template` (generic)
  - `openmove/engineering-design-playbook` (OpenMove)
  - If already inside one of those repos, use that remote’s template

### 2. Create the repo (GitHub template)

Default path — remote yes and `gh` available:

```bash
gh repo create <owner>/<name> --template <template-owner>/<template-repo> --private --clone
```

Use `--public` if they asked. `cd` into the clone.

The template **already includes** the skill trees. Confirm:

- `.cursor/skills/design-docs-template/SKILL.md`
- `.claude/skills/design-docs-template/SKILL.md`
- `.agents/skills/design-docs-template/SKILL.md`

If any path is missing, copy from the skill directory you are executing (parent of this `bootstrap/` folder) into all three destinations in the new repo.

**Fallback only** if `gh` / template create fails: tell them why, then offer (1) fix auth and retry, or (2) local copy from an existing template clone / `degit` of the template repo — never lead with (2).

Completion: working tree with `docs/`, `website/`, `README.md`, and the three skill paths.

### 3. Rebrand the site config

Edit `website/site.config.mjs` (or equivalent):

- `site` — Pages origin (ask if unknown; placeholder OK)
- `base` — `/<repo-name>` unless they chose otherwise
- `repoUrl` — the new GitHub URL

Update root `README.md` title/one-liner to the real project. Leave arc42/ADR/RFC templates intact; do not invent domain content.

### 4. Install and smoke-check

```bash
npm install --prefix website
npm run sync --prefix website   # if the script exists
```

Offer **preview** (or start dev) only if they want localhost now.

### 5. Day-one pointer

Fill later (do not fill unless asked):

1. arc42 §1 goals  
2. arc42 §3 + C4 context  
3. arc42 §4 strategy  
4. arc42 §5 + C4 containers  
5. first **new-adr** / **new-rfc** when trade-offs appear  

### 6. Hand off

Summarise: path, remote URL, `base`, that skills are already in the repo, next command (**preview** or start writing). No commit unless they ask.

## Hard rules

- Do not overwrite a non-empty project directory without explicit confirm.
- Do not invent ADRs/RFCs for the new domain.
- Prefer `gh repo create --template` over any manual clone narrative.
- After bootstrap, the new repo must be usable with Cursor, Claude, Codex, and Pi without a second skill install.
