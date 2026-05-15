## Get Parse Job

`client.parsing.get(stringjobID, ParsingGetParamsquery?, RequestOptionsoptions?): ParsingGetResponse`

**get** `/api/v2/parse/{job_id}`

Retrieve a parse job with optional expanded content.

By default returns job metadata only. Use `expand` to include
parsed content:

- `text` — plain text output
- `markdown` — markdown output
- `items` — structured page-by-page output
- `job_metadata` — usage and processing details

Content metadata fields (e.g. `text_content_metadata`) return
presigned URLs for downloading large results.

### Parameters

- `jobID: string`

- `query: ParsingGetParams`

  - `expand?: Array<string>`

    Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

  - `image_filenames?: string | null`

    Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ParsingGetResponse`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: string`

      Unique parse job identifier

    - `project_id: string`

      Project this job belongs to

    - `status: "PENDING" | "RUNNING" | "COMPLETED" | 2 more`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at?: string | null`

      Creation datetime

    - `error_message?: string | null`

      Error details when status is FAILED

    - `name?: string | null`

      Optional display name for this parse job

    - `tier?: string | null`

      Parsing tier used for this job

    - `updated_at?: string | null`

      Update datetime

  - `images_content_metadata?: ImagesContentMetadata | null`

    Metadata for all extracted images.

    - `images: Array<Image>`

      List of image metadata with presigned URLs

      - `filename: string`

        Image filename (e.g., 'image_0.png')

      - `index: number`

        Index of the image in the extraction order

      - `bbox?: Bbox | null`

        Bounding box for an image on its page.

        - `h: number`

          Height of the bounding box

        - `w: number`

          Width of the bounding box

        - `x: number`

          X coordinate of the bounding box

        - `y: number`

          Y coordinate of the bounding box

      - `category?: "screenshot" | "embedded" | "layout" | null`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type?: string | null`

        MIME type of the image

      - `presigned_url?: string | null`

        Presigned URL to download the image

      - `size_bytes?: number | null`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: number`

      Total number of extracted images

  - `items?: Items | null`

    Structured JSON result (if requested)

    - `pages: Array<StructuredResultPage | FailedStructuredPage>`

      List of structured pages or failed page entries

      - `StructuredResultPage`

        - `items: Array<TextItem | HeadingItem | ListItem | 6 more>`

          List of structured items on the page

          - `TextItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "text"`

              Text item type

              - `"text"`

          - `HeadingItem`

            - `level: number`

              Heading level (1-6)

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Heading text content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "heading"`

              Heading item type

              - `"heading"`

          - `ListItem`

            - `items: Array<TextItem | ListItem>`

              List of nested text or list items

              - `TextItem`

              - `ListItem`

            - `md: string`

              Markdown representation preserving formatting

            - `ordered: boolean`

              Whether the list is ordered or unordered

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "list"`

              List item type

              - `"list"`

          - `CodeItem`

            - `md: string`

              Markdown representation preserving formatting

            - `value: string`

              Code content

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `language?: string | null`

              Programming language identifier

            - `type?: "code"`

              Code block item type

              - `"code"`

          - `TableItem`

            - `csv: string`

              CSV representation of the table

            - `html: string`

              HTML representation of the table

            - `md: string`

              Markdown representation preserving formatting

            - `rows: Array<Array<string | number | null>>`

              Table data as array of arrays (string, number, or null)

              - `string`

              - `number`

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `merged_from_pages?: Array<number> | null`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page?: number | null`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns?: Array<ParseConcern> | null`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: string`

                Human-readable details about the concern

              - `type: string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type?: "table"`

              Table item type

              - `"table"`

          - `ImageItem`

            - `caption: string`

              Image caption

            - `md: string`

              Markdown representation preserving formatting

            - `url: string`

              URL to the image

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "image"`

              Image item type

              - `"image"`

          - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `text: string`

              Display text of the link

            - `url: string`

              URL of the link

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "link"`

              Link item type

              - `"link"`

          - `HeaderItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the header

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "header"`

              Page header container

              - `"header"`

          - `FooterItem`

            - `items: Array<TextItem | HeadingItem | ListItem | 4 more>`

              List of items within the footer

              - `TextItem`

              - `HeadingItem`

              - `ListItem`

              - `CodeItem`

              - `TableItem`

              - `ImageItem`

              - `LinkItem`

            - `md: string`

              Markdown representation preserving formatting

            - `bbox?: Array<BBox> | null`

              List of bounding boxes

              - `h: number`

                Height of the bounding box

              - `w: number`

                Width of the bounding box

              - `x: number`

                X coordinate of the bounding box

              - `y: number`

                Y coordinate of the bounding box

              - `confidence?: number | null`

                Confidence score

              - `end_index?: number | null`

                End index in the text

              - `label?: string | null`

                Label for the bounding box

              - `start_index?: number | null`

                Start index in the text

            - `type?: "footer"`

              Page footer container

              - `"footer"`

        - `page_height: number`

          Height of the page in points

        - `page_number: number`

          Page number of the document

        - `page_width: number`

          Width of the page in points

        - `success: true`

          Success indicator

          - `true`

      - `FailedStructuredPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `job_metadata?: Record<string, unknown> | null`

    Job execution metadata (if requested)

  - `markdown?: Markdown | null`

    Markdown result (if requested)

    - `pages: Array<MarkdownResultPage | FailedMarkdownPage>`

      List of markdown pages or failed page entries

      - `MarkdownResultPage`

        - `markdown: string`

          Markdown content of the page

        - `page_number: number`

          Page number of the document

        - `success: true`

          Success indicator

          - `true`

        - `footer?: string | null`

          Footer of the page in markdown

        - `header?: string | null`

          Header of the page in markdown

      - `FailedMarkdownPage`

        - `error: string`

          Error message describing the failure

        - `page_number: number`

          Page number of the document

        - `success: false`

          Failure indicator

          - `false`

  - `markdown_full?: string | null`

    Full raw markdown content (if requested)

  - `metadata?: Metadata | null`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: Array<Page>`

      List of page metadata entries

      - `page_number: number`

        Page number of the document

      - `confidence?: number | null`

        Confidence score for the page parsing (0-1)

      - `cost_optimized?: boolean | null`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle?: number | null`

        Original orientation angle of the page in degrees

      - `printed_page_number?: string | null`

        Printed page number as it appears in the document

      - `slide_section_name?: string | null`

        Section name from presentation slides

      - `speaker_notes?: string | null`

        Speaker notes from presentation slides

      - `triggered_auto_mode?: boolean | null`

        Whether auto mode was triggered for the page

  - `raw_parameters?: Record<string, unknown> | null`

  - `result_content_metadata?: Record<string, ResultContentMetadata> | null`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: number`

      Size of the result file in bytes

    - `exists?: boolean`

      Whether the result file exists in S3

    - `presigned_url?: string | null`

      Presigned URL to download the result file

  - `text?: Text | null`

    Plain text result (if requested)

    - `pages: Array<Page>`

      List of text pages

      - `page_number: number`

        Page number of the document

      - `text: string`

        Plain text content of the page

  - `text_full?: string | null`

    Full raw text content (if requested)

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const parsing = await client.parsing.get('job_id');

