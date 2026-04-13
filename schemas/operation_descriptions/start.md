**Description:**
Starts the reader radio with all staged Gen2X configuration settings applied and active.

**Usage:**
Send this command after configuring your desired Gen2X settings (such as TagProtect, FastID, TagFocus, and Tag Quieting). Set the `applyImpinjGen2X` parameter to `true` to ensure all configuration changes take effect immediately when the radio starts. The radio will operate with all configured features active. You must stop the radio before making configuration changes using this start command.

---

---

---

<div style="background:#e0f7fa;padding:6px 12px;font-weight:600;border-radius:4px;color:#006064;margin-bottom:4px;">MQTT Endpoint Details</div>

| Field | Value |
|-------|-------|
| Command | `start` |

**MQTT Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `applyImpinjGen2X` | boolean | Yes | true to apply Gen2X config when starting the radio Must be `True` |

<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>

| Field | Value |
|-------|-------|
| Method | <span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">PUT</span>`PUT` |
| Path | `/cloud/start` |
| OperationId | `startIotCloudService` |
| Content-Type | `application/json` |

> Set `applyImpinjGen2X: true` to apply all previously staged Gen2X settings when starting the radio.

**REST Parameters**

| Parameter | Type | Required | Description |
|-----------|------|:--------:|-------------|
| `applyImpinjGen2X` | boolean | No | Set true to apply staged Gen2X configuration while starting. |
