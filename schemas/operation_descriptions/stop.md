**Description:**
Stops the reader radio immediately, halting all inventory operations and RF transmissions.

**Usage:**
Send this command with an empty payload to stop the reader radio. You must stop the radio before applying any Gen2X configuration changes such as enabling/disabling Protected Mode, FastID, TagFocus, or Tag Quieting. Always wait for the success response before attempting to configure settings or restart the radio. Stopping the reader is mandatory for synchronized configuration management.

---

---

---

<div style="background:#e0f7fa;padding:6px 12px;font-weight:600;border-radius:4px;color:#006064;margin-bottom:4px;">MQTT Endpoint Details</div>

| Field | Value |
|-------|-------|
| Command | `stop` |

<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>

| Field | Value |
|-------|-------|
| Method | <span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">PUT</span>`PUT` |
| Path | `/cloud/stop` |
| OperationId | `stopIotCloudService` |
| Content-Type | `application/json` |

> Stop the radio before making any Gen2X configuration changes.

**Parameters (MQTT & REST)**

_The following parameters apply to both MQTT and REST unless otherwise noted._

_No parameters required._
