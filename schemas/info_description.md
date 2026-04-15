Use this guide to enable, configure, and manage Impinj Gen2X features on Zebra fixed RFID readers using both MQTT and REST APIs. These features are currently supported on the FXR90, with additional fixed reader support coming soon.

## Overview

This reference explains how to use Gen2X operations across MQTT and REST for:

- **Protected Mode**: Lock individual tags with a password so they are invisible to unauthorized readers. *(tag-scoped: applies to a specific tag by EPC)*
- **FastID**: Return the EPC and TID in a single inventory response. *(reader-scoped: applies to inventory on the reader)*
- **TagFocus**: Reduce repeated reports from already-read tags so the reader prioritizes new tags. *(reader-scoped: applies to inventory on the reader)*
- **Tag Quieting**: Quiet specific tags by EPC ID. *(tag-scoped: applies to specific tags by EPC)*

Impinj Gen2X extends Gen2 radio and logical layers. Tags must support Gen2X to use these features. For tag compatibility, refer to [Impinj Gen2X specifications](http://www.impinj.com/Gen2X).

## Protocols

This documentation covers both interfaces for the same Gen2X feature set:

- MQTT: Command-based operations for cloud-connected workflows.
- REST: HTTP endpoints for direct API integration.

Use either interface based on your deployment and integration architecture.

## Before You Begin

- For MQTT: Configure broker, topic, and connection before sending Gen2X commands.
- For REST: Confirm the API service is reachable at your reader/host URL and port.

## REST API Getting Started

### Authentication

1. Send `PUT /cloud/localRestLogin`.
2. Extract the access token from the login response.
3. Add the token to all protected requests.

### Configuration Workflow

Use this sequence to safely stage and apply Gen2X updates:

1. Send `GET /cloud/impinjGen2X` to check current Gen2X configuration.
2. Send `PUT /cloud/stop` to stop the IoT cloud service if it is running.
3. Send `PUT /cloud/impinjGen2X` to stage one or more feature updates.
4. Send `GET /cloud/impinjGen2X` to verify staged configuration.
5. Send `PUT /cloud/start` with `applyImpinjGen2X: true` to start the service and apply staged configuration.

## MQTT Getting Started

Use this sequence for the same workflow through MQTT commands:

1. Send `get_impinjGen2X` to check current Gen2X configuration.
2. Send `stop` to stop the IoT cloud service if it is running.
3. Send `set_impinjGen2X` to stage one or more feature updates.
4. Send `get_impinjGen2X` to verify staged configuration.
5. Send `start` with `applyImpinjGen2X: true` to start the service and apply staged configuration.

## Feature Persistence and State Changes

- **Persistence:** When you stop and start the reader, disconnect and reconnect MQTT, or even reboot the device, the reader remembers the last Gen2X feature you configured. That feature will be automatically restored and active when the reader starts up again.

- **Feature Replacement:** Only one Gen2X feature (such as TagFocus, Tag Quieting, etc.) can be active at a time. If you enable a new feature (for example, TagFocus) after previously enabling another (like Tag Quieting), the new feature will replace the previous one. The old feature is no longer active after the change.