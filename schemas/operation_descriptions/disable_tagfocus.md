**Description:**
Disables the TagFocus feature, returning tags to normal operational mode where all tags respond to every inventory round regardless of prior reads.

**Usage:**
Send this command to deactivate TagFocus on the reader. Once disabled, all tags will respond to every inventory round, even if they were previously read in the current session. This is useful when you need to track tag movement, verify tag presence continuously, or when inventory redundancy is more important than throughput optimization.

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
| `tagFocus` | object | Yes | TagFocus feature configuration |
| `tagFocus.enabled` | boolean | Yes | Disable TagFocus feature Must be `False` |

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `setImpinjGen2X` |
| Content-Type | `application/json` |

> This request stages TagFocus settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `tagFocus` | object | Yes | TagFocus configuration. |
| `tagFocus.enabled` | boolean | Yes | Disable the TagFocus feature. Must be `False` |
