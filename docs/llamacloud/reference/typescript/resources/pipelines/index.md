# Pipelines

## Search Pipelines

`client.pipelines.list(PipelineListParamsquery?, RequestOptionsoptions?): PipelineListResponse`

**get** `/api/v1/pipelines`

Search for pipelines by name, type, or project.

### Parameters

- `query: PipelineListParams`

  - `organization_id?: string | null`

  - `pipeline_name?: string | null`

  - `pipeline_type?: PipelineType | null`

    Enum for representing the type of a pipeline

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `project_id?: string | null`

  - `project_name?: string | null`

### Returns

- `PipelineListResponse = Array<Pipeline>`

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelines = await client.pipelines.list();

console.log(pipelines);
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "class_name": "class_name",
        "embed_batch_size": 1,
        "model_name": "openai-text-embedding-3-small",
        "num_workers": 0
      },
      "type": "MANAGED_OPENAI_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "config_hash": {
      "embedding_config_hash": "embedding_config_hash",
      "parsing_config_hash": "parsing_config_hash",
      "transform_config_hash": "transform_config_hash"
    },
    "created_at": "2019-12-27T18:11:19.117Z",
    "data_sink": {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "component": {
        "foo": "bar"
      },
      "name": "name",
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "sink_type": "PINECONE",
      "created_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z"
    },
    "embedding_model_config": {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "embedding_config": {
        "component": {
          "additional_kwargs": {
            "foo": "bar"
          },
          "api_base": "api_base",
          "api_key": "api_key",
          "api_version": "api_version",
          "azure_deployment": "azure_deployment",
          "azure_endpoint": "azure_endpoint",
          "class_name": "class_name",
          "default_headers": {
            "foo": "string"
          },
          "dimensions": 0,
          "embed_batch_size": 1,
          "max_retries": 0,
          "model_name": "model_name",
          "num_workers": 0,
          "reuse_client": true,
          "timeout": 0
        },
        "type": "AZURE_EMBEDDING"
      },
      "name": "name",
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "created_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z"
    },
    "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "llama_parse_parameters": {
      "adaptive_long_table": true,
      "aggressive_table_extraction": true,
      "annotate_links": true,
      "auto_mode": true,
      "auto_mode_configuration_json": "auto_mode_configuration_json",
      "auto_mode_trigger_on_image_in_page": true,
      "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
      "auto_mode_trigger_on_table_in_page": true,
      "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
      "azure_openai_api_version": "azure_openai_api_version",
      "azure_openai_deployment_name": "azure_openai_deployment_name",
      "azure_openai_endpoint": "azure_openai_endpoint",
      "azure_openai_key": "azure_openai_key",
      "bbox_bottom": 0,
      "bbox_left": 0,
      "bbox_right": 0,
      "bbox_top": 0,
      "bounding_box": "bounding_box",
      "compact_markdown_table": true,
      "complemental_formatting_instruction": "complemental_formatting_instruction",
      "content_guideline_instruction": "content_guideline_instruction",
      "continuous_mode": true,
      "disable_image_extraction": true,
      "disable_ocr": true,
      "disable_reconstruction": true,
      "do_not_cache": true,
      "do_not_unroll_columns": true,
      "enable_cost_optimizer": true,
      "extract_charts": true,
      "extract_layout": true,
      "extract_printed_page_number": true,
      "fast_mode": true,
      "formatting_instruction": "formatting_instruction",
      "gpt4o_api_key": "gpt4o_api_key",
      "gpt4o_mode": true,
      "guess_xlsx_sheet_name": true,
      "hide_footers": true,
      "hide_headers": true,
      "high_res_ocr": true,
      "html_make_all_elements_visible": true,
      "html_remove_fixed_elements": true,
      "html_remove_navigation_elements": true,
      "http_proxy": "http_proxy",
      "ignore_document_elements_for_layout_detection": true,
      "images_to_save": [
        "screenshot"
      ],
      "inline_images_in_markdown": true,
      "input_s3_path": "input_s3_path",
      "input_s3_region": "input_s3_region",
      "input_url": "input_url",
      "internal_is_screenshot_job": true,
      "invalidate_cache": true,
      "is_formatting_instruction": true,
      "job_timeout_extra_time_per_page_in_seconds": 0,
      "job_timeout_in_seconds": 0,
      "keep_page_separator_when_merging_tables": true,
      "languages": [
        "af"
      ],
      "layout_aware": true,
      "line_level_bounding_box": true,
      "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
      "max_pages": 0,
      "max_pages_enforced": 0,
      "merge_tables_across_pages_in_markdown": true,
      "model": "model",
      "outlined_table_extraction": true,
      "output_pdf_of_document": true,
      "output_s3_path_prefix": "output_s3_path_prefix",
      "output_s3_region": "output_s3_region",
      "output_tables_as_HTML": true,
      "page_error_tolerance": 0,
      "page_footer_prefix": "page_footer_prefix",
      "page_footer_suffix": "page_footer_suffix",
      "page_header_prefix": "page_header_prefix",
      "page_header_suffix": "page_header_suffix",
      "page_prefix": "page_prefix",
      "page_separator": "page_separator",
      "page_suffix": "page_suffix",
      "parse_mode": "parse_page_without_llm",
      "parsing_instruction": "parsing_instruction",
      "precise_bounding_box": true,
      "premium_mode": true,
      "presentation_out_of_bounds_content": true,
      "presentation_skip_embedded_data": true,
      "preserve_layout_alignment_across_pages": true,
      "preserve_very_small_text": true,
      "preset": "preset",
      "priority": "low",
      "project_id": "project_id",
      "remove_hidden_text": true,
      "replace_failed_page_mode": "raw_text",
      "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
      "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
      "save_images": true,
      "skip_diagonal_text": true,
      "specialized_chart_parsing_agentic": true,
      "specialized_chart_parsing_efficient": true,
      "specialized_chart_parsing_plus": true,
      "specialized_image_parsing": true,
      "spreadsheet_extract_sub_tables": true,
      "spreadsheet_force_formula_computation": true,
      "spreadsheet_include_hidden_sheets": true,
      "strict_mode_buggy_font": true,
      "strict_mode_image_extraction": true,
      "strict_mode_image_ocr": true,
      "strict_mode_reconstruction": true,
      "structured_output": true,
      "structured_output_json_schema": "structured_output_json_schema",
      "structured_output_json_schema_name": "structured_output_json_schema_name",
      "system_prompt": "system_prompt",
      "system_prompt_append": "system_prompt_append",
      "take_screenshot": true,
      "target_pages": "target_pages",
      "tier": "tier",
      "use_vendor_multimodal_model": true,
      "user_prompt": "user_prompt",
      "vendor_multimodal_api_key": "vendor_multimodal_api_key",
      "vendor_multimodal_model_name": "vendor_multimodal_model_name",
      "version": "version",
      "webhook_configurations": [
        {
          "webhook_events": [
            "parse.success",
            "parse.error"
          ],
          "webhook_headers": {
            "Authorization": "Bearer sk-..."
          },
          "webhook_output_format": "json",
          "webhook_url": "https://example.com/webhooks/llamacloud"
        }
      ],
      "webhook_url": "webhook_url"
    },
    "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "metadata_config": {
      "excluded_embed_metadata_keys": [
        "string"
      ],
      "excluded_llm_metadata_keys": [
        "string"
      ]
    },
    "pipeline_type": "PLAYGROUND",
    "preset_retrieval_parameters": {
      "alpha": 0,
      "class_name": "class_name",
      "dense_similarity_cutoff": 0,
      "dense_similarity_top_k": 1,
      "enable_reranking": true,
      "files_top_k": 1,
      "rerank_top_n": 1,
      "retrieval_mode": "chunks",
      "retrieve_image_nodes": true,
      "retrieve_page_figure_nodes": true,
      "retrieve_page_screenshot_nodes": true,
      "search_filters": {
        "filters": [
          {
            "key": "key",
            "value": 0,
            "operator": "=="
          }
        ],
        "condition": "and"
      },
      "search_filters_inference_schema": {
        "foo": {
          "foo": "bar"
        }
      },
      "sparse_similarity_top_k": 1
    },
    "sparse_model_config": {
      "class_name": "class_name",
      "model_type": "splade"
    },
    "status": "CREATED",
    "transform_config": {
      "chunk_overlap": 0,
      "chunk_size": 1,
      "mode": "auto"
    },
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```

## Create Pipeline

`client.pipelines.create(PipelineCreateParamsparams, RequestOptionsoptions?): Pipeline`

**post** `/api/v1/pipelines`

Create a new managed ingestion pipeline.

A pipeline connects data sources to a vector store for RAG.
After creation, call `POST /pipelines/{id}/sync` to start
ingesting documents.

### Parameters

- `params: PipelineCreateParams`

  - `name: string`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `data_sink?: DataSinkCreate | null`

    Body param: Schema for creating a data sink.

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

  - `data_sink_id?: string | null`

    Body param: Data sink ID. When provided instead of data_sink, the data sink will be looked up by ID.

  - `embedding_config?: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more | null`

    Body param

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `embedding_model_config_id?: string | null`

    Body param: Embedding model config ID. When provided instead of embedding_config, the embedding model config will be looked up by ID.

  - `llama_parse_parameters?: LlamaParseParameters`

    Body param: Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    Body param: The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Body param: Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Body param: Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Body param: Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Body param: Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: string | null`

    Body param: Status of the pipeline deployment.

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig | null`

    Body param: Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.create({ name: 'x' });

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Get Pipeline

`client.pipelines.get(stringpipelineID, RequestOptionsoptions?): Pipeline`

**get** `/api/v1/pipelines/{pipeline_id}`

Get a pipeline by ID.

### Parameters

- `pipelineID: string`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.get('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update Existing Pipeline

`client.pipelines.update(stringpipelineID, PipelineUpdateParamsbody, RequestOptionsoptions?): Pipeline`

**put** `/api/v1/pipelines/{pipeline_id}`

Update an existing pipeline's configuration.

### Parameters

- `pipelineID: string`

- `body: PipelineUpdateParams`

  - `data_sink?: DataSinkCreate | null`

    Schema for creating a data sink.

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

  - `data_sink_id?: string | null`

    Data sink ID. When provided instead of data_sink, the data sink will be looked up by ID.

  - `embedding_config?: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more | null`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `embedding_model_config_id?: string | null`

    Embedding model config ID. When provided instead of embedding_config, the embedding model config will be looked up by ID.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `name?: string | null`

  - `preset_retrieval_parameters?: PresetRetrievalParams | null`

    Schema for the search params for an retrieval execution that can be preset for a pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: string | null`

    Status of the pipeline deployment.

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig | null`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Pipeline

`client.pipelines.delete(stringpipelineID, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}`

Delete a pipeline and all associated resources.

Removes pipeline files, data sources, and vector store data.
This operation is irreversible.

### Parameters

- `pipelineID: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Get Pipeline Status

`client.pipelines.getStatus(stringpipelineID, PipelineGetStatusParamsquery?, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/status`

Get the ingestion status of a managed pipeline.

Returns document counts, sync progress, and the last
effective timestamp. Only available for managed pipelines.

### Parameters

- `pipelineID: string`

