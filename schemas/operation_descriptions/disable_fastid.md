## Disable FastID

**Description:**
Disables the FastID feature, returning tags to standard inventory mode where they return only the EPC (Electronic Product Code).

**Usage:**
Return to standard inventory mode where tags only report their EPC. Use this when you don't need TID information in your application, want to reduce response payload size, or are reducing bandwidth or storage requirements.

Just send the disable command. Once disabled, tags return only EPC in inventory responses, making responses smaller and faster to process. If you need TID data later, you must perform separate TID read operations.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Disable FastID feature Must be `False`.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>