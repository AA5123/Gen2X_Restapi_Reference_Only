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

Use this sequence for a standard Gen2X update workflow.

REST URL details:

- Base URL format: `http://<device-ip>:<port>`
- Full endpoint format: `http://<device-ip>:<port><path>`
- Example endpoint: `http://<device-ip>:<port>/cloud/impinjGen2X`
- Common paths used in this flow: `/cloud/localRestLogin`, `/cloud/impinjGen2X`, `/cloud/stop`, `/cloud/start`

Authentication:

1. Call `POST http://<device-ip>:<port>/cloud/localRestLogin` to obtain an access token.
2. Include the token in every protected request header:

   `Authorization: Bearer <token>`

Workflow:

1. Use `GET http://<device-ip>:<port>/cloud/impinjGen2X` to check the currently saved Gen2X configuration.
2. Use `PUT http://<device-ip>:<port>/cloud/stop` to stop the IoT cloud service if it is running.
3. Use `PUT http://<device-ip>:<port>/cloud/impinjGen2X` to stage one or more feature updates.
4. Use `GET http://<device-ip>:<port>/cloud/impinjGen2X` to verify staged configuration before applying it.
5. Use `PUT http://<device-ip>:<port>/cloud/start` with `applyImpinjGen2X: true` to start the service and apply staged configuration.

## MQTT Getting Started

Use this sequence for the same workflow through MQTT commands:

1. Send `get_impinjGen2X` to check current Gen2X configuration.
2. Send `stop` to stop the IoT cloud service if it is running.
3. Send `set_impinjGen2X` to stage one or more feature updates.
4. Send `get_impinjGen2X` to verify staged configuration.
5. Send `start` with `applyImpinjGen2X: true` to start the service and apply staged configuration.