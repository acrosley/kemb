---
title: API Key | Developer Documentation
description: Instructions on how to obtain and manage an API key for LlamaCloud services including Parse, Extract, and Index.
---

You need an API key to use LlamaParse services including Parse, Extract, and Index.

## Generate a New API Key

1. Go to [LlamaCloud](https://cloud.llamaindex.ai) and sign in with your preferred method.

2. Click on “API Key” in the left sidebar navigation.

3. Click the “Generate New Key” button.

   Access the API Key page

   ![Access API Key page](/_astro/api_keys.DwipGkM3_ZfSkud.png)

4. Enter a descriptive name for your key and click “Create new key”.

5. **Important**: Copy your API key immediately. For security reasons, you won’t be able to view the full key after you leave this page.

   Generate your key

   ![Generate a new API key](/_astro/new_key.D4lVF-r2_Z29zYaq.png)

## Managing Your API Keys

You can manage all your API keys from the API Key page:

- **View active keys**: See all currently active keys and when they were created
- **Revoke keys**: If a key is compromised or no longer needed, you can instantly revoke it
- **Create new keys**: Generate additional keys for different projects or environments

The UI lets you manage your keys

![Manage API keys](/_astro/manage_keys.6Pez5JW6_R34gO.png)

## Using Your API Key

Each LlamaCloud product has specific instructions for using your API key:

- [Parse usage instructions](../../llamaparse/getting_started/)
- [Extract usage instructions](../../llamaextract/getting_started/)
- [Index usage instructions](../../llamacloud/getting_started/)

## API Key Scope

API keys in LlamaCloud are scoped to both the individual user and the project:

- **User Scope**: Each API key is associated with the user who created it
- **Project Scope**: Keys are tied to the specific project they were created in and cannot be used across different projects

This scoping ensures proper access control and usage tracking within your organization.

## Security Best Practices

- **Never hardcode your API key** directly in your application code
- Store API keys as environment variables or in a secure key management service
- Rotate your keys periodically for enhanced security
- Use different keys for development and production environments
