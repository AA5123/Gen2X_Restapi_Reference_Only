**Description:**
Disable Impinj Protected Mode — Removes the 32-bit access password protection from an RFID tag, restoring normal operation.

**Usage:**
Send this command with the target tag's EPC ID and the 32-bit access password that was used to enable Protected Mode. Once disabled, the tag returns to normal operation and responds to all standard inventory commands without authentication.

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
| `tagProtect.action` | string | Yes | Disables Protected Mode on the tag Must be `disableTagProtection` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.tagID` | string | Yes | Tag EPC ID |

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
| `tagProtect` | object | Yes | TagProtect configuration for disabling protection on a target tag. |
| `tagProtect.action` | string | Yes | Disables Protected Mode on the specified tag. Must be `disableTagProtection` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password. (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.tagID` | string | Yes | Hexadecimal tagID (EPC) of the target tag. Pattern: `^(?:[0-9A-Fa-f]{2})+$` |
