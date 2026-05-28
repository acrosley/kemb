# Classifier

# Jobs

## Create Classify Job

`client.Classifier.Jobs.New(ctx, params) (*ClassifyJob, error)`

**post** `/api/v1/classifier/jobs`

Create a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `params ClassifierJobNewParams`

  - `FileIDs param.Field[[]string]`

    Body param: The IDs of the files to classify

  - `Rules param.Field[[]ClassifierRule]`

    Body param: The rules to classify the files

    - `Description string`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `Type string`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `OrganizationID param.Field[string]`

    Query param

  - `ProjectID param.Field[string]`

    Query param

  - `Mode param.Field[ClassifierJobNewParamsMode]`

    Body param: The classification mode to use

    - `const ClassifierJobNewParamsModeFast ClassifierJobNewParamsMode = "FAST"`

    - `const ClassifierJobNewParamsModeMultimodal ClassifierJobNewParamsMode = "MULTIMODAL"`

  - `ParsingConfiguration param.Field[ClassifyParsingConfiguration]`

    Body param: The configuration for the parsing job

  - `WebhookConfigurations param.Field[[]ClassifierJobNewParamsWebhookConfiguration]`

    Body param: List of webhook configurations for notifications

    - `WebhookEvents []string`

      Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

    - `WebhookHeaders map[string, any]`

      Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

    - `WebhookURL string`

      HTTPS URL to receive webhook POST requests. Must be publicly accessible

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
  classifyJob, err := client.Classifier.Jobs.New(context.TODO(), llamacloudprod.ClassifierJobNewParams{
    FileIDs: []string{"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
    Rules: []llamacloudprod.ClassifierRuleParam{llamacloudprod.ClassifierRuleParam{
      Description: "contains invoice number, line items, and total amount",
      Type: "invoice",
    }},
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", classifyJob.ID)
}
```

#### Response

```json
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
```

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

## Get Classify Job

`client.Classifier.Jobs.Get(ctx, classifyJobID, query) (*ClassifyJob, error)`

**get** `/api/v1/classifier/jobs/{classify_job_id}`

Get a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classifyJobID string`

- `query ClassifierJobGetParams`

  - `OrganizationID param.Field[string]`

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
  classifyJob, err := client.Classifier.Jobs.Get(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.ClassifierJobGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", classifyJob.ID)
}
```

#### Response

```json
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
```

## Get Classification Job Results

`client.Classifier.Jobs.GetResults(ctx, classifyJobID, query) (*ClassifierJobGetResultsResponse, error)`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classifyJobID string`

- `query ClassifierJobGetResultsParams`

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ClassifierJobGetResultsResponse struct{…}`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `Items []ClassifierJobGetResultsResponseItem`

    The list of items.

    - `ID string`

      Unique identifier

    - `ClassifyJobID string`

      The ID of the classify job

    - `CreatedAt Time`

      Creation datetime

    - `FileID string`

      The ID of the classified file

    - `Result ClassifierJobGetResultsResponseItemResult`

      Result of classifying a single file.

      - `Confidence float64`

        Confidence score of the classification (0.0-1.0)

      - `Reasoning string`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `Type string`

        The document type that best matches, or null if no match.

    - `UpdatedAt Time`

      Update datetime

  - `NextPageToken string`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `TotalSize int64`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

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
  response, err := client.Classifier.Jobs.GetResults(
    context.TODO(),
    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    llamacloudprod.ClassifierJobGetResultsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Items)
}
```

#### Response

```json
{
  "items": [
    {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "classify_job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "created_at": "2019-12-27T18:11:19.117Z",
      "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "result": {
        "confidence": 0,
        "reasoning": "reasoning",
        "type": "type"
      },
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page_token": "next_page_token",
  "total_size": 0
}
```

## Domain Types

### Classifier Rule

- `type ClassifierRule struct{…}`

  A rule for classifying documents - v0 simplified version.

  This represents a single classification rule that will be applied to documents.
  All rules are content-based and use natural language descriptions.

  - `Description string`

    Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

  - `Type string`

    The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

### Classify Job

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

### Classify Parsing Configuration

- `type ClassifyParsingConfiguration struct{…}`

  Parsing configuration for a classify job.

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
