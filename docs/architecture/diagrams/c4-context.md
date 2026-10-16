# C4 — System context

Replace the placeholder names. Keep one box for your system. Everything else is a person or an external system.

GitHub renders Mermaid. If a viewer does not support `C4Context`, use the flowchart below it. Same picture, plainer syntax.

```mermaid
C4Context
  title System context for [System Name]

  Person(user, "User", "Primary person who uses the system")
  Person(operator, "Operator", "Person who configures or supports it")

  System(system, "[System Name]", "What this system is responsible for")

  System_Ext(upstream, "Upstream system", "System this one depends on")
  System_Ext(downstream, "Downstream system", "System this one calls or notifies")

  Rel(user, system, "Uses")
  Rel(operator, system, "Administers")
  Rel(system, upstream, "Reads from")
  Rel(system, downstream, "Sends to")
```

```mermaid
flowchart TB
  user["User"]
  operator["Operator"]
  system["[System Name]"]
  upstream["Upstream system"]
  downstream["Downstream system"]

  user -->|Uses| system
  operator -->|Administers| system
  system -->|Reads from| upstream
  system -->|Sends to| downstream
```
