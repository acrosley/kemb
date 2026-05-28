## Get Parse Job

`parsing.get(strjob_id, ParsingGetParams**kwargs)  -> ParsingGetResponse`

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

- `job_id: str`

- `expand: Optional[SequenceNotStr[str]]`

  Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

- `image_filenames: Optional[str]`

  Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

- `organization_id: Optional[str]`

- `project_id: Optional[str]`

### Returns

- `class ParsingGetResponse: …`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `job: Job`

    Parse job status and metadata

    - `id: str`

      Unique parse job identifier

    - `project_id: str`

      Project this job belongs to

    - `status: Literal["PENDING", "RUNNING", "COMPLETED", 2 more]`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `"PENDING"`

      - `"RUNNING"`

      - `"COMPLETED"`

      - `"FAILED"`

      - `"CANCELLED"`

    - `created_at: Optional[datetime]`

      Creation datetime

    - `error_message: Optional[str]`

      Error details when status is FAILED

    - `name: Optional[str]`

      Optional display name for this parse job

    - `tier: Optional[str]`

      Parsing tier used for this job

    - `updated_at: Optional[datetime]`

      Update datetime

  - `images_content_metadata: Optional[ImagesContentMetadata]`

    Metadata for all extracted images.

    - `images: List[ImagesContentMetadataImage]`

      List of image metadata with presigned URLs

      - `filename: str`

        Image filename (e.g., 'image_0.png')

      - `index: int`

        Index of the image in the extraction order

      - `bbox: Optional[ImagesContentMetadataImageBbox]`

        Bounding box for an image on its page.

        - `h: int`

          Height of the bounding box

        - `w: int`

          Width of the bounding box

        - `x: int`

          X coordinate of the bounding box

        - `y: int`

          Y coordinate of the bounding box

      - `category: Optional[Literal["screenshot", "embedded", "layout"]]`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `"screenshot"`

        - `"embedded"`

        - `"layout"`

      - `content_type: Optional[str]`

        MIME type of the image

      - `presigned_url: Optional[str]`

        Presigned URL to download the image

      - `size_bytes: Optional[int]`

        Deprecated: always returns None. Will be removed in a future release.

    - `total_count: int`

      Total number of extracted images

  - `items: Optional[Items]`

    Structured JSON result (if requested)

    - `pages: List[ItemsPage]`

      List of structured pages or failed page entries

      - `class ItemsPageStructuredResultPage: …`

        - `items: List[ItemsPageStructuredResultPageItem]`

          List of structured items on the page

          - `class TextItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["text"]]`

              Text item type

              - `"text"`

          - `class HeadingItem: …`

            - `level: int`

              Heading level (1-6)

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Heading text content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["heading"]]`

              Heading item type

              - `"heading"`

          - `class ListItem: …`

            - `items: List[Item]`

              List of nested text or list items

              - `class TextItem: …`

              - `class ListItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `ordered: bool`

              Whether the list is ordered or unordered

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["list"]]`

              List item type

              - `"list"`

          - `class CodeItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `value: str`

              Code content

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `language: Optional[str]`

              Programming language identifier

            - `type: Optional[Literal["code"]]`

              Code block item type

              - `"code"`

          - `class TableItem: …`

            - `csv: str`

              CSV representation of the table

            - `html: str`

              HTML representation of the table

            - `md: str`

              Markdown representation preserving formatting

            - `rows: List[List[Union[str, float, null]]]`

              Table data as array of arrays (string, number, or null)

              - `str`

              - `float`

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `merged_from_pages: Optional[List[int]]`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `merged_into_page: Optional[int]`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `parse_concerns: Optional[List[ParseConcern]]`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `details: str`

                Human-readable details about the concern

              - `type: str`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `type: Optional[Literal["table"]]`

              Table item type

              - `"table"`

          - `class ImageItem: …`

            - `caption: str`

              Image caption

            - `md: str`

              Markdown representation preserving formatting

            - `url: str`

              URL to the image

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["image"]]`

              Image item type

              - `"image"`

          - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `text: str`

              Display text of the link

            - `url: str`

              URL of the link

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["link"]]`

              Link item type

              - `"link"`

          - `class HeaderItem: …`

            - `items: List[Item]`

              List of items within the header

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["header"]]`

              Page header container

              - `"header"`

          - `class FooterItem: …`

            - `items: List[Item]`

              List of items within the footer

              - `class TextItem: …`

              - `class HeadingItem: …`

              - `class ListItem: …`

              - `class CodeItem: …`

              - `class TableItem: …`

              - `class ImageItem: …`

              - `class LinkItem: …`

            - `md: str`

              Markdown representation preserving formatting

            - `bbox: Optional[List[BBox]]`

              List of bounding boxes

              - `h: float`

                Height of the bounding box

              - `w: float`

                Width of the bounding box

              - `x: float`

                X coordinate of the bounding box

              - `y: float`

                Y coordinate of the bounding box

              - `confidence: Optional[float]`

                Confidence score

              - `end_index: Optional[int]`

                End index in the text

              - `label: Optional[str]`

                Label for the bounding box

              - `start_index: Optional[int]`

                Start index in the text

            - `type: Optional[Literal["footer"]]`

              Page footer container

              - `"footer"`

        - `page_height: float`

          Height of the page in points

        - `page_number: int`

          Page number of the document

        - `page_width: float`

          Width of the page in points

        - `success: Literal[true]`

          Success indicator

          - `true`

      - `class ItemsPageFailedStructuredPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `job_metadata: Optional[Dict[str, object]]`

    Job execution metadata (if requested)

  - `markdown: Optional[Markdown]`

    Markdown result (if requested)

    - `pages: List[MarkdownPage]`

      List of markdown pages or failed page entries

      - `class MarkdownPageMarkdownResultPage: …`

        - `markdown: str`

          Markdown content of the page

        - `page_number: int`

          Page number of the document

        - `success: Literal[true]`

          Success indicator

          - `true`

        - `footer: Optional[str]`

          Footer of the page in markdown

        - `header: Optional[str]`

          Header of the page in markdown

      - `class MarkdownPageFailedMarkdownPage: …`

        - `error: str`

          Error message describing the failure

        - `page_number: int`

          Page number of the document

        - `success: Literal[false]`

          Failure indicator

          - `false`

  - `markdown_full: Optional[str]`

    Full raw markdown content (if requested)

  - `metadata: Optional[Metadata]`

    Result containing metadata (page level and general) for the parsed document.

    - `pages: List[MetadataPage]`

      List of page metadata entries

      - `page_number: int`

        Page number of the document

      - `confidence: Optional[float]`

        Confidence score for the page parsing (0-1)

      - `cost_optimized: Optional[bool]`

        Whether cost-optimized parsing was used for the page

      - `original_orientation_angle: Optional[int]`

        Original orientation angle of the page in degrees

      - `printed_page_number: Optional[str]`

        Printed page number as it appears in the document

      - `slide_section_name: Optional[str]`

        Section name from presentation slides

      - `speaker_notes: Optional[str]`

        Speaker notes from presentation slides

      - `triggered_auto_mode: Optional[bool]`

        Whether auto mode was triggered for the page

  - `raw_parameters: Optional[Dict[str, object]]`

  - `result_content_metadata: Optional[Dict[str, ResultContentMetadata]]`

    Metadata including size, existence, and presigned URLs for result files

    - `size_bytes: int`

      Size of the result file in bytes

    - `exists: Optional[bool]`

      Whether the result file exists in S3

    - `presigned_url: Optional[str]`

      Presigned URL to download the result file

  - `text: Optional[Text]`

    Plain text result (if requested)

    - `pages: List[TextPage]`

      List of text pages

      - `page_number: int`

        Page number of the document

      - `text: str`

        Plain text content of the page

  - `text_full: Optional[str]`

    Full raw text content (if requested)

### Example

```python
import os
from llama_cloud import LlamaCloud

client = LlamaCloud(
    api_key=os.environ.get("LLAMA_CLOUD_API_KEY"),  # This is the default and can be omitted
)
parsing = client.parsing.get(
    job_id="job_id",
)
print(parsing.job)
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
