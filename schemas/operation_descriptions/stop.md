## Stop IoT Cloud Service

**Description:**
Stops the reader radio immediately, halting all inventory operations and RF transmissions.

**Usage:**
Stop the reader so you can safely change Gen2X configuration. Use this before making ANY Gen2X configuration changes, when you need to prevent tag responses while reconfiguring, when applying new Protected Mode or FastID settings, or before staging configuration changes that must be applied with start.

Just send the stop command. Once stopped, the reader stops immediately, all RF operations cease, the reader becomes idle and ready for configuration, no inventory or tag interaction occurs, and you can safely make configuration changes.

**Parameters (MQTT & REST):**

_No parameters required._

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>stop</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/stop</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/stop</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>