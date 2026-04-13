**Description:**
Starts the reader radio with all staged Gen2X configuration settings applied and active.

**Usage:**
Send this command after configuring your desired Gen2X settings (such as TagProtect, FastID, TagFocus, and Tag Quieting). Set the `applyImpinjGen2X` parameter to `true` to ensure all configuration changes take effect immediately when the radio starts. The radio will operate with all configured features active. You must stop the radio before making configuration changes using this start command.

---

---

**MQTT Endpoint Details**

| Field | Value |
|-------|-------|
| Publish Topic | `controlrequest` |
| Subscribe Topic | `controlresponse` |
| Command | `start` |

**MQTT Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `applyImpinjGen2X` | boolean | Yes | true to apply Gen2X config when starting the radio Must be `True` |

---

**REST Endpoint Details**

| Field | Value |
|-------|-------|
| Method | `PUT` |
| Path | `/cloud/start` |
| OperationId | `startIotCloudService` |
| Content-Type | `application/json` |

> Set `applyImpinjGen2X: true` to apply all previously staged Gen2X settings when starting the radio.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `applyImpinjGen2X` | boolean | No | Set true to apply staged Gen2X configuration while starting. |
