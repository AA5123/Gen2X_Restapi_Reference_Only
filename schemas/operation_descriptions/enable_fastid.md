## Enable FastID

**Description:**
Enables FastID feature so tags return both EPC (Electronic Product Code) and TID (Tag Identifier) in a single inventory response.

**Usage:**
Get both the EPC and TID (Tag Identifier) from tags in a single read operation. Use this when you need tag identification beyond just the EPC code, when you want to improve inventory speed by eliminating separate TID reads, or when your application requires full tag identification data.

Just send the enable command; no tag-specific parameters needed. Once enabled, each tag inventory response automatically includes both EPC and TID, eliminating the need for separate read cycles. This improves inventory speed and reduces RF traffic.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Enable FastID feature Must be `True`.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>