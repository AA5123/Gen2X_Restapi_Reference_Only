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
    "enable_tag_protection":  ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "disable_tag_protection": ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "enable_tag_visibility":  ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "disable_tag_visibility": ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "enable_short_range":     ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "enable_fastid":          ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "disable_fastid":         ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "enable_tagfocus":        ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "disable_tagfocus":       ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "quiet_tags":             ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "unquiet_tags":           ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"),
    "get_gen2x_config":       ("GET", "/cloud/impinjGen2X", "getImpinjGen2X"),
    "start":                  ("PUT", "/cloud/start",       "startIotCloudService"),
    "stop":                   ("PUT", "/cloud/stop",        "stopIotCloudService"),
}

# ── REST staging notes (shown below endpoint table) ───────────────────────────
REST_NOTES = {
    "enable_tag_protection":  "This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "disable_tag_protection": "This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "enable_tag_visibility":  "This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "disable_tag_visibility": "This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "enable_short_range":     "This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "enable_fastid":          "This request stages FastID settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "disable_fastid":         "This request stages FastID settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "enable_tagfocus":        "This request stages TagFocus settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "disable_tagfocus":       "This request stages TagFocus settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "quiet_tags":             "This request stages Tag Quieting settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "unquiet_tags":           "This request stages Tag Quieting settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.",
    "get_gen2x_config":       "Returns the current Gen2X configuration as last saved. Returns an empty object if no configuration has been set.",
    "start":                  "Set `applyImpinjGen2X: true` to apply all previously staged Gen2X settings when starting the radio.",
    "stop":                   "Stop the radio before making any Gen2X configuration changes.",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_existing_md(text):
    """Extract Description, Usage, and Persistence from existing .md file."""
    def extract_section(heading, src):
        pattern = rf"\*\*{re.escape(heading)}:\*\*\s*\n(.*?)(?=\n\*\*[A-Z]|\Z)"
        m = re.search(pattern, src, re.DOTALL)
        return m.group(1).strip() if m else ""

    desc = extract_section("Description", text)
    usage = extract_section("Usage", text)
    persist = extract_section("Persistence", text)
    if persist:
        usage += f"\n\n**Persistence:** {persist}"
    return desc, usage


def flatten_props(schema, prefix="", parent_required=None):
    """
    Recursively flatten JSON schema properties into rows:
    [{name, type, required, description}, ...]
    """
    if not schema:
        return []
    props = schema.get("properties", {})
    if not props:
        return []
    required = parent_required if parent_required is not None else schema.get("required", [])
    rows = []
    for key, prop in props.items():
        full = f"{prefix}.{key}" if prefix else key
        ptype = prop.get("type", "object")

        desc = prop.get("description", "")
        if "const" in prop:
            desc = (desc + f" Must be `{prop['const']}`").strip()
        if prop.get("enum") and "const" not in prop:
            enums = ", ".join(f"`{v}`" for v in prop["enum"])
            desc = (desc + f" One of: {enums}.").strip()
        if prop.get("minLength") and prop.get("maxLength"):
            desc = (desc + f" ({prop['minLength']}–{prop['maxLength']} chars)").strip()
        elif prop.get("minLength"):
            desc = (desc + f" (min {prop['minLength']} chars)").strip()
        elif prop.get("maxLength"):
            desc = (desc + f" (max {prop['maxLength']} chars)").strip()
        if prop.get("pattern"):
            desc = (desc + f" Pattern: `{prop['pattern']}`").strip()
        if prop.get("format"):
            desc = (desc + f" Format: {prop['format']}").strip()

        is_required = key in required

        if ptype == "object" and "properties" in prop:
            rows.append({"name": full, "type": "object", "required": is_required, "description": desc})
            child_req = prop.get("required", [])
            rows.extend(flatten_props(prop, full, child_req))
        elif ptype == "array":
            items = prop.get("items", {})
            item_type = items.get("type", "string") if items else "string"
            desc = (desc + f" Array of {item_type} values.").strip()
            rows.append({"name": full, "type": "array", "required": is_required, "description": desc})
        else:
            rows.append({"name": full, "type": ptype, "required": is_required, "description": desc})
    return rows


def params_table(rows):
    """Render a list of param rows as a markdown table."""
    if not rows:
        return "_No parameters required._\n"
    lines = [
        "| Parameter | Type | Required | Description |",
        "|-----------|------|:--------:|-------------|",
    ]
    for r in rows:
        req = "Yes" if r["required"] else "No"
        desc = r["description"] or ""
        lines.append(f"| `{r['name']}` | {r['type']} | {req} | {desc} |")
    return "\n".join(lines) + "\n"


def mqtt_params_from_cmd(cmd_schema):
    """Extract only payload-level parameters (skip command/command_id)."""
    payload = cmd_schema.get("properties", {}).get("payload", {})
    payload_req = payload.get("required", [])
    return flatten_props(payload, "", payload_req)


def rest_params_from_schema(rest_schema):
    """Extract REST request parameters from request_schema JSON."""
    if not rest_schema:
        return []
    top_req = rest_schema.get("required", [])
    return flatten_props(rest_schema, "", top_req)


def get_mqtt_command_name(cmd_schema):
    return (
        cmd_schema.get("properties", {})
        .get("command", {})
        .get("const", "set_impinjGen2X")
    )


# ── Main generator ────────────────────────────────────────────────────────────

def generate(op_name):
    # Load existing narrative
    md_path = os.path.join(OP_DESC_DIR, f"{op_name}.md")
    if os.path.exists(md_path):
        with open(md_path, encoding="utf-8") as f:
            existing = f.read()
        description, usage = parse_existing_md(existing)
    else:
        description, usage = "", ""

    # Load MQTT command schema
    cmd_path = os.path.join(CMD_DIR, f"{op_name}.json")
    cmd_schema = load_json(cmd_path) if os.path.exists(cmd_path) else {}
    mqtt_cmd = get_mqtt_command_name(cmd_schema)
    mqtt_params = mqtt_params_from_cmd(cmd_schema)

    # Load REST request schema
    rest_folder = OP_TO_REST.get(op_name, "")
    rest_schema_path = os.path.join(REST_API_DIR, rest_folder, f"{rest_folder}_request_schema.json")
    rest_schema = load_json(rest_schema_path) if os.path.exists(rest_schema_path) else {}
    rest_params = rest_params_from_schema(rest_schema)

    # REST endpoint details
    method, path, op_id = REST_ENDPOINT.get(op_name, ("PUT", "/cloud/impinjGen2X", "setImpinjGen2X"))
    rest_note = REST_NOTES.get(op_name, "")

    # ── Build markdown ────────────────────────────────────────────────────────
    lines = []

    lines.append("**Description:**")
    lines.append(description or "")
    lines.append("")

    lines.append("**Usage:**")
    lines.append(usage or "")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Compare MQTT and REST parameters for merging
    def param_rows_key(rows):
        # Only compare name/type/required/description
        return [ (r['name'], r['type'], r['required'], r['description']) for r in rows ]

    merged = param_rows_key(mqtt_params) == param_rows_key(rest_params)

    # Colored headings (HTML for docs UI)
    mqtt_heading = '<div style="background:#e0f7fa;padding:6px 12px;font-weight:600;border-radius:4px;color:#006064;margin-bottom:4px;">MQTT Endpoint Details</div>'
    rest_heading = '<div style="background:#e8eaf6;padding:6px 12px;font-weight:600;border-radius:4px;color:#1a237e;margin-bottom:4px;">REST Endpoint Details</div>'

    # Colored method badge
    method_badge = f'<span style="display:inline-block;background:#ffd54f;color:#795548;font-weight:700;padding:2px 10px;border-radius:12px;margin-right:8px;">{method}</span>'

    if merged:
        lines.append(mqtt_heading)
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Command | `{mqtt_cmd}` |")
        lines.append("")

        lines.append(rest_heading)
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Method | {method_badge}`{method}` |")
        lines.append(f"| Path | `{path}` |")
        lines.append(f"| OperationId | `{op_id}` |")
        lines.append(f"| Content-Type | `application/json` |")
        lines.append("")
        if rest_note:
            lines.append(f"> {rest_note}")
            lines.append("")

        lines.append('**Parameters (MQTT & REST)**')
        lines.append("")
        lines.append('_The following parameters apply to both MQTT and REST unless otherwise noted._\n')
        lines.append(params_table(mqtt_params))
    else:
        lines.append(mqtt_heading)
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Command | `{mqtt_cmd}` |")
        lines.append("")
        lines.append('**MQTT Parameters**')
        lines.append("")
        lines.append(params_table(mqtt_params))

        lines.append(rest_heading)
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Method | {method_badge}`{method}` |")
        lines.append(f"| Path | `{path}` |")
        lines.append(f"| OperationId | `{op_id}` |")
        lines.append(f"| Content-Type | `application/json` |")
        lines.append("")
        if rest_note:
            lines.append(f"> {rest_note}")
            lines.append("")
        lines.append('**REST Parameters**')
        lines.append("")
        lines.append(params_table(rest_params))

    return "\n".join(lines)


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
