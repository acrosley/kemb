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
