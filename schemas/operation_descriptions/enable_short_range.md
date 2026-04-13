**Description:**
Enable Impinj Protected Mode with Short Range — Protects an RFID tag with a 32-bit access password and restricts its response range to short distance only.

**Usage:**
Send this command with the target tag's EPC ID, a 32-bit access password, and set `enableShortRange` to `true`. The tag enters Protected Mode and only responds to readers in close physical proximity. This is ideal for point-of-sale operations or scenarios requiring location-specific tag reads.

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
| `tagProtect.tagID` | string | Yes | Hexadecimal tagID (EPC) of the target tag Pattern: `^[0-9A-Fa-f]+$` |
| `tagProtect.enableShortRange` | boolean | Yes | true to enable short-range protection mode for higher security |

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
| `tagProtect` | object | Yes | TagProtect configuration for enabling protection with short range. |
| `tagProtect.action` | string | Yes | Enables Protected Mode on the specified tag. Must be `enableTagProtection` |
| `tagProtect.password` | string | Yes | 8-character hexadecimal 32-bit password. (8–8 chars) Pattern: `^[0-9A-Fa-f]{8}$` |
| `tagProtect.tagID` | string | Yes | Hexadecimal tagID (EPC) of the target tag. Pattern: `^(?:[0-9A-Fa-f]{2})+$` |
| `tagProtect.enableShortRange` | boolean | Yes | Must be true to enable short-range protection mode. |