- `query: PipelineGetStatusParams`

  - `full_details?: boolean | null`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.getStatus(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(managedIngestionStatusResponse.job_id);
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Upsert Pipeline

`client.pipelines.upsert(PipelineUpsertParamsparams, RequestOptionsoptions?): Pipeline`

**put** `/api/v1/pipelines`

Upsert a pipeline.

Updates the pipeline if one with the same name and project
already exists, otherwise creates a new one.

### Parameters

- `params: PipelineUpsertParams`

  - `name: string`

    Body param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `data_sink?: DataSinkCreate | null`

    Body param: Schema for creating a data sink.

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

  - `data_sink_id?: string | null`

    Body param: Data sink ID. When provided instead of data_sink, the data sink will be looked up by ID.

  - `embedding_config?: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more | null`

    Body param

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `embedding_model_config_id?: string | null`

    Body param: Embedding model config ID. When provided instead of embedding_config, the embedding model config will be looked up by ID.

  - `llama_parse_parameters?: LlamaParseParameters`

    Body param: Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    Body param: The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Body param: Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Body param: Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Body param: Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Body param: Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: string | null`

    Body param: Status of the pipeline deployment.

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig | null`

    Body param: Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.upsert({ name: 'x' });

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Run Search

`client.pipelines.retrieve(stringpipelineID, PipelineRetrieveParamsparams, RequestOptionsoptions?): PipelineRetrieveResponse`

**post** `/api/v1/pipelines/{pipeline_id}/retrieve`

Run a retrieval query against a managed pipeline.

Searches the pipeline's vector store using the provided query
and retrieval parameters. Supports dense, sparse, and hybrid
search modes with configurable top-k and reranking.

### Parameters

- `pipelineID: string`

- `params: PipelineRetrieveParams`

  - `query: string`

    Body param: The query to retrieve against.

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

  - `alpha?: number | null`

    Body param: Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

  - `class_name?: string`

    Body param

  - `dense_similarity_cutoff?: number | null`

    Body param: Minimum similarity score wrt query for retrieval

  - `dense_similarity_top_k?: number | null`

    Body param: Number of nodes for dense retrieval.

  - `enable_reranking?: boolean | null`

    Body param: Enable reranking for retrieval

  - `files_top_k?: number | null`

    Body param: Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

  - `rerank_top_n?: number | null`

    Body param: Number of reranked nodes for returning.

  - `retrieval_mode?: RetrievalMode`

    Body param: The retrieval mode for the query.

    - `"chunks"`

    - `"files_via_metadata"`

    - `"files_via_content"`

    - `"auto_routed"`

  - `retrieve_image_nodes?: boolean`

    Body param: Whether to retrieve image nodes.

  - `retrieve_page_figure_nodes?: boolean`

    Body param: Whether to retrieve page figure nodes.

  - `retrieve_page_screenshot_nodes?: boolean`

    Body param: Whether to retrieve page screenshot nodes.

  - `search_filters?: MetadataFilters | null`

    Body param: Metadata filters for vector stores.

    - `filters: Array<MetadataFilter | MetadataFilters>`

      - `MetadataFilter`

        Comprehensive metadata filter for vector stores to support more operators.

        Value uses Strict types, as int, float and str are compatible types and were all
        converted to string before.

        See: https://docs.pydantic.dev/latest/usage/types/#strict-types

        - `key: string`

        - `value: number | string | Array<string> | 2 more | null`

          - `number`

          - `string`

          - `Array<string>`

          - `Array<number>`

          - `Array<number>`

        - `operator?: "==" | ">" | "<" | 11 more`

          Vector store filter operator.

          - `"=="`

          - `">"`

          - `"<"`

          - `"!="`

          - `">="`

          - `"<="`

          - `"in"`

          - `"nin"`

          - `"any"`

          - `"all"`

          - `"text_match"`

          - `"text_match_insensitive"`

          - `"contains"`

          - `"is_empty"`

      - `MetadataFilters`

        Metadata filters for vector stores.

    - `condition?: "and" | "or" | "not" | null`

      Vector store filter conditions to combine different filters.

      - `"and"`

      - `"or"`

      - `"not"`

  - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Body param: JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `sparse_similarity_top_k?: number | null`

    Body param: Number of nodes for sparse retrieval.

### Returns

- `PipelineRetrieveResponse`

  Schema for the result of an retrieval execution.

  - `pipeline_id: string`

    The ID of the pipeline that the query was retrieved against.

  - `retrieval_nodes: Array<RetrievalNode>`

    The nodes retrieved by the pipeline for the given query.

    - `node: TextNode`

      Provided for backward compatibility.

      - `class_name?: string`

      - `embedding?: Array<number> | null`

        Embedding of the node.

      - `end_char_idx?: number | null`

        End char index of the node.

      - `excluded_embed_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the embed model.

      - `excluded_llm_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the LLM.

      - `extra_info?: Record<string, unknown>`

        A flat dictionary of metadata fields

      - `id_?: string`

        Unique ID of the node.

      - `metadata_seperator?: string`

        Separator between metadata fields when converting to string.

      - `metadata_template?: string`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `mimetype?: string`

        MIME type of the node content.

      - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

        A mapping of relationships to other node information.

        - `RelatedNodeInfo`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

        - `Array<UnionMember1>`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

      - `start_char_idx?: number | null`

        Start char index of the node.

      - `text?: string`

        Text content of the node.

      - `text_template?: string`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `class_name?: string`

    - `score?: number | null`

  - `class_name?: string`

  - `image_nodes?: Array<PageScreenshotNodeWithScore>`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata?: Record<string, unknown> | null`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name?: string`

  - `inferred_search_filters?: MetadataFilters | null`

    Metadata filters for vector stores.

    - `filters: Array<MetadataFilter | MetadataFilters>`

      - `MetadataFilter`

        Comprehensive metadata filter for vector stores to support more operators.

        Value uses Strict types, as int, float and str are compatible types and were all
        converted to string before.

        See: https://docs.pydantic.dev/latest/usage/types/#strict-types

        - `key: string`

        - `value: number | string | Array<string> | 2 more | null`

          - `number`

          - `string`

          - `Array<string>`

          - `Array<number>`

          - `Array<number>`

        - `operator?: "==" | ">" | "<" | 11 more`

          Vector store filter operator.

          - `"=="`

          - `">"`

          - `"<"`

          - `"!="`

          - `">="`

          - `"<="`

          - `"in"`

          - `"nin"`

          - `"any"`

          - `"all"`

          - `"text_match"`

          - `"text_match_insensitive"`

          - `"contains"`

          - `"is_empty"`

      - `MetadataFilters`

        Metadata filters for vector stores.

    - `condition?: "and" | "or" | "not" | null`

      Vector store filter conditions to combine different filters.

      - `"and"`

      - `"or"`

      - `"not"`

  - `metadata?: Record<string, string>`

    Metadata associated with the retrieval execution

  - `page_figure_nodes?: Array<PageFigureNodeWithScore>`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: number`

        The confidence of the figure

      - `figure_name: string`

        The name of the figure

      - `figure_size: number`

        The size of the figure in bytes

      - `file_id: string`

        The ID of the file that the figure was taken from

      - `page_index: number`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise?: boolean`

        Whether the figure is likely to be noise

      - `metadata?: Record<string, unknown> | null`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name?: string`

  - `retrieval_latency?: Record<string, number>`

    The end-to-end latency for retrieval and reranking.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  query: 'x',
});

console.log(pipeline.pipeline_id);
```

#### Response

```json
{
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "retrieval_nodes": [
    {
      "node": {
        "class_name": "class_name",
        "embedding": [
          0
        ],
        "end_char_idx": 0,
        "excluded_embed_metadata_keys": [
          "string"
        ],
        "excluded_llm_metadata_keys": [
          "string"
        ],
        "extra_info": {
          "foo": "bar"
        },
        "id_": "id_",
        "metadata_seperator": "metadata_seperator",
        "metadata_template": "metadata_template",
        "mimetype": "mimetype",
        "relationships": {
          "foo": {
            "node_id": "node_id",
            "class_name": "class_name",
            "hash": "hash",
            "metadata": {
              "foo": "bar"
            },
            "node_type": "1"
          }
        },
        "start_char_idx": 0,
        "text": "text",
        "text_template": "text_template"
      },
      "class_name": "class_name",
      "score": 0
    }
  ],
  "class_name": "class_name",
  "image_nodes": [
    {
      "node": {
        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "image_size": 0,
        "page_index": 0,
        "metadata": {
          "foo": "bar"
        }
      },
      "score": 0,
      "class_name": "class_name"
    }
  ],
  "inferred_search_filters": {
    "filters": [
      {
        "key": "key",
        "value": 0,
        "operator": "=="
      }
    ],
    "condition": "and"
  },
  "metadata": {
    "foo": "string"
  },
  "page_figure_nodes": [
    {
      "node": {
        "confidence": 0,
        "figure_name": "figure_name",
        "figure_size": 0,
        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "page_index": 0,
        "is_likely_noise": true,
        "metadata": {
          "foo": "bar"
        }
      },
      "score": 0,
      "class_name": "class_name"
    }
  ],
  "retrieval_latency": {
    "foo": 0
  }
}
```

## Domain Types

### Advanced Mode Transform Config

- `AdvancedModeTransformConfig`

  - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

    Configuration for the chunking.

    - `NoneChunkingConfig`

      - `mode?: "none"`

        - `"none"`

    - `CharacterChunkingConfig`

      - `chunk_overlap?: number`

      - `chunk_size?: number`

      - `mode?: "character"`

        - `"character"`

    - `TokenChunkingConfig`

      - `chunk_overlap?: number`

      - `chunk_size?: number`

      - `mode?: "token"`

        - `"token"`

      - `separator?: string`

    - `SentenceChunkingConfig`

      - `chunk_overlap?: number`

      - `chunk_size?: number`

      - `mode?: "sentence"`

        - `"sentence"`

      - `paragraph_separator?: string`

      - `separator?: string`

    - `SemanticChunkingConfig`

      - `breakpoint_percentile_threshold?: number`

      - `buffer_size?: number`

      - `mode?: "semantic"`

        - `"semantic"`

  - `mode?: "advanced"`

    - `"advanced"`

  - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

    Configuration for the segmentation.

    - `NoneSegmentationConfig`

      - `mode?: "none"`

        - `"none"`

    - `PageSegmentationConfig`

      - `mode?: "page"`

        - `"page"`

      - `page_separator?: string`

    - `ElementSegmentationConfig`

      - `mode?: "element"`

        - `"element"`

### Auto Transform Config

- `AutoTransformConfig`

  - `chunk_overlap?: number`

    Chunk overlap for the transformation.

  - `chunk_size?: number`

    Chunk size for the transformation.

  - `mode?: "auto"`

    - `"auto"`

### Azure OpenAI Embedding

- `AzureOpenAIEmbedding`

  - `additional_kwargs?: Record<string, unknown>`

    Additional kwargs for the OpenAI API.

  - `api_base?: string`

    The base URL for Azure deployment.

  - `api_key?: string | null`

    The OpenAI API key.

  - `api_version?: string`

    The version for Azure OpenAI API.

  - `azure_deployment?: string | null`

    The Azure deployment to use.

  - `azure_endpoint?: string | null`

    The Azure endpoint to use.

  - `class_name?: string`

  - `default_headers?: Record<string, string> | null`

    The default headers for API requests.

  - `dimensions?: number | null`

    The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `max_retries?: number`

    Maximum number of retries.

  - `model_name?: string`

    The name of the OpenAI embedding model.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `reuse_client?: boolean`

    Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

  - `timeout?: number`

    Timeout for each request.

### Azure OpenAI Embedding Config

- `AzureOpenAIEmbeddingConfig`

  - `component?: AzureOpenAIEmbedding`

    Configuration for the Azure OpenAI embedding model.

    - `additional_kwargs?: Record<string, unknown>`

      Additional kwargs for the OpenAI API.

    - `api_base?: string`

      The base URL for Azure deployment.

    - `api_key?: string | null`

      The OpenAI API key.

    - `api_version?: string`

      The version for Azure OpenAI API.

    - `azure_deployment?: string | null`

      The Azure deployment to use.

    - `azure_endpoint?: string | null`

      The Azure endpoint to use.

    - `class_name?: string`

    - `default_headers?: Record<string, string> | null`

      The default headers for API requests.

    - `dimensions?: number | null`

      The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `max_retries?: number`

      Maximum number of retries.

    - `model_name?: string`

      The name of the OpenAI embedding model.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `reuse_client?: boolean`

      Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

    - `timeout?: number`

      Timeout for each request.

  - `type?: "AZURE_EMBEDDING"`

    Type of the embedding model.

    - `"AZURE_EMBEDDING"`

### Bedrock Embedding

- `BedrockEmbedding`

  - `additional_kwargs?: Record<string, unknown>`

    Additional kwargs for the bedrock client.

  - `aws_access_key_id?: string | null`

    AWS Access Key ID to use

  - `aws_secret_access_key?: string | null`

    AWS Secret Access Key to use

  - `aws_session_token?: string | null`

    AWS Session Token to use

  - `class_name?: string`

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `max_retries?: number`

    The maximum number of API retries.

  - `model_name?: string`

    The modelId of the Bedrock model to use.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `profile_name?: string | null`

    The name of aws profile to use. If not given, then the default profile is used.

  - `region_name?: string | null`

    AWS region name to use. Uses region configured in AWS CLI if not passed

  - `timeout?: number`

    The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

### Bedrock Embedding Config

- `BedrockEmbeddingConfig`

  - `component?: BedrockEmbedding`

    Configuration for the Bedrock embedding model.

    - `additional_kwargs?: Record<string, unknown>`

      Additional kwargs for the bedrock client.

    - `aws_access_key_id?: string | null`

      AWS Access Key ID to use

    - `aws_secret_access_key?: string | null`

      AWS Secret Access Key to use

    - `aws_session_token?: string | null`

      AWS Session Token to use

    - `class_name?: string`

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `max_retries?: number`

      The maximum number of API retries.

    - `model_name?: string`

      The modelId of the Bedrock model to use.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `profile_name?: string | null`

      The name of aws profile to use. If not given, then the default profile is used.

    - `region_name?: string | null`

      AWS region name to use. Uses region configured in AWS CLI if not passed

    - `timeout?: number`

      The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

  - `type?: "BEDROCK_EMBEDDING"`

    Type of the embedding model.

    - `"BEDROCK_EMBEDDING"`

### Cohere Embedding

- `CohereEmbedding`

  - `api_key: string | null`

    The Cohere API key.

  - `class_name?: string`

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `embedding_type?: string`

    Embedding type. If not provided float embedding_type is used when needed.

  - `input_type?: string | null`

    Model Input type. If not provided, search_document and search_query are used when needed.

  - `model_name?: string`

    The modelId of the Cohere model to use.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `truncate?: string`

    Truncation type - START/ END/ NONE

### Cohere Embedding Config

- `CohereEmbeddingConfig`

  - `component?: CohereEmbedding`

    Configuration for the Cohere embedding model.

    - `api_key: string | null`

      The Cohere API key.

    - `class_name?: string`

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `embedding_type?: string`

      Embedding type. If not provided float embedding_type is used when needed.

    - `input_type?: string | null`

      Model Input type. If not provided, search_document and search_query are used when needed.

    - `model_name?: string`

      The modelId of the Cohere model to use.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `truncate?: string`

      Truncation type - START/ END/ NONE

  - `type?: "COHERE_EMBEDDING"`

    Type of the embedding model.

    - `"COHERE_EMBEDDING"`

### Data Sink Create

- `DataSinkCreate`

  Schema for creating a data sink.

  - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

    Component that implements the data sink

    - `Record<string, unknown>`

    - `CloudPineconeVectorStore`

      Cloud Pinecone Vector Store.

      This class is used to store the configuration for a Pinecone vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      api_key (str): API key for authenticating with Pinecone
      index_name (str): name of the Pinecone index
      namespace (optional[str]): namespace to use in the Pinecone index
      insert_kwargs (optional[dict]): additional kwargs to pass during insertion

      - `api_key: string`

        The API key for authenticating with Pinecone

      - `index_name: string`

      - `class_name?: string`

      - `insert_kwargs?: Record<string, unknown> | null`

      - `namespace?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudPostgresVectorStore`

      - `database: string`

      - `embed_dim: number`

      - `host: string`

      - `password: string`

      - `port: number`

      - `schema_name: string`

      - `table_name: string`

      - `user: string`

      - `class_name?: string`

      - `hnsw_settings?: PgVectorHnswSettings | null`

        HNSW settings for PGVector.

        - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

          The distance method to use.

          - `"l2"`

          - `"ip"`

          - `"cosine"`

          - `"l1"`

          - `"hamming"`

          - `"jaccard"`

        - `ef_construction?: number`

          The number of edges to use during the construction phase.

        - `ef_search?: number`

          The number of edges to use during the search phase.

        - `m?: number`

          The number of bi-directional links created for each new element.

        - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

          The type of vector to use.

          - `"vector"`

          - `"half_vec"`

          - `"bit"`

          - `"sparse_vec"`

      - `hybrid_search?: boolean | null`

      - `perform_setup?: boolean`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudQdrantVectorStore`

      Cloud Qdrant Vector Store.

      This class is used to store the configuration for a Qdrant vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      collection_name (str): name of the Qdrant collection
      url (str): url of the Qdrant instance
      api_key (str): API key for authenticating with Qdrant
      max_retries (int): maximum number of retries in case of a failure. Defaults to 3
      client_kwargs (dict): additional kwargs to pass to the Qdrant client

      - `api_key: string`

      - `collection_name: string`

      - `url: string`

      - `class_name?: string`

      - `client_kwargs?: Record<string, unknown>`

      - `max_retries?: number`

      - `supports_nested_metadata_filters?: true`

        - `true`

    - `CloudAzureAISearchVectorStore`

      Cloud Azure AI Search Vector Store.

      - `search_service_api_key: string`

      - `search_service_endpoint: string`

      - `class_name?: string`

      - `client_id?: string | null`

      - `client_secret?: string | null`

      - `embedding_dimension?: number | null`

      - `filterable_metadata_field_keys?: Record<string, unknown> | null`

      - `index_name?: string | null`

      - `search_service_api_version?: string | null`

      - `supports_nested_metadata_filters?: true`

        - `true`

      - `tenant_id?: string | null`

    - `CloudMongoDBAtlasVectorSearch`

      Cloud MongoDB Atlas Vector Store.

      This class is used to store the configuration for a MongoDB Atlas vector store,
      so that it can be created and used in LlamaCloud.

      Args:
      mongodb_uri (str): URI for connecting to MongoDB Atlas
      db_name (str): name of the MongoDB database
      collection_name (str): name of the MongoDB collection
      vector_index_name (str): name of the MongoDB Atlas vector index
      fulltext_index_name (str): name of the MongoDB Atlas full-text index

      - `collection_name: string`

      - `db_name: string`

      - `mongodb_uri: string`

      - `class_name?: string`

      - `embedding_dimension?: number | null`

      - `fulltext_index_name?: string | null`

      - `supports_nested_metadata_filters?: boolean`

      - `vector_index_name?: string | null`

    - `CloudMilvusVectorStore`

      Cloud Milvus Vector Store.

      - `uri: string`

      - `token?: string | null`

      - `class_name?: string`

      - `collection_name?: string | null`

      - `embedding_dimension?: number | null`

      - `supports_nested_metadata_filters?: boolean`

    - `CloudAstraDBVectorStore`

      Cloud AstraDB Vector Store.

      This class is used to store the configuration for an AstraDB vector store, so that it can be
      created and used in LlamaCloud.

      Args:
      token (str): The Astra DB Application Token to use.
      api_endpoint (str): The Astra DB JSON API endpoint for your database.
      collection_name (str): Collection name to use. If not existing, it will be created.
      embedding_dimension (int): Length of the embedding vectors in use.
      keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

      - `token: string`

        The Astra DB Application Token to use

      - `api_endpoint: string`

        The Astra DB JSON API endpoint for your database

      - `collection_name: string`

        Collection name to use. If not existing, it will be created

      - `embedding_dimension: number`

        Length of the embedding vectors in use

      - `class_name?: string`

      - `keyspace?: string | null`

        The keyspace to use. If not provided, 'default_keyspace'

      - `supports_nested_metadata_filters?: true`

        - `true`

  - `name: string`

    The name of the data sink.

  - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

    - `"PINECONE"`

    - `"POSTGRES"`

    - `"QDRANT"`

    - `"AZUREAI_SEARCH"`

    - `"MONGODB_ATLAS"`

    - `"MILVUS"`

    - `"ASTRA_DB"`

### Gemini Embedding

- `GeminiEmbedding`

  - `api_base?: string | null`

    API base to access the model. Defaults to None.

  - `api_key?: string | null`

    API key to access the model. Defaults to None.

  - `class_name?: string`

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `model_name?: string`

    The modelId of the Gemini model to use.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `output_dimensionality?: number | null`

    Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

  - `task_type?: string | null`

    The task for embedding model.

  - `title?: string | null`

    Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

  - `transport?: string | null`

    Transport to access the model. Defaults to None.

### Gemini Embedding Config

- `GeminiEmbeddingConfig`

  - `component?: GeminiEmbedding`

    Configuration for the Gemini embedding model.

    - `api_base?: string | null`

      API base to access the model. Defaults to None.

    - `api_key?: string | null`

      API key to access the model. Defaults to None.

    - `class_name?: string`

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `model_name?: string`

      The modelId of the Gemini model to use.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `output_dimensionality?: number | null`

      Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

    - `task_type?: string | null`

      The task for embedding model.

    - `title?: string | null`

      Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

    - `transport?: string | null`

      Transport to access the model. Defaults to None.

  - `type?: "GEMINI_EMBEDDING"`

    Type of the embedding model.

    - `"GEMINI_EMBEDDING"`

### Hugging Face Inference API Embedding

- `HuggingFaceInferenceAPIEmbedding`

  - `token?: string | boolean | null`

    Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

    - `string`

    - `boolean`

  - `class_name?: string`

  - `cookies?: Record<string, string> | null`

    Additional cookies to send to the server.

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `headers?: Record<string, string> | null`

    Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

  - `model_name?: string | null`

    Hugging Face model name. If None, the task will be used.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `pooling?: "cls" | "mean" | "last" | null`

    Enum of possible pooling choices with pooling behaviors.

    - `"cls"`

    - `"mean"`

    - `"last"`

  - `query_instruction?: string | null`

    Instruction to prepend during query embedding.

  - `task?: string | null`

    Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

  - `text_instruction?: string | null`

    Instruction to prepend during text embedding.

  - `timeout?: number | null`

    The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

### Hugging Face Inference API Embedding Config

- `HuggingFaceInferenceAPIEmbeddingConfig`

  - `component?: HuggingFaceInferenceAPIEmbedding`

    Configuration for the HuggingFace Inference API embedding model.

    - `token?: string | boolean | null`

      Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

      - `string`

      - `boolean`

    - `class_name?: string`

    - `cookies?: Record<string, string> | null`

      Additional cookies to send to the server.

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `headers?: Record<string, string> | null`

      Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

    - `model_name?: string | null`

      Hugging Face model name. If None, the task will be used.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `pooling?: "cls" | "mean" | "last" | null`

      Enum of possible pooling choices with pooling behaviors.

      - `"cls"`

      - `"mean"`

      - `"last"`

    - `query_instruction?: string | null`

      Instruction to prepend during query embedding.

    - `task?: string | null`

      Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

    - `text_instruction?: string | null`

      Instruction to prepend during text embedding.

    - `timeout?: number | null`

      The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

  - `type?: "HUGGINGFACE_API_EMBEDDING"`

    Type of the embedding model.

    - `"HUGGINGFACE_API_EMBEDDING"`

### Llama Parse Parameters

- `LlamaParseParameters`

  - `adaptive_long_table?: boolean | null`

  - `aggressive_table_extraction?: boolean | null`

  - `annotate_links?: boolean | null`

  - `auto_mode?: boolean | null`

  - `auto_mode_configuration_json?: string | null`

  - `auto_mode_trigger_on_image_in_page?: boolean | null`

  - `auto_mode_trigger_on_regexp_in_page?: string | null`

  - `auto_mode_trigger_on_table_in_page?: boolean | null`

  - `auto_mode_trigger_on_text_in_page?: string | null`

  - `azure_openai_api_version?: string | null`

  - `azure_openai_deployment_name?: string | null`

  - `azure_openai_endpoint?: string | null`

  - `azure_openai_key?: string | null`

  - `bbox_bottom?: number | null`

  - `bbox_left?: number | null`

  - `bbox_right?: number | null`

  - `bbox_top?: number | null`

  - `bounding_box?: string | null`

  - `compact_markdown_table?: boolean | null`

  - `complemental_formatting_instruction?: string | null`

  - `content_guideline_instruction?: string | null`

  - `continuous_mode?: boolean | null`

  - `disable_image_extraction?: boolean | null`

  - `disable_ocr?: boolean | null`

  - `disable_reconstruction?: boolean | null`

  - `do_not_cache?: boolean | null`

  - `do_not_unroll_columns?: boolean | null`

  - `enable_cost_optimizer?: boolean | null`

  - `extract_charts?: boolean | null`

  - `extract_layout?: boolean | null`

  - `extract_printed_page_number?: boolean | null`

  - `fast_mode?: boolean | null`

  - `formatting_instruction?: string | null`

  - `gpt4o_api_key?: string | null`

  - `gpt4o_mode?: boolean | null`

  - `guess_xlsx_sheet_name?: boolean | null`

  - `hide_footers?: boolean | null`

  - `hide_headers?: boolean | null`

  - `high_res_ocr?: boolean | null`

  - `html_make_all_elements_visible?: boolean | null`

  - `html_remove_fixed_elements?: boolean | null`

  - `html_remove_navigation_elements?: boolean | null`

  - `http_proxy?: string | null`

  - `ignore_document_elements_for_layout_detection?: boolean | null`

  - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

    - `"screenshot"`

    - `"embedded"`

    - `"layout"`

  - `inline_images_in_markdown?: boolean | null`

  - `input_s3_path?: string | null`

  - `input_s3_region?: string | null`

  - `input_url?: string | null`

  - `internal_is_screenshot_job?: boolean | null`

  - `invalidate_cache?: boolean | null`

  - `is_formatting_instruction?: boolean | null`

  - `job_timeout_extra_time_per_page_in_seconds?: number | null`

  - `job_timeout_in_seconds?: number | null`

  - `keep_page_separator_when_merging_tables?: boolean | null`

  - `languages?: Array<ParsingLanguages>`

    - `"af"`

    - `"az"`

    - `"bs"`

    - `"cs"`

    - `"cy"`

    - `"da"`

    - `"de"`

    - `"en"`

    - `"es"`

    - `"et"`

    - `"fr"`

    - `"ga"`

    - `"hr"`

    - `"hu"`

    - `"id"`

    - `"is"`

    - `"it"`

    - `"ku"`

    - `"la"`

    - `"lt"`

    - `"lv"`

    - `"mi"`

    - `"ms"`

    - `"mt"`

    - `"nl"`

    - `"no"`

    - `"oc"`

    - `"pi"`

    - `"pl"`

    - `"pt"`

    - `"ro"`

    - `"rs_latin"`

    - `"sk"`

    - `"sl"`

    - `"sq"`

    - `"sv"`

    - `"sw"`

    - `"tl"`

    - `"tr"`

    - `"uz"`

    - `"vi"`

    - `"ar"`

    - `"fa"`

    - `"ug"`

    - `"ur"`

    - `"bn"`

    - `"as"`

    - `"mni"`

    - `"ru"`

    - `"rs_cyrillic"`

    - `"be"`

    - `"bg"`

    - `"uk"`

    - `"mn"`

    - `"abq"`

    - `"ady"`

    - `"kbd"`

    - `"ava"`

    - `"dar"`

    - `"inh"`

    - `"che"`

    - `"lbe"`

    - `"lez"`

    - `"tab"`

    - `"tjk"`

    - `"hi"`

    - `"mr"`

    - `"ne"`

    - `"bh"`

    - `"mai"`

    - `"ang"`

    - `"bho"`

    - `"mah"`

    - `"sck"`

    - `"new"`

    - `"gom"`

    - `"sa"`

    - `"bgc"`

    - `"th"`

    - `"ch_sim"`

    - `"ch_tra"`

    - `"ja"`

    - `"ko"`

    - `"ta"`

    - `"te"`

    - `"kn"`

  - `layout_aware?: boolean | null`

  - `line_level_bounding_box?: boolean | null`

  - `markdown_table_multiline_header_separator?: string | null`

  - `max_pages?: number | null`

  - `max_pages_enforced?: number | null`

  - `merge_tables_across_pages_in_markdown?: boolean | null`

  - `model?: string | null`

  - `outlined_table_extraction?: boolean | null`

  - `output_pdf_of_document?: boolean | null`

  - `output_s3_path_prefix?: string | null`

  - `output_s3_region?: string | null`

  - `output_tables_as_HTML?: boolean | null`

  - `page_error_tolerance?: number | null`

  - `page_footer_prefix?: string | null`

  - `page_footer_suffix?: string | null`

  - `page_header_prefix?: string | null`

  - `page_header_suffix?: string | null`

  - `page_prefix?: string | null`

  - `page_separator?: string | null`

  - `page_suffix?: string | null`

  - `parse_mode?: ParsingMode | null`

    Enum for representing the mode of parsing to be used.

    - `"parse_page_without_llm"`

    - `"parse_page_with_llm"`

    - `"parse_page_with_lvm"`

    - `"parse_page_with_agent"`

    - `"parse_page_with_layout_agent"`

    - `"parse_document_with_llm"`

    - `"parse_document_with_lvm"`

    - `"parse_document_with_agent"`

  - `parsing_instruction?: string | null`

  - `precise_bounding_box?: boolean | null`

  - `premium_mode?: boolean | null`

  - `presentation_out_of_bounds_content?: boolean | null`

  - `presentation_skip_embedded_data?: boolean | null`

  - `preserve_layout_alignment_across_pages?: boolean | null`

  - `preserve_very_small_text?: boolean | null`

  - `preset?: string | null`

  - `priority?: "low" | "medium" | "high" | "critical" | null`

    The priority for the request. This field may be ignored or overwritten depending on the organization tier.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"critical"`

  - `project_id?: string | null`

  - `remove_hidden_text?: boolean | null`

  - `replace_failed_page_mode?: FailPageMode | null`

    Enum for representing the different available page error handling modes.

    - `"raw_text"`

    - `"blank_page"`

    - `"error_message"`

  - `replace_failed_page_with_error_message_prefix?: string | null`

  - `replace_failed_page_with_error_message_suffix?: string | null`

  - `save_images?: boolean | null`

  - `skip_diagonal_text?: boolean | null`

  - `specialized_chart_parsing_agentic?: boolean | null`

  - `specialized_chart_parsing_efficient?: boolean | null`

  - `specialized_chart_parsing_plus?: boolean | null`

  - `specialized_image_parsing?: boolean | null`

  - `spreadsheet_extract_sub_tables?: boolean | null`

  - `spreadsheet_force_formula_computation?: boolean | null`

  - `spreadsheet_include_hidden_sheets?: boolean | null`

  - `strict_mode_buggy_font?: boolean | null`

  - `strict_mode_image_extraction?: boolean | null`

  - `strict_mode_image_ocr?: boolean | null`

  - `strict_mode_reconstruction?: boolean | null`

  - `structured_output?: boolean | null`

  - `structured_output_json_schema?: string | null`

  - `structured_output_json_schema_name?: string | null`

  - `system_prompt?: string | null`

  - `system_prompt_append?: string | null`

  - `take_screenshot?: boolean | null`

  - `target_pages?: string | null`

  - `tier?: string | null`

  - `use_vendor_multimodal_model?: boolean | null`

  - `user_prompt?: string | null`

  - `vendor_multimodal_api_key?: string | null`

  - `vendor_multimodal_model_name?: string | null`

  - `version?: string | null`

  - `webhook_configurations?: Array<WebhookConfiguration> | null`

    Outbound webhook endpoints to notify on job status changes

    - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

      Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

      - `"extract.pending"`

      - `"extract.success"`

      - `"extract.error"`

      - `"extract.partial_success"`

      - `"extract.cancelled"`

      - `"parse.pending"`

      - `"parse.running"`

      - `"parse.success"`

      - `"parse.error"`

      - `"parse.partial_success"`

      - `"parse.cancelled"`

      - `"classify.pending"`

      - `"classify.success"`

      - `"classify.error"`

      - `"classify.partial_success"`

      - `"classify.cancelled"`

      - `"unmapped_event"`

    - `webhook_headers?: Record<string, string> | null`

      Custom HTTP headers sent with each webhook request (e.g. auth tokens)

    - `webhook_output_format?: string | null`

      Response format sent to the webhook: 'string' (default) or 'json'

    - `webhook_url?: string | null`

      URL to receive webhook POST notifications

  - `webhook_url?: string | null`

### Llm Parameters

- `LlmParameters`

  - `class_name?: string`

  - `model_name?: "GPT_4O" | "GPT_4O_MINI" | "GPT_4_1" | 10 more`

    The name of the model to use for LLM completions.

    - `"GPT_4O"`

    - `"GPT_4O_MINI"`

    - `"GPT_4_1"`

    - `"GPT_4_1_NANO"`

    - `"GPT_4_1_MINI"`

    - `"AZURE_OPENAI_GPT_4O"`

    - `"AZURE_OPENAI_GPT_4O_MINI"`

    - `"AZURE_OPENAI_GPT_4_1"`

    - `"AZURE_OPENAI_GPT_4_1_MINI"`

    - `"AZURE_OPENAI_GPT_4_1_NANO"`

    - `"CLAUDE_4_5_SONNET"`

    - `"BEDROCK_CLAUDE_3_5_SONNET_V1"`

    - `"BEDROCK_CLAUDE_3_5_SONNET_V2"`

  - `system_prompt?: string | null`

    The system prompt to use for the completion.

  - `temperature?: number | null`

    The temperature value for the model.

  - `use_chain_of_thought_reasoning?: boolean | null`

    Whether to use chain of thought reasoning.

  - `use_citation?: boolean | null`

    Whether to show citations in the response.

### Managed Ingestion Status Response

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Message Role

- `MessageRole = "system" | "developer" | "user" | 5 more`

  Message role.

  - `"system"`

  - `"developer"`

  - `"user"`

  - `"assistant"`

  - `"function"`

  - `"tool"`

  - `"chatbot"`

  - `"model"`

### Metadata Filters

- `MetadataFilters`

  Metadata filters for vector stores.

  - `filters: Array<MetadataFilter | MetadataFilters>`

    - `MetadataFilter`

      Comprehensive metadata filter for vector stores to support more operators.

      Value uses Strict types, as int, float and str are compatible types and were all
      converted to string before.

      See: https://docs.pydantic.dev/latest/usage/types/#strict-types

      - `key: string`

      - `value: number | string | Array<string> | 2 more | null`

        - `number`

        - `string`

        - `Array<string>`

        - `Array<number>`

        - `Array<number>`

      - `operator?: "==" | ">" | "<" | 11 more`

        Vector store filter operator.

        - `"=="`

        - `">"`

        - `"<"`

        - `"!="`

        - `">="`

        - `"<="`

        - `"in"`

        - `"nin"`

        - `"any"`

        - `"all"`

        - `"text_match"`

        - `"text_match_insensitive"`

        - `"contains"`

        - `"is_empty"`

    - `MetadataFilters`

      Metadata filters for vector stores.

  - `condition?: "and" | "or" | "not" | null`

    Vector store filter conditions to combine different filters.

    - `"and"`

    - `"or"`

    - `"not"`

### OpenAI Embedding

- `OpenAIEmbedding`

  - `additional_kwargs?: Record<string, unknown>`

    Additional kwargs for the OpenAI API.

  - `api_base?: string | null`

    The base URL for OpenAI API.

  - `api_key?: string | null`

    The OpenAI API key.

  - `api_version?: string | null`

    The version for OpenAI API.

  - `class_name?: string`

  - `default_headers?: Record<string, string> | null`

    The default headers for API requests.

  - `dimensions?: number | null`

    The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `max_retries?: number`

    Maximum number of retries.

  - `model_name?: string`

    The name of the OpenAI embedding model.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

  - `reuse_client?: boolean`

    Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

  - `timeout?: number`

    Timeout for each request.

### OpenAI Embedding Config

- `OpenAIEmbeddingConfig`

  - `component?: OpenAIEmbedding`

    Configuration for the OpenAI embedding model.

    - `additional_kwargs?: Record<string, unknown>`

      Additional kwargs for the OpenAI API.

    - `api_base?: string | null`

      The base URL for OpenAI API.

    - `api_key?: string | null`

      The OpenAI API key.

    - `api_version?: string | null`

      The version for OpenAI API.

    - `class_name?: string`

    - `default_headers?: Record<string, string> | null`

      The default headers for API requests.

    - `dimensions?: number | null`

      The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `max_retries?: number`

      Maximum number of retries.

    - `model_name?: string`

      The name of the OpenAI embedding model.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

    - `reuse_client?: boolean`

      Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

    - `timeout?: number`

      Timeout for each request.

  - `type?: "OPENAI_EMBEDDING"`

    Type of the embedding model.

    - `"OPENAI_EMBEDDING"`

### Page Figure Node With Score

- `PageFigureNodeWithScore`

  Page figure metadata with score

  - `node: Node`

    - `confidence: number`

      The confidence of the figure

    - `figure_name: string`

      The name of the figure

    - `figure_size: number`

      The size of the figure in bytes

    - `file_id: string`

      The ID of the file that the figure was taken from

    - `page_index: number`

      The index of the page for which the figure is taken (0-indexed)

    - `is_likely_noise?: boolean`

      Whether the figure is likely to be noise

    - `metadata?: Record<string, unknown> | null`

      Metadata for the figure

  - `score: number`

    The score of the figure node

  - `class_name?: string`

### Page Screenshot Node With Score

- `PageScreenshotNodeWithScore`

  Page screenshot metadata with score

  - `node: Node`

    - `file_id: string`

      The ID of the file that the page screenshot was taken from

    - `image_size: number`

      The size of the image in bytes

    - `page_index: number`

      The index of the page for which the screenshot is taken (0-indexed)

    - `metadata?: Record<string, unknown> | null`

      Metadata for the screenshot

  - `score: number`

    The score of the screenshot node

  - `class_name?: string`

### Pipeline

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Pipeline Create

- `PipelineCreate`

  Schema for creating a pipeline.

  - `name: string`

  - `data_sink?: DataSinkCreate | null`

    Schema for creating a data sink.

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

  - `data_sink_id?: string | null`

    Data sink ID. When provided instead of data_sink, the data sink will be looked up by ID.

  - `embedding_config?: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more | null`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `embedding_model_config_id?: string | null`

    Embedding model config ID. When provided instead of embedding_config, the embedding model config will be looked up by ID.

  - `llama_parse_parameters?: LlamaParseParameters`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: string | null`

    Status of the pipeline deployment.

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig | null`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

### Pipeline Metadata Config

- `PipelineMetadataConfig`

  - `excluded_embed_metadata_keys?: Array<string>`

    List of metadata keys to exclude from embeddings

  - `excluded_llm_metadata_keys?: Array<string>`

    List of metadata keys to exclude from LLM during retrieval

### Pipeline Type

- `PipelineType = "PLAYGROUND" | "MANAGED"`

  Enum for representing the type of a pipeline

  - `"PLAYGROUND"`

  - `"MANAGED"`

### Preset Retrieval Params

- `PresetRetrievalParams`

  Schema for the search params for an retrieval execution that can be preset for a pipeline.

  - `alpha?: number | null`

    Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

  - `class_name?: string`

  - `dense_similarity_cutoff?: number | null`

    Minimum similarity score wrt query for retrieval

  - `dense_similarity_top_k?: number | null`

    Number of nodes for dense retrieval.

  - `enable_reranking?: boolean | null`

    Enable reranking for retrieval

  - `files_top_k?: number | null`

    Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

  - `rerank_top_n?: number | null`

    Number of reranked nodes for returning.

  - `retrieval_mode?: RetrievalMode`

    The retrieval mode for the query.

    - `"chunks"`

    - `"files_via_metadata"`

    - `"files_via_content"`

    - `"auto_routed"`

  - `retrieve_image_nodes?: boolean`

    Whether to retrieve image nodes.

  - `retrieve_page_figure_nodes?: boolean`

    Whether to retrieve page figure nodes.

  - `retrieve_page_screenshot_nodes?: boolean`

    Whether to retrieve page screenshot nodes.

  - `search_filters?: MetadataFilters | null`

    Metadata filters for vector stores.

    - `filters: Array<MetadataFilter | MetadataFilters>`

      - `MetadataFilter`

        Comprehensive metadata filter for vector stores to support more operators.

        Value uses Strict types, as int, float and str are compatible types and were all
        converted to string before.

        See: https://docs.pydantic.dev/latest/usage/types/#strict-types

        - `key: string`

        - `value: number | string | Array<string> | 2 more | null`

          - `number`

          - `string`

          - `Array<string>`

          - `Array<number>`

          - `Array<number>`

        - `operator?: "==" | ">" | "<" | 11 more`

          Vector store filter operator.

          - `"=="`

          - `">"`

          - `"<"`

          - `"!="`

          - `">="`

          - `"<="`

          - `"in"`

          - `"nin"`

          - `"any"`

          - `"all"`

          - `"text_match"`

          - `"text_match_insensitive"`

          - `"contains"`

          - `"is_empty"`

      - `MetadataFilters`

        Metadata filters for vector stores.

    - `condition?: "and" | "or" | "not" | null`

      Vector store filter conditions to combine different filters.

      - `"and"`

      - `"or"`

      - `"not"`

  - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `sparse_similarity_top_k?: number | null`

    Number of nodes for sparse retrieval.

### Retrieval Mode

- `RetrievalMode = "chunks" | "files_via_metadata" | "files_via_content" | "auto_routed"`

  - `"chunks"`

  - `"files_via_metadata"`

  - `"files_via_content"`

  - `"auto_routed"`

### Sparse Model Config

- `SparseModelConfig`

  Configuration for sparse embedding models used in hybrid search.

  This allows users to choose between Splade and BM25 models for
  sparse retrieval in managed data sinks.

  - `class_name?: string`

  - `model_type?: "splade" | "bm25" | "auto"`

    The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

    - `"splade"`

    - `"bm25"`

    - `"auto"`

### Vertex AI Embedding Config

- `VertexAIEmbeddingConfig`

  - `component?: VertexTextEmbedding`

    Configuration for the VertexAI embedding model.

    - `client_email: string | null`

      The client email for the VertexAI credentials.

    - `location: string`

      The default location to use when making API calls.

    - `private_key: string | null`

      The private key for the VertexAI credentials.

    - `private_key_id: string | null`

      The private key ID for the VertexAI credentials.

    - `project: string`

      The default GCP project to use when making Vertex API calls.

    - `token_uri: string | null`

      The token URI for the VertexAI credentials.

    - `additional_kwargs?: Record<string, unknown>`

      Additional kwargs for the Vertex.

    - `class_name?: string`

    - `embed_batch_size?: number`

      The batch size for embedding calls.

    - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

      The embedding mode to use.

      - `"default"`

      - `"classification"`

      - `"clustering"`

      - `"similarity"`

      - `"retrieval"`

    - `model_name?: string`

      The modelId of the VertexAI model to use.

    - `num_workers?: number | null`

      The number of workers to use for async embedding calls.

  - `type?: "VERTEXAI_EMBEDDING"`

    Type of the embedding model.

    - `"VERTEXAI_EMBEDDING"`

### Vertex Text Embedding

- `VertexTextEmbedding`

  - `client_email: string | null`

    The client email for the VertexAI credentials.

  - `location: string`

    The default location to use when making API calls.

  - `private_key: string | null`

    The private key for the VertexAI credentials.

  - `private_key_id: string | null`

    The private key ID for the VertexAI credentials.

  - `project: string`

    The default GCP project to use when making Vertex API calls.

  - `token_uri: string | null`

    The token URI for the VertexAI credentials.

  - `additional_kwargs?: Record<string, unknown>`

    Additional kwargs for the Vertex.

  - `class_name?: string`

  - `embed_batch_size?: number`

    The batch size for embedding calls.

  - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

    The embedding mode to use.

    - `"default"`

    - `"classification"`

    - `"clustering"`

    - `"similarity"`

    - `"retrieval"`

  - `model_name?: string`

    The modelId of the VertexAI model to use.

  - `num_workers?: number | null`

    The number of workers to use for async embedding calls.

### Pipeline List Response

- `PipelineListResponse = Array<Pipeline>`

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Pipeline Retrieve Response

- `PipelineRetrieveResponse`

  Schema for the result of an retrieval execution.

  - `pipeline_id: string`

    The ID of the pipeline that the query was retrieved against.

  - `retrieval_nodes: Array<RetrievalNode>`

    The nodes retrieved by the pipeline for the given query.

    - `node: TextNode`

      Provided for backward compatibility.

      - `class_name?: string`

      - `embedding?: Array<number> | null`

        Embedding of the node.

      - `end_char_idx?: number | null`

        End char index of the node.

      - `excluded_embed_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the embed model.

      - `excluded_llm_metadata_keys?: Array<string>`

        Metadata keys that are excluded from text for the LLM.

      - `extra_info?: Record<string, unknown>`

        A flat dictionary of metadata fields

      - `id_?: string`

        Unique ID of the node.

      - `metadata_seperator?: string`

        Separator between metadata fields when converting to string.

      - `metadata_template?: string`

        Template for how metadata is formatted, with {key} and {value} placeholders.

      - `mimetype?: string`

        MIME type of the node content.

      - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

        A mapping of relationships to other node information.

        - `RelatedNodeInfo`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

        - `Array<UnionMember1>`

          - `node_id: string`

          - `class_name?: string`

          - `hash?: string | null`

          - `metadata?: Record<string, unknown>`

          - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

            - `"1" | "2" | "3" | 2 more`

              - `"1"`

              - `"2"`

              - `"3"`

              - `"4"`

              - `"5"`

            - `(string & {})`

      - `start_char_idx?: number | null`

        Start char index of the node.

      - `text?: string`

        Text content of the node.

      - `text_template?: string`

        Template for how text is formatted, with {content} and {metadata_str} placeholders.

    - `class_name?: string`

    - `score?: number | null`

  - `class_name?: string`

  - `image_nodes?: Array<PageScreenshotNodeWithScore>`

    The image nodes retrieved by the pipeline for the given query. Deprecated - will soon be replaced with 'page_screenshot_nodes'.

    - `node: Node`

      - `file_id: string`

        The ID of the file that the page screenshot was taken from

      - `image_size: number`

        The size of the image in bytes

      - `page_index: number`

        The index of the page for which the screenshot is taken (0-indexed)

      - `metadata?: Record<string, unknown> | null`

        Metadata for the screenshot

    - `score: number`

      The score of the screenshot node

    - `class_name?: string`

  - `inferred_search_filters?: MetadataFilters | null`

    Metadata filters for vector stores.

    - `filters: Array<MetadataFilter | MetadataFilters>`

      - `MetadataFilter`

        Comprehensive metadata filter for vector stores to support more operators.

        Value uses Strict types, as int, float and str are compatible types and were all
        converted to string before.

        See: https://docs.pydantic.dev/latest/usage/types/#strict-types

        - `key: string`

        - `value: number | string | Array<string> | 2 more | null`

          - `number`

          - `string`

          - `Array<string>`

          - `Array<number>`

          - `Array<number>`

        - `operator?: "==" | ">" | "<" | 11 more`

          Vector store filter operator.

          - `"=="`

          - `">"`

          - `"<"`

          - `"!="`

          - `">="`

          - `"<="`

          - `"in"`

          - `"nin"`

          - `"any"`

          - `"all"`

          - `"text_match"`

          - `"text_match_insensitive"`

          - `"contains"`

          - `"is_empty"`

      - `MetadataFilters`

        Metadata filters for vector stores.

    - `condition?: "and" | "or" | "not" | null`

      Vector store filter conditions to combine different filters.

      - `"and"`

      - `"or"`

      - `"not"`

  - `metadata?: Record<string, string>`

    Metadata associated with the retrieval execution

  - `page_figure_nodes?: Array<PageFigureNodeWithScore>`

    The page figure nodes retrieved by the pipeline for the given query.

    - `node: Node`

      - `confidence: number`

        The confidence of the figure

      - `figure_name: string`

        The name of the figure

      - `figure_size: number`

        The size of the figure in bytes

      - `file_id: string`

        The ID of the file that the figure was taken from

      - `page_index: number`

        The index of the page for which the figure is taken (0-indexed)

      - `is_likely_noise?: boolean`

        Whether the figure is likely to be noise

      - `metadata?: Record<string, unknown> | null`

        Metadata for the figure

    - `score: number`

      The score of the figure node

    - `class_name?: string`

  - `retrieval_latency?: Record<string, number>`

    The end-to-end latency for retrieval and reranking.

# Sync

## Sync Pipeline

`client.pipelines.sync.create(stringpipelineID, RequestOptionsoptions?): Pipeline`

**post** `/api/v1/pipelines/{pipeline_id}/sync`

Trigger an incremental sync for a managed pipeline.

Processes new and updated documents from data sources and
files, then updates the index for retrieval.

### Parameters

- `pipelineID: string`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.sync.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Cancel Pipeline Sync

`client.pipelines.sync.cancel(stringpipelineID, RequestOptionsoptions?): Pipeline`

**post** `/api/v1/pipelines/{pipeline_id}/sync/cancel`

Cancel all running sync jobs for a pipeline.

### Parameters

- `pipelineID: string`

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.sync.cancel('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

# Data Sources

## List Pipeline Data Sources

`client.pipelines.dataSources.getDataSources(stringpipelineID, RequestOptionsoptions?): DataSourceGetDataSourcesResponse`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources`

Get data sources for a pipeline.

### Parameters

- `pipelineID: string`

### Returns

- `DataSourceGetDataSourcesResponse = Array<PipelineDataSource>`

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineDataSources = await client.pipelines.dataSources.getDataSources(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(pipelineDataSources);
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "last_synced_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "source_type": "S3",
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "sync_interval": 0,
    "sync_schedule_set_by": "sync_schedule_set_by",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "version_metadata": {
      "reader_version": "1.0"
    }
  }
]
```

## Add Data Sources To Pipeline

`client.pipelines.dataSources.updateDataSources(stringpipelineID, DataSourceUpdateDataSourcesParamsparams, RequestOptionsoptions?): DataSourceUpdateDataSourcesResponse`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources`

