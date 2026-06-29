import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> dict:
    params = StdioServerParameters(command="python", args=["servidor_mcp.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:

            # Inicializa a conexão MCP
            await session.initialize()

            # Lista as ferramentas disponíveis
            tools = await session.list_tools()
            nomes = [tool.name for tool in tools.tools]

            # Chama criar_tarefa
            criar = await session.call_tool(
                "criar_tarefa",
                {"titulo": "tarefa via mcp"},
            )
#Sugestão ChatGPT
            print(type(criar))
            print(criar)

            print(type(criar.content))
            print(criar.content)

            print(type(criar.content[0]))
            print(criar.content[0])

            print(dir(criar.content[0]))
           
            # Chama listar_tarefas
            listar = await session.call_tool(
                "listar_tarefas",
                {},
            )

            return {
                "tools": nomes,
                "criar_resultado": json.loads(criar.content[0].text),
                "listar_resultado": json.loads(listar.content[0].text),
            }


if __name__ == "__main__":
    print(json.dumps(asyncio.run(main())))
