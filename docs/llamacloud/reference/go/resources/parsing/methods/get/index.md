## Get Parse Job

`client.Parsing.Get(ctx, jobID, query) (*ParsingGetResponse, error)`

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

- `jobID string`

- `query ParsingGetParams`

  - `Expand param.Field[[]string]`

    Fields to include: text, markdown, items, metadata, job_metadata, text_content_metadata, markdown_content_metadata, items_content_metadata, metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata, output_pdf_content_metadata, images_content_metadata. Metadata fields include presigned URLs.

  - `ImageFilenames param.Field[string]`

    Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

  - `OrganizationID param.Field[string]`

  - `ProjectID param.Field[string]`

### Returns

- `type ParsingGetResponse struct{…}`

  Parse result response with job status and optional content or metadata.

  The job field is always included. Other fields are included based on expand parameters.

  - `Job ParsingGetResponseJob`

    Parse job status and metadata

    - `ID string`

      Unique parse job identifier

    - `ProjectID string`

      Project this job belongs to

    - `Status string`

      Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED

      - `const ParsingGetResponseJobStatusPending ParsingGetResponseJobStatus = "PENDING"`

      - `const ParsingGetResponseJobStatusRunning ParsingGetResponseJobStatus = "RUNNING"`

      - `const ParsingGetResponseJobStatusCompleted ParsingGetResponseJobStatus = "COMPLETED"`

      - `const ParsingGetResponseJobStatusFailed ParsingGetResponseJobStatus = "FAILED"`

      - `const ParsingGetResponseJobStatusCancelled ParsingGetResponseJobStatus = "CANCELLED"`

    - `CreatedAt Time`

      Creation datetime

    - `ErrorMessage string`

      Error details when status is FAILED

    - `Name string`

      Optional display name for this parse job

    - `Tier string`

      Parsing tier used for this job

    - `UpdatedAt Time`

      Update datetime

  - `ImagesContentMetadata ParsingGetResponseImagesContentMetadata`

    Metadata for all extracted images.

    - `Images []ParsingGetResponseImagesContentMetadataImage`

      List of image metadata with presigned URLs

      - `Filename string`

        Image filename (e.g., 'image_0.png')

      - `Index int64`

        Index of the image in the extraction order

      - `Bbox ParsingGetResponseImagesContentMetadataImageBbox`

        Bounding box for an image on its page.

        - `H int64`

          Height of the bounding box

        - `W int64`

          Width of the bounding box

        - `X int64`

          X coordinate of the bounding box

        - `Y int64`

          Y coordinate of the bounding box

      - `Category string`

        Image category: 'screenshot' (full page), 'embedded' (images in document), or 'layout' (cropped from layout detection)

        - `const ParsingGetResponseImagesContentMetadataImageCategoryScreenshot ParsingGetResponseImagesContentMetadataImageCategory = "screenshot"`

        - `const ParsingGetResponseImagesContentMetadataImageCategoryEmbedded ParsingGetResponseImagesContentMetadataImageCategory = "embedded"`

        - `const ParsingGetResponseImagesContentMetadataImageCategoryLayout ParsingGetResponseImagesContentMetadataImageCategory = "layout"`

      - `ContentType string`

        MIME type of the image

      - `PresignedURL string`

        Presigned URL to download the image

      - `SizeBytes int64`

        Deprecated: always returns None. Will be removed in a future release.

    - `TotalCount int64`

      Total number of extracted images

  - `Items ParsingGetResponseItems`

    Structured JSON result (if requested)

    - `Pages []ParsingGetResponseItemsPageUnion`

      List of structured pages or failed page entries

      - `type ParsingGetResponseItemsPageStructuredResultPage struct{…}`

        - `Items []ParsingGetResponseItemsPageStructuredResultPageItemUnion`

          List of structured items on the page

          - `type TextItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Text content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type TextItemType`

              Text item type

              - `const TextItemTypeText TextItemType = "text"`

          - `type HeadingItem struct{…}`

            - `Level int64`

              Heading level (1-6)

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Heading text content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type HeadingItemType`

              Heading item type

              - `const HeadingItemTypeHeading HeadingItemType = "heading"`

          - `type ListItem struct{…}`

            - `Items []ListItemItemUnion`

              List of nested text or list items

              - `type TextItem struct{…}`

              - `type ListItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Ordered bool`

              Whether the list is ordered or unordered

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type ListItemType`

              List item type

              - `const ListItemTypeList ListItemType = "list"`

          - `type CodeItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Value string`

              Code content

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Language string`

              Programming language identifier

            - `Type CodeItemType`

              Code block item type

              - `const CodeItemTypeCode CodeItemType = "code"`

          - `type TableItem struct{…}`

            - `Csv string`

              CSV representation of the table

            - `HTML string`

              HTML representation of the table

            - `Md string`

              Markdown representation preserving formatting

            - `Rows [][]TableItemRowUnion`

              Table data as array of arrays (string, number, or null)

              - `string`

              - `float64`

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `MergedFromPages []int64`

              List of page numbers with tables that were merged into this table (e.g., [1, 2, 3, 4])

            - `MergedIntoPage int64`

              Populated when merged into another table. Page number where the full merged table begins (used on empty tables).

            - `ParseConcerns []TableItemParseConcern`

              Quality concerns detected during table extraction, indicating the table may have issues

              - `Details string`

                Human-readable details about the concern

              - `Type string`

                Type of parse concern (e.g. header_value_type_mismatch, inconsistent_row_cell_count)

            - `Type TableItemType`

              Table item type

              - `const TableItemTypeTable TableItemType = "table"`

          - `type ImageItem struct{…}`

            - `Caption string`

              Image caption

            - `Md string`

              Markdown representation preserving formatting

            - `URL string`

              URL to the image

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type ImageItemType`

              Image item type

              - `const ImageItemTypeImage ImageItemType = "image"`

          - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Text string`

              Display text of the link

            - `URL string`

              URL of the link

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type LinkItemType`

              Link item type

              - `const LinkItemTypeLink LinkItemType = "link"`

          - `type HeaderItem struct{…}`

            - `Items []HeaderItemItemUnion`

              List of items within the header

              - `type TextItem struct{…}`

              - `type HeadingItem struct{…}`

              - `type ListItem struct{…}`

              - `type CodeItem struct{…}`

              - `type TableItem struct{…}`

              - `type ImageItem struct{…}`

              - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type HeaderItemType`

              Page header container

              - `const HeaderItemTypeHeader HeaderItemType = "header"`

          - `type FooterItem struct{…}`

            - `Items []FooterItemItemUnion`

              List of items within the footer

              - `type TextItem struct{…}`

              - `type HeadingItem struct{…}`

              - `type ListItem struct{…}`

              - `type CodeItem struct{…}`

              - `type TableItem struct{…}`

              - `type ImageItem struct{…}`

              - `type LinkItem struct{…}`

            - `Md string`

              Markdown representation preserving formatting

            - `Bbox []BBox`

              List of bounding boxes

              - `H float64`

                Height of the bounding box

              - `W float64`

                Width of the bounding box

              - `X float64`

                X coordinate of the bounding box

              - `Y float64`

                Y coordinate of the bounding box

              - `Confidence float64`

                Confidence score

              - `EndIndex int64`

                End index in the text

              - `Label string`

                Label for the bounding box

              - `StartIndex int64`

                Start index in the text

            - `Type FooterItemType`

              Page footer container

              - `const FooterItemTypeFooter FooterItemType = "footer"`

        - `PageHeight float64`

          Height of the page in points

        - `PageNumber int64`

          Page number of the document

        - `PageWidth float64`

          Width of the page in points

        - `Success bool`

          Success indicator

          - `const ParsingGetResponseItemsPageStructuredResultPageSuccessTrue ParsingGetResponseItemsPageStructuredResultPageSuccess = true`

      - `type ParsingGetResponseItemsPageFailedStructuredPage struct{…}`

        - `Error string`

          Error message describing the failure

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Failure indicator

          - `const ParsingGetResponseItemsPageFailedStructuredPageSuccessFalse ParsingGetResponseItemsPageFailedStructuredPageSuccess = false`

  - `JobMetadata map[string, any]`

    Job execution metadata (if requested)

  - `Markdown ParsingGetResponseMarkdown`

    Markdown result (if requested)

    - `Pages []ParsingGetResponseMarkdownPageUnion`

      List of markdown pages or failed page entries

      - `type ParsingGetResponseMarkdownPageMarkdownResultPage struct{…}`

        - `Markdown string`

          Markdown content of the page

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Success indicator

          - `const ParsingGetResponseMarkdownPageMarkdownResultPageSuccessTrue ParsingGetResponseMarkdownPageMarkdownResultPageSuccess = true`

        - `Footer string`

          Footer of the page in markdown

        - `Header string`

          Header of the page in markdown

      - `type ParsingGetResponseMarkdownPageFailedMarkdownPage struct{…}`

        - `Error string`

          Error message describing the failure

        - `PageNumber int64`

          Page number of the document

        - `Success bool`

          Failure indicator

          - `const ParsingGetResponseMarkdownPageFailedMarkdownPageSuccessFalse ParsingGetResponseMarkdownPageFailedMarkdownPageSuccess = false`

  - `MarkdownFull string`

    Full raw markdown content (if requested)

  - `Metadata ParsingGetResponseMetadata`

    Result containing metadata (page level and general) for the parsed document.

    - `Pages []ParsingGetResponseMetadataPage`

      List of page metadata entries

      - `PageNumber int64`

        Page number of the document

      - `Confidence float64`

        Confidence score for the page parsing (0-1)

      - `CostOptimized bool`

        Whether cost-optimized parsing was used for the page

      - `OriginalOrientationAngle int64`

        Original orientation angle of the page in degrees

      - `PrintedPageNumber string`

        Printed page number as it appears in the document

      - `SlideSectionName string`

        Section name from presentation slides

      - `SpeakerNotes string`

        Speaker notes from presentation slides

      - `TriggeredAutoMode bool`

        Whether auto mode was triggered for the page

  - `RawParameters map[string, any]`

  - `ResultContentMetadata map[string, ParsingGetResponseResultContentMetadata]`

    Metadata including size, existence, and presigned URLs for result files

    - `SizeBytes int64`

      Size of the result file in bytes

    - `Exists bool`

      Whether the result file exists in S3

    - `PresignedURL string`

      Presigned URL to download the result file

  - `Text ParsingGetResponseText`

    Plain text result (if requested)

    - `Pages []ParsingGetResponseTextPage`

      List of text pages

      - `PageNumber int64`

        Page number of the document

      - `Text string`

        Plain text content of the page

  - `TextFull string`

    Full raw text content (if requested)

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
  parsing, err := client.Parsing.Get(
    context.TODO(),
    "job_id",
    llamacloudprod.ParsingGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", parsing.Job)
}
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
