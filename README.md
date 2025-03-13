
# XiYan MCP Server

A Model Context Protocol (MCP) server that enables natural language queries to MySQL databases, power by XiYanSQL as text-to-sql technique.


## Features
- Fetch data by natural language throught XiYanSQL (https://github.com/XGenerationLab/XiYan-SQL)
- List available MySQL tables as resources
- Read table contents

## Installation

```bash
pip install xiyan-mcp-server
```

## Configuration

Set the following environment variables:

```bash
YML=    # yml config file path
```

see config_demo.yml for example

## Models

Any LLMs are supported as long as they support the `chat` API. 
We recommend using xiyansql-qwencoder-32b (https://github.com/XGenerationLab/XiYanSQL-QwenCoder) for best performance.

## Usage

### With Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "xiyan": {
      "command": "uv",
      "args": [
        "--directory", 
        "path/to/xiyan_mcp_server",
        "run",
        "xiyan_mcp_server"
      ],
      "env": {
        "YML": "path/to/yml"
      }
    }
  }
}
```

### As a standalone server

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python -m xiyan_mcp_server
```

## Development

```bash
# Clone the repository
git clone https://github.com/XGenerationLab/xiyan_mcp_server.git
cd xiyan_mcp_server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install -r requirements.txt

```
