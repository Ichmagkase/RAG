# RAG Memory System 
  ## Overview
  This project implements a lightweight retrieval-augmented memory system for a local LLM workflow.
  User interactions are embedded, stored in SQLite, retrieved by semantic similarity, and injected into future prompts
  as context.
  ## Features
  - Stores conversation memories in SQLite
  - Generates semantic embeddings for each memory
  - Retrieves top-k relevant memories using cosine similarity
  - Prepends retrieved memories to the next prompt
  - Persists memory across application restarts
  ## Tech Stack
  - Python 3.12+
  - SQLite
  - `sentence-transformers` 
  - PyTorch
  - Local model runtime (Unsloth)
  - Docker
  ## Prerequisites
  - Python 3.12+
  - Docker (for containerized run)
  - (If using GPU path) NVIDIA drivers/runtime configured
  ## Project Structure
  - `main.py` - CLI entrypoint, retrieval + prompt flow
  - `database.py` - SQLite schema + insert/select/update logic
  - `transformer.py` - embedding generation + similarity ranking
  - `memory.py` - memory data model
  - `model.py` - local model inference wrapper
  - `cleanup.py` - utility to delete/reset `memory.db`
  - `docker-compose.yml` / `Dockerfile` - container setup
  ## Docker Run
  ### 1) Build and start container
  ```bash
  docker compose up --build
  ```
  ### 2) Run in detached mode (optional)
  ```bash
  docker compose up -d --build
  ```
  ### 3) Stop services
  ```bash
  docker compose down
  ```
