import argparse

from .server import mcp



def main():
    parser = argparse.ArgumentParser(description="Run MCP server.")
    parser.add_argument('transport', nargs='?', default='stdio', choices=['stdio', 'sse'],
                        help='Transport type (stdio or sse)')
    args = parser.parse_args()
    mcp.run(transport=args.transport)

if __name__ == "__main__":
    main()
