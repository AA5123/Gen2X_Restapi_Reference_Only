## Enable TagFocus

**Description:**
Enables TagFocus feature so tags that have already been inventoried remain silent in subsequent inventory rounds, allowing the reader to focus exclusively on new or unread tags.

**Usage:**
Make the reader focus on NEW tags by silencing tags already read in this session. Use this when you have high-density tag environments, want to find tags that haven't been read yet, are discovering tags in a crowded area, or need to improve read rates for hard-to-reach tags.

Just send the enable command; it works on all tags. Once enabled, tags that have already been inventoried in this session stay silent while new or unread tags in range respond. The reader concentrates RF energy on finding new tags instead of re-reading known inventory.

**Parameters (MQTT & REST):**

- **enabled** (boolean): Enable TagFocus feature Must be `True`.

<div class="endpoint-block"><div class="ep-heading ep-mqtt">MQTT Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Command</td><td><code>set_impinjGen2X</code></td></tr></tbody></table></div>

<div class="endpoint-block"><div class="ep-heading ep-rest">REST Endpoint Details</div><table class="endpoint-table"><tbody><tr><td>Method</td><td><span class="ep-method ep-method-put">PUT</span></td></tr><tr><td>Path</td><td><code>/cloud/impinjGen2X</code></td></tr><tr><td>Request URL</td><td><code>https://10.233.48.49/cloud/impinjGen2X</code></td></tr><tr><td>Content-Type</td><td><code>application/json</code></td></tr></tbody></table></div>