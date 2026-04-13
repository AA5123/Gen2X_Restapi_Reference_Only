**Description:**
Enables FastID feature so tags return both EPC (Electronic Product Code) and TID (Tag Identifier) in a single inventory response.

**Usage:**
Send this command to activate FastID on the reader. Once enabled, each tag inventory response includes both the EPC and TID simultaneously, eliminating the need for separate TID read operations. This significantly improves inventory throughput and reduces the number of RF transmissions required.

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
| `fastID.enabled` | boolean | Yes | Enable FastID feature Must be `True` |

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
| `fastID.enabled` | boolean | Yes | Enable the FastID feature. Must be `True` |
