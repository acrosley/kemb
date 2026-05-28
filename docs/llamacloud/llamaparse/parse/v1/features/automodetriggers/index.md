---
title: LlamaParse Document Pipeline Triggers | Developer Documentation
---

This document provides detailed information about all available triggers in the LlamaParse document pipeline. These triggers can be used in the `auto_mode_configuration_json` to conditionally apply specific parsing configurations to pages that match certain criteria.

## Content-Based Triggers

| Trigger          | Description                                                                                | Example                                    |
| ---------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------ |
| `text_in_page`   | Activates when a specific text string is found within the page’s text or markdown content. | `"text_in_page": "Executive Summary"`      |
| `table_in_page`  | Activates when the page contains an HTML table element or markdown table syntax.           | `"table_in_page": true`                    |
| `image_in_page`  | Activates when the page contains images (excluding full-page screenshots).                 | `"image_in_page": true`                    |
| `regexp_in_page` | Activates when the page’s markdown content matches a specified regular expression pattern. | `"regexp_in_page": "\\d{4}-\\d{2}-\\d{2}"` |

## File-Based Triggers

| Trigger           | Description                                                                 | Example                                |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------- |
| `filename_regexp` | Activates when the filename matches a specified regular expression pattern. | `"filename_regexp": "invoice.*\\.pdf"` |

## Text Metrics Triggers

| Trigger                          | Description                                                                                    | Example                                   |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `page_longer_than_n_chars`       | Activates when the page’s text or markdown content exceeds a specified character count.        | `"page_longer_than_n_chars": "1000"`      |
| `page_shorter_than_n_chars`      | Activates when the page’s text or markdown content is less than a specified character count.   | `"page_shorter_than_n_chars": "500"`      |
| `page_contains_at_least_n_words` | Activates when the page contains more than a specified number of valid words (2+ characters).  | `"page_contains_at_least_n_words": "200"` |
| `page_contains_at_most_n_words`  | Activates when the page contains fewer than a specified number of valid words (2+ characters). | `"page_contains_at_most_n_words": "50"`   |
| `page_contains_at_least_n_lines` | Activates when the page has more than a specified number of non-empty lines.                   | `"page_contains_at_least_n_lines": "20"`  |
| `page_contains_at_most_n_lines`  | Activates when the page has fewer than a specified number of non-empty lines.                  | `"page_contains_at_most_n_lines": "10"`   |

## Element Count Triggers

| Trigger                                    | Description                                                                        | Example                                            |
| ------------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------- |
| `page_contains_at_least_n_images`          | Activates when the page contains more than a specified number of images.           | `"page_contains_at_least_n_images": "2"`           |
| `page_contains_at_most_n_images`           | Activates when the page contains fewer than a specified number of images.          | `"page_contains_at_most_n_images": "1"`            |
| `page_contains_at_least_n_tables`          | Activates when the page contains more than a specified number of tables.           | `"page_contains_at_least_n_tables": "1"`           |
| `page_contains_at_most_n_tables`           | Activates when the page contains fewer than a specified number of tables.          | `"page_contains_at_most_n_tables": "3"`            |
| `page_contains_at_least_n_links`           | Activates when the page contains more than a specified number of links.            | `"page_contains_at_least_n_links": "5"`            |
| `page_contains_at_most_n_links`            | Activates when the page contains fewer than a specified number of links.           | `"page_contains_at_most_n_links": "10"`            |
| `page_contains_at_least_n_charts`          | Activates when the page contains more than a specified number of charts.           | `"page_contains_at_least_n_charts": "1"`           |
| `page_contains_at_most_n_charts`           | Activates when the page contains fewer than a specified number of charts.          | `"page_contains_at_most_n_charts": "2"`            |
| `page_contains_at_least_n_layout_elements` | Activates when the page contains more than a specified number of layout elements.  | `"page_contains_at_least_n_layout_elements": "10"` |
| `page_contains_at_most_n_layout_elements`  | Activates when the page contains fewer than a specified number of layout elements. | `"page_contains_at_most_n_layout_elements": "5"`   |
| `full_page_image_in_page`                  | Activates when page has \~full page image, likely scan                             |                                                    |

## Numeric Content Triggers

| Trigger                                    | Description                                                                                                                                            | Example                                            |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `page_contains_at_least_n_percent_numbers` | Activates when more than a specified percentage of words in the page are numbers. Numbers with punctuation (like “1,000.50”) are correctly identified. | `"page_contains_at_least_n_percent_numbers": "30"` |
| `page_contains_at_most_n_percent_numbers`  | Activates when less than a specified percentage of words in the page are numbers. Numbers with punctuation are correctly identified.                   | `"page_contains_at_most_n_percent_numbers": "10"`  |

## Layout-Based Triggers

| Trigger                                       | Description                                                                      | Example                                                |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `layout_element_in_page`                      | Activates when the page contains a specific layout element type.                 | `"layout_element_in_page": "table"`                    |
| `layout_element_in_page_confidence_threshold` | Specifies the minimum confidence level for the `layout_element_in_page` trigger. | `"layout_element_in_page_confidence_threshold": "0.8"` |

## Usage Example

Here’s an example of how to use these triggers in an `auto_mode_configuration_json`:

```
[
  {
    "parsing_conf": {
      "user_prompt": "Extract all tabular data into a structured format",
    },
    "table_in_page": true
  },
  {
    "parsing_conf": {
      "user_prompt": "Summarize the executive summary section",
    },
    "text_in_page": "Executive Summary"
  },
  {
    "parsing_conf": {
      "user_prompt": "Extract financial figures from this numbers-heavy page",
    },
    "page_contains_at_least_n_percent_numbers": "25"
  }
]
```

## Notes

- Multiple triggers can be specified in a single configuration object. All specified conditions must be met for the parsing configuration to be applied.
- Values for numeric thresholds should be provided as strings, as shown in the examples.
- Regular expressions should use proper escaping as shown in the examples.
- When a page matches multiple configurations, only the first matching configuration in the array will be applied.
