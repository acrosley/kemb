## Validate Extraction Schema

`$ llamacloud-prod extract validate-schema`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `--data-schema: map[map[unknown] or array of unknown or string or 2 more]`

  JSON Schema to validate for use with extract jobs

### Returns

- `extract_v2_schema_validate_response: object { data_schema }`

  Response schema for schema validation.

  - `data_schema: map[map[unknown] or array of unknown or string or 2 more]`

    Validated JSON Schema, ready for use in extract jobs

    - `union_member_0: map[unknown]`

    - `union_member_1: array of unknown`

    - `union_member_2: string`

    - `union_member_3: number`

    - `union_member_4: boolean`

### Example

```cli
llamacloud-prod extract validate-schema \
  --api-key 'My API Key' \
  --data-schema '{foo: {foo: bar}}'
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
