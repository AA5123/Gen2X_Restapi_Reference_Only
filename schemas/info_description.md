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

1. Configure the Gen2X features you want to use with the set commands below.
2. Verify your configuration with `get_gen2x_config`.
3. Stop the radio if it's running.
4. Start the radio with `start_with_gen2x` and set `applyImpinjGen2X` to `true`.

> **Note:** You must stop the radio before applying Gen2X configuration changes. Starting the radio while it's already running returns an error.
