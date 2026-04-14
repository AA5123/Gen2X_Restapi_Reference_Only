## Get Gen2X Configuration

**Description:**
Retrieves and displays the current Gen2X configuration stored on the reader, including all enabled features and their settings.

**Usage:**
Check what Gen2X settings are currently saved on the reader. Use this when you need to audit current settings before making changes, want to verify configuration was applied correctly, are troubleshooting unexpected behavior, or need to document the current state.

Just query the current state with no parameters. The response returns all enabled Gen2X features and their settings, shows Protected Mode configurations if any exist, lists quieted tags if any are silent, and shows FastID and TagFocus status.

**Parameters (MQTT & REST):**

_No parameters required._

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>get_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-get">GET</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>