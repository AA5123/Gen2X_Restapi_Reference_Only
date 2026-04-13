**Description:**
Clear Protected Mode Configuration — Revokes the reader's authorization to inventory protected tags, restoring them to invisible status.

**Usage:**
Send this command with the 32-bit access password to revoke the reader's visibility permissions. After sending this command, the reader will no longer surface protected tags in inventory results. This does not remove Protected Mode from the tags; it only prevents the reader from seeing them.

**MQTT Parameters:**

- **action** (string): Disables reading of protected tags Must be `disableTagVisibility`.
- **password** (string): 8-character hexadecimal 32-bit password

**REST Parameters:**

- **action** (string): Disables the reader from reading protected tags. Must be `disableTagVisibility`.
- **password** (string): 8-character hexadecimal 32-bit password.
- **enableShortRange** (boolean): Enables short-range protection mode for higher security.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>OperationId</td><td><code>setImpinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table><p class="ep-note">This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.</p></div>