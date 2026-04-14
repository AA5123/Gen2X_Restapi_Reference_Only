#!/usr/bin/env python3
"""
generate_combined_descriptions.py
----------------------------------
Regenerates schemas/operation_descriptions/*.md files in a unified format
that includes both MQTT and REST endpoint details and parameter tables.

Format per file:
  Description -> Usage -> MQTT Endpoint -> MQTT Params Table
  -> REST Endpoint -> REST Params Table

Run:
    python scripts/generate_combined_descriptions.py
Then:
    python scripts/generate_openapi_tags_md.py
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)

OP_DESC_DIR = os.path.join(ROOT, "schemas", "operation_descriptions")
CMD_DIR = os.path.join(ROOT, "schemas", "commands", "gen2x")
REST_API_DIR = os.path.join(ROOT, "rest api")
BASE_URL_TEMPLATE = "https://10.233.48.49"

# ── Operation command name headings ──────────────────────────────────────────
OP_COMMAND_NAMES = {
    "enable_tag_protection":  "Enable Impinj Protected Mode",
    "disable_tag_protection": "Disable Impinj Protected Mode",
    "enable_tag_visibility":  "Enable Inventory of Protected Tags",
    "disable_tag_visibility": "Clear Protected Mode Configuration",
    "enable_short_range":     "Enable Protected Mode with Short Range",
    "enable_fastid":          "Enable FastID",
    "disable_fastid":         "Disable FastID",
    "enable_tagfocus":        "Enable TagFocus",
    "disable_tagfocus":       "Disable TagFocus",
    "quiet_tags":             "Quiet Tags",
    "unquiet_tags":           "Unquiet Tags",
    "get_gen2x_config":       "Get Gen2X Configuration",
    "start":                  "Start IoT Cloud Service",
    "stop":                   "Stop IoT Cloud Service",
}

# ── Operation → REST folder mapping ──────────────────────────────────────────
OP_TO_REST = {
    "enable_tag_protection":  "enableTagProtection",
    "disable_tag_protection": "disableTagProtection",
    "enable_tag_visibility":  "enableTagVisibility",
    "disable_tag_visibility": "disableTagVisibility",
    "enable_short_range":     "enableShortRange",
    "enable_fastid":          "enableFastid",
    "disable_fastid":         "disableFastid",
    "enable_tagfocus":        "enableTagfocus",
    "disable_tagfocus":       "disableTagfocus",
    "quiet_tags":             "quietTags",
    "unquiet_tags":           "unquietTags",
    "get_gen2x_config":       "getGen2xConfig",
    "start":                  "start",
    "stop":                   "stop",
}

# ── REST endpoint routing ─────────────────────────────────────────────────────
REST_ENDPOINT = {
    "enable_tag_protection":  ("PUT", "/cloud/impinjGen2X"),
    "disable_tag_protection": ("PUT", "/cloud/impinjGen2X"),
    "enable_tag_visibility":  ("PUT", "/cloud/impinjGen2X"),
    "disable_tag_visibility": ("PUT", "/cloud/impinjGen2X"),
    "enable_short_range":     ("PUT", "/cloud/impinjGen2X"),
    "enable_fastid":          ("PUT", "/cloud/impinjGen2X"),
    "disable_fastid":         ("PUT", "/cloud/impinjGen2X"),
    "enable_tagfocus":        ("PUT", "/cloud/impinjGen2X"),
    "disable_tagfocus":       ("PUT", "/cloud/impinjGen2X"),
    "quiet_tags":             ("PUT", "/cloud/impinjGen2X"),
    "unquiet_tags":           ("PUT", "/cloud/impinjGen2X"),
    "get_gen2x_config":       ("GET", "/cloud/impinjGen2X"),
    "start":                  ("PUT", "/cloud/start"),
    "stop":                   ("PUT", "/cloud/stop"),
}

# ── REST staging notes (shown below endpoint table) ───────────────────────────
REST_NOTES = {
    "enable_tag_protection":  "",
    "disable_tag_protection": "",
    "enable_tag_visibility":  "",
    "disable_tag_visibility": "",
    "enable_short_range":     "",
    "enable_fastid":          "",
    "disable_fastid":         "",
    "enable_tagfocus":        "",
    "disable_tagfocus":       "",
    "quiet_tags":             "",
    "unquiet_tags":           "",
    "get_gen2x_config":       "",
    "start":                  "",
    "stop":                   "",
}

# ── Improved action-oriented usage descriptions ──────────────────────────────
IMPROVED_USAGES = {
    "enable_tag_protection": """Protect a specific RFID tag from unauthorized reading by requiring a password. Use this when you need to prevent others from reading or cloning sensitive tags, or when implementing tag-level security in a multi-reader environment.

