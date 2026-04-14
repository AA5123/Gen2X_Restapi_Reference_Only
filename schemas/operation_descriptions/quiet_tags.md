## Quiet Tags

**Description:**
Selectively silences one or more specific tags by their EPC ID, preventing them from responding to inventory rounds without affecting other tags.

**Usage:**
Silence specific tags by their EPC so they don't respond to inventory. Use this when you want to exclude certain tags from inventory reports, known bad tags should not appear in reports, you need to test reader performance without interference from specific tags, or you're isolating problem tags for troubleshooting.

You can quiet up to 31 tags at once by listing their EPCs. Once quieted, listed tags stop responding to inventory commands and won't appear in any inventory reports. Other tags continue normal operation, and quieted tags remain silent until unquieted.

**Parameters (MQTT & REST):**

- **action** (string): Silence the specified tags Must be `quiet`.
- **tagIDs** (array): List of tag EPCs (hex strings) to quiet

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>