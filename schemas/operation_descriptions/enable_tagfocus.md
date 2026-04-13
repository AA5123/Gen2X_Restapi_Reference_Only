**Description:**
Enables TagFocus feature so tags that have already been inventoried remain silent in subsequent inventory rounds, allowing the reader to focus exclusively on new or unread tags.

**Usage:**
Send this command to activate TagFocus on the reader. Once enabled, any tag that has been successfully read in the current session (S1) will stop responding to subsequent inventory rounds. This dramatically improves read rates in dense tag environments by eliminating duplicate reads and concentrating RF energy on newly encountered tags.

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
| `tagFocus.enabled` | boolean | Yes | Enable TagFocus feature Must be `True` |

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
| `tagFocus.enabled` | boolean | Yes | Enable the TagFocus feature. Must be `True` |
