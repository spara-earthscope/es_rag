# Literature Review for SSA 2026 Workshop

## Methodology

Created a 100+ corpus of articles using search terms for seismic and geodetic research using cloud based data and machine learning listed in Google Scholar.

Wrote a script using llamaindex to ingest corpus into duckdb as embeddings. Embeddings were created using Ollama for inference and the gemmaembedding model.

Zero-shot prompts were used to generate responses with Ollama running gemma3:4b model for inference.

Responses were saved in markdown. ChatGPT was used to create a lesson plan and notional Python exercises based on the responses included in the prompt's context.

## Artifacts
- `es_ssa2026.py` - script for creating embeddings, loading duckdb, and generate response to prompts.
- `./docs` contains corpus of articles
- `/responses` contains summaries generated from zero-shot prompts
- `./lesson_plan` contains ChatGPT generated lesson plan and exercises.