Add data sources to a pipeline.

### Parameters

- `pipelineID: string`

- `params: DataSourceUpdateDataSourcesParams`

  - `body: Array<Body>`

    - `data_source_id: string`

      The ID of the data source.

    - `sync_interval?: number | null`

      The interval at which the data source should be synced. Valid values are: 21600, 43200, 86400

### Returns

- `DataSourceUpdateDataSourcesResponse = Array<PipelineDataSource>`

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineDataSources = await client.pipelines.dataSources.updateDataSources(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { body: [{ data_source_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' }] },
);

console.log(pipelineDataSources);
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "last_synced_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "source_type": "S3",
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "sync_interval": 0,
    "sync_schedule_set_by": "sync_schedule_set_by",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "version_metadata": {
      "reader_version": "1.0"
    }
  }
]
```

## Update Pipeline Data Source

`client.pipelines.dataSources.update(stringdataSourceID, DataSourceUpdateParamsparams, RequestOptionsoptions?): PipelineDataSource`

**put** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}`

Update the configuration of a data source in a pipeline.

### Parameters

- `dataSourceID: string`

- `params: DataSourceUpdateParams`

  - `pipeline_id: string`

    Path param

  - `sync_interval?: number | null`

    Body param: The interval at which the data source should be synced.

### Returns

- `PipelineDataSource`

  Schema for a data source in a pipeline.

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineDataSource = await client.pipelines.dataSources.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(pipelineDataSource.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "component": {
    "foo": "bar"
  },
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "last_synced_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "source_type": "S3",
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "status": "NOT_STARTED",
  "status_updated_at": "2019-12-27T18:11:19.117Z",
  "sync_interval": 0,
  "sync_schedule_set_by": "sync_schedule_set_by",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "version_metadata": {
    "reader_version": "1.0"
  }
}
```

## Get Pipeline Data Source Status

`client.pipelines.dataSources.getStatus(stringdataSourceID, DataSourceGetStatusParamsparams, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status`

Get the status of a data source for a pipeline.

### Parameters

- `dataSourceID: string`

- `params: DataSourceGetStatusParams`

  - `pipeline_id: string`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.dataSources.getStatus(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(managedIngestionStatusResponse.job_id);
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Sync Pipeline Data Source

`client.pipelines.dataSources.sync(stringdataSourceID, DataSourceSyncParamsparams, RequestOptionsoptions?): Pipeline`

**post** `/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync`

Run ingestion for the pipeline data source by incrementally updating the data-sink with upstream changes from data-source.

### Parameters

- `dataSourceID: string`

- `params: DataSourceSyncParams`

  - `pipeline_id: string`

    Path param

  - `pipeline_file_ids?: Array<string> | null`

    Body param

### Returns

- `Pipeline`

  Schema for a pipeline.

  - `id: string`

    Unique identifier

  - `embedding_config: ManagedOpenAIEmbeddingConfig | AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | 5 more`

    - `ManagedOpenAIEmbeddingConfig`

      - `component?: Component`

        Configuration for the Managed OpenAI embedding model.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: "openai-text-embedding-3-small"`

          The name of the OpenAI embedding model.

          - `"openai-text-embedding-3-small"`

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "MANAGED_OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"MANAGED_OPENAI_EMBEDDING"`

    - `AzureOpenAIEmbeddingConfig`

      - `component?: AzureOpenAIEmbedding`

        Configuration for the Azure OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string`

          The base URL for Azure deployment.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string`

          The version for Azure OpenAI API.

        - `azure_deployment?: string | null`

          The Azure deployment to use.

        - `azure_endpoint?: string | null`

          The Azure endpoint to use.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "AZURE_EMBEDDING"`

        Type of the embedding model.

        - `"AZURE_EMBEDDING"`

    - `CohereEmbeddingConfig`

      - `component?: CohereEmbedding`

        Configuration for the Cohere embedding model.

        - `api_key: string | null`

          The Cohere API key.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embedding_type?: string`

          Embedding type. If not provided float embedding_type is used when needed.

        - `input_type?: string | null`

          Model Input type. If not provided, search_document and search_query are used when needed.

        - `model_name?: string`

          The modelId of the Cohere model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `truncate?: string`

          Truncation type - START/ END/ NONE

      - `type?: "COHERE_EMBEDDING"`

        Type of the embedding model.

        - `"COHERE_EMBEDDING"`

    - `GeminiEmbeddingConfig`

      - `component?: GeminiEmbedding`

        Configuration for the Gemini embedding model.

        - `api_base?: string | null`

          API base to access the model. Defaults to None.

        - `api_key?: string | null`

          API key to access the model. Defaults to None.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `model_name?: string`

          The modelId of the Gemini model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `output_dimensionality?: number | null`

          Optional reduced dimension for output embeddings. Supported by models/text-embedding-004 and newer (e.g. gemini-embedding-001). Not supported by models/embedding-001.

        - `task_type?: string | null`

          The task for embedding model.

        - `title?: string | null`

          Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.

        - `transport?: string | null`

          Transport to access the model. Defaults to None.

      - `type?: "GEMINI_EMBEDDING"`

        Type of the embedding model.

        - `"GEMINI_EMBEDDING"`

    - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `component?: HuggingFaceInferenceAPIEmbedding`

        Configuration for the HuggingFace Inference API embedding model.

        - `token?: string | boolean | null`

          Hugging Face token. Will default to the locally saved token. Pass token=False if you don’t want to send your token to the server.

          - `string`

          - `boolean`

        - `class_name?: string`

        - `cookies?: Record<string, string> | null`

          Additional cookies to send to the server.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `headers?: Record<string, string> | null`

          Additional headers to send to the server. By default only the authorization and user-agent headers are sent. Values in this dictionary will override the default values.

        - `model_name?: string | null`

          Hugging Face model name. If None, the task will be used.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `pooling?: "cls" | "mean" | "last" | null`

          Enum of possible pooling choices with pooling behaviors.

          - `"cls"`

          - `"mean"`

          - `"last"`

        - `query_instruction?: string | null`

          Instruction to prepend during query embedding.

        - `task?: string | null`

          Optional task to pick Hugging Face's recommended model, used when model_name is left as default of None.

        - `text_instruction?: string | null`

          Instruction to prepend during text embedding.

        - `timeout?: number | null`

          The maximum number of seconds to wait for a response from the server. Loading a new model in Inference API can take up to several minutes. Defaults to None, meaning it will loop until the server is available.

      - `type?: "HUGGINGFACE_API_EMBEDDING"`

        Type of the embedding model.

        - `"HUGGINGFACE_API_EMBEDDING"`

    - `OpenAIEmbeddingConfig`

      - `component?: OpenAIEmbedding`

        Configuration for the OpenAI embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the OpenAI API.

        - `api_base?: string | null`

          The base URL for OpenAI API.

        - `api_key?: string | null`

          The OpenAI API key.

        - `api_version?: string | null`

          The version for OpenAI API.

        - `class_name?: string`

        - `default_headers?: Record<string, string> | null`

          The default headers for API requests.

        - `dimensions?: number | null`

          The number of dimensions on the output embedding vectors. Works only with v3 embedding models.

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          Maximum number of retries.

        - `model_name?: string`

          The name of the OpenAI embedding model.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `reuse_client?: boolean`

          Reuse the OpenAI client between requests. When doing anything with large volumes of async API calls, setting this to false can improve stability.

        - `timeout?: number`

          Timeout for each request.

      - `type?: "OPENAI_EMBEDDING"`

        Type of the embedding model.

        - `"OPENAI_EMBEDDING"`

    - `VertexAIEmbeddingConfig`

      - `component?: VertexTextEmbedding`

        Configuration for the VertexAI embedding model.

        - `client_email: string | null`

          The client email for the VertexAI credentials.

        - `location: string`

          The default location to use when making API calls.

        - `private_key: string | null`

          The private key for the VertexAI credentials.

        - `private_key_id: string | null`

          The private key ID for the VertexAI credentials.

        - `project: string`

          The default GCP project to use when making Vertex API calls.

        - `token_uri: string | null`

          The token URI for the VertexAI credentials.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the Vertex.

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `embed_mode?: "default" | "classification" | "clustering" | 2 more`

          The embedding mode to use.

          - `"default"`

          - `"classification"`

          - `"clustering"`

          - `"similarity"`

          - `"retrieval"`

        - `model_name?: string`

          The modelId of the VertexAI model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

      - `type?: "VERTEXAI_EMBEDDING"`

        Type of the embedding model.

        - `"VERTEXAI_EMBEDDING"`

    - `BedrockEmbeddingConfig`

      - `component?: BedrockEmbedding`

        Configuration for the Bedrock embedding model.

        - `additional_kwargs?: Record<string, unknown>`

          Additional kwargs for the bedrock client.

        - `aws_access_key_id?: string | null`

          AWS Access Key ID to use

        - `aws_secret_access_key?: string | null`

          AWS Secret Access Key to use

        - `aws_session_token?: string | null`

          AWS Session Token to use

        - `class_name?: string`

        - `embed_batch_size?: number`

          The batch size for embedding calls.

        - `max_retries?: number`

          The maximum number of API retries.

        - `model_name?: string`

          The modelId of the Bedrock model to use.

        - `num_workers?: number | null`

          The number of workers to use for async embedding calls.

        - `profile_name?: string | null`

          The name of aws profile to use. If not given, then the default profile is used.

        - `region_name?: string | null`

          AWS region name to use. Uses region configured in AWS CLI if not passed

        - `timeout?: number`

          The timeout for the Bedrock API request in seconds. It will be used for both connect and read timeouts.

      - `type?: "BEDROCK_EMBEDDING"`

        Type of the embedding model.

        - `"BEDROCK_EMBEDDING"`

  - `name: string`

  - `project_id: string`

  - `config_hash?: ConfigHash | null`

    Hashes for the configuration of a pipeline.

    - `embedding_config_hash?: string | null`

      Hash of the embedding config.

    - `parsing_config_hash?: string | null`

      Hash of the llama parse parameters.

    - `transform_config_hash?: string | null`

      Hash of the transform config.

  - `created_at?: string | null`

    Creation datetime

  - `data_sink?: DataSink | null`

    Schema for a data sink.

    - `id: string`

      Unique identifier

    - `component: Record<string, unknown> | CloudPineconeVectorStore | CloudPostgresVectorStore | 5 more`

      Component that implements the data sink

      - `Record<string, unknown>`

      - `CloudPineconeVectorStore`

        Cloud Pinecone Vector Store.

        This class is used to store the configuration for a Pinecone vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        api_key (str): API key for authenticating with Pinecone
        index_name (str): name of the Pinecone index
        namespace (optional[str]): namespace to use in the Pinecone index
        insert_kwargs (optional[dict]): additional kwargs to pass during insertion

        - `api_key: string`

          The API key for authenticating with Pinecone

        - `index_name: string`

        - `class_name?: string`

        - `insert_kwargs?: Record<string, unknown> | null`

        - `namespace?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudPostgresVectorStore`

        - `database: string`

        - `embed_dim: number`

        - `host: string`

        - `password: string`

        - `port: number`

        - `schema_name: string`

        - `table_name: string`

        - `user: string`

        - `class_name?: string`

        - `hnsw_settings?: PgVectorHnswSettings | null`

          HNSW settings for PGVector.

          - `distance_method?: "l2" | "ip" | "cosine" | 3 more`

            The distance method to use.

            - `"l2"`

            - `"ip"`

            - `"cosine"`

            - `"l1"`

            - `"hamming"`

            - `"jaccard"`

          - `ef_construction?: number`

            The number of edges to use during the construction phase.

          - `ef_search?: number`

            The number of edges to use during the search phase.

          - `m?: number`

            The number of bi-directional links created for each new element.

          - `vector_type?: "vector" | "half_vec" | "bit" | "sparse_vec"`

            The type of vector to use.

            - `"vector"`

            - `"half_vec"`

            - `"bit"`

            - `"sparse_vec"`

        - `hybrid_search?: boolean | null`

        - `perform_setup?: boolean`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudQdrantVectorStore`

        Cloud Qdrant Vector Store.

        This class is used to store the configuration for a Qdrant vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        collection_name (str): name of the Qdrant collection
        url (str): url of the Qdrant instance
        api_key (str): API key for authenticating with Qdrant
        max_retries (int): maximum number of retries in case of a failure. Defaults to 3
        client_kwargs (dict): additional kwargs to pass to the Qdrant client

        - `api_key: string`

        - `collection_name: string`

        - `url: string`

        - `class_name?: string`

        - `client_kwargs?: Record<string, unknown>`

        - `max_retries?: number`

        - `supports_nested_metadata_filters?: true`

          - `true`

      - `CloudAzureAISearchVectorStore`

        Cloud Azure AI Search Vector Store.

        - `search_service_api_key: string`

        - `search_service_endpoint: string`

        - `class_name?: string`

        - `client_id?: string | null`

        - `client_secret?: string | null`

        - `embedding_dimension?: number | null`

        - `filterable_metadata_field_keys?: Record<string, unknown> | null`

        - `index_name?: string | null`

        - `search_service_api_version?: string | null`

        - `supports_nested_metadata_filters?: true`

          - `true`

        - `tenant_id?: string | null`

      - `CloudMongoDBAtlasVectorSearch`

        Cloud MongoDB Atlas Vector Store.

        This class is used to store the configuration for a MongoDB Atlas vector store,
        so that it can be created and used in LlamaCloud.

        Args:
        mongodb_uri (str): URI for connecting to MongoDB Atlas
        db_name (str): name of the MongoDB database
        collection_name (str): name of the MongoDB collection
        vector_index_name (str): name of the MongoDB Atlas vector index
        fulltext_index_name (str): name of the MongoDB Atlas full-text index

        - `collection_name: string`

        - `db_name: string`

        - `mongodb_uri: string`

        - `class_name?: string`

        - `embedding_dimension?: number | null`

        - `fulltext_index_name?: string | null`

        - `supports_nested_metadata_filters?: boolean`

        - `vector_index_name?: string | null`

      - `CloudMilvusVectorStore`

        Cloud Milvus Vector Store.

        - `uri: string`

        - `token?: string | null`

        - `class_name?: string`

        - `collection_name?: string | null`

        - `embedding_dimension?: number | null`

        - `supports_nested_metadata_filters?: boolean`

      - `CloudAstraDBVectorStore`

        Cloud AstraDB Vector Store.

        This class is used to store the configuration for an AstraDB vector store, so that it can be
        created and used in LlamaCloud.

        Args:
        token (str): The Astra DB Application Token to use.
        api_endpoint (str): The Astra DB JSON API endpoint for your database.
        collection_name (str): Collection name to use. If not existing, it will be created.
        embedding_dimension (int): Length of the embedding vectors in use.
        keyspace (optional[str]): The keyspace to use. If not provided, 'default_keyspace'

        - `token: string`

          The Astra DB Application Token to use

        - `api_endpoint: string`

          The Astra DB JSON API endpoint for your database

        - `collection_name: string`

          Collection name to use. If not existing, it will be created

        - `embedding_dimension: number`

          Length of the embedding vectors in use

        - `class_name?: string`

        - `keyspace?: string | null`

          The keyspace to use. If not provided, 'default_keyspace'

        - `supports_nested_metadata_filters?: true`

          - `true`

    - `name: string`

      The name of the data sink.

    - `project_id: string`

    - `sink_type: "PINECONE" | "POSTGRES" | "QDRANT" | 4 more`

      - `"PINECONE"`

      - `"POSTGRES"`

      - `"QDRANT"`

      - `"AZUREAI_SEARCH"`

      - `"MONGODB_ATLAS"`

      - `"MILVUS"`

      - `"ASTRA_DB"`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config?: EmbeddingModelConfig | null`

    Schema for an embedding model config.

    - `id: string`

      Unique identifier

    - `embedding_config: AzureOpenAIEmbeddingConfig | CohereEmbeddingConfig | GeminiEmbeddingConfig | 4 more`

      The embedding configuration for the embedding model config.

      - `AzureOpenAIEmbeddingConfig`

      - `CohereEmbeddingConfig`

      - `GeminiEmbeddingConfig`

      - `HuggingFaceInferenceAPIEmbeddingConfig`

      - `OpenAIEmbeddingConfig`

      - `VertexAIEmbeddingConfig`

      - `BedrockEmbeddingConfig`

    - `name: string`

      The name of the embedding model config.

    - `project_id: string`

    - `created_at?: string | null`

      Creation datetime

    - `updated_at?: string | null`

      Update datetime

  - `embedding_model_config_id?: string | null`

    The ID of the EmbeddingModelConfig this pipeline is using.

  - `llama_parse_parameters?: LlamaParseParameters | null`

    Settings that can be configured for how to use LlamaParse to parse files within a LlamaCloud pipeline.

    - `adaptive_long_table?: boolean | null`

    - `aggressive_table_extraction?: boolean | null`

    - `annotate_links?: boolean | null`

    - `auto_mode?: boolean | null`

    - `auto_mode_configuration_json?: string | null`

    - `auto_mode_trigger_on_image_in_page?: boolean | null`

    - `auto_mode_trigger_on_regexp_in_page?: string | null`

    - `auto_mode_trigger_on_table_in_page?: boolean | null`

    - `auto_mode_trigger_on_text_in_page?: string | null`

    - `azure_openai_api_version?: string | null`

    - `azure_openai_deployment_name?: string | null`

    - `azure_openai_endpoint?: string | null`

    - `azure_openai_key?: string | null`

    - `bbox_bottom?: number | null`

    - `bbox_left?: number | null`

    - `bbox_right?: number | null`

    - `bbox_top?: number | null`

    - `bounding_box?: string | null`

    - `compact_markdown_table?: boolean | null`

    - `complemental_formatting_instruction?: string | null`

    - `content_guideline_instruction?: string | null`

    - `continuous_mode?: boolean | null`

    - `disable_image_extraction?: boolean | null`

    - `disable_ocr?: boolean | null`

    - `disable_reconstruction?: boolean | null`

    - `do_not_cache?: boolean | null`

    - `do_not_unroll_columns?: boolean | null`

    - `enable_cost_optimizer?: boolean | null`

    - `extract_charts?: boolean | null`

    - `extract_layout?: boolean | null`

    - `extract_printed_page_number?: boolean | null`

    - `fast_mode?: boolean | null`

    - `formatting_instruction?: string | null`

    - `gpt4o_api_key?: string | null`

    - `gpt4o_mode?: boolean | null`

    - `guess_xlsx_sheet_name?: boolean | null`

    - `hide_footers?: boolean | null`

    - `hide_headers?: boolean | null`

    - `high_res_ocr?: boolean | null`

    - `html_make_all_elements_visible?: boolean | null`

    - `html_remove_fixed_elements?: boolean | null`

    - `html_remove_navigation_elements?: boolean | null`

    - `http_proxy?: string | null`

    - `ignore_document_elements_for_layout_detection?: boolean | null`

    - `images_to_save?: Array<"screenshot" | "embedded" | "layout"> | null`

      - `"screenshot"`

      - `"embedded"`

      - `"layout"`

    - `inline_images_in_markdown?: boolean | null`

    - `input_s3_path?: string | null`

    - `input_s3_region?: string | null`

    - `input_url?: string | null`

    - `internal_is_screenshot_job?: boolean | null`

    - `invalidate_cache?: boolean | null`

    - `is_formatting_instruction?: boolean | null`

    - `job_timeout_extra_time_per_page_in_seconds?: number | null`

    - `job_timeout_in_seconds?: number | null`

    - `keep_page_separator_when_merging_tables?: boolean | null`

    - `languages?: Array<ParsingLanguages>`

      - `"af"`

      - `"az"`

      - `"bs"`

      - `"cs"`

      - `"cy"`

      - `"da"`

      - `"de"`

      - `"en"`

      - `"es"`

      - `"et"`

      - `"fr"`

      - `"ga"`

      - `"hr"`

      - `"hu"`

      - `"id"`

      - `"is"`

      - `"it"`

      - `"ku"`

      - `"la"`

      - `"lt"`

      - `"lv"`

      - `"mi"`

      - `"ms"`

      - `"mt"`

      - `"nl"`

      - `"no"`

      - `"oc"`

      - `"pi"`

      - `"pl"`

      - `"pt"`

      - `"ro"`

      - `"rs_latin"`

      - `"sk"`

      - `"sl"`

      - `"sq"`

      - `"sv"`

      - `"sw"`

      - `"tl"`

      - `"tr"`

      - `"uz"`

      - `"vi"`

      - `"ar"`

      - `"fa"`

      - `"ug"`

      - `"ur"`

      - `"bn"`

      - `"as"`

      - `"mni"`

      - `"ru"`

      - `"rs_cyrillic"`

      - `"be"`

      - `"bg"`

      - `"uk"`

      - `"mn"`

      - `"abq"`

      - `"ady"`

      - `"kbd"`

      - `"ava"`

      - `"dar"`

      - `"inh"`

      - `"che"`

      - `"lbe"`

      - `"lez"`

      - `"tab"`

      - `"tjk"`

      - `"hi"`

      - `"mr"`

      - `"ne"`

      - `"bh"`

      - `"mai"`

      - `"ang"`

      - `"bho"`

      - `"mah"`

      - `"sck"`

      - `"new"`

      - `"gom"`

      - `"sa"`

      - `"bgc"`

      - `"th"`

      - `"ch_sim"`

      - `"ch_tra"`

      - `"ja"`

      - `"ko"`

      - `"ta"`

      - `"te"`

      - `"kn"`

    - `layout_aware?: boolean | null`

    - `line_level_bounding_box?: boolean | null`

    - `markdown_table_multiline_header_separator?: string | null`

    - `max_pages?: number | null`

    - `max_pages_enforced?: number | null`

    - `merge_tables_across_pages_in_markdown?: boolean | null`

    - `model?: string | null`

    - `outlined_table_extraction?: boolean | null`

    - `output_pdf_of_document?: boolean | null`

    - `output_s3_path_prefix?: string | null`

    - `output_s3_region?: string | null`

    - `output_tables_as_HTML?: boolean | null`

    - `page_error_tolerance?: number | null`

    - `page_footer_prefix?: string | null`

    - `page_footer_suffix?: string | null`

    - `page_header_prefix?: string | null`

    - `page_header_suffix?: string | null`

    - `page_prefix?: string | null`

    - `page_separator?: string | null`

    - `page_suffix?: string | null`

    - `parse_mode?: ParsingMode | null`

      Enum for representing the mode of parsing to be used.

      - `"parse_page_without_llm"`

      - `"parse_page_with_llm"`

      - `"parse_page_with_lvm"`

      - `"parse_page_with_agent"`

      - `"parse_page_with_layout_agent"`

      - `"parse_document_with_llm"`

      - `"parse_document_with_lvm"`

      - `"parse_document_with_agent"`

    - `parsing_instruction?: string | null`

    - `precise_bounding_box?: boolean | null`

    - `premium_mode?: boolean | null`

    - `presentation_out_of_bounds_content?: boolean | null`

    - `presentation_skip_embedded_data?: boolean | null`

    - `preserve_layout_alignment_across_pages?: boolean | null`

    - `preserve_very_small_text?: boolean | null`

    - `preset?: string | null`

    - `priority?: "low" | "medium" | "high" | "critical" | null`

      The priority for the request. This field may be ignored or overwritten depending on the organization tier.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"critical"`

    - `project_id?: string | null`

    - `remove_hidden_text?: boolean | null`

    - `replace_failed_page_mode?: FailPageMode | null`

      Enum for representing the different available page error handling modes.

      - `"raw_text"`

      - `"blank_page"`

      - `"error_message"`

    - `replace_failed_page_with_error_message_prefix?: string | null`

    - `replace_failed_page_with_error_message_suffix?: string | null`

    - `save_images?: boolean | null`

    - `skip_diagonal_text?: boolean | null`

    - `specialized_chart_parsing_agentic?: boolean | null`

    - `specialized_chart_parsing_efficient?: boolean | null`

    - `specialized_chart_parsing_plus?: boolean | null`

    - `specialized_image_parsing?: boolean | null`

    - `spreadsheet_extract_sub_tables?: boolean | null`

    - `spreadsheet_force_formula_computation?: boolean | null`

    - `spreadsheet_include_hidden_sheets?: boolean | null`

    - `strict_mode_buggy_font?: boolean | null`

    - `strict_mode_image_extraction?: boolean | null`

    - `strict_mode_image_ocr?: boolean | null`

    - `strict_mode_reconstruction?: boolean | null`

    - `structured_output?: boolean | null`

    - `structured_output_json_schema?: string | null`

    - `structured_output_json_schema_name?: string | null`

    - `system_prompt?: string | null`

    - `system_prompt_append?: string | null`

    - `take_screenshot?: boolean | null`

    - `target_pages?: string | null`

    - `tier?: string | null`

    - `use_vendor_multimodal_model?: boolean | null`

    - `user_prompt?: string | null`

    - `vendor_multimodal_api_key?: string | null`

    - `vendor_multimodal_model_name?: string | null`

    - `version?: string | null`

    - `webhook_configurations?: Array<WebhookConfiguration> | null`

      Outbound webhook endpoints to notify on job status changes

      - `webhook_events?: Array<"extract.pending" | "extract.success" | "extract.error" | 14 more> | null`

        Events to subscribe to (e.g. 'parse.success', 'extract.error'). If null, all events are delivered.

        - `"extract.pending"`

        - `"extract.success"`

        - `"extract.error"`

        - `"extract.partial_success"`

        - `"extract.cancelled"`

        - `"parse.pending"`

        - `"parse.running"`

        - `"parse.success"`

        - `"parse.error"`

        - `"parse.partial_success"`

        - `"parse.cancelled"`

        - `"classify.pending"`

        - `"classify.success"`

        - `"classify.error"`

        - `"classify.partial_success"`

        - `"classify.cancelled"`

        - `"unmapped_event"`

      - `webhook_headers?: Record<string, string> | null`

        Custom HTTP headers sent with each webhook request (e.g. auth tokens)

      - `webhook_output_format?: string | null`

        Response format sent to the webhook: 'string' (default) or 'json'

      - `webhook_url?: string | null`

        URL to receive webhook POST notifications

    - `webhook_url?: string | null`

  - `managed_pipeline_id?: string | null`

    The ID of the ManagedPipeline this playground pipeline is linked to.

  - `metadata_config?: PipelineMetadataConfig | null`

    Metadata configuration for the pipeline.

    - `excluded_embed_metadata_keys?: Array<string>`

      List of metadata keys to exclude from embeddings

    - `excluded_llm_metadata_keys?: Array<string>`

      List of metadata keys to exclude from LLM during retrieval

  - `pipeline_type?: PipelineType`

    Type of pipeline. Either PLAYGROUND or MANAGED.

    - `"PLAYGROUND"`

    - `"MANAGED"`

  - `preset_retrieval_parameters?: PresetRetrievalParams`

    Preset retrieval parameters for the pipeline.

    - `alpha?: number | null`

      Alpha value for hybrid retrieval to determine the weights between dense and sparse retrieval. 0 is sparse retrieval and 1 is dense retrieval.

    - `class_name?: string`

    - `dense_similarity_cutoff?: number | null`

      Minimum similarity score wrt query for retrieval

    - `dense_similarity_top_k?: number | null`

      Number of nodes for dense retrieval.

    - `enable_reranking?: boolean | null`

      Enable reranking for retrieval

    - `files_top_k?: number | null`

      Number of files to retrieve (only for retrieval mode files_via_metadata and files_via_content).

    - `rerank_top_n?: number | null`

      Number of reranked nodes for returning.

    - `retrieval_mode?: RetrievalMode`

      The retrieval mode for the query.

      - `"chunks"`

      - `"files_via_metadata"`

      - `"files_via_content"`

      - `"auto_routed"`

    - `retrieve_image_nodes?: boolean`

      Whether to retrieve image nodes.

    - `retrieve_page_figure_nodes?: boolean`

      Whether to retrieve page figure nodes.

    - `retrieve_page_screenshot_nodes?: boolean`

      Whether to retrieve page screenshot nodes.

    - `search_filters?: MetadataFilters | null`

      Metadata filters for vector stores.

      - `filters: Array<MetadataFilter | MetadataFilters>`

        - `MetadataFilter`

          Comprehensive metadata filter for vector stores to support more operators.

          Value uses Strict types, as int, float and str are compatible types and were all
          converted to string before.

          See: https://docs.pydantic.dev/latest/usage/types/#strict-types

          - `key: string`

          - `value: number | string | Array<string> | 2 more | null`

            - `number`

            - `string`

            - `Array<string>`

            - `Array<number>`

            - `Array<number>`

          - `operator?: "==" | ">" | "<" | 11 more`

            Vector store filter operator.

            - `"=="`

            - `">"`

            - `"<"`

            - `"!="`

            - `">="`

            - `"<="`

            - `"in"`

            - `"nin"`

            - `"any"`

            - `"all"`

            - `"text_match"`

            - `"text_match_insensitive"`

            - `"contains"`

            - `"is_empty"`

        - `MetadataFilters`

          Metadata filters for vector stores.

      - `condition?: "and" | "or" | "not" | null`

        Vector store filter conditions to combine different filters.

        - `"and"`

        - `"or"`

        - `"not"`

    - `search_filters_inference_schema?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      JSON Schema that will be used to infer search_filters. Omit or leave as null to skip inference.

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

    - `sparse_similarity_top_k?: number | null`

      Number of nodes for sparse retrieval.

  - `sparse_model_config?: SparseModelConfig | null`

    Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.

    - `class_name?: string`

    - `model_type?: "splade" | "bm25" | "auto"`

      The sparse model type to use. 'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade' uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC uses term frequency, Cloud uses Splade).

      - `"splade"`

      - `"bm25"`

      - `"auto"`

  - `status?: "CREATED" | "DELETING" | null`

    Status of the pipeline.

    - `"CREATED"`

    - `"DELETING"`

  - `transform_config?: AutoTransformConfig | AdvancedModeTransformConfig`

    Configuration for the transformation.

    - `AutoTransformConfig`

      - `chunk_overlap?: number`

        Chunk overlap for the transformation.

      - `chunk_size?: number`

        Chunk size for the transformation.

      - `mode?: "auto"`

        - `"auto"`

    - `AdvancedModeTransformConfig`

      - `chunking_config?: NoneChunkingConfig | CharacterChunkingConfig | TokenChunkingConfig | 2 more`

        Configuration for the chunking.

        - `NoneChunkingConfig`

          - `mode?: "none"`

            - `"none"`

        - `CharacterChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "character"`

            - `"character"`

        - `TokenChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "token"`

            - `"token"`

          - `separator?: string`

        - `SentenceChunkingConfig`

          - `chunk_overlap?: number`

          - `chunk_size?: number`

          - `mode?: "sentence"`

            - `"sentence"`

          - `paragraph_separator?: string`

          - `separator?: string`

        - `SemanticChunkingConfig`

          - `breakpoint_percentile_threshold?: number`

          - `buffer_size?: number`

          - `mode?: "semantic"`

            - `"semantic"`

      - `mode?: "advanced"`

        - `"advanced"`

      - `segmentation_config?: NoneSegmentationConfig | PageSegmentationConfig | ElementSegmentationConfig`

        Configuration for the segmentation.

        - `NoneSegmentationConfig`

          - `mode?: "none"`

            - `"none"`

        - `PageSegmentationConfig`

          - `mode?: "page"`

            - `"page"`

          - `page_separator?: string`

        - `ElementSegmentationConfig`

          - `mode?: "element"`

            - `"element"`

  - `updated_at?: string | null`

    Update datetime

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipeline = await client.pipelines.dataSources.sync('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(pipeline.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "embedding_config": {
    "component": {
      "class_name": "class_name",
      "embed_batch_size": 1,
      "model_name": "openai-text-embedding-3-small",
      "num_workers": 0
    },
    "type": "MANAGED_OPENAI_EMBEDDING"
  },
  "name": "name",
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "embedding_config_hash": "embedding_config_hash",
    "parsing_config_hash": "parsing_config_hash",
    "transform_config_hash": "transform_config_hash"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "data_sink": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "component": {
      "foo": "bar"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "sink_type": "PINECONE",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config": {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "embedding_config": {
      "component": {
        "additional_kwargs": {
          "foo": "bar"
        },
        "api_base": "api_base",
        "api_key": "api_key",
        "api_version": "api_version",
        "azure_deployment": "azure_deployment",
        "azure_endpoint": "azure_endpoint",
        "class_name": "class_name",
        "default_headers": {
          "foo": "string"
        },
        "dimensions": 0,
        "embed_batch_size": 1,
        "max_retries": 0,
        "model_name": "model_name",
        "num_workers": 0,
        "reuse_client": true,
        "timeout": 0
      },
      "type": "AZURE_EMBEDDING"
    },
    "name": "name",
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "embedding_model_config_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "llama_parse_parameters": {
    "adaptive_long_table": true,
    "aggressive_table_extraction": true,
    "annotate_links": true,
    "auto_mode": true,
    "auto_mode_configuration_json": "auto_mode_configuration_json",
    "auto_mode_trigger_on_image_in_page": true,
    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
    "auto_mode_trigger_on_table_in_page": true,
    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
    "azure_openai_api_version": "azure_openai_api_version",
    "azure_openai_deployment_name": "azure_openai_deployment_name",
    "azure_openai_endpoint": "azure_openai_endpoint",
    "azure_openai_key": "azure_openai_key",
    "bbox_bottom": 0,
    "bbox_left": 0,
    "bbox_right": 0,
    "bbox_top": 0,
    "bounding_box": "bounding_box",
    "compact_markdown_table": true,
    "complemental_formatting_instruction": "complemental_formatting_instruction",
    "content_guideline_instruction": "content_guideline_instruction",
    "continuous_mode": true,
    "disable_image_extraction": true,
    "disable_ocr": true,
    "disable_reconstruction": true,
    "do_not_cache": true,
    "do_not_unroll_columns": true,
    "enable_cost_optimizer": true,
    "extract_charts": true,
    "extract_layout": true,
    "extract_printed_page_number": true,
    "fast_mode": true,
    "formatting_instruction": "formatting_instruction",
    "gpt4o_api_key": "gpt4o_api_key",
    "gpt4o_mode": true,
    "guess_xlsx_sheet_name": true,
    "hide_footers": true,
    "hide_headers": true,
    "high_res_ocr": true,
    "html_make_all_elements_visible": true,
    "html_remove_fixed_elements": true,
    "html_remove_navigation_elements": true,
    "http_proxy": "http_proxy",
    "ignore_document_elements_for_layout_detection": true,
    "images_to_save": [
      "screenshot"
    ],
    "inline_images_in_markdown": true,
    "input_s3_path": "input_s3_path",
    "input_s3_region": "input_s3_region",
    "input_url": "input_url",
    "internal_is_screenshot_job": true,
    "invalidate_cache": true,
    "is_formatting_instruction": true,
    "job_timeout_extra_time_per_page_in_seconds": 0,
    "job_timeout_in_seconds": 0,
    "keep_page_separator_when_merging_tables": true,
    "languages": [
      "af"
    ],
    "layout_aware": true,
    "line_level_bounding_box": true,
    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
    "max_pages": 0,
    "max_pages_enforced": 0,
    "merge_tables_across_pages_in_markdown": true,
    "model": "model",
    "outlined_table_extraction": true,
    "output_pdf_of_document": true,
    "output_s3_path_prefix": "output_s3_path_prefix",
    "output_s3_region": "output_s3_region",
    "output_tables_as_HTML": true,
    "page_error_tolerance": 0,
    "page_footer_prefix": "page_footer_prefix",
    "page_footer_suffix": "page_footer_suffix",
    "page_header_prefix": "page_header_prefix",
    "page_header_suffix": "page_header_suffix",
    "page_prefix": "page_prefix",
    "page_separator": "page_separator",
    "page_suffix": "page_suffix",
    "parse_mode": "parse_page_without_llm",
    "parsing_instruction": "parsing_instruction",
    "precise_bounding_box": true,
    "premium_mode": true,
    "presentation_out_of_bounds_content": true,
    "presentation_skip_embedded_data": true,
    "preserve_layout_alignment_across_pages": true,
    "preserve_very_small_text": true,
    "preset": "preset",
    "priority": "low",
    "project_id": "project_id",
    "remove_hidden_text": true,
    "replace_failed_page_mode": "raw_text",
    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
    "save_images": true,
    "skip_diagonal_text": true,
    "specialized_chart_parsing_agentic": true,
    "specialized_chart_parsing_efficient": true,
    "specialized_chart_parsing_plus": true,
    "specialized_image_parsing": true,
    "spreadsheet_extract_sub_tables": true,
    "spreadsheet_force_formula_computation": true,
    "spreadsheet_include_hidden_sheets": true,
    "strict_mode_buggy_font": true,
    "strict_mode_image_extraction": true,
    "strict_mode_image_ocr": true,
    "strict_mode_reconstruction": true,
    "structured_output": true,
    "structured_output_json_schema": "structured_output_json_schema",
    "structured_output_json_schema_name": "structured_output_json_schema_name",
    "system_prompt": "system_prompt",
    "system_prompt_append": "system_prompt_append",
    "take_screenshot": true,
    "target_pages": "target_pages",
    "tier": "tier",
    "use_vendor_multimodal_model": true,
    "user_prompt": "user_prompt",
    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
    "version": "version",
    "webhook_configurations": [
      {
        "webhook_events": [
          "parse.success",
          "parse.error"
        ],
        "webhook_headers": {
          "Authorization": "Bearer sk-..."
        },
        "webhook_output_format": "json",
        "webhook_url": "https://example.com/webhooks/llamacloud"
      }
    ],
    "webhook_url": "webhook_url"
  },
  "managed_pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "metadata_config": {
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ]
  },
  "pipeline_type": "PLAYGROUND",
  "preset_retrieval_parameters": {
    "alpha": 0,
    "class_name": "class_name",
    "dense_similarity_cutoff": 0,
    "dense_similarity_top_k": 1,
    "enable_reranking": true,
    "files_top_k": 1,
    "rerank_top_n": 1,
    "retrieval_mode": "chunks",
    "retrieve_image_nodes": true,
    "retrieve_page_figure_nodes": true,
    "retrieve_page_screenshot_nodes": true,
    "search_filters": {
      "filters": [
        {
          "key": "key",
          "value": 0,
          "operator": "=="
        }
      ],
      "condition": "and"
    },
    "search_filters_inference_schema": {
      "foo": {
        "foo": "bar"
      }
    },
    "sparse_similarity_top_k": 1
  },
  "sparse_model_config": {
    "class_name": "class_name",
    "model_type": "splade"
  },
  "status": "CREATED",
  "transform_config": {
    "chunk_overlap": 0,
    "chunk_size": 1,
    "mode": "auto"
  },
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain Types

