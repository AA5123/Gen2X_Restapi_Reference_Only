**Description:**
Clear Protected Mode Configuration — Revokes the reader's authorization to inventory protected tags, restoring them to invisible status.

**Usage:**
Send this command with the 32-bit access password to revoke the reader's visibility permissions. After sending this command, the reader will no longer surface protected tags in inventory results. This does not remove Protected Mode from the tags; it only prevents the reader from seeing them.

---

---

**MQTT Endpoint Details**

| Field | Value |
|-------|-------|
| Publish Topic | `controlrequest` |
| Subscribe Topic | `controlresponse` |
| Command | `set_impinjGen2X` |

**MQTT Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `tagProtect` | object | Yes | Protected Mode configuration |
| `tagProtect.action` | string | Yes | Disables reading of protected tags Must be `disableTagVisibility` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `setImpinjGen2X` |
| Content-Type | `application/json` |

> This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `tagProtect` | object | Yes | TagProtect configuration for disabling protected tag reading. |
| `tagProtect.action` | string | Yes | Disables the reader from reading protected tags. Must be `disableTagVisibility` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password. (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.enableShortRange` | boolean | No | Enables short-range protection mode for higher security. |
