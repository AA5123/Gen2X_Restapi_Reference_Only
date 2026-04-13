**Description:**
Disables the FastID feature, returning tags to standard inventory mode where they return only the EPC (Electronic Product Code).

**Usage:**
Send this command to deactivate FastID on the reader. Once disabled, tags will only return their EPC in inventory responses. If you need the TID (Tag Identifier), you must perform a separate dedicated TID read operation. This is useful for reducing response payload size or simplifying data processing when TID data is not required.

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
| `fastID` | object | Yes | FastID feature configuration |
| `fastID.enabled` | boolean | Yes | Disable FastID feature Must be `False` |

<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>

| Field | Value |
|-------|-------|
| Method | <span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">PUT</span>`PUT` |
| Path | `/cloud/impinjGen2X` |
| OperationId | `setImpinjGen2X` |
| Content-Type | `application/json` |

> This request stages FastID settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `fastID` | object | Yes | FastID configuration. |
| `fastID.enabled` | boolean | Yes | Disable the FastID feature. Must be `False` |