### Pipeline Data Source

- `PipelineDataSource`

  Schema for a data source in a pipeline.

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Data Source Get Data Sources Response

- `DataSourceGetDataSourcesResponse = Array<PipelineDataSource>`

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

### Data Source Update Data Sources Response

- `DataSourceUpdateDataSourcesResponse = Array<PipelineDataSource>`

  - `id: string`

    Unique identifier

  - `component: Record<string, unknown> | CloudS3DataSource | CloudAzStorageBlobDataSource | 9 more`

    Component that implements the data source

    - `Record<string, unknown>`

    - `CloudS3DataSource`

      - `bucket: string`

        The name of the S3 bucket to read from.

      - `aws_access_id?: string | null`

        The AWS access ID to use for authentication.

      - `aws_access_secret?: string | null`

        The AWS access secret to use for authentication.

      - `class_name?: string`

      - `prefix?: string | null`

        The prefix of the S3 objects to read from.

      - `regex_pattern?: string | null`

        The regex pattern to filter S3 objects. Must be a valid regex pattern.

      - `s3_endpoint_url?: string | null`

        The S3 endpoint URL to use for authentication.

      - `supports_access_control?: boolean`

    - `CloudAzStorageBlobDataSource`

      - `account_url: string`

        The Azure Storage Blob account URL to use for authentication.

      - `container_name: string`

        The name of the Azure Storage Blob container to read from.

      - `account_key?: string | null`

        The Azure Storage Blob account key to use for authentication.

      - `account_name?: string | null`

        The Azure Storage Blob account name to use for authentication.

      - `blob?: string | null`

        The blob name to read from.

      - `class_name?: string`

      - `client_id?: string | null`

        The Azure AD client ID to use for authentication.

      - `client_secret?: string | null`

        The Azure AD client secret to use for authentication.

      - `prefix?: string | null`

        The prefix of the Azure Storage Blob objects to read from.

      - `supports_access_control?: boolean`

      - `tenant_id?: string | null`

        The Azure AD tenant ID to use for authentication.

    - `CloudGoogleDriveDataSource`

      - `folder_id: string`

        The ID of the Google Drive folder to read from.

      - `class_name?: string`

      - `service_account_key?: Record<string, string> | null`

        A dictionary containing secret values

      - `supports_access_control?: boolean`

    - `CloudOneDriveDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `user_principal_name: string`

        The user principal name to use for authentication.

      - `class_name?: string`

      - `folder_id?: string | null`

        The ID of the OneDrive folder to read from.

      - `folder_path?: string | null`

        The path of the OneDrive folder to read from.

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `supports_access_control?: true`

        - `true`

    - `CloudSharepointDataSource`

      - `client_id: string`

        The client ID to use for authentication.

      - `client_secret: string`

        The client secret to use for authentication.

      - `tenant_id: string`

        The tenant ID to use for authentication.

      - `class_name?: string`

      - `drive_name?: string | null`

        The name of the Sharepoint drive to read from.

      - `exclude_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to exclude. Files whose paths (including filename) match any pattern will be excluded. Example: ['/temp/', '/backup/', '.git/', '.tmp$', '^~']

      - `folder_id?: string | null`

        The ID of the Sharepoint folder to read from.

      - `folder_path?: string | null`

        The path of the Sharepoint folder to read from.

      - `get_permissions?: boolean | null`

        Whether to get permissions for the sharepoint site.

      - `include_path_patterns?: Array<string> | null`

        List of regex patterns for file paths to include. Full paths (including filename) must match at least one pattern to be included. Example: ['/reports/', '/docs/.*.pdf$', '^Report.*.pdf$']

      - `required_exts?: Array<string> | null`

        The list of required file extensions.

      - `site_id?: string | null`

        The ID of the SharePoint site to download from.

      - `site_name?: string | null`

        The name of the SharePoint site to download from.

      - `supports_access_control?: true`

        - `true`

    - `CloudSlackDataSource`

      - `slack_token: string`

        Slack Bot Token.

      - `channel_ids?: string | null`

        Slack Channel.

      - `channel_patterns?: string | null`

        Slack Channel name pattern.

      - `class_name?: string`

      - `earliest_date?: string | null`

        Earliest date.

      - `earliest_date_timestamp?: number | null`

        Earliest date timestamp.

      - `latest_date?: string | null`

        Latest date.

      - `latest_date_timestamp?: number | null`

        Latest date timestamp.

      - `supports_access_control?: boolean`

    - `CloudNotionPageDataSource`

      - `integration_token: string`

        The integration token to use for authentication.

      - `class_name?: string`

      - `database_ids?: string | null`

        The Notion Database Id to read content from.

      - `page_ids?: string | null`

        The Page ID's of the Notion to read from.

      - `supports_access_control?: boolean`

    - `CloudConfluenceDataSource`

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Confluence APIs.

      - `server_url: string`

        The server URL of the Confluence instance.

      - `api_token?: string | null`

        The API token to use for authentication.

      - `class_name?: string`

      - `cql?: string | null`

        The CQL query to use for fetching pages.

      - `failure_handling?: FailureHandlingConfig`

        Configuration for handling failures during processing. Key-value object controlling failure handling behaviors.

        Example:
        {
        "skip_list_failures": true
        }

        Currently supports:

        - skip_list_failures: Skip failed batches/lists and continue processing

        - `skip_list_failures?: boolean`

          Whether to skip failed batches/lists and continue processing

      - `index_restricted_pages?: boolean`

        Whether to index restricted pages.

      - `keep_markdown_format?: boolean`

        Whether to keep the markdown format.

      - `label?: string | null`

        The label to use for fetching pages.

      - `page_ids?: string | null`

        The page IDs of the Confluence to read from.

      - `space_key?: string | null`

        The space key to read from.

      - `supports_access_control?: boolean`

      - `user_name?: string | null`

        The username to use for authentication.

    - `CloudJiraDataSource`

      Cloud Jira Data Source integrating JiraReader.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `api_token?: string | null`

        The API/ Access Token used for Basic, PAT and OAuth2 authentication.

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `server_url?: string | null`

        The server url for Jira Cloud.

      - `supports_access_control?: boolean`

    - `CloudJiraDataSourceV2`

      Cloud Jira Data Source integrating JiraReaderV2.

      - `authentication_mechanism: string`

        Type of Authentication for connecting to Jira APIs.

      - `query: string`

        JQL (Jira Query Language) query to search.

      - `server_url: string`

        The server url for Jira Cloud.

      - `api_token?: string | null`

        The API Access Token used for Basic, PAT and OAuth2 authentication.

      - `api_version?: "2" | "3"`

        Jira REST API version to use (2 or 3). 3 supports Atlassian Document Format (ADF).

        - `"2"`

        - `"3"`

      - `class_name?: string`

      - `cloud_id?: string | null`

        The cloud ID, used in case of OAuth2.

      - `email?: string | null`

        The email address to use for authentication.

      - `expand?: string | null`

        Fields to expand in the response.

      - `fields?: Array<string> | null`

        List of fields to retrieve from Jira. If None, retrieves all fields.

      - `get_permissions?: boolean`

        Whether to fetch project role permissions and issue-level security

      - `requests_per_minute?: number | null`

        Rate limit for Jira API requests per minute.

      - `supports_access_control?: boolean`

    - `CloudBoxDataSource`

      - `authentication_mechanism: "developer_token" | "ccg"`

        The type of authentication to use (Developer Token or CCG)

        - `"developer_token"`

        - `"ccg"`

      - `class_name?: string`

      - `client_id?: string | null`

        Box API key used for identifying the application the user is authenticating with

      - `client_secret?: string | null`

        Box API secret used for making auth requests.

      - `developer_token?: string | null`

        Developer token for authentication if authentication_mechanism is 'developer_token'.

      - `enterprise_id?: string | null`

        Box Enterprise ID, if provided authenticates as service.

      - `folder_id?: string | null`

        The ID of the Box folder to read from.

      - `supports_access_control?: boolean`

      - `user_id?: string | null`

        Box User ID, if provided authenticates as user.

  - `data_source_id: string`

    The ID of the data source.

  - `last_synced_at: string`

    The last time the data source was automatically synced.

  - `name: string`

    The name of the data source.

  - `pipeline_id: string`

    The ID of the pipeline.

  - `project_id: string`

  - `source_type: "S3" | "AZURE_STORAGE_BLOB" | "GOOGLE_DRIVE" | 8 more`

    - `"S3"`

    - `"AZURE_STORAGE_BLOB"`

    - `"GOOGLE_DRIVE"`

    - `"MICROSOFT_ONEDRIVE"`

    - `"MICROSOFT_SHAREPOINT"`

    - `"SLACK"`

    - `"NOTION_PAGE"`

    - `"CONFLUENCE"`

    - `"JIRA"`

    - `"JIRA_V2"`

    - `"BOX"`

  - `created_at?: string | null`

    Creation datetime

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata that will be present on all data loaded from the data source

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    The status of the data source in the pipeline.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `sync_interval?: number | null`

    The interval at which the data source should be synced.

  - `sync_schedule_set_by?: string | null`

    The id of the user who set the sync schedule.

  - `updated_at?: string | null`

    Update datetime

  - `version_metadata?: DataSourceReaderVersionMetadata | null`

    Version metadata for the data source

    - `reader_version?: "1.0" | "2.0" | "2.1" | null`

      The version of the reader to use for this data source.

      - `"1.0"`

      - `"2.0"`

      - `"2.1"`

