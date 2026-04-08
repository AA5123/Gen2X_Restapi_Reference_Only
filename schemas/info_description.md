Use this API to configure and control Impinj Gen2X features on Zebra fixed RFID readers over MQTT.

## Overview

This tutorial provides a walk-through of the steps to use Impinj Gen2X tag features via the MQTT API on Zebra fixed RFID readers, including:

- **Tag Protection** — Lock individual tags with a password so they're invisible to unauthorized readers.
- **FastID** — Return the EPC and TID in a single inventory response.
- **TagFocus** — Silence already-read tags so the reader focuses on new ones.
- **Tag Quieting** — Silence specific tags by EPC ID.

Impinj Gen2X extends the Gen2 radio and logical layers. Your tags must support Gen2X to use these features. To check whether your tags are compatible, see the [Impinj Gen2X tag specifications](http://www.impinj.com/Gen2X).

## Before you begin

Set up your MQTT connection, broker, and topic before using this API. For setup instructions, see the [Zebra IoTC MQTT Setup Guide](https://zebradevs.github.io/rfid-ziotc-docs/other_cloud_support/MQTT/index.html).


## Get started
Follow these steps to configure and apply Gen2X features on the reader:

1. **Check current state (optional)** — Send `get_impinjGen2X` to see which Gen2X features are currently active on the reader.
2. **Stop the radio** — Send the `stop` command. The radio must be stopped before you can apply configuration changes.
3. **Configure features** — Use the `set_impinjGen2X` command to stage the Gen2X features you want to enable (e.g., TagProtect, FastID, TagFocus).
4. **Start with Gen2X** — Send the `start` command with `applyImpinjGen2X` set to `true`. This applies the staged Gen2X configuration and starts the radio.
5. **Confirm applied state** — Send `get_impinjGen2X` again to verify the configuration is active on the reader.