from fastmcp import FastMCP

mcp = FastMCP("MCP Training Demo")


@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}! Welcome to the MCP Training demo."


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together."""
    return a + b


if __name__ == "__main__":
    mcp.run()