# Images

## List File Page Screenshots

`client.pipelines.images.listPageScreenshots(stringid, ImageListPageScreenshotsParamsquery?, RequestOptionsoptions?): ImageListPageScreenshotsResponse`

**get** `/api/v1/files/{id}/page_screenshots`

List metadata for all screenshots of pages from a file.

### Parameters

- `id: string`

- `query: ImageListPageScreenshotsParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ImageListPageScreenshotsResponse = Array<ImageListPageScreenshotsResponseItem>`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata?: Record<string, unknown> | null`

    Metadata for the screenshot

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.listPageScreenshots(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response);
```

#### Response

```json
[
  {
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "image_size": 0,
    "page_index": 0,
    "metadata": {
      "foo": "bar"
    }
  }
]
```

## Get File Page Screenshot

`client.pipelines.images.getPageScreenshot(numberpageIndex, ImageGetPageScreenshotParamsparams, RequestOptionsoptions?): ImageGetPageScreenshotResponse`

**get** `/api/v1/files/{id}/page_screenshots/{page_index}`

Get screenshot of a page from a file.

### Parameters

- `pageIndex: number`

- `params: ImageGetPageScreenshotParams`

  - `id: string`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `ImageGetPageScreenshotResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.getPageScreenshot(0, {
  id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response);
```

