**Description:**
Selectively silences one or more specific tags by their EPC ID, preventing them from responding to inventory rounds without affecting other tags.

**Usage:**
Send this command with an array of one or more EPC IDs to quiet. Quieted tags will not participate in inventory responses and will not transmit RF signals to the reader. This is useful for isolating problematic tags, managing high-density inventory operations, or testing specific tag subsets. You can quiet up to 31 tag EPCs in a single command.

---

---

---

<div style="background:#e0f7fa;padding:6px 12px;font-weight:600;border-radius:4px;color:#006064;margin-bottom:4px;">MQTT Endpoint Details</div>

| Field | Value |
|-------|-------|
| Command | `set_impinjGen2X` |

**MQTT Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `tagQuieting` | object | Yes | Tag quieting configuration |
| `tagQuieting.basic` | object | Yes | Basic tag quieting settings |
| `tagQuieting.basic.action` | string | Yes | Silence the specified tags Must be `quiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of tag EPCs (hex strings) to quiet Array of string values. |

<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>

| Field | Value |
|-------|-------|
| Method | <span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">PUT</span>`PUT` |
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
