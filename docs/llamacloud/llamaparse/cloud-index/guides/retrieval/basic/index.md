---
title: Basic | Developer Documentation
---

Data Retrieval is a key step in any RAG application. The most common use case is to retrieve relevant context from your data to help with a question.

Once data has been ingested into LlamaCloud, you can use the Retrieval API to retrieve relevant context from your data.

Our Retrieval API allows you to retrieve relevant ground truth text chunks that have been ingested into a Index for a given query. The following snippets show how to run this basic form of retrieval:

- [Python Framework](#tab-panel-231)
- [Python Client SDK](#tab-panel-232)
- [TypeScript Client SDK](#tab-panel-233)

```
import os


os.environ[
    "LLAMA_CLOUD_API_KEY"
] = "llx-..."  # can provide API-key in env or in the constructor later on


from llama_cloud.lib.index import LlamaCloudIndex


# connect to existing index
index = LlamaCloudIndex("my_first_index", project_name="Default")


# configure retriever
# alpha=1.0 restricts it to vector search.
retriever = index.as_retriever(
  dense_similarity_top_k=3,
  alpha=1.0,
  enable_reranking=False,
)
nodes = retriever.retrieve("Example query")
```

```
from llama_cloud import LlamaCloud, AsyncLlamaCloud


client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


# configure retriever
# alpha=1.0 restricts it to vector search.
results = client.pipelines.retrieve(
  pipeline_id='your-existing-pipeline-id',
  query='Example Query',
  dense_similarity_top_k=3,
  alpha=1.0,
  enable_reranking=False,
)


for n in results.retrieval_nodes:
    print(f"Score: {n.score}, Text: {n.node.text}")
```

```
import LlamaCloud from "@llama-index/llama-cloud";


let client = new LlamaCloud({
  apiKey: process.env.LLAMA_CLOUD_API_KEY, // can provide API-key in the constructor or in the env
});


// configure retriever
// alpha=1.0 restricts it to vector search.
const results = await client.pipelines.retrieve('your-existing-pipeline-id', {
  query: 'Example Query',
  dense_similarity_top_k: 3,
  alpha: 1.0,
  enable_reranking: false,
});


for (const n of results.retrieval_nodes || []) {
  console.log(`Score: ${n.score}, Text: ${n.node?.text}`);
}
```

We can build upon this basic form of retrieval by including things like hybrid search, reranking, and metadata filtering to improve the accuracy of the retrieval. These advanced retrieval parameters are described in greater detail in the next section ➡️