#### Response

```json
{}
```

## Get File Page Figure

`client.pipelines.images.getPageFigure(stringfigureName, ImageGetPageFigureParamsparams, RequestOptionsoptions?): ImageGetPageFigureResponse`

**get** `/api/v1/files/{id}/page-figures/{page_index}/{figure_name}`

Get a specific figure from a page of a file.

### Parameters

- `figureName: string`

- `params: ImageGetPageFigureParams`

  - `id: string`

    Path param

  - `page_index: number`

    Path param

  - `organization_id?: string | null`

    Query param

  - `project_id?: string | null`

    Query param

### Returns

- `ImageGetPageFigureResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.getPageFigure('figure_name', {
  id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  page_index: 0,
});

console.log(response);
```

#### Response

```json
{}
```

## List File Pages Figures

`client.pipelines.images.listPageFigures(stringid, ImageListPageFiguresParamsquery?, RequestOptionsoptions?): ImageListPageFiguresResponse`

**get** `/api/v1/files/{id}/page-figures`

List metadata for all figures from all pages of a file.

### Parameters

- `id: string`

- `query: ImageListPageFiguresParams`

  - `organization_id?: string | null`

  - `project_id?: string | null`

### Returns

- `ImageListPageFiguresResponse = Array<ImageListPageFiguresResponseItem>`

  - `confidence: number`

    The confidence of the figure

  - `figure_name: string`

    The name of the figure

  - `figure_size: number`

    The size of the figure in bytes

  - `file_id: string`

    The ID of the file that the figure was taken from

  - `page_index: number`

    The index of the page for which the figure is taken (0-indexed)

  - `is_likely_noise?: boolean`

    Whether the figure is likely to be noise

  - `metadata?: Record<string, unknown> | null`

    Metadata for the figure

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.images.listPageFigures(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response);
```

#### Response

```json
[
  {
    "confidence": 0,
    "figure_name": "figure_name",
    "figure_size": 0,
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "page_index": 0,
    "is_likely_noise": true,
    "metadata": {
      "foo": "bar"
    }
  }
]
```

## Domain Types

### Image List Page Screenshots Response

- `ImageListPageScreenshotsResponse = Array<ImageListPageScreenshotsResponseItem>`

  - `file_id: string`

    The ID of the file that the page screenshot was taken from

  - `image_size: number`

    The size of the image in bytes

  - `page_index: number`

    The index of the page for which the screenshot is taken (0-indexed)

  - `metadata?: Record<string, unknown> | null`

    Metadata for the screenshot

### Image Get Page Screenshot Response

- `ImageGetPageScreenshotResponse = unknown`

### Image Get Page Figure Response

- `ImageGetPageFigureResponse = unknown`

### Image List Page Figures Response

- `ImageListPageFiguresResponse = Array<ImageListPageFiguresResponseItem>`

  - `confidence: number`

    The confidence of the figure

  - `figure_name: string`

    The name of the figure

  - `figure_size: number`

    The size of the figure in bytes

  - `file_id: string`

    The ID of the file that the figure was taken from

  - `page_index: number`

    The index of the page for which the figure is taken (0-indexed)

  - `is_likely_noise?: boolean`

    Whether the figure is likely to be noise

  - `metadata?: Record<string, unknown> | null`

    Metadata for the figure

# Files

## Get Pipeline File Status Counts

`client.pipelines.files.getStatusCounts(stringpipelineID, FileGetStatusCountsParamsquery?, RequestOptionsoptions?): FileGetStatusCountsResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/status-counts`

Get files for a pipeline.

### Parameters

- `pipelineID: string`

- `query: FileGetStatusCountsParams`

  - `data_source_id?: string | null`

  - `only_manually_uploaded?: boolean`

### Returns

- `FileGetStatusCountsResponse`

  - `counts: Record<string, number>`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id?: string | null`

    The ID of the data source that the files belong to

  - `only_manually_uploaded?: boolean`

    Whether to only count manually uploaded files

  - `pipeline_id?: string | null`

    The ID of the pipeline that the files belong to

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.files.getStatusCounts(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response.data_source_id);
```

#### Response

```json
{
  "counts": {
    "foo": 0
  },
  "total_count": 0,
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "only_manually_uploaded": true,
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Get Pipeline File Status

`client.pipelines.files.getStatus(stringfileID, FileGetStatusParamsparams, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/files/{file_id}/status`

Get status of a file for a pipeline.

### Parameters

- `fileID: string`

- `params: FileGetStatusParams`

  - `pipeline_id: string`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.files.getStatus(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  { pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' },
);

console.log(managedIngestionStatusResponse.job_id);
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Add Files To Pipeline Api

`client.pipelines.files.create(stringpipelineID, FileCreateParamsparams, RequestOptionsoptions?): FileCreateResponse`

**put** `/api/v1/pipelines/{pipeline_id}/files`

Add files to a pipeline.

### Parameters

- `pipelineID: string`

- `params: FileCreateParams`

  - `body: Array<Body>`

    - `file_id: string`

      The ID of the file

    - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

      Custom metadata for the file

      - `Record<string, unknown>`

      - `Array<unknown>`

      - `string`

      - `number`

      - `boolean`

### Returns

- `FileCreateResponse = Array<PipelineFile>`

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineFiles = await client.pipelines.files.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  body: [{ file_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e' }],
});

console.log(pipelineFiles);
```

#### Response

```json
[
  {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "config_hash": {
      "foo": {
        "foo": "bar"
      }
    },
    "created_at": "2019-12-27T18:11:19.117Z",
    "custom_metadata": {
      "foo": {
        "foo": "bar"
      }
    },
    "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "external_file_id": "external_file_id",
    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "file_size": 0,
    "file_type": "file_type",
    "indexed_page_count": 0,
    "last_modified_at": "2019-12-27T18:11:19.117Z",
    "name": "name",
    "permission_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "resource_info": {
      "foo": {
        "foo": "bar"
      }
    },
    "status": "NOT_STARTED",
    "status_updated_at": "2019-12-27T18:11:19.117Z",
    "updated_at": "2019-12-27T18:11:19.117Z"
  }
]
```

## Update Pipeline File

`client.pipelines.files.update(stringfileID, FileUpdateParamsparams, RequestOptionsoptions?): PipelineFile`

**put** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Update a file for a pipeline.

### Parameters

- `fileID: string`

- `params: FileUpdateParams`

  - `pipeline_id: string`

    Path param

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Body param: Custom metadata for the file

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

### Returns

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const pipelineFile = await client.pipelines.files.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(pipelineFile.id);
```

#### Response

```json
{
  "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "config_hash": {
    "foo": {
      "foo": "bar"
    }
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "custom_metadata": {
    "foo": {
      "foo": "bar"
    }
  },
  "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "external_file_id": "external_file_id",
  "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "file_size": 0,
  "file_type": "file_type",
  "indexed_page_count": 0,
  "last_modified_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "permission_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
  "resource_info": {
    "foo": {
      "foo": "bar"
    }
  },
  "status": "NOT_STARTED",
  "status_updated_at": "2019-12-27T18:11:19.117Z",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete Pipeline File

`client.pipelines.files.delete(stringfileID, FileDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/files/{file_id}`

Delete a file from a pipeline.

### Parameters

- `fileID: string`

- `params: FileDeleteParams`

  - `pipeline_id: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.files.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```

## List Pipeline Files2

`client.pipelines.files.list(stringpipelineID, FileListParamsquery?, RequestOptionsoptions?): PaginatedPipelineFiles<PipelineFile>`

**get** `/api/v1/pipelines/{pipeline_id}/files2`

List files for a pipeline with optional filtering, sorting, and pagination.

### Parameters

- `pipelineID: string`

- `query: FileListParams`

  - `data_source_id?: string | null`

  - `file_name_contains?: string | null`

  - `limit?: number | null`

  - `offset?: number | null`

  - `only_manually_uploaded?: boolean`

  - `order_by?: string | null`

  - `statuses?: Array<"NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more> | null`

    Filter by file statuses

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

### Returns

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const pipelineFile of client.pipelines.files.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(pipelineFile.id);
}
```

#### Response

```json
{
  "files": [
    {
      "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "config_hash": {
        "foo": {
          "foo": "bar"
        }
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "custom_metadata": {
        "foo": {
          "foo": "bar"
        }
      },
      "data_source_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "external_file_id": "external_file_id",
      "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "file_size": 0,
      "file_type": "file_type",
      "indexed_page_count": 0,
      "last_modified_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "permission_info": {
        "foo": {
          "foo": "bar"
        }
      },
      "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "resource_info": {
        "foo": {
          "foo": "bar"
        }
      },
      "status": "NOT_STARTED",
      "status_updated_at": "2019-12-27T18:11:19.117Z",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```

## Domain Types

### Pipeline File

- `PipelineFile`

  A file associated with a pipeline.

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

### File Get Status Counts Response

- `FileGetStatusCountsResponse`

  - `counts: Record<string, number>`

    The counts of files by status

  - `total_count: number`

    The total number of files

  - `data_source_id?: string | null`

    The ID of the data source that the files belong to

  - `only_manually_uploaded?: boolean`

    Whether to only count manually uploaded files

  - `pipeline_id?: string | null`

    The ID of the pipeline that the files belong to

### File Create Response

- `FileCreateResponse = Array<PipelineFile>`

  - `id: string`

    Unique identifier for the pipeline file.

  - `pipeline_id: string`

    The ID of the pipeline that the file is associated with.

  - `config_hash?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Hashes for the configuration of the pipeline.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `created_at?: string | null`

    When the pipeline file was created.

  - `custom_metadata?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Custom metadata for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `data_source_id?: string | null`

    The ID of the data source that the file belongs to.

  - `external_file_id?: string | null`

    The ID of the file in the external system.

  - `file_id?: string | null`

    The ID of the file.

  - `file_size?: number | null`

    Size of the file in bytes.

  - `file_type?: string | null`

    File type (e.g. pdf, docx, etc.).

  - `indexed_page_count?: number | null`

    The number of pages that have been indexed for this file.

  - `last_modified_at?: string | null`

    The last modified time of the file.

  - `name?: string | null`

    Name of the file.

  - `permission_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Permission information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `project_id?: string | null`

    The ID of the project that the file belongs to.

  - `resource_info?: Record<string, Record<string, unknown> | Array<unknown> | string | 2 more | null> | null`

    Resource information for the file.

    - `Record<string, unknown>`

    - `Array<unknown>`

    - `string`

    - `number`

    - `boolean`

  - `status?: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 2 more | null`

    Status of the pipeline file.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"CANCELLED"`

  - `status_updated_at?: string | null`

    The last time the status was updated.

  - `updated_at?: string | null`

    When the pipeline file was last updated.

# Metadata

## Import Pipeline Metadata

`client.pipelines.metadata.create(stringpipelineID, MetadataCreateParamsbody, RequestOptionsoptions?): MetadataCreateResponse`

**put** `/api/v1/pipelines/{pipeline_id}/metadata`

Import metadata for a pipeline.

### Parameters

- `pipelineID: string`

- `body: MetadataCreateParams`

  - `upload_file: Uploadable`

### Returns

- `MetadataCreateResponse = Record<string, string>`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const metadata = await client.pipelines.metadata.create('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  upload_file: fs.createReadStream('path/to/file'),
});

console.log(metadata);
```

#### Response

```json
{
  "foo": "string"
}
```

## Delete Pipeline Files Metadata

`client.pipelines.metadata.deleteAll(stringpipelineID, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/metadata`

Delete metadata for all files in a pipeline.

### Parameters

- `pipelineID: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.metadata.deleteAll('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');
```

## Domain Types

### Metadata Create Response

- `MetadataCreateResponse = Record<string, string>`

# Documents

## Create Batch Pipeline Documents

`client.pipelines.documents.create(stringpipelineID, DocumentCreateParamsparams, RequestOptionsoptions?): DocumentCreateResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create documents for a pipeline.

### Parameters

- `pipelineID: string`

- `params: DocumentCreateParams`

  - `body: Array<CloudDocumentCreate>`

    - `metadata: Record<string, unknown>`

    - `text: string`

    - `id?: string | null`

    - `excluded_embed_metadata_keys?: Array<string>`

    - `excluded_llm_metadata_keys?: Array<string>`

    - `page_positions?: Array<number> | null`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `DocumentCreateResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocuments = await client.pipelines.documents.create(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    body: [
      {
        metadata: { foo: 'bar' },
        text: 'text',
      },
    ],
  },
);

console.log(cloudDocuments);
```

#### Response

```json
[
  {
    "id": "id",
    "metadata": {
      "foo": "bar"
    },
    "text": "text",
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "page_positions": [
      0
    ],
    "status_metadata": {
      "foo": "bar"
    }
  }
]
```

## Paginated List Pipeline Documents

`client.pipelines.documents.list(stringpipelineID, DocumentListParamsquery?, RequestOptionsoptions?): PaginatedCloudDocuments<CloudDocument>`

**get** `/api/v1/pipelines/{pipeline_id}/documents/paginated`

Return a list of documents for a pipeline.

### Parameters

- `pipelineID: string`

- `query: DocumentListParams`

  - `file_id?: string | null`

  - `limit?: number`

  - `only_api_data_source_documents?: boolean | null`

  - `only_direct_upload?: boolean | null`

  - `skip?: number`

  - `status_refresh_policy?: "cached" | "ttl"`

    - `"cached"`

    - `"ttl"`

### Returns

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const cloudDocument of client.pipelines.documents.list(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(cloudDocument.id);
}
```

#### Response

```json
{
  "documents": [
    {
      "id": "id",
      "metadata": {
        "foo": "bar"
      },
      "text": "text",
      "excluded_embed_metadata_keys": [
        "string"
      ],
      "excluded_llm_metadata_keys": [
        "string"
      ],
      "page_positions": [
        0
      ],
      "status_metadata": {
        "foo": "bar"
      }
    }
  ],
  "limit": 0,
  "offset": 0,
  "total_count": 0
}
```

## Get Pipeline Document

`client.pipelines.documents.get(stringdocumentID, DocumentGetParamsparams, RequestOptionsoptions?): CloudDocument`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Return a single document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentGetParams`

  - `pipeline_id: string`

### Returns

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocument = await client.pipelines.documents.get('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(cloudDocument.id);
```

#### Response

```json
{
  "id": "id",
  "metadata": {
    "foo": "bar"
  },
  "text": "text",
  "excluded_embed_metadata_keys": [
    "string"
  ],
  "excluded_llm_metadata_keys": [
    "string"
  ],
  "page_positions": [
    0
  ],
  "status_metadata": {
    "foo": "bar"
  }
}
```

## Delete Pipeline Document

`client.pipelines.documents.delete(stringdocumentID, DocumentDeleteParamsparams, RequestOptionsoptions?): void`

**delete** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}`

Delete a document from a pipeline.
Initiates an async job that will:

1. Delete vectors from the vector store
1. Delete the document from MongoDB after vectors are successfully deleted

### Parameters

- `documentID: string`

- `params: DocumentDeleteParams`

  - `pipeline_id: string`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

await client.pipelines.documents.delete('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});
```

