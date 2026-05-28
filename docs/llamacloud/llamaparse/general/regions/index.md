---
title: Regions | Developer Documentation
description: Information about LlamaCloud regions, including North America and Europe, and their features.
---

LlamaCloud provides cloud services across multiple regions, with availability in North America and Europe currently. You can [sign up](https://cloud.llamaindex.ai/) for a free account to get started in either region.

## Regional Endpoints

|                | North America (NA)      | Europe (EU)                |
| -------------- | ----------------------- | -------------------------- |
| **Cloud**      | cloud.llamaindex.ai     | cloud.eu.llamaindex.ai     |
| **API**        | api.cloud.llamaindex.ai | api.cloud.eu.llamaindex.ai |
| **AWS Region** | us-east-1               | eu-central-1               |

## Features

### How do I use the EU region with the client?

When setting up the LlamaCloud client pass the attribute `base_url = 'api.cloud.eu.llamaindex.ai'`:

```
from llama_cloud.client import LlamaCloud


client = LlamaCloud(
    token='<llama-cloud-api-key>',
    base_url='api.cloud.eu.llamaindex.ai'
)
```

### Are there any differences between NA and EU LlamaCloud?

Both regions support the same core functionality. NA is our primary region where new features are released first, so EU may occasionally have small variations in product behavior or receive new features slightly later. This is primarily due to model availability from our upstream providers.

### Can I connect NA organizations and EU organizations for LlamaCloud, LlamaParse, Billing, etc…?

LlamaIndex does not support this at the moment, Please [let us know](mailto:support@runllama.ai) if you’re interested in this feature.

### Where is my data stored and processed?

Data will be stored within the region it is uploaded to. If interacting with LlamaCloud EU for example, all data provided will remain within the EU region for storage and processing.

### How can I see my organization’s region?

Check your URL. If your url is `https://cloud.llamaindex.ai` that is LlamaCloud NA, if your url is `https://cloud.eu.llamaindex.ai` that is LlamaCloud EU.

### Can I switch my organization between regions?

LlamaCloud does not support migrating between regions at this time. Please [let us know](mailto:support@runllama.ai) if you’re interested in this feature.

## Legal & Compliance

### What privacy and data protection frameworks does LlamaCloud comply with?

LlamaCloud adheres to the General Data Protection Regulation (GDPR) and all other applicable laws and regulations governing our services. We are also SOC 2 Type 2 certified and HIPAA compliant. For more details on our security policies and practices, visit our [Trust Center](https://app.vanta.com/runllama.ai/trust/pkcgbjf8b3ihxjpqdx17nu).

## Can I sign a Data Processing Addendum (DPA) with LlamaIndex?

Yes, if you’d like to sign a Data Processing Addendum (DPA), please [contact us](mailto:support@runllama.ai). Please note that Business Associate Agreements (BAAs) are only available for customers on our Enterprise plan.

### My company is not based in the EU, can I still have my data hosted there?

Yes, you can use LlamaCloud EU independent of your location.

### Do you have a legal entity in the EU that we can contract with?

No, we do not have a legal entity in the EU for customer contracting today.

### Do different legal terms apply if I choose the EU region?

No, the terms are the same for the EU and NA regions.
