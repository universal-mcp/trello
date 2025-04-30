# Universal Mcp Trello MCP Server

An MCP Server for the Universal Mcp Trello API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_trello/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Trello API.


| Tool | Description |
|------|-------------|
| `get1_boards_id` | Retrieve board details by ID from the API endpoint. |
| `get1_boards_id_lists` | Retrieves lists for a specific board from the Trello API using its ID. |
| `post1_cards` | Creates a new card by sending a POST request to the /1/cards endpoint. |
| `get1_cards_id` | Retrieve card details by ID using the API endpoint. |
| `put1_cards_id` | Updates a card by making a PUT request to the /1/cards/{id} endpoint with optional description, name, key, and token parameters. |
| `delete1_cards_id` | Deletes a card with the specified ID by sending a DELETE request including key and token parameters. |

## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_trello/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Trello app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 