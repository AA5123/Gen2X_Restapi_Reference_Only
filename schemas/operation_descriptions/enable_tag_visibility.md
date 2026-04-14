## Enable Inventory of Protected Tags

**Description:**
Enable Inventory of Protected Tags — Grants the reader authorization to inventory protected tags using the correct 32-bit access password.

**Usage:**
Allow your reader to see and inventory protected tags without removing their protection. Use this when you need to read inventory of protected tags but leave them protected, when multiple readers need controlled access to the same protected tags, or when performing maintenance or auditing protected assets.

You need the password for the protected tags you want to read. Once enabled, your reader gains temporary visibility of protected tags while they remain locked for other readers without the password. You can inventory, read, and report on protected tags while they stay protected for unauthorized readers.

**Parameters (MQTT & REST):**

- **action** (string): Enables the reader to read protected tags Must be `enableTagVisibility`.
- **password** (string): 8-character hexadecimal 32-bit password

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>