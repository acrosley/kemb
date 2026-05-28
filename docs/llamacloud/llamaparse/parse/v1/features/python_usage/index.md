---
title: Python Usage | Developer Documentation
---



## Python options

Some parameters are specific to the Python implementation



## Number of workers

This controls the number of workers to use sending API requests for parsing. The default is 4.

- [Python](#tab-panel-513)

```
parser = LlamaParse(
  num_workers=10
)
```



## Check interval

In synchronous mode (see below), Python will poll to check the status of the job. The default is 1 second.

- [Python](#tab-panel-514)

```
parser = LlamaParse(
  check_interval=10
)
```



## Verbose mode

By default, LlamaParse will print the status of the job as it is uploaded and checked. You can disable this output.

- [Python](#tab-panel-515)

```
parser = LlamaParse(
  verbose=False
)
```



## Use with SimpleDirectoryReader

You can use LlamaParse directly within LlamaIndex by using `SimpleDirectoryReader`. This will parse all files in a directory called `data` and return the parsed documents.

```
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader


parser = LlamaParse()


file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()
```



## Direct usage

It is also possible to call the parser directly, in one of 4 modes:

#### Synchronous parsing

```
documents = parser.load_data("./my_file.pdf")
```

#### Synchronous batch parsing

```
documents = parser.load_data(["./my_file1.pdf", "./my_file2.pdf"])
```

#### Asynchronous parsing

```
documents = await parser.aload_data("./my_file.pdf")
```

#### Asynchronous batch parsing

```
documents = await parser.aload_data(["./my_file1.pdf", "./my_file2.pdf"])
```



## Large document partitioning

The `LlamaParse.partition_pages` option can be used to split parsing of a large document into smaller parse jobs. By default, partitioning is disabled to maintain consistent default behavior between the Python SDK and the raw API.

```
parser = LlamaParse(
    api_key="llx-...",
    num_workers=4,
    partition_pages=100,  # Split large documents into partitions of up to 100 pages each
)
result = parser.parse("./1000-page-long.pdf")
```

In this example, parsing of the 1000 page document would be split into 10 jobs (with 100 pages per job), with up to 4 of the jobs being run concurrently at a time. Once all jobs are completed, the partitioned result would be returned.

`partition_pages` can be used in conjunction with `target_pages` and `max_pages`.

**Note**:

- Due to limitations in the Python SDK, when parsing a single document, partitioned jobs will only be run concurrently if either `target_pages` or `max_pages` are set. If both `target_pages` and `max_pages` are unset, partitioned jobs will be run sequentially when parsing a single document.
- When parsing multiple documents, concurrency is handled at the document level.
