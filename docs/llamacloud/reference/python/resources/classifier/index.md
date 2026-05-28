# Classifier

# Jobs

## Create Classify Job

`classifier.jobs.create(JobCreateParams**kwargs)  -> ClassifyJob`

**post** `/api/v1/classifier/jobs`

Create a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `file_ids: SequenceNotStr[str]`

  The IDs of the files to classify

- `rules: Iterable[ClassifierRuleParam]`

  The rules to classify the files

  - `description: str`

    Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

  - `type: str`

    The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

- `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

  The classification mode to use

  - `"FAST"`

  - `"MULTIMODAL"`

- `parsing_configuration: Optional[ClassifyParsingConfigurationParam]`

  The configuration for the parsing job

  - `lang: Optional[ParsingLanguages]`

    The language to parse the files in

    - `"af"`

    - `"az"`

    - `"bs"`

    - `"cs"`

    - `"cy"`

    - `"da"`

    - `"de"`

    - `"en"`

    - `"es"`

    - `"et"`

    - `"fr"`

    - `"ga"`

    - `"hr"`

    - `"hu"`

    - `"id"`

    - `"is"`

    - `"it"`

    - `"ku"`

    - `"la"`

    - `"lt"`

    - `"lv"`

    - `"mi"`

    - `"ms"`

    - `"mt"`

    - `"nl"`

    - `"no"`

    - `"oc"`

    - `"pi"`

    - `"pl"`

    - `"pt"`

    - `"ro"`

    - `"rs_latin"`

    - `"sk"`

    - `"sl"`

    - `"sq"`

    - `"sv"`

    - `"sw"`

    - `"tl"`

    - `"tr"`

    - `"uz"`

    - `"vi"`

    - `"ar"`

    - `"fa"`

    - `"ug"`

    - `"ur"`

    - `"bn"`

    - `"as"`

    - `"mni"`

    - `"ru"`

    - `"rs_cyrillic"`

    - `"be"`

    - `"bg"`

    - `"uk"`

    - `"mn"`

    - `"abq"`

    - `"ady"`

    - `"kbd"`

    - `"ava"`

    - `"dar"`

    - `"inh"`

    - `"che"`

    - `"lbe"`

    - `"lez"`

    - `"tab"`

    - `"tjk"`

    - `"hi"`

    - `"mr"`

    - `"ne"`

    - `"bh"`

    - `"mai"`

    - `"ang"`

    - `"bho"`

    - `"mah"`

    - `"sck"`

    - `"new"`

    - `"gom"`

    - `"sa"`

    - `"bgc"`

    - `"th"`

    - `"ch_sim"`

    - `"ch_tra"`

    - `"ja"`

    - `"ko"`

    - `"ta"`

    - `"te"`

    - `"kn"`

  - `max_pages: Optional[int]`

    The maximum number of pages to parse

  - `target_pages: Optional[List[int]]`

    The pages to target for parsing (0-indexed, so first page is at 0)

- `webhook_configurations: Optional[Iterable[WebhookConfiguration]]`

  List of webhook configurations for notifications

  - `webhook_events: Optional[SequenceNotStr[str]]`

    Events that trigger this webhook. Options: 'parse.success' (job completed), 'parse.failure' (job failed), 'parse.partial' (some pages failed). If not specified, webhook fires for all events

  - `webhook_headers: Optional[Dict[str, object]]`

    Custom HTTP headers to include in webhook requests. Use for authentication tokens or custom routing. Example: {'Authorization': 'Bearer xyz'}

  - `webhook_url: Optional[str]`

    HTTPS URL to receive webhook POST requests. Must be publicly accessible

### Returns

- `class ClassifyJob: …`

  A classify job.

  - `id: str`

    Unique identifier

  - `project_id: str`

    The ID of the project

  - `rules: List[ClassifierRule]`

    The rules to classify the files

    - `description: str`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `type: str`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `status: StatusEnum`

    The status of the classify job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `user_id: str`

    The ID of the user

  - `created_at: Optional[datetime]`

    Creation datetime

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

    The classification mode to use

    - `"FAST"`

    - `"MULTIMODAL"`

  - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

    The configuration for the parsing job

    - `lang: Optional[ParsingLanguages]`

      The language to parse the files in

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `max_pages: Optional[int]`

      The maximum number of pages to parse

    - `target_pages: Optional[List[int]]`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
classify_job = client.classifier.jobs.create(
    file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
    rules=[{
        "description": "contains invoice number, line items, and total amount",
        "type": "invoice",
    }],
)
print(classify_job.id)
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

`classifier.jobs.list(JobListParams**kwargs)  -> SyncPaginatedCursor[ClassifyJob]`

**get** `/api/v1/classifier/jobs`

List classify jobs.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `organization_id: Optional[str]`

- `page_size: Optional[int]`

- `page_token: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class ClassifyJob: …`

  A classify job.

  - `id: str`

    Unique identifier

  - `project_id: str`

    The ID of the project

  - `rules: List[ClassifierRule]`

    The rules to classify the files

    - `description: str`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `type: str`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `status: StatusEnum`

    The status of the classify job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `user_id: str`

    The ID of the user

  - `created_at: Optional[datetime]`

    Creation datetime

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

    The classification mode to use

    - `"FAST"`

    - `"MULTIMODAL"`

  - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

    The configuration for the parsing job

    - `lang: Optional[ParsingLanguages]`

      The language to parse the files in

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `max_pages: Optional[int]`

      The maximum number of pages to parse

    - `target_pages: Optional[List[int]]`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
page = client.classifier.jobs.list()
page = page.items[0]
print(page.id)
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

`classifier.jobs.get(strclassify_job_id, JobGetParams**kwargs)  -> ClassifyJob`

**get** `/api/v1/classifier/jobs/{classify_job_id}`

Get a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classify_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class ClassifyJob: …`

  A classify job.

  - `id: str`

    Unique identifier

  - `project_id: str`

    The ID of the project

  - `rules: List[ClassifierRule]`

    The rules to classify the files

    - `description: str`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `type: str`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `status: StatusEnum`

    The status of the classify job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `user_id: str`

    The ID of the user

  - `created_at: Optional[datetime]`

    Creation datetime

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

    The classification mode to use

    - `"FAST"`

    - `"MULTIMODAL"`

  - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

    The configuration for the parsing job

    - `lang: Optional[ParsingLanguages]`

      The language to parse the files in

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `max_pages: Optional[int]`

      The maximum number of pages to parse

    - `target_pages: Optional[List[int]]`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `updated_at: Optional[datetime]`

    Update datetime

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
classify_job = client.classifier.jobs.get(
    classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(classify_job.id)
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

`classifier.jobs.get_results(strclassify_job_id, JobGetResultsParams**kwargs)  -> JobGetResultsResponse`

**get** `/api/v1/classifier/jobs/{classify_job_id}/results`

Get the results of a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `classify_job_id: str`

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class JobGetResultsResponse: …`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `items: List[Item]`

    The list of items.

    - `id: str`

      Unique identifier

    - `classify_job_id: str`

      The ID of the classify job

    - `created_at: Optional[datetime]`

      Creation datetime

    - `file_id: Optional[str]`

      The ID of the classified file

    - `result: Optional[ItemResult]`

      Result of classifying a single file.

      - `confidence: float`

        Confidence score of the classification (0.0-1.0)

      - `reasoning: str`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `type: Optional[str]`

        The document type that best matches, or null if no match.

    - `updated_at: Optional[datetime]`

      Update datetime

  - `next_page_token: Optional[str]`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: Optional[int]`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
response = client.classifier.jobs.get_results(
    classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(response.items)
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

- `class ClassifierRule: …`

  A rule for classifying documents - v0 simplified version.

  This represents a single classification rule that will be applied to documents.
  All rules are content-based and use natural language descriptions.

  - `description: str`

    Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

  - `type: str`

    The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

### Classify Job

- `class ClassifyJob: …`

  A classify job.

  - `id: str`

    Unique identifier

  - `project_id: str`

    The ID of the project

  - `rules: List[ClassifierRule]`

    The rules to classify the files

    - `description: str`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `type: str`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `status: StatusEnum`

    The status of the classify job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `user_id: str`

    The ID of the user

  - `created_at: Optional[datetime]`

    Creation datetime

  - `effective_at: Optional[datetime]`

  - `error_message: Optional[str]`

    Error message for the latest job attempt, if any.

  - `job_record_id: Optional[str]`

    The job record ID associated with this status, if any.

  - `mode: Optional[Literal["FAST", "MULTIMODAL"]]`

    The classification mode to use

    - `"FAST"`

    - `"MULTIMODAL"`

  - `parsing_configuration: Optional[ClassifyParsingConfiguration]`

    The configuration for the parsing job

    - `lang: Optional[ParsingLanguages]`

      The language to parse the files in

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `max_pages: Optional[int]`

      The maximum number of pages to parse

    - `target_pages: Optional[List[int]]`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `updated_at: Optional[datetime]`

    Update datetime

### Classify Parsing Configuration

- `class ClassifyParsingConfiguration: …`

  Parsing configuration for a classify job.

  - `lang: Optional[ParsingLanguages]`

    The language to parse the files in

    - `"af"`

    - `"az"`

    - `"bs"`

    - `"cs"`

    - `"cy"`

    - `"da"`

    - `"de"`

    - `"en"`

    - `"es"`

    - `"et"`

    - `"fr"`

    - `"ga"`

    - `"hr"`

    - `"hu"`

    - `"id"`

    - `"is"`

    - `"it"`

    - `"ku"`

    - `"la"`

    - `"lt"`

    - `"lv"`

    - `"mi"`

    - `"ms"`

    - `"mt"`

    - `"nl"`

    - `"no"`

    - `"oc"`

    - `"pi"`

    - `"pl"`

    - `"pt"`

    - `"ro"`

    - `"rs_latin"`

    - `"sk"`

    - `"sl"`

    - `"sq"`

    - `"sv"`

    - `"sw"`

    - `"tl"`

    - `"tr"`

    - `"uz"`

    - `"vi"`

    - `"ar"`

    - `"fa"`

    - `"ug"`

    - `"ur"`

    - `"bn"`

    - `"as"`

    - `"mni"`

    - `"ru"`

    - `"rs_cyrillic"`

    - `"be"`

    - `"bg"`

    - `"uk"`

    - `"mn"`

    - `"abq"`

    - `"ady"`

    - `"kbd"`

    - `"ava"`

    - `"dar"`

    - `"inh"`

    - `"che"`

    - `"lbe"`

    - `"lez"`

    - `"tab"`

    - `"tjk"`

    - `"hi"`

    - `"mr"`

    - `"ne"`

    - `"bh"`

    - `"mai"`

    - `"ang"`

    - `"bho"`

    - `"mah"`

    - `"sck"`

    - `"new"`

    - `"gom"`

    - `"sa"`

    - `"bgc"`

    - `"th"`

    - `"ch_sim"`

    - `"ch_tra"`

    - `"ja"`

    - `"ko"`

    - `"ta"`

    - `"te"`

    - `"kn"`

  - `max_pages: Optional[int]`

    The maximum number of pages to parse

  - `target_pages: Optional[List[int]]`

    The pages to target for parsing (0-indexed, so first page is at 0)

### Job Get Results Response

- `class JobGetResultsResponse: …`

  Response model for the classify endpoint following AIP-132 pagination standard.

  - `items: List[Item]`

    The list of items.

    - `id: str`

      Unique identifier

    - `classify_job_id: str`

      The ID of the classify job

    - `created_at: Optional[datetime]`

      Creation datetime

    - `file_id: Optional[str]`

      The ID of the classified file

    - `result: Optional[ItemResult]`

      Result of classifying a single file.

      - `confidence: float`

        Confidence score of the classification (0.0-1.0)

      - `reasoning: str`

        Step-by-step explanation of why this classification was chosen and the confidence score assigned

      - `type: Optional[str]`

        The document type that best matches, or null if no match.

    - `updated_at: Optional[datetime]`

      Update datetime

  - `next_page_token: Optional[str]`

    A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages.

  - `total_size: Optional[int]`

    The total number of items available. This is only populated when specifically requested. The value may be an estimate and can be used for display purposes only.
