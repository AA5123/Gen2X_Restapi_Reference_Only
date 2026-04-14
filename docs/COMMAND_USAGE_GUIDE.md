# Gen2X Command Usage Guide

Complete operational guide for all Impinj Gen2X REST API commands with practical examples and use cases.

---

## Protected Mode Commands

### Enable Impinj Protected Mode

**Goal:** Protect a specific RFID tag from unauthorized reading by requiring a password.

**When to use:** 
- You want to prevent others from reading or cloning a sensitive tag
- You need to secure high-value items or access credentials on a tag
- You're implementing tag-level security in a multi-reader environment

**What you need:**
- Target tag's EPC ID (Electronic Product Code)
- A 32-bit password (8 hexadecimal characters, e.g., "ABCD1234")

**What happens:**
- The tag becomes invisible to all readers that don't know the password
- The tag stops responding to standard inventory commands
- Only readers that receive the correct password can interact with the tag

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "345d9511-40ac-4aed-894f-006df1205b99",
    "payload": {
      "tagProtect": {
        "action": "enableTagProtection",
        "password": "77777777",
        "tagID": "e2801191a5030069073b426d"
      }
    }
  }'
```

---

### Disable Impinj Protected Mode

**Goal:** Remove password protection from a tag, restoring normal operation.

**When to use:**
- You need to re-enable reading of a previously protected tag
- A tag's protection is no longer needed
- You're transferring a tag to another location or user

**What you need:**
- Target tag's EPC ID
- The EXACT password that was used to protect the tag (you must know it)

**What happens:**
- The tag returns to normal operation mode
- The tag becomes visible and responsive to all readers
- Standard inventory commands work without authentication

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "a157818d-9667-4d9f-8181-114ab48306f6",
    "payload": {
      "tagProtect": {
        "action": "disableTagProtection",
        "password": "77777777",
        "tagID": "e2801191a5030069073b426d"
      }
    }
  }'
```

---

### Enable Inventory of Protected Tags

**Goal:** Temporarily allow your reader to see and inventory protected tags without removing their protection.

**When to use:**
- You need to read inventory of protected tags but leave them protected
- Multiple readers need controlled access to the same protected tags
- You're performing maintenance or auditing protected assets
- You want to verify tags are still present without changing their state

**What you need:**
- The password for the protected tags you want to read
- Permission from the administrator who set the password

**What happens:**
- Your reader gains temporary visibility of protected tags
- The protected tags remain locked for other readers without the password
- You can inventory, read, and report on protected tags
- The tags stay protected for unauthorized readers

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "eb8db4d8-f641-4bdb-9858-302c4dbec101",
    "payload": {
      "tagProtect": {
        "action": "enableTagVisibility",
        "password": "77777777"
      }
    }
  }'
```

---

### Clear Protected Mode Configuration

**Goal:** Revoke your reader's access to protected tags, making them invisible again.

**When to use:**
- You want to stop seeing protected tags
- You need to secure the reader by removing visibility permissions
- You're transferring the reader to a different location or user
- An authorized session with protected tags should end

**What you need:**
- The password you used to enable visibility

**What happens:**
- Your reader loses visibility of protected tags
- Protected tags become invisible to your reader again
- Other readers without the password also can't see these tags
- The tags remain protected on the network

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "3f27e129-a532-488d-8fc8-8699245de663",
    "payload": {
      "tagProtect": {
        "action": "disableTagVisibility",
        "password": "77777777"
      }
    }
  }'
```

---

### Enable Protected Mode with Short Range

**Goal:** Protect a tag AND require readers to be physically close to interact with it.

**When to use:**
- You need both password protection and physical proximity security
- Tags contain critical access credentials (badges, keys)
- You're securing point-of-sale transactions or payments
- You want to prevent long-range tag cloning attacks

**What you need:**
- Target tag's EPC ID
- A 32-bit password for protection
- Knowledge that short-range mode activates proximity enforcement

**What happens:**
- The tag becomes password-protected like standard protection
- Additionally, readers must be within close physical range of the tag
- This prevents remote scanning or RF attacks
- Provides dual-layer security: password + proximity

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "ea05d934-16cf-4fa4-9fa7-4c01f4bd4bea",
    "payload": {
      "tagProtect": {
        "action": "enableTagProtection",
        "password": "77777777",
        "tagID": "e28011b0a5050076c4d7521a",
        "enableShortRange": true
      }
    }
  }'
```

---

## FastID Command

### Enable FastID

**Goal:** Get both the EPC and TID (Tag Identifier) from tags in a single read operation.

**When to use:**
- You need tag identification beyond just the EPC code
- You want to improve inventory speed by eliminating separate TID reads
- Your application requires full tag identification data
- You're optimizing RF performance and reducing scan time

**What you need:**
- Just send the enable command; no tag-specific parameters needed
- Works across all tags in range

**What happens:**
- Each tag inventory response now includes both EPC and TID automatically
- No need for separate read cycles for TID information
- Inventory speed increases; RF traffic decreases
- All tags respond to inventory with complete identification

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "657298d3-98de-421c-9b7c-ad3b53b7474f",
    "payload": {
      "fastID": {
        "enabled": true
      }
    }
  }'
```

