## List Classify Jobs

`client.Classifier.Jobs.List(ctx, query) (*PaginatedCursor[ClassifyJob], error)`

**get** `/api/v1/classifier/jobs`

List classify jobs.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `query ClassifierJobListParams`

  - `OrganizationID param.Field[string]`

  - `PageSize param.Field[int64]`

  - `PageToken param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ClassifyJob struct{…}`

  A classify job.

  - `ID string`

    Unique identifier

  - `ProjectID string`

    The ID of the project

  - `Rules []ClassifierRule`

    The rules to classify the files

    - `Description string`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `Type string`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `Status StatusEnum`

    The status of the classify job

    - `const StatusEnumPending StatusEnum = "PENDING"`

    - `const StatusEnumSuccess StatusEnum = "SUCCESS"`

    - `const StatusEnumError StatusEnum = "ERROR"`

    - `const StatusEnumPartialSuccess StatusEnum = "PARTIAL_SUCCESS"`

    - `const StatusEnumCancelled StatusEnum = "CANCELLED"`

  - `UserID string`

    The ID of the user

  - `CreatedAt Time`

    Creation datetime

  - `EffectiveAt Time`

  - `ErrorMessage string`

    Error message for the latest job attempt, if any.

  - `JobRecordID string`

    The job record ID associated with this status, if any.

  - `Mode ClassifyJobMode`

    The classification mode to use

    - `const ClassifyJobModeFast ClassifyJobMode = "FAST"`

    - `const ClassifyJobModeMultimodal ClassifyJobMode = "MULTIMODAL"`

  - `ParsingConfiguration ClassifyParsingConfiguration`

    The configuration for the parsing job

    - `Lang ParsingLanguages`

      The language to parse the files in

      - `const ParsingLanguagesAf ParsingLanguages = "af"`

      - `const ParsingLanguagesAz ParsingLanguages = "az"`

      - `const ParsingLanguagesBs ParsingLanguages = "bs"`

      - `const ParsingLanguagesCs ParsingLanguages = "cs"`

      - `const ParsingLanguagesCy ParsingLanguages = "cy"`

      - `const ParsingLanguagesDa ParsingLanguages = "da"`

      - `const ParsingLanguagesDe ParsingLanguages = "de"`

      - `const ParsingLanguagesEn ParsingLanguages = "en"`

      - `const ParsingLanguagesEs ParsingLanguages = "es"`

      - `const ParsingLanguagesEt ParsingLanguages = "et"`

      - `const ParsingLanguagesFr ParsingLanguages = "fr"`

      - `const ParsingLanguagesGa ParsingLanguages = "ga"`

      - `const ParsingLanguagesHr ParsingLanguages = "hr"`

      - `const ParsingLanguagesHu ParsingLanguages = "hu"`

      - `const ParsingLanguagesID ParsingLanguages = "id"`

      - `const ParsingLanguagesIs ParsingLanguages = "is"`

      - `const ParsingLanguagesIt ParsingLanguages = "it"`

      - `const ParsingLanguagesKu ParsingLanguages = "ku"`

      - `const ParsingLanguagesLa ParsingLanguages = "la"`

      - `const ParsingLanguagesLt ParsingLanguages = "lt"`

      - `const ParsingLanguagesLv ParsingLanguages = "lv"`

      - `const ParsingLanguagesMi ParsingLanguages = "mi"`

      - `const ParsingLanguagesMs ParsingLanguages = "ms"`

      - `const ParsingLanguagesMt ParsingLanguages = "mt"`

      - `const ParsingLanguagesNl ParsingLanguages = "nl"`

      - `const ParsingLanguagesNo ParsingLanguages = "no"`

      - `const ParsingLanguagesOc ParsingLanguages = "oc"`

      - `const ParsingLanguagesPi ParsingLanguages = "pi"`

      - `const ParsingLanguagesPl ParsingLanguages = "pl"`

      - `const ParsingLanguagesPt ParsingLanguages = "pt"`

      - `const ParsingLanguagesRo ParsingLanguages = "ro"`

      - `const ParsingLanguagesRsLatin ParsingLanguages = "rs_latin"`

      - `const ParsingLanguagesSk ParsingLanguages = "sk"`

      - `const ParsingLanguagesSl ParsingLanguages = "sl"`

      - `const ParsingLanguagesSq ParsingLanguages = "sq"`

      - `const ParsingLanguagesSv ParsingLanguages = "sv"`

      - `const ParsingLanguagesSw ParsingLanguages = "sw"`

      - `const ParsingLanguagesTl ParsingLanguages = "tl"`

      - `const ParsingLanguagesTr ParsingLanguages = "tr"`

      - `const ParsingLanguagesUz ParsingLanguages = "uz"`

      - `const ParsingLanguagesVi ParsingLanguages = "vi"`

      - `const ParsingLanguagesAr ParsingLanguages = "ar"`

      - `const ParsingLanguagesFa ParsingLanguages = "fa"`

      - `const ParsingLanguagesUg ParsingLanguages = "ug"`

      - `const ParsingLanguagesUr ParsingLanguages = "ur"`

      - `const ParsingLanguagesBn ParsingLanguages = "bn"`

      - `const ParsingLanguagesAs ParsingLanguages = "as"`

      - `const ParsingLanguagesMni ParsingLanguages = "mni"`

      - `const ParsingLanguagesRu ParsingLanguages = "ru"`

      - `const ParsingLanguagesRsCyrillic ParsingLanguages = "rs_cyrillic"`

      - `const ParsingLanguagesBe ParsingLanguages = "be"`

      - `const ParsingLanguagesBg ParsingLanguages = "bg"`

      - `const ParsingLanguagesUk ParsingLanguages = "uk"`

      - `const ParsingLanguagesMn ParsingLanguages = "mn"`

      - `const ParsingLanguagesAbq ParsingLanguages = "abq"`

      - `const ParsingLanguagesAdy ParsingLanguages = "ady"`

      - `const ParsingLanguagesKbd ParsingLanguages = "kbd"`

      - `const ParsingLanguagesAva ParsingLanguages = "ava"`

      - `const ParsingLanguagesDar ParsingLanguages = "dar"`

      - `const ParsingLanguagesInh ParsingLanguages = "inh"`

      - `const ParsingLanguagesChe ParsingLanguages = "che"`

      - `const ParsingLanguagesLbe ParsingLanguages = "lbe"`

      - `const ParsingLanguagesLez ParsingLanguages = "lez"`

      - `const ParsingLanguagesTab ParsingLanguages = "tab"`

      - `const ParsingLanguagesTjk ParsingLanguages = "tjk"`

      - `const ParsingLanguagesHi ParsingLanguages = "hi"`

      - `const ParsingLanguagesMr ParsingLanguages = "mr"`

      - `const ParsingLanguagesNe ParsingLanguages = "ne"`

      - `const ParsingLanguagesBh ParsingLanguages = "bh"`

      - `const ParsingLanguagesMai ParsingLanguages = "mai"`

      - `const ParsingLanguagesAng ParsingLanguages = "ang"`

      - `const ParsingLanguagesBho ParsingLanguages = "bho"`

      - `const ParsingLanguagesMah ParsingLanguages = "mah"`

      - `const ParsingLanguagesSck ParsingLanguages = "sck"`

      - `const ParsingLanguagesNew ParsingLanguages = "new"`

      - `const ParsingLanguagesGom ParsingLanguages = "gom"`

      - `const ParsingLanguagesSa ParsingLanguages = "sa"`

      - `const ParsingLanguagesBgc ParsingLanguages = "bgc"`

      - `const ParsingLanguagesTh ParsingLanguages = "th"`

      - `const ParsingLanguagesChSim ParsingLanguages = "ch_sim"`

      - `const ParsingLanguagesChTra ParsingLanguages = "ch_tra"`

      - `const ParsingLanguagesJa ParsingLanguages = "ja"`

      - `const ParsingLanguagesKo ParsingLanguages = "ko"`

      - `const ParsingLanguagesTa ParsingLanguages = "ta"`

      - `const ParsingLanguagesTe ParsingLanguages = "te"`

      - `const ParsingLanguagesKn ParsingLanguages = "kn"`

    - `MaxPages int64`

      The maximum number of pages to parse

    - `TargetPages []int64`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `UpdatedAt Time`

    Update datetime

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
  page, err := client.Classifier.Jobs.List(context.TODO(), llamacloudprod.ClassifierJobListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "items": [
    {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "rules": [
        {
          "description": "contains invoice number, line items, and total amount",
          "type": "invoice"
        }
      ],
      "status": "PENDING",
      "user_id": "user_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "effective_at": "2019-12-27T18:11:19.117Z",
      "error_message": "error_message",
      "job_record_id": "job_record_id",
      "mode": "FAST",
      "parsing_configuration": {
        "lang": "af",
        "max_pages": 0,
        "target_pages": [
          0
        ]
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```
