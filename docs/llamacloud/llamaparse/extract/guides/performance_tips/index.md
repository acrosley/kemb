---
title: Performance Tips | Developer Documentation
description: Best practices and optimization strategies for successful data extraction workflows
---

## Overall Performance Best Practices

For maximum extraction success:

1. **Start with the agentic tier for debugging**: When troubleshooting extraction issues, use the `agentic` tier which uses the most capable models. If extraction succeeds with `agentic`, you can try `cost_effective` to see if quality holds for your use case. If extraction fails even with `agentic`, the issue is likely in your schema design (e.g., ambiguous field descriptions).

   ```
   # Start debugging with agentic tier
   job = client.extract.create(
       file_input=file_obj.id,
       configuration={
           "data_schema": schema,
           "extraction_target": "per_doc",
           "tier": "agentic",
       },
   )
   ```

2. **Start small and iterate**: Begin with a subset of your data or schema to validate your extraction approach and iterate on your schema description (e.g. adding examples, formatting instructions etc.) to get better accuracy before scaling.

3. **Design clear, focused schemas**: Prefer precise short descriptions over verbose fields that try to do too much. See the [section on schema design](../schema_design) and [avoiding complex transformations](../performance_tips/#avoid-complex-field-transformations).

4. **Leverage document structure**: Use page ranges, extraction targets, sections, and chunking strategies to optimize processing. See [options](../options).

5. **Combine tools strategically**: Extract excels at extracting information from documents. Focus on leveraging this strength while using complementary tools for computational tasks and validation (e.g., heavy calculations are better handled in a post-processing step).

## Extracting from Tables and Ordered Lists

**The situation:** When working with documents containing tables, spreadsheets (CSV/Excel), or ordered lists of entities, you want to ensure comprehensive and accurate extraction of each row or item.

**Use `per_table_row` extraction target**: If you are only interested in extracting or transforming data from a table or ordered list of entities, use the `per_table_row` extraction target. This processes each row individually for comprehensive coverage and accurate results.

```
# Optimal: Use per_table_row for tabular data extraction
extraction_config = {
    "extraction_target": "per_table_row",
}
```

**When your schema has additional elements beyond the table:** If your schema includes fields that need to be extracted from outside the table (e.g., document metadata, headers, or summary information), you can run separate extractions for tabular data (using `per_table_row`) and non-tabular elements.

```
# First extraction: Get document-level metadata
metadata_job = client.extract.create(
    file_input=file_id,
    configuration={
        "data_schema": metadata_schema,
        "extraction_target": "per_doc",
        "tier": "agentic",
    },
)


# Second extraction: Get table row data
table_job = client.extract.create(
    file_input=file_id,
    configuration={
        "data_schema": table_row_schema,
        "extraction_target": "per_table_row",
        "target_pages": "5-10",
        "tier": "agentic",
    },
)
```

2. **Use `agentic` tier for mixed content**: If you need to extract both tabular and non-tabular elements in a single pass, the `agentic` tier uses more capable models that handle complex layouts better. Note that this approach uses more credits (15/page vs 5/page).

## Avoid Complex Field Transformations

Don’t embed business logic in field descriptions. Extract clean data first, then compute in your application code.

```
# ❌ Problematic: Too much logic in the field description
problematic_field = {
    "calculated_score": {
        "type": "number",
        "description": "If revenue > 1M, multiply by 0.8, else if revenue < 500K multiply by 1.2, otherwise use the base score from table 3, but only if the date is after 2020 and the category is not 'exempt'"
    }
}


# ✅ Better: Simple extraction, handle logic separately
better_schema = {
    "revenue": {"type": "number", "description": "Total revenue in dollars"},
    "base_score": {"type": "number", "description": "Base score value from the scoring table"},
    "date": {"type": "string", "description": "Date in YYYY-MM-DD format"},
    "category": {"type": "string", "description": "Business category"}
}


# Then handle calculations in your application code:
def calculate_final_score(extracted_data):
    revenue = extracted_data["revenue"]
    if revenue > 1000000:
        return extracted_data["base_score"] * 0.8
    elif revenue < 500000:
        return extracted_data["base_score"] * 1.2
    return extracted_data["base_score"]
```
