---
name: docs-template-bootstrap
description: >-
  Bootstraps a new design-docs repository from alessandroros/design-docs-template
  (RFC, ADR, arc42, Starlight site). Day-zero scaffolding so the docs stack is
  never rebuilt from scratch. Invoked via design-docs-template.
---

# bootstrap — new docs repo

**What:** Clone or create a repo from `design-docs-template` and rebrand site config for this project.  
**When:** Empty folder, new product docs, or “I don’t want to recreate arc42/Starlight by hand.”  
**Not:** Filling architecture content — that comes after day-one pointers.

## Process

### 1. Collect inputs

Ask only what is missing (one batch):

- **Project name** (folder + GitHub repo name)
- **Parent directory** (default: current workspace parent, or `~/Projects`)
- **Visibility** (`private` default)
- **GitHub owner** (user or org; default: authenticated `gh` user)
- **Site `base` path** for Starlight/Pages (default: `/<repo-name>`)
- **Create remote now?** yes → `gh repo create --template`; no → local copy only
- **Template flavour** if not obvious: `alessandroros/design-docs-template` (generic) or `openmove/engineering-design-playbook` (OpenMove). If the current repo’s `origin`/`openmove` already is one of those, use that.

### 2. Create the repo

Prefer, when remote yes and `gh` works:

```bash
gh repo create <owner>/<name> --template <template-owner>/<template-repo> --private --clone
```

Use `--public` if they asked. `cd` into the clone.

If template create fails or remote is no: copy from a local clone of the same template (e.g. `~/Projects/design-docs-template` or `~/Projects/engineering-design-playbook`), excluding `node_modules/`, `website/dist/`, `.git/`, then `git init` (and add remote later if they want).

Completion: working tree exists with `docs/`, `website/`, `README.md`.

### 3. Rebrand the site config

Edit `website/site.config.mjs` (or equivalent):

- `site` — Pages origin they will use (ask if unknown; keep a placeholder they can fix)
- `base` — `/<repo-name>` unless they chose otherwise
- `repoUrl` — the GitHub URL

Update root `README.md` title/one-liner to the real project. Leave arc42/ADR/RFC **templates** intact; do not invent project architecture.

### 4. Install and smoke-check

```bash
npm install --prefix website
npm run sync --prefix website   # if the script exists
```

Optional: start `npm run dev --prefix website` only if they want localhost now; report the Local URL from the template’s base path.

### 5. Day-one pointer

Tell them to fill only, when ready (do not fill for them unless asked):

1. arc42 §1 goals  
2. arc42 §3 + C4 context  
3. arc42 §4 strategy  
4. arc42 §5 + C4 containers  
5. first ADRs (`new-adr`) or first RFC (`new-rfc`) when trade-offs appear  

### 6. Hand off

Summarise: path created, remote URL (if any), `base`, how to preview. Do not force a commit unless they ask.

## Hard rules

- Do not overwrite an existing non-empty project directory without explicit confirm.
- Do not invent ADRs/RFCs/content for the new domain in bootstrap.
- Prefer the GitHub template flow over hand-copy when possible.
