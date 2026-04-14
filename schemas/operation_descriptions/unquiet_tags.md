**Description:**
Restores previously silenced tags, allowing them to resume normal participation in inventory rounds.

**Usage:**
Send this command with the EPC IDs of the tags you wish to restore. These must be the same EPC IDs you provided to the Quiet Tags command. Once sent, the specified tags will resume responding to inventory operations and will transmit RF signals normally. You can restore individual tags or multiple tags in a single command. Tags not explicitly restored remain in quiet state.

**Parameters (MQTT & REST):**

- **action** (string): Restore the specified tags Must be `unquiet`.
- **tagIDs** (array): List of tag EPCs (hex strings) to unquiet

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>http://<host>:<port>/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>