---

### Disable FastID

**Goal:** Return to standard inventory mode where tags only report their EPC.

**When to use:**
- You don't need TID information in your application
- You want to reduce response payload size
- You're reducing bandwidth or storage requirements
- You need to simplify data processing on limited devices

**What you need:**
- Just send the disable command

**What happens:**
- Tags return only EPC in inventory responses
- Response data is smaller and faster to process
- If you need TID data, you must perform separate TID read operations
- Standard inventory mode is restored

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "b35808c8-0e10-42a1-8f81-799e7843e5c9",
    "payload": {
      "fastID": {
        "enabled": false
      }
    }
  }'
```

---

## TagFocus Command

### Enable TagFocus

**Goal:** Make the reader focus on NEW tags by silencing tags already read in this session.

**When to use:**
- You have high-density tag environments
- You want to find tags that haven't been read yet
- You're discovering tags in a crowded area
- You need to improve read rates for hard-to-reach tags

**What you need:**
- Just send the enable command; works on all tags

**What happens:**
- Tags that have already been inventoried in this session stay silent
- New or unread tags in range will respond
- The reader concentrates RF energy on finding new tags
- Session S1 memory tracks which tags have been read

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "a3987547-62a8-4005-a064-485524e25bff",
    "payload": {
      "tagFocus": {
        "enabled": true
      }
    }
  }'
```

---

### Disable TagFocus

**Goal:** Return to standard inventory where all tags respond every time.

**When to use:**
- You need to track tag movement continuously
- You want to verify tags are still present (redundancy)
- You're performing a final inventory count
- You need to ensure no tags are missed in reporting

**What you need:**
- Just send the disable command

**What happens:**
- All tags respond to every inventory round
- Tags previously read will respond again
- Inventory may be slower due to duplicate reads
- No session-based tag memory; fresh inventories every time

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "331c364f-ba53-4529-a150-d786f134b27b",
    "payload": {
      "tagFocus": {
        "enabled": false
      }
    }
  }'
```

---

## Tag Quieting Commands

### Quiet Tags

**Goal:** Silence specific tags by their EPC so they don't respond to inventory.

**When to use:**
- You want to exclude certain tags from inventory
- Known bad tags should not appear in reports
- You need to test reader performance without interference from specific tags
- You're isolating problem tags for troubleshooting

**What you need:**
- List of tag EPCs you want to silence (up to 31 tags at once)

**What happens:**
- Listed tags stop responding to inventory commands
- They won't appear in any inventory reports
- Other tags continue normal operation
- Quieted tags remain silent until unquieted

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "43505552-cb1b-406c-a027-cf101f576034",
    "payload": {
      "tagQuieting": {
        "basic": {
          "action": "quiet",
          "tagIDs": [
            "e28011b0a5050076c4d751e9",
            "e28011b0a5050076c4d77307",
            "e28011b0a5050076c4d751ec"
          ]
        }
      }
    }
  }'
```

---

### Unquiet Tags

**Goal:** Restore silenced tags to normal operation.

**When to use:**
- You need to include previously silenced tags in inventory again
- A problem with a tag has been fixed
- You're restoring tags to full operation
- You need to verify silenced tags are still present

**What you need:**
- List of tag EPCs that should resume operation
- Must be the exact EPCs you quieted earlier

**What happens:**
- Listed tags resume normal responding
- They will appear in inventory again
- Other tags remain in their current state
- Only specified tags are restored

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "set_impinjGen2X",
    "command_id": "4c352333-3869-43e1-bba8-eda8692d8c40",
    "payload": {
      "tagQuieting": {
        "basic": {
          "action": "unquiet",
          "tagIDs": [
            "e28011b0a5050076c4d751e9",
            "e28011b0a5050076c4d77307"
          ]
        }
      }
    }
  }'
```

---

## Configuration Commands

### Get Gen2X Configuration

**Goal:** Check what Gen2X settings are currently saved on the reader.

**When to use:**
- You need to audit current settings before making changes
- You want to verify configuration was applied correctly
- You're troubleshooting unexpected behavior
- You need to document the current state

**What you need:**
- Nothing; just query the current state

**What happens:**
- Returns all enabled Gen2X features and their settings
- Shows Protected Mode configurations if any
- Lists quieted tags if any are silent
- Shows FastID and TagFocus status

**Example Request:**
```bash
curl -X GET https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

**Example Response:**
```json
{
  "command": "get_impinjGen2X",
  "command_id": "9d744286-7b97-40b8-9e91-190df0334557",
  "payload": {
    "fastID": {
      "enabled": true,
      "tidSelector": "TID[0]"
    },
    "tagFocus": {
      "enabled": true
    },
    "tagQuieting": {
      "basic": {
        "action": "quiet",
        "tagIDs": ["e28011b0a5050076c4d751e9"]
      }
    }
  },
  "response": "success"
}
```

---

## Control Commands

### Start IoT Cloud Service

**Goal:** Start the reader and apply all staged Gen2X configuration changes.