You'll need the target tag's EPC ID and a 32-bit password (8 hexadecimal characters). Once enabled, the tag becomes invisible to all readers that don't know the password and stops responding to standard inventory commands. Only readers with the correct password can interact with the tag.""",

    "disable_tag_protection": """Remove password protection from a tag and restore normal operation. Use this when you no longer need protection, need to re-enable reading of a previously protected tag, or are transferring a tag to another location or user.

You must know the EXACT password that was used to protect the tag. Once disabled, the tag returns to normal operation mode, becomes visible to all readers, and responds to standard inventory commands without authentication.""",

    "enable_tag_visibility": """Allow your reader to see and inventory protected tags without removing their protection. Use this when you need to read inventory of protected tags but leave them protected, when multiple readers need controlled access to the same protected tags, or when performing maintenance or auditing protected assets.

You need the password for the protected tags you want to read. Once enabled, your reader gains temporary visibility of protected tags while they remain locked for other readers without the password. You can inventory, read, and report on protected tags while they stay protected for unauthorized readers.""",

    "disable_tag_visibility": """Revoke your reader's access to protected tags and make them invisible again. Use this when you want to stop seeing protected tags, need to secure the reader by removing visibility permissions, or are transferring the reader to a different location or user.

You need the password you used to enable visibility. Once disabled, your reader loses visibility of protected tags, and they become invisible to your reader again. Other readers without the password also can't see these tags.""",

    "enable_short_range": """Protect a tag with both password protection AND proximity enforcement. Use this when you need dual-layer security for critical access credentials (badges, keys), when securing point-of-sale transactions or payments, or when you want to prevent long-range tag cloning attacks.

You'll need the target tag's EPC ID and a 32-bit password. Once enabled, the tag becomes password-protected AND requires readers to be within close physical range to interact with it. This provides both password security and prevents remote scanning or RF attacks.""",

    "enable_fastid": """Get both the EPC and TID (Tag Identifier) from tags in a single read operation. Use this when you need tag identification beyond just the EPC code, when you want to improve inventory speed by eliminating separate TID reads, or when your application requires full tag identification data.

Just send the enable command; no tag-specific parameters needed. Once enabled, each tag inventory response automatically includes both EPC and TID, eliminating the need for separate read cycles. This improves inventory speed and reduces RF traffic.""",

    "disable_fastid": """Return to standard inventory mode where tags only report their EPC. Use this when you don't need TID information in your application, want to reduce response payload size, or are reducing bandwidth or storage requirements.

Just send the disable command. Once disabled, tags return only EPC in inventory responses, making responses smaller and faster to process. If you need TID data later, you must perform separate TID read operations.""",

    "enable_tagfocus": """Make the reader focus on NEW tags by silencing tags already read in this session. Use this when you have high-density tag environments, want to find tags that haven't been read yet, are discovering tags in a crowded area, or need to improve read rates for hard-to-reach tags.

Just send the enable command; it works on all tags. Once enabled, tags that have already been inventoried in this session stay silent while new or unread tags in range respond. The reader concentrates RF energy on finding new tags instead of re-reading known inventory.""",

    "disable_tagfocus": """Return to standard inventory where all tags respond every time. Use this when you need to track tag movement continuously, want to verify tags are still present (redundancy), are performing a final inventory count, or need to ensure no tags are missed in reporting.

Just send the disable command. Once disabled, all tags respond to every inventory round. Tags previously read will respond again, which may be slower due to duplicate reads, but ensures complete visibility with no session-based tag memory.""",

    "quiet_tags": """Silence specific tags by their EPC so they don't respond to inventory. Use this when you want to exclude certain tags from inventory reports, known bad tags should not appear in reports, you need to test reader performance without interference from specific tags, or you're isolating problem tags for troubleshooting.

You can quiet up to 31 tags at once by listing their EPCs. Once quieted, listed tags stop responding to inventory commands and won't appear in any inventory reports. Other tags continue normal operation, and quieted tags remain silent until unquieted.""",

    "unquiet_tags": """Restore silenced tags to normal operation. Use this when you need to include previously silenced tags in inventory again, a problem with a tag has been fixed, you're restoring tags to full operation, or you need to verify silenced tags are still present.

You need the list of tag EPCs that should resume operation, using the exact EPCs you quieted earlier. Once unquieted, listed tags resume normal responding and will appear in inventory again. Other tags remain in their current state, and only specified tags are restored.""",

    "get_gen2x_config": """Check what Gen2X settings are currently saved on the reader. Use this when you need to audit current settings before making changes, want to verify configuration was applied correctly, are troubleshooting unexpected behavior, or need to document the current state.

Just query the current state with no parameters. The response returns all enabled Gen2X features and their settings, shows Protected Mode configurations if any exist, lists quieted tags if any are silent, and shows FastID and TagFocus status.""",

    "start": """Start the reader and apply all staged Gen2X configuration changes. Use this after you've finished configuring all Gen2X settings and want to activate your configuration changes. You must have called stop first before making configuration changes.

Set `applyImpinjGen2X` to `true` to activate your staged configuration. Once started, the reader starts up immediately, all Gen2X settings you staged become active, tags respond according to your configuration, and inventory operations begin with your new settings.""",

    "stop": """Stop the reader so you can safely change Gen2X configuration. Use this before making ANY Gen2X configuration changes, when you need to prevent tag responses while reconfiguring, when applying new Protected Mode or FastID settings, or before staging configuration changes that must be applied with start.

Just send the stop command. Once stopped, the reader stops immediately, all RF operations cease, the reader becomes idle and ready for configuration, no inventory or tag interaction occurs, and you can safely make configuration changes.""",
}

