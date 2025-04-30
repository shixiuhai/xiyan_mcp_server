import argparse
import sys

from .server import run_mcp


def main():
    parser = argparse.ArgumentParser(description="Run MCP server.")
    parser.add_argument("-transport", type=str, default="stdio",
                        help="Transport method: 'stdio' or 'sse'")
    args = parser.parse_args(sys.argv[1:])  # 忽略第一个参数（模块名）
    run_mcp(transport=args.transport)

if __name__ == "__main__":
    main()