**When to use:**
- You've finished configuring all Gen2X settings
- You want to activate your configuration changes
- You must stop the reader before changing config, so start applies them
- You're ready to begin inventory with new settings

**What you need:**
- Set `applyImpinjGen2X` to `true` to activate staged configuration
- Must have called stop first, before making configuration changes

**What happens:**
- Reader starts up immediately
- All Gen2X settings you staged are now active
- Tags respond according to your configuration
- Inventory operations begin with new settings

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/start \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "start",
    "command_id": "81dd51a2-b0d3-4099-b46a-5a3f82796ba1",
    "payload": {
      "applyImpinjGen2X": true
    }
  }'
```

---

### Stop IoT Cloud Service

**Goal:** Stop the reader so you can safely change Gen2X configuration.

**When to use:**
- Before making ANY Gen2X configuration changes
- You need to prevent tag responses while reconfiguring
- You're applying new Protected Mode or FastID settings
- Configuration changes must be staged while reader is stopped

**What you need:**
- Just send the stop command

**What happens:**
- Reader stops immediately
- All RF operations cease
- Reader becomes idle and ready for configuration
- No inventory or tag interaction occurs
- You can now make configuration changes safely

**Example Request:**
```bash
curl -X PUT https://10.233.48.49/cloud/stop \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "stop",
    "command_id": "c3f1a2b4-5678-4def-abcd-123456789abc",
    "payload": {}
  }'
```

---

## Workflow Examples

### Example 1: Enable Protected Mode and Verify

```bash
# Step 1: Stop the reader
curl -X PUT https://10.233.48.49/cloud/stop \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"command":"stop","command_id":"uuid1","payload":{}}'

# Step 2: Enable protection on a specific tag
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command":"set_impinjGen2X",
    "command_id":"uuid2",
    "payload":{
      "tagProtect":{
        "action":"enableTagProtection",
        "password":"ABCD1234",
        "tagID":"e2801191a5030069073b426d"
      }
    }
  }'

# Step 3: Check the configuration was staged
curl -X GET https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN"

# Step 4: Start the reader and apply settings
curl -X PUT https://10.233.48.49/cloud/start \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"command":"start","command_id":"uuid3","payload":{"applyImpinjGen2X":true}}'
```

### Example 2: Enable FastID and TagFocus for Better Performance

```bash
# Stop reader
curl -X PUT https://10.233.48.49/cloud/stop \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"command":"stop","command_id":"uuid1","payload":{}}'

# Enable FastID
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "command":"set_impinjGen2X",
    "command_id":"uuid2",
    "payload":{"fastID":{"enabled":true}}
  }'

# Enable TagFocus
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "command":"set_impinjGen2X",
    "command_id":"uuid3",
    "payload":{"tagFocus":{"enabled":true}}
  }'

# Start and apply
curl -X PUT https://10.233.48.49/cloud/start \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"command":"start","command_id":"uuid4","payload":{"applyImpinjGen2X":true}}'
```

### Example 3: Quiet Problematic Tags and Continue Inventory

```bash
# Stop reader
curl -X PUT https://10.233.48.49/cloud/stop \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"command":"stop","command_id":"uuid1","payload":{}}'

# Quiet the problematic tags
curl -X PUT https://10.233.48.49/cloud/impinjGen2X \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "command":"set_impinjGen2X",
    "command_id":"uuid2",
    "payload":{
      "tagQuieting":{
        "basic":{
          "action":"quiet",
          "tagIDs":["e28011b0a5050076c4d751e9","e28011b0a5050076c4d77307"]
        }
      }
    }
  }'

# Start and apply configuration
curl -X PUT https://10.233.48.49/cloud/start \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"command":"start","command_id":"uuid3","payload":{"applyImpinjGen2X":true}}'

# Now inventory will exclude the quieted tags
```

---

## Authentication

Before using any command, authenticate with the reader:

```bash
curl -X POST https://10.233.48.49/cloud/localRestLogin \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "your_reader_password"
  }'
```

This returns an access token that you include in all subsequent requests:
```bash
-H "Authorization: Bearer YOUR_RETURNED_TOKEN"
```

---

## Standard Return Codes

All commands return either `success` or `failure` status.

**Success Response:**
```json
{
  "command": "command_name",
  "command_id": "unique_uuid",
  "payload": {
    "message": "Success message"
  },
  "response": "success"
}
```

**Failure Response:**
```json
{
  "command": "command_name",
  "command_id": "unique_uuid",
  "payload": {
    "message": "Error description"
  },
  "response": "failure"
}
```

---

## Key Parameters Reference

| Parameter | Format | Example | Notes |
|-----------|--------|---------|-------|
| **tagID** | Hex string | `e2801191a5030069073b426d` | 24-character EPC |
| **password** | 8 hex chars | `ABCD1234` | Must be exactly 8 characters |
| **host** | IP address | `10.233.48.49` | Reader's network IP |
| **port** | Number | `80` or `443` | Default depends on HTTP/HTTPS |
| **command_id** | UUID | `a1b2c3d4-e5f6-7890-1234-567890abcdef` | Unique per request |
