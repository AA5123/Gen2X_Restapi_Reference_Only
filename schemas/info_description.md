Use this API to configure and control Impinj Gen2X features on Zebra fixed RFID readers over MQTT.

## Overview

This API lets you configure the following Impinj Gen2X features:

- **Tag Protection** — Lock individual tags with a password so they're invisible to unauthorized readers.
- **FastID** — Return the EPC and TID in a single inventory response.
- **TagFocus** — Silence already-read tags so the reader focuses on new ones.
- **Tag Quieting** — Silence specific tags by EPC ID.

Impinj Gen2X extends the Gen2 radio and logical layers. Your tags must support Gen2X to use these features. To check whether your tags are compatible, see the [Impinj Gen2X tag specifications](http://www.impinj.com/Gen2X).

## Before you begin

Set up your MQTT connection, broker, and topic before using this API. For setup instructions, see the [Zebra IoTC MQTT Setup Guide](https://zebradevs.github.io/rfid-ziotc-docs/other_cloud_support/MQTT/index.html).

## Get started

1. **Check current state** — Send `get_gen2x_config` to see which Gen2X features are currently active on the reader.
2. **Configure features** — Use the set commands below to configure the Gen2X features you want to use.
3. **Stop the radio** — Stop the radio before applying configuration changes.
4. **Start with Gen2X** — Send `start_with_gen2x` and set `applyImpinjGen2X` to `true` to apply your configuration and start the radio.

> **Note:** You must stop the radio before applying Gen2X configuration changes. Starting the radio while it's already running returns an error.

### Example

The following example shows the full workflow — check config, configure a feature, stop the radio, then start with Gen2X applied.

**Step 1 — Check the current Gen2X configuration**

Publish to `rfid/cmd`:
```json
{
  "command": "get_impinjGen2X",
  "command_id": "9d744286-7b97-40b8-9e91-190df0334557",
  "payload": {}
}
```

**Step 2 — Configure a feature (example: enable FastID)**

Publish to `rfid/cmd`:
```json
{
  "command": "set_impinjGen2X",
  "command_id": "657298d3-98de-421c-9b7c-ad3b53b7474f",
  "payload": {
    "fastID": {
      "action": "enableFastID"
    }
  }
}
```

**Step 3 — Stop the radio**

Publish to `rfid/cmd`:
```json
{
  "command": "stop",
  "command_id": "c3f1a2b4-5678-4def-abcd-123456789abc",
  "payload": {}
}
```

**Step 4 — Start the radio with Gen2X applied**

Publish to `rfid/cmd`:
```json
{
  "command": "start",
  "command_id": "81dd51a2-b0d3-4099-b46a-5a3f82796ba1",
  "payload": {
    "applyImpinjGen2X": true
  }
}
```

Subscribe to `rfid/resp` to receive the response for each command:
```json
{
  "command": "start",
  "command_id": "81dd51a2-b0d3-4099-b46a-5a3f82796ba1",
  "payload": {
    "message": "Success: Gen2X configured. Use applyImpinjGen2X flag in start command to apply features."
  },
  "response": "success"
}
```
