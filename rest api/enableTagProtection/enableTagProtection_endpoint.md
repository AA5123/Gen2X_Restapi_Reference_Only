# Enable Impinj Protected Mode (REST)

Source: docs/rest_openapi.yaml

- Method: `PUT`
- Path: `/cloud/impinjGen2X`
- OperationId: `setImpinjGen2X`
- Content-Type: `application/json`

This request stages TagProtect settings. Use `PUT /cloud/start` with `applyImpinjGen2X: true` to apply staged settings.

## REST Example

### Request Example

```json
{
	"tagProtect": {
		"action": "enableTagProtection",
		"password": "77777777",
		"tagID": "e2801191a5030069073b426d",
		"enableShortRange": true
	}
}
```

### Response Example

```json
""
```

## REST Schema

### Request Schema

```json
{
	"$schema": "https://json-schema.org/draft/2020-12/schema",
	"title": "Enable Impinj Protected Mode Request",
	"type": "object",
	"required": [
		"tagProtect"
	],
	"properties": {
		"tagProtect": {
			"type": "object",
			"required": [
				"action",
				"password",
				"tagID"
			],
			"properties": {
				"action": {
					"type": "string",
					"const": "enableTagProtection",
					"description": "Sets a tag to protected mode."
				},
				"password": {
					"type": "string",
					"description": "8-character hexadecimal 32-bit password used for tag protection.",
					"minLength": 8,
					"maxLength": 8,
					"pattern": "^[0-9A-Fa-f]{8}$"
				},
				"tagID": {
					"type": "string",
					"description": "Hexadecimal tagID (EPC) of the target tag.",
					"pattern": "^([0-9A-Fa-f]{24})+$"
				},
				"enableShortRange": {
					"type": "boolean",
					"description": "Enables short-range protection mode for higher security."
				}
			},
			"additionalProperties": false
		}
	},
	"additionalProperties": false
}
```

### Response Schema

```json
{
	"$schema": "https://json-schema.org/draft/2020-12/schema",
	"title": "Enable Impinj Protected Mode Success Response",
	"description": "From PUT /cloud/impinjGen2X 200 response in docs/rest_openapi.yaml",
	"type": "string",
	"examples": [
		""
	]
}
```
