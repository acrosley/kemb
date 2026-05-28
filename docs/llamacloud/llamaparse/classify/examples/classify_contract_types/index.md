---
title: Classify Contract Types | Developer Documentation
---

In this example, we’ll be classifying various contracts by type using LlamaClassify. When provided with a file, we’ll classify it as either a `co_branding` contract or an `affiliate_agreement`.

We’ll use the [CUAD](https://zenodo.org/records/4595826) dataset, which includes various contract types: Affiliate Agreements, Co-Branding contracts, Franchise contracts, and more.

The same workflow can be replicated in the LlamaCloud UI, where you can create classification rules visually instead of in code.

## Install

- [Python](#tab-panel-102)
- [TypeScript](#tab-panel-103)

Terminal window

```
pip install llama-cloud>=1.6
```

Terminal window

```
npm install @llamaindex/llama-cloud
```

## Download Contracts

Download a few contracts from the **Affiliate Agreements** and **Co-Branding** sections of the [CUAD dataset](https://zenodo.org/records/4595826).

## Connect to LlamaCloud

Make sure you have a [LlamaCloud API key](https://cloud.llamaindex.ai?utm_campaign=extract\&utm_medium=recipe). Set it as an environment variable or pass it directly to the SDK.

## Initialize a Client

- [Python](#tab-panel-104)
- [TypeScript](#tab-panel-105)

```
import os
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])
```

```
import LlamaCloud from "@llamaindex/llama-cloud";


const client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY,
});
```

## Define Classification Rules

For this example we’ll classify between `co_branding` and `affiliate_agreements`:

- [Python](#tab-panel-106)
- [TypeScript](#tab-panel-107)

```
rules = [
  {
    "type": "affiliate_agreements",
    "description": "This is a contract that outlines an affiliate agreement",
  },
  {
    "type": "co_branding",
    "description": "This is a contract that outlines a co-branding deal/agreement",
  },
]
```

```
const rules = [
  {
    type: 'affiliate_agreements',
    description: 'This is a contract that outlines an affiliate agreement',
  },
  {
    type: 'co_branding',
    description: 'This is a contract that outlines a co-branding deal/agreement',
  },
];
```

## Classify Files

Upload a file and classify it:

- [Python](#tab-panel-108)
- [TypeScript](#tab-panel-109)

```
import time


file_obj = client.files.create(
    file="CybergyHoldingsInc_Affliate Agreement.pdf",
    purpose="classify",
)


# Create a classify job
job = client.classify.create(
    file_id=file_obj.id,
    configuration={"rules": rules, "mode": "FAST"},  # or "MULTIMODAL"
)


# Poll until complete
status = client.classify.get(job.id)
while status.status == "PENDING":
    time.sleep(2)
    status = client.classify.get(job.id)


if status.result:
    print("Classification Result: " + status.result.type)
    print("Classification Reason: " + status.result.reasoning)
```

```
import fs from 'fs';


const fileObj = await client.files.create({
    file: fs.createReadStream('CybergyHoldingsInc_Affliate Agreement.pdf'),
    purpose: "classify",
});


// Create a classify job
let job = await client.classify.create({
  file_id: fileObj.id,
  configuration: { rules, mode: 'FAST' },  // or 'MULTIMODAL'
});


// Poll until complete
while (job.status === 'PENDING') {
  await new Promise((r) => setTimeout(r, 2000));
  job = await client.classify.get(job.id);
}


if (job.result) {
    console.log("Classification Result: " + job.result.type);
    console.log("Classification Reason: " + job.result.reasoning);
}
```

Once classification is complete, the results include the predicted contract type and the model’s reasoning. For example:

```
Classification Result: affiliate_agreements
Classification Reason: The document is titled 'MARKETING AFFILIATE AGREEMENT' and repeatedly refers to one party as the 'Marketing Affiliate.' The agreement outlines the rights and obligations of the 'Marketing Affiliate' (MA) to market, sell, and support certain technology products, and details the relationship between the company and the affiliate. There is no mention of joint branding, shared trademarks, or collaborative marketing under both parties' brands, which would be indicative of a co-branding agreement. The content is entirely consistent with an affiliate agreement, where one party (the affiliate) is authorized to market and sell the products of another company, rather than a co-branding arrangement. Therefore, the best match is 'affiliate_agreements' with very high confidence.
```
