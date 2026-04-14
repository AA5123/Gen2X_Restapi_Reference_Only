## Disable Impinj Protected Mode

**Description:**
Disable Impinj Protected Mode — Removes the 32-bit access password protection from an RFID tag, restoring normal operation.

**Usage:**
Remove password protection from a tag and restore normal operation. Use this when you no longer need protection, need to re-enable reading of a previously protected tag, or are transferring a tag to another location or user.

You must know the EXACT password that was used to protect the tag. Once disabled, the tag returns to normal operation mode, becomes visible to all readers, and responds to standard inventory commands without authentication.

**Parameters (MQTT & REST):**

- **action** (string): Disables Protected Mode on the tag Must be `disableTagProtection`.
- **password** (string): 8-character hexadecimal 32-bit password
- **tagID** (string): Tag EPC ID

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>