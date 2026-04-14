## Disable TagFocus

**Description:**
Disables the TagFocus feature, returning tags to normal operational mode where all tags respond to every inventory round regardless of prior reads.

**Usage:**
Return to standard inventory where all tags respond every time. Use this when you need to track tag movement continuously, want to verify tags are still present (redundancy), are performing a final inventory count, or need to ensure no tags are missed in reporting.

Just send the disable command. Once disabled, all tags respond to every inventory round. Tags previously read will respond again, which may be slower due to duplicate reads, but ensures complete visibility with no session-based tag memory.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Disable TagFocus feature Must be `False`.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>