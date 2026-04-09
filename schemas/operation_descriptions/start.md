**Description:**
Starts the reader radio with all staged Gen2X configuration settings applied and active.

**Usage:**
Send this command after configuring your desired Gen2X settings (such as TagProtect, FastID, TagFocus, and Tag Quieting). Set the `applyImpinjGen2X` parameter to `true` to ensure all configuration changes take effect immediately when the radio starts. The radio will operate with all configured features active. You must stop the radio before making configuration changes using this start command.

**Parameters:**
- `applyImpinjGen2X` (boolean): Set to `true` to apply all staged Gen2X configurations