## Get Pipeline Document Status

`client.pipelines.documents.getStatus(stringdocumentID, DocumentGetStatusParamsparams, RequestOptionsoptions?): ManagedIngestionStatusResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status`

Return a single document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentGetStatusParams`

  - `pipeline_id: string`

### Returns

- `ManagedIngestionStatusResponse`

  - `status: "NOT_STARTED" | "IN_PROGRESS" | "SUCCESS" | 3 more`

    Status of the ingestion.

    - `"NOT_STARTED"`

    - `"IN_PROGRESS"`

    - `"SUCCESS"`

    - `"ERROR"`

    - `"PARTIAL_SUCCESS"`

    - `"CANCELLED"`

  - `deployment_date?: string | null`

    Date of the deployment.

  - `effective_at?: string | null`

    When the status is effective

  - `error?: Array<Error> | null`

    List of errors that occurred during ingestion.

    - `job_id: string`

      ID of the job that failed.

    - `message: string`

      List of errors that occurred during ingestion.

    - `step: "MANAGED_INGESTION" | "DATA_SOURCE" | "FILE_UPDATER" | 4 more`

      Name of the job that failed.

      - `"MANAGED_INGESTION"`

      - `"DATA_SOURCE"`

      - `"FILE_UPDATER"`

      - `"PARSE"`

      - `"TRANSFORM"`

      - `"INGESTION"`

      - `"METADATA_UPDATE"`

  - `job_id?: string | null`

    ID of the latest job.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const managedIngestionStatusResponse = await client.pipelines.documents.getStatus('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(managedIngestionStatusResponse.job_id);
```

