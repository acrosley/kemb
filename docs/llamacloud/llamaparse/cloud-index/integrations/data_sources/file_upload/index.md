---
title: File Upload Data Source | Developer Documentation
description: Guide to uploading files directly to LlamaCloud as a data source, including UI, API, and client instructions.
---

Directly upload files

## Configure via UI

![file upload](/_astro/file_upload.eFPLj_OD_Z2wc2BW.png)

## Configure via API / Client

```
from llama_cloud import LlamaCloud


client = LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")


file_obj = client.files.create(file="path/to/your/file.txt", purpose="general")
```

\`\`\`typescript import fs from "fs"; import { LlamaCloud } from "@llamaindex/llama-cloud";

````
const client = new LlamaCloud({
  apiKey: "LLAMA_CLOUD_API_KEY",
});


const fileObj = await client.files.create({
  file: fs.createReadStream('path/to/your/file.txt'),
  purpose: 'general',
});
```
````

\`\`\`python file\_obj = client.files.upload(upload\_file="path/to/your/file.txt") \`\`\` \`\`\`typescript const fileObj = await client.files.upload({ upload\_file: "path/to/your/file.txt", }); \`\`\` \`\`\` # Step 1: Generate a presigned URL for file upload curl -X POST "https\://api.cloud.llamaindex.ai/api/v1/files/presigned-url" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $LLAMA\_CLOUD\_API\_KEY" \ -d '{ "name": "example.txt" }'

````
# Step 2: Use the presigned URL to upload the file to S3 within 30 seconds
curl -X PUT "https://your-presigned-url-from-step-1" \
    -H "Content-Type: text/plain" \
    -F 'file=@path/to/your/example.txt'


# Step 3: Confirm the file upload with LlamaCloud
curl -X PUT "https://api.cloud.llamaindex.ai/api/v1/files/sync" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"
```
````
