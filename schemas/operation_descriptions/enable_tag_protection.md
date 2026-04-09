**Description:**
Locks an RFID tag using a 32-bit access password to prevent unauthorized access and inventory operations.

**Usage:**
Send this command with the target tag's EPC ID and a 32-bit access password. Once enabled, the tag enters a protected state where it ceases to respond to standard inventory commands and becomes RF silent. The tag will remain inaccessible to Gen2 commands until a reader successfully authenticates with the correct access password.

**Parameters:**
- `epc_id` (string): The unique EPC identifier of the tag to protect
- `access_password` (string): A 32-bit (8-character hexadecimal) password required to unlock the tag