console.log(parsing.job);
```

#### Response

```json
{
  "job": {
    "id": "pjb-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "project_id": "prj-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "status": "PENDING",
    "created_at": "2019-12-27T18:11:19.117Z",
    "error_message": "error_message",
    "name": "Q4 Financial Report",
    "tier": "fast",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "images_content_metadata": {
    "images": [
      {
        "filename": "filename",
        "index": 0,
        "bbox": {
          "h": 0,
          "w": 0,
          "x": 0,
          "y": 0
        },
        "category": "screenshot",
        "content_type": "content_type",
        "presigned_url": "presigned_url",
        "size_bytes": 0
      }
    ],
    "total_count": 0
  },
  "items": {
    "pages": [
      {
        "items": [
          {
            "md": "md",
            "value": "value",
            "bbox": [
              {
                "h": 0,
                "w": 0,
                "x": 0,
                "y": 0,
                "confidence": 0,
                "end_index": 0,
                "label": "label",
                "start_index": 0
              }
            ],
            "type": "text"
          }
        ],
        "page_height": 0,
        "page_number": 0,
        "page_width": 0,
        "success": true
      }
    ]
  },
  "job_metadata": {
    "foo": "bar"
  },
  "markdown": {
    "pages": [
      {
        "markdown": "markdown",
        "page_number": 0,
        "success": true,
        "footer": "footer",
        "header": "header"
      }
    ]
  },
  "markdown_full": "markdown_full",
  "metadata": {
    "pages": [
      {
        "page_number": 0,
        "confidence": 0,
        "cost_optimized": true,
        "original_orientation_angle": 0,
        "printed_page_number": "printed_page_number",
        "slide_section_name": "slide_section_name",
        "speaker_notes": "speaker_notes",
        "triggered_auto_mode": true
      }
    ]
  },
  "raw_parameters": {
    "foo": "bar"
  },
  "result_content_metadata": {
    "foo": {
      "size_bytes": 0,
      "exists": true,
      "presigned_url": "presigned_url"
    }
  },
  "text": {
    "pages": [
      {
        "page_number": 0,
        "text": "text"
      }
    ]
  },
  "text_full": "text_full"
}
```
