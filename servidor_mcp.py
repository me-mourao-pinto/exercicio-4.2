"""MCP server that exposes tools calling the API 4.1 endpoint."""

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Exercicio4.2")

API_BASE = "http://localhost:8000"


@mcp.tool()
async def consultar_saldo(conta_id: str) -> str:
    """Consulta o saldo de uma conta."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE}/api/contas/{conta_id}/saldo")
        resp.raise_for_status()
        return resp.text


@mcp.tool()
async def transferir(
    conta_origem: str, conta_destino: str, valor: float
) -> str:
    """Realiza uma transferência entre contas."""
    async with httpx.AsyncClient() as client:
        payload = {
            "conta_origem": conta_origem,
            "conta_destino": conta_destino,
            "valor": valor,
        }
        resp = await client.post(f"{API_BASE}/api/transferencias", json=payload)
        resp.raise_for_status()
        return resp.text


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
