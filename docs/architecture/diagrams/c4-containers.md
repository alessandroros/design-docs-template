# C4 — Containers

A container is something you can deploy or run: an application, a datastore, a queue. Replace every TBD once an ADR chooses the technology. Do not invent containers here before that decision.

```mermaid
C4Container
  title Containers for [System Name]

  Person(user, "User")

  System_Boundary(system, "[System Name]") {
    Container(client, "Client", "TBD", "UI used by the user")
    Container(api, "Application", "TBD", "Domain behavior and APIs")
    ContainerDb(db, "Database", "TBD", "Persistent state")
  }

  System_Ext(external, "External system")

  Rel(user, client, "Uses")
  Rel(client, api, "Calls")
  Rel(api, db, "Reads and writes")
  Rel(api, external, "Integrates with")
```

```mermaid
flowchart TB
  user["User"]

  subgraph system["[System Name]"]
    client["Client (TBD)"]
    api["Application (TBD)"]
    db[("Database (TBD)")]
  end

  external["External system"]

  user --> client --> api
  api --> db
  api --> external
```
