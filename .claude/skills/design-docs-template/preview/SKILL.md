---
name: docs-template-preview
description: >-
  Starts the local Starlight docs site: syncs docs/ into the website, runs the
  Astro/Starlight dev server, and reports the Local URL including the configured
  base path. Use when the user wants to preview design docs on localhost.
  Invoked via design-docs-template.
---

# preview — local Starlight site

**What:** Sync Markdown from `docs/` into the Starlight site and run the dev server; print the URL with the correct `base`.  
**When:** “Alza i docs in locale”, “preview”, “localhost”, after edits that need a hard look in the browser.  
**Not:** Publishing to GitHub Pages / Cloudflare (CI does that) or inventing content.

## Process

### 1. Find the website root

Prefer `<repo>/website/` with `package.json` scripts `sync` and `dev` (or `dev` that already runs sync). If missing, stop and suggest **bootstrap**.

Read `website/site.config.mjs` (or equivalent) for `base` (e.g. `/design-docs-template`, `/openmove--sta-maas-docs`).

### 2. Install if needed

If `website/node_modules` is missing:

```bash
npm install --prefix website
```

### 3. Free or reuse the port

Default Astro port is **4321**. If something already listens there and it is this project’s `astro dev`, report that URL and do not start a second server.

If another process owns the port, ask once: kill it, or use another port (`astro dev --port N`).

### 4. Start the server

From `website/` (background):

```bash
npm run dev -- --host
```

(`dev` already runs `sync` in the template.) Wait until the log shows ready / Local URL.

If `dev` does not sync, run `npm run sync` first, then `npx astro dev --host`.

### 5. Hand off

Report:

- **Local** URL: `http://localhost:<port><base>` (no trailing slash issues — match what Astro prints)
- **Network** URLs if Astro printed them
- Reminder: after editing `docs/`, either rely on the next `dev`/sync or re-run `npm run sync --prefix website` and hard-refresh if the page looks stale

Leave the server running unless they asked to stop it.

## Hard rules

- Do not commit, push, or deploy as part of preview.
- Do not change `site.config.mjs` unless they asked to fix a wrong `base`.
- Prefer one dev server per repo; do not pile duplicate `astro dev` processes.
