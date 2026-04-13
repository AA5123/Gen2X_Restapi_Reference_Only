**Description:**
Stops the reader radio immediately, halting all inventory operations and RF transmissions.

**Usage:**
Send this command with an empty payload to stop the reader radio. You must stop the radio before applying any Gen2X configuration changes such as enabling/disabling Protected Mode, FastID, TagFocus, or Tag Quieting. Always wait for the success response before attempting to configure settings or restart the radio. Stopping the reader is mandatory for synchronized configuration management.

---

---

**MQTT Endpoint Details**

| Field | Value |
|-------|-------|
| Publish Topic | `controlrequest` |
| Subscribe Topic | `controlresponse` |
| Command | `stop` |

**MQTT Parameters**

_No parameters required._

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/stop` |
| OperationId | `stopIotCloudService` |
| Content-Type | `application/json` |

> Stop the radio before making any Gen2X configuration changes.

**REST Parameters**

_No parameters required._
