**Description:**
Disables the FastID feature, returning tags to standard inventory mode where they return only the EPC (Electronic Product Code).

**Usage:**
Send this command to deactivate FastID on the reader. Once disabled, tags will only return their EPC in inventory responses. If you need the TID (Tag Identifier), you must perform a separate dedicated TID read operation. This is useful for reducing response payload size or simplifying data processing when TID data is not required.

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
| `fastID` | object | Yes | FastID feature configuration |
| `fastID.enabled` | boolean | Yes | Disable FastID feature Must be `False` |

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `setImpinjGen2X` |
| Content-Type | `application/json` |

> This request stages FastID settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `fastID` | object | Yes | FastID configuration. |
| `fastID.enabled` | boolean | Yes | Disable the FastID feature. Must be `False` |
