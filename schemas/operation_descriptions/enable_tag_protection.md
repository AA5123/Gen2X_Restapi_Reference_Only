**Description:**
Enable Impinj Protected Mode — Locks an RFID tag using a 32-bit access password, rendering it invisible to readers.

**Usage:**
Send this command with the target tag's EPC ID and a 32-bit access password. Once enabled, the tag enters Protected Mode and ceases to respond to standard inventory commands. The tag remains RF silent and inaccessible until a reader provides the correct password.

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
| `tagProtect.action` | string | Yes | Enables Protected Mode on the tag Must be `enableTagProtection` |
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
| `tagProtect` | object | Yes | TagProtect configuration for enabling protection on a target tag. |
| `tagProtect.action` | string | Yes | Sets a tag to protected mode. Must be `enableTagProtection` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password used for tag protection. (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.tagID` | string | Yes | Hexadecimal tagID (EPC) of the target tag. Pattern: `^(?:[0-9A-Fa-f]{2})+$` |
| `tagProtect.enableShortRange` | boolean | No | Enables short-range protection mode for higher security. |