#### Response

```json
{
  "status": "NOT_STARTED",
  "deployment_date": "2019-12-27T18:11:19.117Z",
  "effective_at": "2019-12-27T18:11:19.117Z",
  "error": [
    {
      "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
      "message": "message",
      "step": "MANAGED_INGESTION"
    }
  ],
  "job_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
}
```

## Sync Pipeline Document

`client.pipelines.documents.sync(stringdocumentID, DocumentSyncParamsparams, RequestOptionsoptions?): DocumentSyncResponse`

**post** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync`

Sync a specific document for a pipeline.

### Parameters

- `documentID: string`

- `params: DocumentSyncParams`

  - `pipeline_id: string`

### Returns

- `DocumentSyncResponse = unknown`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const response = await client.pipelines.documents.sync('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(response);
```

#### Response

```json
{}
```

## List Pipeline Document Chunks

`client.pipelines.documents.getChunks(stringdocumentID, DocumentGetChunksParamsparams, RequestOptionsoptions?): DocumentGetChunksResponse`

**get** `/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks`

Return a list of chunks for a pipeline document.

### Parameters

- `documentID: string`

- `params: DocumentGetChunksParams`

  - `pipeline_id: string`

### Returns

- `DocumentGetChunksResponse = Array<TextNode>`

  - `class_name?: string`

  - `embedding?: Array<number> | null`

    Embedding of the node.

  - `end_char_idx?: number | null`

    End char index of the node.

  - `excluded_embed_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info?: Record<string, unknown>`

    A flat dictionary of metadata fields

  - `id_?: string`

    Unique ID of the node.

  - `metadata_seperator?: string`

    Separator between metadata fields when converting to string.

  - `metadata_template?: string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype?: string`

    MIME type of the node content.

  - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

    A mapping of relationships to other node information.

    - `RelatedNodeInfo`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

    - `Array<UnionMember1>`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

  - `start_char_idx?: number | null`

    Start char index of the node.

  - `text?: string`

    Text content of the node.

  - `text_template?: string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const textNodes = await client.pipelines.documents.getChunks('document_id', {
  pipeline_id: '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
});

console.log(textNodes);
```

#### Response

```json
[
  {
    "class_name": "class_name",
    "embedding": [
      0
    ],
    "end_char_idx": 0,
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "extra_info": {
      "foo": "bar"
    },
    "id_": "id_",
    "metadata_seperator": "metadata_seperator",
    "metadata_template": "metadata_template",
    "mimetype": "mimetype",
    "relationships": {
      "foo": {
        "node_id": "node_id",
        "class_name": "class_name",
        "hash": "hash",
        "metadata": {
          "foo": "bar"
        },
        "node_type": "1"
      }
    },
    "start_char_idx": 0,
    "text": "text",
    "text_template": "text_template"
  }
]
```

## Upsert Batch Pipeline Documents

`client.pipelines.documents.upsert(stringpipelineID, DocumentUpsertParamsparams, RequestOptionsoptions?): DocumentUpsertResponse`

**put** `/api/v1/pipelines/{pipeline_id}/documents`

Batch create or update a document for a pipeline.

### Parameters

- `pipelineID: string`

- `params: DocumentUpsertParams`

  - `body: Array<CloudDocumentCreate>`

    - `metadata: Record<string, unknown>`

    - `text: string`

    - `id?: string | null`

    - `excluded_embed_metadata_keys?: Array<string>`

    - `excluded_llm_metadata_keys?: Array<string>`

    - `page_positions?: Array<number> | null`

      indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Returns

- `DocumentUpsertResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Example

```typescript
import LlamaCloud from '@llamaindex/llama-cloud';

const client = new LlamaCloud({
  apiKey: process.env['LLAMA_CLOUD_API_KEY'], // This is the default and can be omitted
});

const cloudDocuments = await client.pipelines.documents.upsert(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
  {
    body: [
      {
        metadata: { foo: 'bar' },
        text: 'text',
      },
    ],
  },
);

console.log(cloudDocuments);
```

#### Response

```json
[
  {
    "id": "id",
    "metadata": {
      "foo": "bar"
    },
    "text": "text",
    "excluded_embed_metadata_keys": [
      "string"
    ],
    "excluded_llm_metadata_keys": [
      "string"
    ],
    "page_positions": [
      0
    ],
    "status_metadata": {
      "foo": "bar"
    }
  }
]
```

## Domain Types

### Cloud Document

- `CloudDocument`

  Cloud document stored in S3.

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Cloud Document Create

- `CloudDocumentCreate`

  Create a new cloud document.

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `id?: string | null`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

### Text Node

- `TextNode`

  Provided for backward compatibility.

  - `class_name?: string`

  - `embedding?: Array<number> | null`

    Embedding of the node.

  - `end_char_idx?: number | null`

    End char index of the node.

  - `excluded_embed_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info?: Record<string, unknown>`

    A flat dictionary of metadata fields

  - `id_?: string`

    Unique ID of the node.

  - `metadata_seperator?: string`

    Separator between metadata fields when converting to string.

  - `metadata_template?: string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype?: string`

    MIME type of the node content.

  - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

    A mapping of relationships to other node information.

    - `RelatedNodeInfo`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

    - `Array<UnionMember1>`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

  - `start_char_idx?: number | null`

    Start char index of the node.

  - `text?: string`

    Text content of the node.

  - `text_template?: string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Document Create Response

- `DocumentCreateResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`

### Document Sync Response

- `DocumentSyncResponse = unknown`

### Document Get Chunks Response

- `DocumentGetChunksResponse = Array<TextNode>`

  - `class_name?: string`

  - `embedding?: Array<number> | null`

    Embedding of the node.

  - `end_char_idx?: number | null`

    End char index of the node.

  - `excluded_embed_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the embed model.

  - `excluded_llm_metadata_keys?: Array<string>`

    Metadata keys that are excluded from text for the LLM.

  - `extra_info?: Record<string, unknown>`

    A flat dictionary of metadata fields

  - `id_?: string`

    Unique ID of the node.

  - `metadata_seperator?: string`

    Separator between metadata fields when converting to string.

  - `metadata_template?: string`

    Template for how metadata is formatted, with {key} and {value} placeholders.

  - `mimetype?: string`

    MIME type of the node content.

  - `relationships?: Record<string, RelatedNodeInfo | Array<UnionMember1>>`

    A mapping of relationships to other node information.

    - `RelatedNodeInfo`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

    - `Array<UnionMember1>`

      - `node_id: string`

      - `class_name?: string`

      - `hash?: string | null`

      - `metadata?: Record<string, unknown>`

      - `node_type?: "1" | "2" | "3" | 2 more | (string & {}) | null`

        - `"1" | "2" | "3" | 2 more`

          - `"1"`

          - `"2"`

          - `"3"`

          - `"4"`

          - `"5"`

        - `(string & {})`

  - `start_char_idx?: number | null`

    Start char index of the node.

  - `text?: string`

    Text content of the node.

  - `text_template?: string`

    Template for how text is formatted, with {content} and {metadata_str} placeholders.

### Document Upsert Response

- `DocumentUpsertResponse = Array<CloudDocument>`

  - `id: string`

  - `metadata: Record<string, unknown>`

  - `text: string`

  - `excluded_embed_metadata_keys?: Array<string>`

  - `excluded_llm_metadata_keys?: Array<string>`

  - `page_positions?: Array<number> | null`

    indices in the CloudDocument.text where a new page begins. e.g. Second page starts at index specified by page_positions[1].

  - `status_metadata?: Record<string, unknown> | null`
