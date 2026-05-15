## Get Classify Job

`$ llamacloud-prod classifier:jobs get`

**get** `/api/v1/classifier/jobs/{classify_job_id}`

Get a classify job.
Experimental: This endpoint is not yet ready for production use and is subject to change at any time.

### Parameters

- `--classify-job-id: string`

- `--organization-id: optional string`

- `--project-id: optional string`

### Returns

- `classify_job: object { id, project_id, rules, 9 more }`

  A classify job.

  - `id: string`

    Unique identifier

  - `project_id: string`

    The ID of the project

  - `rules: array of ClassifierRule`

    The rules to classify the files

    - `description: string`

      Natural language description of what to classify. Be specific about the content characteristics that identify this document type.

    - `type: string`

      The document type to assign when this rule matches (e.g., 'invoice', 'receipt', 'contract')

  - `status: "PENDING" or "SUCCESS" or "ERROR" or 2 more`

    The status of the classify job

    - `"PENDING"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `user_id: string`

    The ID of the user

  - `created_at: optional string`

    Creation datetime

  - `effective_at: optional string`

  - `error_message: optional string`

    Error message for the latest job attempt, if any.

  - `job_record_id: optional string`

    The job record ID associated with this status, if any.

  - `mode: optional "FAST" or "MULTIMODAL"`

    The classification mode to use

    - `"FAST"`

    - `"MULTIMODAL"`

  - `parsing_configuration: optional object { lang, max_pages, target_pages }`

    The configuration for the parsing job

    - `lang: optional "af" or "az" or "bs" or 83 more`

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

    - `max_pages: optional number`

      The maximum number of pages to parse

    - `target_pages: optional array of number`

      The pages to target for parsing (0-indexed, so first page is at 0)

  - `updated_at: optional string`

    Update datetime

### Example

```cli
llamacloud-prod classifier:jobs get \
  --api-key 'My API Key' \
  --classify-job-id 182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e
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
