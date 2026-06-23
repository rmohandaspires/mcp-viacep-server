# MCP ViaCEP Server

Servidor MCP (Model Context Protocol) para consulta de CEPs brasileiros via API [ViaCEP](https://viacep.com.br). Permite que assistentes de IA como o Claude consultem endereços e busquem CEPs diretamente durante uma conversa.

## Ferramentas disponíveis

### `consultar_cep`
Consulta um CEP brasileiro e retorna o endereço completo.

**Parâmetros:**
- `cep` (string): CEP com ou sem formatação (ex: `01310-100` ou `01310100`)

**Retorno:**
```
CEP: 01310-100
Logradouro: Avenida Paulista
Complemento: de 1 a 610 - lado par
Bairro: Bela Vista
Cidade: São Paulo
Estado: SP
IBGE: 3550308
```

### `buscar_ceps_por_endereco`
Busca CEPs a partir de estado, cidade e logradouro. Retorna até 10 resultados.

**Parâmetros:**
- `estado` (string): Sigla do estado (ex: `SP`)
- `cidade` (string): Nome da cidade (ex: `São Paulo`)
- `logradouro` (string): Nome da rua ou avenida (ex: `Paulista`)

## Instalação

### Pré-requisitos
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recomendado) ou pip

### Com uv

```bash
git clone https://github.com/rmohandaspires/mcp-viacep-server.git
cd mcp-viacep-server
uv venv
uv pip install mcp httpx
```

### Com pip

```bash
git clone https://github.com/rmohandaspires/mcp-viacep-server.git
cd mcp-viacep-server
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/macOS
pip install mcp httpx
```

## Configuração no Claude Desktop

Adicione ao arquivo de configuração do Claude Desktop (`claude_desktop_config.json`):

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "viacep": {
      "command": "python",
      "args": ["C:/caminho/para/mcp-viacep-server/server.py"]
    }
  }
}
```

> Substitua `C:/caminho/para/mcp-viacep-server/` pelo caminho real do projeto na sua máquina.

## Execução manual

```bash
python server.py
```

## Dependências

| Pacote  | Versão  | Uso                            |
|---------|---------|--------------------------------|
| mcp     | 1.28.0+ | Framework MCP (FastMCP)        |
| httpx   | 0.28.0+ | Requisições HTTP assíncronas   |

## API utilizada

Este servidor consome a [API ViaCEP](https://viacep.com.br), que é gratuita, pública e não requer autenticação.

- Consulta por CEP: `GET https://viacep.com.br/ws/{cep}/json/`
- Busca por endereço: `GET https://viacep.com.br/ws/{UF}/{cidade}/{logradouro}/json/`

## Licença

MIT
