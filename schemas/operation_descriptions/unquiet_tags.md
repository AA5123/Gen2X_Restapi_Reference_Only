## Unquiet Tags

**Description:**
Restores previously silenced tags, allowing them to resume normal participation in inventory rounds.

**Usage:**
Restore silenced tags to normal operation. Use this when you need to include previously silenced tags in inventory again, a problem with a tag has been fixed, you're restoring tags to full operation, or you need to verify silenced tags are still present.

You need the list of tag EPCs that should resume operation, using the exact EPCs you quieted earlier. Once unquieted, listed tags resume normal responding and will appear in inventory again. Other tags remain in their current state, and only specified tags are restored.

**Parameters (MQTT & REST):**

- **action** (string): Restore the specified tags Must be `unquiet`.
- **tagIDs** (array): List of tag EPCs (hex strings) to unquiet

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>