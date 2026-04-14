## Start IoT Cloud Service

**Description:**
Starts the reader radio with all staged Gen2X configuration settings applied and active.

**Usage:**
Start the reader and apply all staged Gen2X configuration changes. Use this after you've finished configuring all Gen2X settings and want to activate your configuration changes. You must have called stop first before making configuration changes.

Set `applyImpinjGen2X` to `true` to activate your staged configuration. Once started, the reader starts up immediately, all Gen2X settings you staged become active, tags respond according to your configuration, and inventory operations begin with your new settings.

**Parameters (MQTT & REST):**

- **applyImpinjGen2X** (boolean): true to apply Gen2X config when starting the radio Must be `True`.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>start</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/start</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/start</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>