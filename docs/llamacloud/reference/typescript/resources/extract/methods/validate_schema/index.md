## Validate Extraction Schema

`client.extract.validateSchema(ExtractValidateSchemaParamsbody, RequestOptionsoptions?): ExtractV2SchemaValidateResponse`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `body: ExtractValidateSchemaParams`

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    JSON Schema to validate for use with extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Returns

- `ExtractV2SchemaValidateResponse`

  Response schema for schema validation.

  - `data_schema: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null>`

    Validated JSON Schema, ready for use in extract jobs

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const extractV2SchemaValidateResponse = await client.extract.validateSchema({
  data_schema: { foo: { foo: 'bar' } },
});

console.log(extractV2SchemaValidateResponse.data_schema);
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
