## Validate Extraction Schema

`client.Extract.ValidateSchema(ctx, body) (*ExtractV2SchemaValidateResponse, error)`

**post** `/api/v2/extract/schema/validation`

Validate a JSON schema for extraction.

### Parameters

- `body ExtractValidateSchemaParams`

  - `ExtractV2SchemaValidateRequest param.Field[ExtractV2SchemaValidateRequest]`

    Request schema for validating an extraction schema.

### Returns

- `type ExtractV2SchemaValidateResponse struct{…}`

  Response schema for schema validation.

  - `DataSchema map[string, ExtractV2SchemaValidateResponseDataSchemaUnion]`

    Validated JSON Schema, ready for use in extract jobs

    - `type ExtractV2SchemaValidateResponseDataSchemaMap map[string, any]`

    - `type ExtractV2SchemaValidateResponseDataSchemaArray []any`

    - `string`

    - `float64`

    - `bool`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/stainless-sdks/llamacloud-prod-go"
  "github.com/stainless-sdks/llamacloud-prod-go/option"
)

func main() {
  client := llamacloudprod.NewClient(
    option.WithAPIKey("My API Key"),
  )
  extractV2SchemaValidateResponse, err := client.Extract.ValidateSchema(context.TODO(), llamacloudprod.ExtractValidateSchemaParams{
    ExtractV2SchemaValidateRequest: llamacloudprod.ExtractV2SchemaValidateRequestParam{
      DataSchema: map[string]llamacloudprod.ExtractV2SchemaValidateRequestDataSchemaUnionParam{
      "properties": llamacloudprod.ExtractV2SchemaValidateRequestDataSchemaUnionParam{
        OfAnyMap: map[string]any{
        "vendor_name": "bar",
        "invoice_number": "bar",
        "total_amount": "bar",
        "line_items": "bar",
        },
      },
      "required": llamacloudprod.ExtractV2SchemaValidateRequestDataSchemaUnionParam{
        OfAnyArray: []any{"vendor_name", "invoice_number", "total_amount"},
      },
      "type": llamacloudprod.ExtractV2SchemaValidateRequestDataSchemaUnionParam{
        OfString: llamacloudprod.String("object"),
      },
      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", extractV2SchemaValidateResponse.DataSchema)
}
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
