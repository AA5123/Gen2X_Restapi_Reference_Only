## Enable Protected Mode with Short Range

**Description:**
Enable Impinj Protected Mode with Short Range — Protects an RFID tag with a 32-bit access password and restricts its response range to short distance only.

**Usage:**
Protect a tag with both password protection AND proximity enforcement. Use this when you need dual-layer security for critical access credentials (badges, keys), when securing point-of-sale transactions or payments, or when you want to prevent long-range tag cloning attacks.

You'll need the target tag's EPC ID and a 32-bit password. Once enabled, the tag becomes password-protected AND requires readers to be within close physical range to interact with it. This provides both password security and prevents remote scanning or RF attacks.

**Parameters (MQTT & REST):**

- **action** (string): Enables Protected Mode on the tag Must be `enableTagProtection`.
- **password** (string): 8-character hexadecimal 32-bit password
- **tagID** (string): Hexadecimal tagID (EPC) of the target tag
- **enableShortRange** (boolean): true to enable short-range protection mode for higher security

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>