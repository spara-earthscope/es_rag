# Literature Review for SSA 2026 Workshop

## Methodology

Created a 100+ corpus of articles using search terms for seismic and geodetic research using cloud based data and machine learning listed in Google Scholar.

Wrote a script using llamaindex to ingest corpus into duckdb as embeddings. Embeddings were created using Ollama for inference and the gemmaembedding model.

Prompts (included in script) were used to generate responses with Ollama running gemma3:4b model for inference.

Responses were saved in markdown. Few-shot prompts with ChatGPT were used to create a lesson plan and notional Python exercises based on the responses included in the prompt's context.

## Artifacts
- `es_ssa2026.py` - script for creating embeddings, loading duckdb, and generate response to prompts.
- `./docs` contains corpus of articles
- `/responses` contains summaries generated from zero-shot prompts
- `./summaries` contains summaries for all seismic and geodetic articles.

## To Do

- Streaming client with memory UI (probably streamlit)
- Setup instructions
- MCP framework: 
    - agent for Google Scholar search 
    - agent for document/pdf retrieval and to stream results to summarizer 
    - agent to eval articles
    - agent to summarize articles
    - agent to chunk and encode articles
    - agent to upsert to DuckDB

search => eval articles => download => summarize => chunk/encode => upsert

## Implementation considerations

1. DuckDuckGo search vs SERP
2. Agent swarm in MCP???
3. Pydantic model??? Bibtex results?
4. Multiple models for different tasks?


