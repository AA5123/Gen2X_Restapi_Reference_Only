**Description:**
Enable Inventory of Protected Tags — Grants the reader authorization to inventory protected tags using the correct 32-bit access password.

**Usage:**
Send this command with the 32-bit access password. The reader will use this password to authenticate and unmask all protected tags that match during inventory rounds. This allows the reader to interact with protected tags without permanently removing their Protected Mode.

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
| `tagProtect.action` | string | Yes | Enables the reader to read protected tags Must be `enableTagVisibility` |
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
| `tagProtect` | object | Yes | TagProtect configuration for enabling visibility of protected tags. |
| `tagProtect.action` | string | Yes | Enables the reader to read protected tags. Must be `enableTagVisibility` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password. (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.enableShortRange` | boolean | No | Enables short-range protection mode for higher security. |