# Always render one combined parameter section for these operations.
FORCE_MERGED_PARAMS = {
    "enable_tag_protection",
    "enable_tag_visibility",
    "disable_tag_visibility",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_existing_md(text):
    """Extract Description, Usage, and Persistence from existing .md file.
    Stops at '---', HTML tags, or the next bold heading to avoid picking up
    generated endpoint/parameter blocks from a previous run.
    """
    def extract_section(heading, src):
        pattern = rf"\*\*{re.escape(heading)}:\*\*\s*\n(.*?)(?=\n\*\*[A-Z]|\n---|\n<|\Z)"
        m = re.search(pattern, src, re.DOTALL)
        return m.group(1).strip() if m else ""

    desc = extract_section("Description", text)
    usage = extract_section("Usage", text)
    return desc, usage


def leaf_params_for_bullets(schema):
    """
    Recursively extract leaf (non-object) parameters for bullet-list display.
    Skips object-wrapper fields, showing only concrete typed leaf fields.
    """
    if not schema:
        return []
    props = schema.get("properties", {})
    required = schema.get("required", [])
    rows = []
    for key, prop in props.items():
        ptype = prop.get("type", "object")
        if ptype == "object" and "properties" in prop:
            child_schema = dict(prop)
            child_schema.setdefault("required", [])
            rows.extend(leaf_params_for_bullets(child_schema))
        else:
            desc = prop.get("description", "")
            const = prop.get("const")
            if const is not None:
                desc = (desc + f" Must be `{const}`.").strip()
            elif prop.get("enum") and "const" not in prop:
                vals = ", ".join(f"`{v}`" for v in prop["enum"])
                desc = (desc + f" One of: {vals}.").strip()
            rows.append({
                "name": key,
                "type": ptype,
                "required": key in required,
                "description": desc,
            })
    return rows


def params_bullets(rows):
    """Render parameter rows as a markdown bullet list."""
    if not rows:
        return "_No parameters required._"
    return "\n".join(
        f"- **{r['name']}** ({r['type']}): {r['description']}"
        for r in rows
    )


def html_endpoint_table(row_pairs):
    """Build an HTML endpoint detail table from (label, value_html) pairs."""
    inner = "".join(
        f"<tr><td>{label}</td><td>{value}</td></tr>"
        for label, value in row_pairs
    )
    return f'<table class="endpoint-table"><tbody>{inner}</tbody></table>'


def method_badge_html(method):
    cls = f"ep-method ep-method-{method.lower()}"
    return f'<span class="{cls}">{method}</span>'


def get_mqtt_command_name(cmd_schema):
    return (
        cmd_schema.get("properties", {})
        .get("command", {})
        .get("const", "set_impinjGen2X")
    )


# ── Main generator ────────────────────────────────────────────────────────────

def generate(op_name):
    # Load existing description or use improved usage
    md_path = os.path.join(OP_DESC_DIR, f"{op_name}.md")
    if os.path.exists(md_path):
        with open(md_path, encoding="utf-8") as f:
            existing = f.read()
        description, _ = parse_existing_md(existing)
    else:
        description = ""

    # Use improved action-oriented usage descriptions
    usage = IMPROVED_USAGES.get(op_name, "")

    # Load MQTT command schema
    cmd_path = os.path.join(CMD_DIR, f"{op_name}.json")
    cmd_schema = load_json(cmd_path) if os.path.exists(cmd_path) else {}
    mqtt_cmd = get_mqtt_command_name(cmd_schema)
    mqtt_payload = cmd_schema.get("properties", {}).get("payload", {})
    mqtt_leaf = leaf_params_for_bullets(mqtt_payload)

    # Load REST request schema
    rest_folder = OP_TO_REST.get(op_name, "")
    rest_schema_path = os.path.join(REST_API_DIR, rest_folder, f"{rest_folder}_request_schema.json")
    rest_schema = load_json(rest_schema_path) if os.path.exists(rest_schema_path) else {}
    rest_leaf = leaf_params_for_bullets(rest_schema)

    # REST endpoint details
    method, path = REST_ENDPOINT.get(op_name, ("PUT", "/cloud/impinjGen2X"))
    rest_note = REST_NOTES.get(op_name, "")

    # Merge params if MQTT and REST field names are identical
    mqtt_names = {r["name"] for r in mqtt_leaf}
    rest_names = {r["name"] for r in rest_leaf}
    merged = (mqtt_names == rest_names) or (op_name in FORCE_MERGED_PARAMS)

    # For forced-merged operations, keep only parameters common to both protocols.
    if op_name in FORCE_MERGED_PARAMS:
        common_names = rest_names.intersection(mqtt_names)
        mqtt_leaf = [r for r in mqtt_leaf if r["name"] in common_names]

    # MQTT endpoint HTML block — single <div> passes md() block check unchanged
    mqtt_block = (
        '<div class="endpoint-block">'
        '<div class="ep-heading ep-mqtt">MQTT Endpoint Details</div>'
        + html_endpoint_table([("Command", f"<code>{mqtt_cmd}</code>")])
        + "</div>"
    )

    # REST endpoint HTML block
    rest_rows = [
        ("Method", method_badge_html(method)),
        ("Path", f"<code>{path}</code>"),
        ("Request URL", f"<code>{BASE_URL_TEMPLATE}{path}</code>"),
        ("Content-Type", "<code>application/json</code>"),
    ]
    note_html = f'<p class="ep-note">{rest_note}</p>' if rest_note else ""
    rest_block = (
        '<div class="endpoint-block">'
        '<div class="ep-heading ep-rest">REST Endpoint Details</div>'
        + html_endpoint_table(rest_rows)
        + note_html
        + "</div>"
    )

    # Assemble parts joined with double newlines so md() block-splits correctly
    parts = []
    cmd_name = OP_COMMAND_NAMES.get(op_name, op_name.replace("_", " ").title())
    parts.append(f"## {cmd_name}")
    parts.append(f"**Description:**\n{description}")
    parts.append(f"**Usage:**\n{usage}")

    if merged:
        parts.append("**Parameters (MQTT & REST):**")
        parts.append(params_bullets(mqtt_leaf))
    else:
        if mqtt_leaf:
            parts.append("**MQTT Parameters:**")
            parts.append(params_bullets(mqtt_leaf))
        if rest_leaf:
            parts.append("**REST Parameters:**")
            parts.append(params_bullets(rest_leaf))

    parts.append(mqtt_block)
    parts.append(rest_block)

    return "\n\n".join(parts)


def main():
    ops = list(OP_TO_REST.keys())
    print(f"Generating combined descriptions for {len(ops)} operations...")
    for op_name in ops:
        out = generate(op_name)
        dest = os.path.join(OP_DESC_DIR, f"{op_name}.md")
        with open(dest, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"  Updated: {op_name}.md")
    print("Done.")
    print("\nNext steps:")
    print("  python scripts/generate_openapi_tags_md.py")


if __name__ == "__main__":
    main()
