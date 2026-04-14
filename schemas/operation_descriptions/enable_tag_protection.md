## Enable Impinj Protected Mode

**Description:**
Enable Impinj Protected Mode — Locks an RFID tag using a 32-bit access password, rendering it invisible to readers.

**Usage:**
Protect a specific RFID tag from unauthorized reading by requiring a password. Use this when you need to prevent others from reading or cloning sensitive tags, or when implementing tag-level security in a multi-reader environment.

You'll need the target tag's EPC ID and a 32-bit password (8 hexadecimal characters). Once enabled, the tag becomes invisible to all readers that don't know the password and stops responding to standard inventory commands. Only readers with the correct password can interact with the tag.

**Parameters (MQTT & REST):**

- **action** (string): Enables Protected Mode on the tag Must be `enableTagProtection`.
- **password** (string): 8-character hexadecimal 32-bit password
- **tagID** (string): Tag EPC ID

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>