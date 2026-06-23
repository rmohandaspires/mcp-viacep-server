import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ViaCEP")


@mcp.tool()
async def consultar_cep(cep: str) -> str:
    """Consulta um CEP brasileiro e retorna o endereço completo."""
    cep_limpo = cep.replace("-", "").replace(".", "").strip()

    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        return "CEP inválido. Informe 8 dígitos numéricos (ex: 01310100)."

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://viacep.com.br/ws/{cep_limpo}/json/")

    if response.status_code != 200:
        return "Erro ao consultar o ViaCEP. Tente novamente."

    dados = response.json()

    if "erro" in dados:
        return f"CEP {cep} não encontrado."

    return (
        f"CEP: {dados.get('cep', '')}\n"
        f"Logradouro: {dados.get('logradouro', '')}\n"
        f"Complemento: {dados.get('complemento', '') or '—'}\n"
        f"Bairro: {dados.get('bairro', '')}\n"
        f"Cidade: {dados.get('localidade', '')}\n"
        f"Estado: {dados.get('uf', '')}\n"
        f"IBGE: {dados.get('ibge', '')}"
    )


@mcp.tool()
async def buscar_ceps_por_endereco(estado: str, cidade: str, logradouro: str) -> str:
    """Busca CEPs a partir de estado (UF), cidade e logradouro."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://viacep.com.br/ws/{estado}/{cidade}/{logradouro}/json/"
        )

    if response.status_code != 200:
        return "Erro ao consultar o ViaCEP."

    resultados = response.json()

    if not resultados:
        return "Nenhum endereço encontrado."

    linhas = []
    for r in resultados[:10]:  # limita a 10 resultados
        linhas.append(f"- {r.get('cep')} | {r.get('logradouro')} | {r.get('bairro')}")

    return f"Encontrados {len(resultados)} resultado(s):\n" + "\n".join(linhas)


if __name__ == "__main__":
    mcp.run()