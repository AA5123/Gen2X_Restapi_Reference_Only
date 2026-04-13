**Description:**
Selectively silences one or more specific tags by their EPC ID, preventing them from responding to inventory rounds without affecting other tags.

**Usage:**
Send this command with an array of one or more EPC IDs to quiet. Quieted tags will not participate in inventory responses and will not transmit RF signals to the reader. This is useful for isolating problematic tags, managing high-density inventory operations, or testing specific tag subsets. You can quiet up to 31 tag EPCs in a single command.

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
| `tagQuieting` | object | Yes | Tag quieting configuration |
| `tagQuieting.basic` | object | Yes | Basic tag quieting settings |
| `tagQuieting.basic.action` | string | Yes | Silence the specified tags Must be `quiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of tag EPCs (hex strings) to quiet Array of string values. |

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `setImpinjGen2X` |
| Content-Type | `application/json` |

> This request stages Tag Quieting settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `tagQuieting` | object | Yes | Tag quieting configuration. |
| `tagQuieting.basic` | object | Yes | Basic tag quieting settings. |
| `tagQuieting.basic.action` | string | Yes | Silence the specified tags. Must be `quiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of hexadecimal EPC strings of tags to quiet. Array of string values. |
