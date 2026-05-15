## Validate Extraction Schema

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Cookie Parameters

- `session: optional string`

### Body Parameters

- `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

  JSON Schema to validate for use with extract jobs

  - `map[unknown]`

  - `array of unknown`

  - `string`

  - `number`

  - `boolean`

### Returns

- `ExtractV2SchemaValidateResponse = object { data_schema }`

  Response schema for schema validation.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    Validated JSON Schema, ready for use in extract jobs

    - `map[unknown]`

    - `array of unknown`

    - `string`

    - `number`

    - `boolean`

### Example

```http
curl https://api.cloud.llamaindex.ai/api/v2/extract/schema/validation \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    -d '{
          "data_schema": {
            "foo": {
              "foo": "bar"
            }
          }
        }'
```

#### Response

```json
{
  "data_schema": {
    "foo": {
      "foo": "bar"
    }
  }
}
```
