**Description:**
Enable Impinj Protected Mode — Locks an RFID tag using a 32-bit access password, rendering it invisible to readers.

**Usage:**
Send this command with the target tag's EPC ID and a 32-bit access password. Once enabled, the tag enters Protected Mode and ceases to respond to standard inventory commands. The tag remains RF silent and inaccessible until a reader provides the correct password.

**REST Endpoint Mapping:**
- Method: `PUT`
- Path: `/cloud/impinjGen2X`
- OperationId: `setImpinjGen2X`
- Content-Type: `application/json`

This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

**Parameters:**
- `action` (string): Set to `enableTagProtection` to enable Protected Mode for the tag
- `tagID` (string): The unique EPC identifier of the tag to protect
- `password` (string): A 32-bit (8-character hexadecimal) password used for Protected Mode access

