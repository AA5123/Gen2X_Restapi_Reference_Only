## Clear Protected Mode Configuration

**Description:**
Clear Protected Mode Configuration — Revokes the reader's authorization to inventory protected tags, restoring them to invisible status.

**Usage:**
Revoke your reader's access to protected tags and make them invisible again. Use this when you want to stop seeing protected tags, need to secure the reader by removing visibility permissions, or are transferring the reader to a different location or user.

You need the password you used to enable visibility. Once disabled, your reader loses visibility of protected tags, and they become invisible to your reader again. Other readers without the password also can't see these tags.

**Parameters (MQTT & REST):**

- **action** (string): Disables reading of protected tags Must be `disableTagVisibility`.
- **password** (string): 8-character hexadecimal 32-bit password

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>