## Validate Extraction Schema

`extract.validate_schema(ExtractValidateSchemaParams**kwargs)  -> ExtractV2SchemaValidateResponse`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `data_schema: Dict[str, Union[Dict[str, object], Iterable[object], str, 3 more]]`

  JSON Schema to validate for use with extract jobs

  - `Dict[str, object]`

  - `Iterable[object]`

  - `str`

  - `float`

  - `bool`

### Returns

- `class ExtractV2SchemaValidateResponse: …`

  Response schema for schema validation.

  - `data_schema: Dict[str, Union[Dict[str, object], List[object], str, 3 more]]`

    Validated JSON Schema, ready for use in extract jobs

    - `Dict[str, object]`

    - `List[object]`

    - `str`

    - `float`

    - `bool`

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
extract_v2_schema_validate_response = client.extract.validate_schema(
    data_schema={
        "foo": {
            "foo": "bar"
        }
    },
)
print(extract_v2_schema_validate_response.data_schema)
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
