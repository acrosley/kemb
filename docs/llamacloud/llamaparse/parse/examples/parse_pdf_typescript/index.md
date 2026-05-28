---
title: Parse a PDF in TypeScript | Developer Documentation
---

This tutorial walks through parsing a PDF with Parse from a Node.js TypeScript script — install the SDK, set your API key, run the parse, walk the markdown output. It’s the TypeScript counterpart to the [Quick Start: Parse a PDF & Interpret Outputs](/llamaparse/parse/examples/parse_pdf_outputs/index.md) Python tutorial, and it’s the recommended starting point if you’re building a server-side or CLI-style integration in Node.

## When to use TypeScript

The Parse SDK works the same way in Python and TypeScript — same tier system, same option buckets, same response shapes. Pick TypeScript when:

- You’re integrating Parse into a Node.js or Bun service, an Edge function, or a CLI tool you’ll distribute as a package
- Your team is already on TS and you want a single language across the stack
- You need to wire Parse into a Next.js, Astro, or other JS-first framework

If you’re prototyping in a notebook, the [Python tutorials](/llamaparse/parse/examples/index.md) are a faster path. Once you’re ready to ship, the patterns translate cleanly.

## 1. Set up your project

Initialize a fresh project (or skip this if you already have one):

Terminal window

```
mkdir parse-tutorial && cd parse-tutorial
npm init -y
```

Install the SDK and `tsx` (a TypeScript runner that supports modern ESM syntax including top-level `await`):

Terminal window

```
npm install @llamaindex/llama-cloud
npm install --save-dev tsx typescript @types/node
```

Set your Parse API key as an environment variable so the SDK picks it up automatically:

Terminal window

```
export LLAMA_CLOUD_API_KEY="llx-..."
```

[Get an API key](/llamaparse/general/api_key/index.md) from the LlamaCloud dashboard if you don’t have one yet.

## 2. Download a sample PDF

