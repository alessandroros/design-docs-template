"""Show MADR YAML metadata in the page body.

MkDocs treats a leading `---` block as page front matter and removes it
from the rendered Markdown. MADR keeps status and decision-makers there,
so this hook prints that block back above the page.
"""

KEYS = ("status", "date", "decision-makers", "consulted", "informed")


def on_page_markdown(markdown, *, page, config, files):
    meta = page.meta or {}
    present = [key for key in KEYS if key in meta]
    if not present:
        return markdown
    lines = ["```yaml"]
    for key in present:
        lines.append(f"{key}: {meta[key]}")
    lines.append("```")
    return "\n".join(lines) + "\n\n" + markdown
