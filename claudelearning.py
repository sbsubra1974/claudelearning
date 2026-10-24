# pip install claude-agent-sdk
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions, ClaudeSDKClient
import asyncio

# 1. Define your tool natively
@tool("fetch_data", "Fetches database insights for the agent", {"query": str})
async def fetch_data(args):
    return {"content": [{"type": "text", "text": f"Result for {args['query']}"}]}

async def main():
    # 2. Package your tools into an in-process SDK MCP server
    my_server = create_sdk_mcp_server(
        name="internal-analytics",
        version="1.0.0",
        tools=[fetch_data]
    )

    # 3. Mount the server inside the Agent configuration
    options = ClaudeAgentOptions(
        mcp_servers={"analytics_scope": my_server},
        allowed_tools=["mcp__analytics_scope__fetch_data"] # Auto-approved tool execution
    )

    # 4. Programmatically run queries against the agent host
    async with ClaudeSDKClient(options=options) as client:
        await client.query("Run a fetch_data query for recent signups")
        async for msg in client.receive_response():
            print(msg)

if __name__ == "__main__":
    asyncio.run(main())
