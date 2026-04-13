**Description:**
Restores previously silenced tags, allowing them to resume normal participation in inventory rounds.

**Usage:**
Send this command with the EPC IDs of the tags you wish to restore. These must be the same EPC IDs you provided to the Quiet Tags command. Once sent, the specified tags will resume responding to inventory operations and will transmit RF signals normally. You can restore individual tags or multiple tags in a single command. Tags not explicitly restored remain in quiet state.

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
| `tagQuieting.basic.action` | string | Yes | Restore the specified tags Must be `unquiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of tag EPCs (hex strings) to unquiet Array of string values. |

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
| `tagQuieting.basic.action` | string | Yes | Restore the specified tags. Must be `unquiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of hexadecimal EPC strings of tags to unquiet. Array of string values. |
