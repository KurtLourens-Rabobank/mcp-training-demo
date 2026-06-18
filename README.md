# MCP Training

This repository contains a small demo MCP server built with FastMCP in Python.

## What it includes
- A minimal MCP server setup
- Two example tools:
  - `greet(name)`
  - `add(a, b)`

## Setup

1. Create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies
   ```bash
   pip install -e .
   ```
3. Run the server
   ```bash
   python server.py
   ```

## Notes
- This demo uses the FastMCP Python SDK.
- For a client, you can connect to the server using any MCP-compatible client.
