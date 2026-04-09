**Description:**
Unlocks an RFID tag and removes the 32-bit access password protection, making it invisible mode disabled.

**Usage:**
Send this command with the target tag's EPC ID and the 32-bit access password that was used to enable protection. Once disabled, the tag returns to normal operation and responds to all standard inventory commands. The tag becomes discoverable and responsive to all readers without requiring authentication.

**Parameters:**
- `tagID` (string): The unique EPC identifier of the tag to unlock
- `password` (string): A 32-bit (8-character hexadecimal) access password that matches the protection password