For this tutorial, we’ll parse the [LLaMA paper](https://arxiv.org/pdf/2302.13971.pdf) — a public research paper with the kind of multi-column layout, tables, and figures that show off Parse’s strengths.

Terminal window

```
curl -L -o llama.pdf https://arxiv.org/pdf/2302.13971.pdf
```

You can use any PDF — substitute its path in the script below.

## 3. Write the parse script

Create `parse.ts` with the bare minimum: upload, parse, print the markdown.

```
import LlamaCloud from "@llamaindex/llama-cloud";
import fs from "fs";


const client = new LlamaCloud(); // reads LLAMA_CLOUD_API_KEY from the environment


console.log("Uploading file...");
const file = await client.files.create({
  file: fs.createReadStream("./llama.pdf"),
  purpose: "parse",
});


console.log(`Uploaded file ${file.id}, parsing...`);
const result = await client.parsing.parse({
  file_id: file.id,
  tier: "agentic",
  version: "latest",
  expand: ["markdown"],
});


console.log(`Job status: ${result.job.status}`);
console.log(`Total pages: ${result.markdown.pages.length}`);
console.log("\n--- First page markdown ---\n");
console.log(result.markdown.pages[0].markdown);
```

A few things worth noting:

- **`new LlamaCloud()` reads `LLAMA_CLOUD_API_KEY` from the environment** — you don’t need to pass it explicitly. If you do want to pass it, use `new LlamaCloud({ apiKey: "llx-..." })`.
- **`client.parsing.parse()` blocks until the job finishes and returns the full result.** The SDK handles polling for you. If you’re hitting the raw REST API directly, you’d need to poll yourself — see the [REST API tab in Getting Started](/llamaparse/parse/getting_started/index.md).
- **Top-level `await`** works here because `tsx` runs the file as an ES module. If you’re targeting CommonJS (`"type": "commonjs"` in your `package.json`), wrap the body in an `async function main()` and call `main()`.

## 4. Run it

Terminal window

```
npx tsx parse.ts
```

You should see the upload, the parse job run, and the first page of the LLaMA paper printed as markdown — title, author block, abstract, section headings, all preserved as proper markdown structure.

## 5. Walk every page

The bare-bones script above only prints the first page. To process the entire document, iterate over `result.markdown.pages`:

```
for (const page of result.markdown.pages) {
  console.log(`\n=== Page ${page.page_number} ===\n`);
  console.log(page.markdown);
}
```

Or concatenate the whole document into a single markdown string for an LLM prompt:

```
const fullDocument = result.markdown.pages
  .map((p) => p.markdown)
  .join("\n\n---\n\n");


console.log(`Full document is ${fullDocument.length} characters.`);
// fullDocument is now ready to feed into your LLM
```

## 6. Get more than markdown

The `expand` array controls what comes back in the response. Ask for `items` if you want the structured tree (tables, headings, figures), `text` if you want plain text per page, `metadata` if you want confidence scores and per-page metadata:

```
const result = await client.parsing.parse({
  file_id: file.id,
  tier: "agentic",
  version: "latest",
  expand: ["markdown", "items", "metadata"],
});


// Walk the items tree to find tables
for (const page of result.items.pages) {
  for (const item of page.items) {
    if (item.type === "table") {
      console.log(
        `Table on page ${page.page_number}: ${item.rows.length} rows`,
      );
    }
  }
}


// Inspect per-page confidence
for (const page of result.metadata.pages) {
  console.log(`Page ${page.page_number}: confidence ${page.confidence}`);
}
```

See [Retrieving Results](/llamaparse/parse/guides/retrieving-results/index.md) for every legal `expand` value and what it returns.

## 7. Add a custom prompt

Steer the parser with natural-language instructions via `agentic_options.custom_prompt`:

```
const result = await client.parsing.parse({
  file_id: file.id,
  tier: "agentic",
  version: "latest",
  agentic_options: {
    custom_prompt:
      "This is a scientific research paper. Preserve all mathematical equations in LaTeX. Keep inline citations like (Smith 2024) intact in the flowing text. Do not flatten the multi-column layout into a single column.",
  },
  expand: ["markdown"],
});
```

Custom prompts only work on the `cost_effective`, `agentic`, and `agentic_plus` tiers (not `fast`). See [Custom Prompt](/llamaparse/parse/guides/configuring-parse/#custom-prompt/index.md) for the full prompt-engineering guide.

## 8. Save the results to disk

The most common pattern after parsing is writing the markdown to a file:

```
import { writeFileSync } from "fs";


const fullDocument = result.markdown.pages
  .map((p) => p.markdown)
  .join("\n\n---\n\n");


writeFileSync("./llama-parsed.md", fullDocument);
console.log("Wrote llama-parsed.md");
```

Or write each page as a separate file for downstream chunking:

```
for (const page of result.markdown.pages) {
  writeFileSync(`./pages/page-${page.page_number}.md`, page.markdown);
}
```

## Common gotchas

- **`tsx` not running top-level `await`?** Check that your `package.json` has `"type": "module"` (or use `tsx`’s ESM mode explicitly). If you’re stuck on CommonJS, wrap the script in `async function main() { ... } main()`.
- **Authentication errors?** Make sure `LLAMA_CLOUD_API_KEY` is set in the same shell session you’re running `tsx` in. `echo $LLAMA_CLOUD_API_KEY` should print your key, not be empty.
- **`fs.createReadStream` issues?** The path is relative to your current working directory, not the script file. Use an absolute path with `path.resolve(__dirname, "llama.pdf")` if you’re running from a different directory.
- **Parse job hangs?** It shouldn’t — `client.parsing.parse()` blocks for as long as the job takes, but the SDK has built-in timeouts. If a single job takes more than a couple of minutes, check the document — very long documents (1000+ pages) on `agentic_plus` can take several minutes.

## See also

- [Getting Started → TypeScript tab](/llamaparse/parse/getting_started/index.md) — the canonical first-parse setup with simpler scope
- [Quick Start: Parse a PDF & Interpret Outputs](/llamaparse/parse/examples/parse_pdf_outputs/index.md) — the Python equivalent of this tutorial with deeper interpretation of each output view
- [Tiers](/llamaparse/parse/guides/tiers/index.md) — pick the right tier for your document
- [Configuration Model](/llamaparse/parse/guides/configuring-parse/index.md) — where every option lives in the request shape
- [Retrieving Results](/llamaparse/parse/guides/retrieving-results/index.md) — every legal `expand` value
- [Custom Prompt](/llamaparse/parse/guides/configuring-parse/#custom-prompt/index.md) — natural-language steering of the agentic parser
