---
title: Structured Output (Beta) | Developer Documentation
---



Structured Output is deprecated on the llamaParse API, use the LlamaExtract API instead.



## About Structured Output

Structured output allows you to extract structured data (such as JSON) from a document directly at the parsing stage, reducing cost and time needed.

Structured output is currently only compatible with our default parsing mode and can be activated by setting `structured_output=True` in the API.

- [Python](#tab-panel-517)
- [API](#tab-panel-518)

```
parser = LlamaParse(
  structured_output=True
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'structured_output="true"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



You then need to provide either:

- a JSON schema in the `structured_output_json_schema` API variable, which will be used to extract data in the desired format
- or the name of one of our pre-defined schemas in the variable `structured_output_json_schema_name`

* [Python (Schema)](#tab-panel-519)
* [API (Schema)](#tab-panel-520)
* [Python (Preset)](#tab-panel-521)
* [API (Preset)](#tab-panel-522)

```
parser = LlamaParse(
  structured_output_json_schema='A JSON SCHEMA'
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'structured_output_json_schema="A JSON SCHEMA"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```

```
parser = LlamaParse(
  structured_output_json_schema_name="invoice"
)
```

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'structured_output_json_schema_name="invoice"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Supported Pre-defined Schemas



## imFeelingLucky

Wildcard schema that lets LlamaParse infer output format

- [API](#tab-panel-516)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'structured_output_json_schema_name="imFeelingLucky"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```



## Invoice

Standard invoice schema for line items, tax, and totals

- [API](#tab-panel-523)
- [Invoice Schema](#tab-panel-524)

Terminal window

```
  curl -X 'POST' \
    'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
    --form 'structured_output_json_schema_name="invoice"' \
    -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```

#### Structured Output: Invoice Schema

Type: `object`

***Properties***

- **invoiceNumber** `required`

  - *Unique identifier for the invoice*
  - Type: `string`

- **invoiceDate** `required`

  - *Date the invoice was issued (ISO format)*
  - Type: `string`
  - String format must be a “date”

- **dueDate**

  - *Payment due date (ISO format)*
  - Type: `string`
  - String format must be a “date”

- **billingAddress** `required`

  - *Billing address details*

  - Type: `object`

  - ***Properties***

    - **name** `required`
      - Type: `string`
    - **street** `required`
      - Type: `string`
    - **city** `required`
      - Type: `string`
    - **state**
      - Type: `string`
    - **postalCode** `required`
      - Type: `string`
    - **country** `required`
      - Type: `string`

- **shippingAddress**

  - *Shipping address details*

  - Type: `object`

  - ***Properties***

    - **name** `required`
      - Type: `string`
    - **street** `required`
      - Type: `string`
    - **city** `required`
      - Type: `string`
    - **state**
      - Type: `string`
    - **postalCode** `required`
      - Type: `string`
    - **country** `required`
      - Type: `string`

- **items** `required`

  - *List of items included in the invoice*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **description** `required`

        - *Description of the item*
        - Type: `string`

      - **quantity** `required`

        - *Quantity of the item*
        - Type: `number`
        - Range: ≥ 1

      - **unitPrice** `required`

        - *Price per unit of the item*
        - Type: `number`
        - Range: ≥ 0

      - **totalPrice** `required`

        - *Total price for this item*
        - Type: `number`
        - Range: ≥ 0

- **subTotal** `required`

  - *Subtotal for all items*
  - Type: `number`
  - Range: ≥ 0

- **tax** `required`

  - *Tax details*

  - Type: `object`

  - ***Properties***

    - **rate** `required`

      - *Tax rate as a percentage*
      - Type: `number`
      - Range: ≥ 0

    - **amount** `required`

      - *Total tax amount*
      - Type: `number`
      - Range: ≥ 0

- **total** `required`

  - *Total amount due (subtotal + tax)*
  - Type: `number`
  - Range: ≥ 0

- **notes**

  - *Additional notes or instructions for the invoice*
  - Type: `string`

- **status** `required`

  - *Current payment status of the invoice*

  - Type: `string`

  - The value is restricted to the following:

    1. *“Paid”*
    2. *“Unpaid”*
    3. *“Overdue”*



## Resume

Follows the JSON Resume standard

- [API](#tab-panel-525)
- [Resume Schema](#tab-panel-526)

Terminal window

```
curl -X 'POST' \
  'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'  \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \
  --form 'structured_output_json_schema_name="resume"' \
  -F 'file=@/path/to/your/file.pdf;type=application/pdf'
```

#### Structured Output: Resume Schema

Based on <https://github.com/jsonresume/resume-schema>

Type: `object`

***Properties***

- **basics**

  - Type: `object`

  - ***Properties***

    - **name**
      - Type: `string`

    - **label**

      - *e.g. Web Developer*
      - Type: `string`

    - **image**

      - *URL (as per RFC 3986) to a image in JPEG or PNG format*
      - Type: `string`

    - **email**

      - *e.g. <thomas@gmail.com>*
      - Type: `string`
      - String format must be a “email”

    - **phone**

      - *Phone numbers are stored as strings so use any format you like, e.g. 712-117-2923*
      - Type: `string`

    - **url**

      - *URL (as per RFC 3986) to your website, e.g. personal homepage*
      - Type: `string`
      - String format must be a “uri”

    - **summary**

      - *Write a short 2-3 sentence biography about yourself*
      - Type: `string`

    - **location**

      - Type: `object`

      - ***Properties***

        - **address**
          - Type: `string`

        - **postalCode**
          - Type: `string`

        - **city**
          - Type: `string`

        - **countryCode**

          - *code as per ISO-3166-1 ALPHA-2, e.g. US, AU, IN*
          - Type: `string`

        - **region**

          - *The general region where you live. Can be a US state, or a province, for instance.*
          - Type: `string`

    - **profiles**

      - *Specify any number of social networks that you participate in*

      - Type: `array`

        - ***Items***

        - Type: `object`

        - This schema accepts additional properties.

        - ***Properties***

          - **network**

            - *e.g. Facebook or Twitter*
            - Type: `string`

          - **username**

            - *e.g. neutralthoughts*
            - Type: `string`

          - **url**

            - *e.g. <http://twitter.example.com/neutralthoughts>*
            - Type: `string`
            - String format must be a “uri”

- **work**

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **name**

        - *e.g. Facebook*
        - Type: `string`

      - **location**

        - *e.g. Menlo Park, CA*
        - Type: `string`

      - **description**

        - *e.g. Social Media Company*
        - Type: `string`

      - **position**

        - *e.g. Software Engineer*
        - Type: `string`

      - **url**

        - *e.g. <http://facebook.example.com>*
        - Type: `string`
        - String format must be a “uri”

      - **startDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **endDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **summary**

        - *Give an overview of your responsibilities at the company*
        - Type: `string`

      - **highlights**

        - *Specify multiple accomplishments*

        - Type: `array`

          - ***Items***
          - *e.g. Increased profits by 20% from 2011-2012 through viral advertising*
          - Type: `string`

- **volunteer**

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **organization**

        - *e.g. Facebook*
        - Type: `string`

      - **position**

        - *e.g. Software Engineer*
        - Type: `string`

      - **url**

        - *e.g. <http://facebook.example.com>*
        - Type: `string`
        - String format must be a “uri”

      - **startDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **endDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **summary**

        - *Give an overview of your responsibilities at the company*
        - Type: `string`

      - **highlights**

        - *Specify accomplishments and achievements*

        - Type: `array`

          - ***Items***
          - *e.g. Increased profits by 20% from 2011-2012 through viral advertising*
          - Type: `string`

- **education**

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **institution**

        - *e.g. Massachusetts Institute of Technology*
        - Type: `string`

      - **url**

        - *e.g. <http://facebook.example.com>*
        - Type: `string`
        - String format must be a “uri”

      - **area**

        - *e.g. Arts*
        - Type: `string`

      - **studyType**

        - *e.g. Bachelor*
        - Type: `string`

      - **startDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **endDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **score**

        - *grade point average, e.g. 3.67/4.0*
        - Type: `string`

      - **courses**

        - *List notable courses/subjects*

        - Type: `array`

          - ***Items***
          - *e.g. H1302 - Introduction to American history*
          - Type: `string`

- **awards**

  - *Specify any awards you have received throughout your professional career*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **title**

        - *e.g. One of the 100 greatest minds of the century*
        - Type: `string`

      - **date**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **awarder**

        - *e.g. Time Magazine*
        - Type: `string`

      - **summary**

        - *e.g. Received for my work with Quantum Physics*
        - Type: `string`

- **certificates**

  - *Specify any certificates you have received throughout your professional career*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - This schema accepts additional properties.

    - ***Properties***

      - **name**

        - *e.g. Certified Kubernetes Administrator*
        - Type: `string`

      - **date**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **url**

        - *e.g. <http://example.com>*
        - Type: `string`
        - String format must be a “uri”

      - **issuer**

        - *e.g. CNCF*
        - Type: `string`

- **publications**

  - *Specify your publications through your career*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **name**

        - *e.g. The World Wide Web*
        - Type: `string`

      - **publisher**

        - *e.g. IEEE, Computer Magazine*
        - Type: `string`

      - **releaseDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **url**

        - *e.g. <http://www.computer.org.example.com/csdl/mags/co/1996/10/rx069-abs.html>*
        - Type: `string`
        - String format must be a “uri”

      - **summary**

        - *Short summary of publication. e.g. Discussion of the World Wide Web, HTTP, HTML.*
        - Type: `string`

- **skills**

  - *List out your professional skill-set*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - This schema accepts additional properties.

    - ***Properties***

      - **name**

        - *e.g. Web Development*
        - Type: `string`

      - **level**

        - *e.g. Master*
        - Type: `string`

      - **keywords**

        - *List some keywords pertaining to this skill*

        - Type: `array`

          - ***Items***
          - *e.g. HTML*
          - Type: `string`

- **languages**

  - *List any other languages you speak*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **language**

        - *e.g. English, Spanish*
        - Type: `string`

      - **fluency**

        - *e.g. Fluent, Beginner*
        - Type: `string`

- **interests**

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **name**

        - *e.g. Philosophy*
        - Type: `string`

      - **keywords**

        - Type: `array`

          - ***Items***
          - *e.g. Friedrich Nietzsche*
          - Type: `string`

- **references**

  - *List references you have received*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **name**

        - *e.g. Timothy Cook*
        - Type: `string`

      - **reference**

        - *e.g. Joe blogs was a great employee, who turned up to work at least once a week. He exceeded my expectations when it came to doing nothing.*
        - Type: `string`

- **projects**

  - *Specify career projects*

  - Type: `array`

    - ***Items***

    - Type: `object`

    - ***Properties***

      - **name**

        - *e.g. The World Wide Web*
        - Type: `string`

      - **description**

        - *Short summary of project. e.g. Collated works of 2017.*
        - Type: `string`

      - **highlights**

        - *Specify multiple features*

        - Type: `array`

          - ***Items***
          - *e.g. Directs you close but not quite there*
          - Type: `string`

      - **keywords**

        - *Specify special elements involved*

        - Type: `array`

          - ***Items***
          - *e.g. AngularJS*
          - Type: `string`

      - **startDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **endDate**
        - $ref: [#/definitions/iso8601](#/definitions/iso8601)

      - **url**

        - *e.g. <http://www.computer.org/csdl/mags/co/1996/10/rx069-abs.html>*
        - Type: `string`
        - String format must be a “uri”

      - **roles**

        - *Specify your role on this project or in company*

        - Type: `array`

          - ***Items***
          - *e.g. Team Lead, Speaker, Writer*
          - Type: `string`

      - **entity**

        - *Specify the relevant company/entity affiliations e.g. ‘greenpeace’, ‘corporationXYZ’*
        - Type: `string`

      - **type**

        - \_ e.g. ‘volunteering’, ‘presentation’, ‘talk’, ‘application’, ‘conference’\_
        - Type: `string`
