**Description:**
Restores previously silenced tags, allowing them to resume normal participation in inventory rounds.

**Usage:**
Send this command with the EPC IDs of the tags you wish to restore. These must be the same EPC IDs you provided to the Quiet Tags command. Once sent, the specified tags will resume responding to inventory operations and will transmit RF signals normally. You can restore individual tags or multiple tags in a single command. Tags not explicitly restored remain in quiet state.

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
| `tagQuieting.basic.action` | string | Yes | Restore the specified tags Must be `unquiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of tag EPCs (hex strings) to unquiet Array of string values. |

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
| `tagQuieting.basic.action` | string | Yes | Restore the specified tags. Must be `unquiet` |
| `tagQuieting.basic.tagIDs` | array | Yes | List of hexadecimal EPC strings of tags to unquiet. Array of string values. |
