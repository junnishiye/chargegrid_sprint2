# ChargeGrid Intelligence Chatbot

## EV Challenge 2026 – FIAP x GoodWe
### Sprint 2 – Desenvolvimento e Evolução do Chatbot

---

# Integrantes

| Nome | RM |
|--------|--------|
| Davi Sinhorini | 569487 |
| Gabriel da Silva | 568910 |
| Henrique de Souza | 570529 |
| André Balan | 571691 |
| João Vitor Jun | 572079 |

---

# Objetivo do Projeto

O ChargeGrid Intelligence Chatbot foi desenvolvido para auxiliar operadores comerciais de eletropostos GoodWe na consulta rápida de informações técnicas e operacionais relacionadas à gestão de carregadores de veículos elétricos.

A solução utiliza Inteligência Artificial Generativa combinada com RAG (Retrieval-Augmented Generation), permitindo responder perguntas com base em documentos técnicos oficiais e conteúdos do site da GoodWe.

---

# Problema Abordado

Atualmente, operadores de eletropostos precisam consultar diversos manuais e documentações para realizar tarefas como:

- Configuração de tarifas
- Controle de sessões de recarga
- Cadastro de cartões RFID
- Diagnóstico de falhas
- Monitoramento operacional
- Controle de potência e consumo

O chatbot centraliza esse conhecimento e fornece respostas rápidas em linguagem natural.

---

# Arquitetura da Solução

A arquitetura implementada segue o padrão RAG:

```text
Usuário
   │
   ▼
Pergunta
   │
   ▼
Embedding da pergunta
   │
   ▼
Busca Vetorial
   │
   ▼
Documentos relevantes
   │
   ▼
System Prompt + Contexto + Histórico
   │
   ▼
GPT-4o-mini
   │
   ▼
Resposta ao usuário
```

Além disso, foi implementada memória conversacional para manter o contexto entre perguntas consecutivas.

---

# Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Linguagem principal |
| OpenAI GPT-4o-mini | Geração das respostas |
| LangChain | Orquestração do pipeline RAG |
| LangGraph | Fluxo do chatbot |
| OpenAI Embeddings | Vetorização dos documentos |
| InMemoryVectorStore | Armazenamento vetorial |
| PyPDFLoader | Leitura dos PDFs |
| WebBaseLoader | Coleta de conteúdo do site |
| Google Colab | Ambiente de desenvolvimento |

---

# Base de Conhecimento

O chatbot consulta as seguintes fontes:

### PDFs

- GW_HCA-G2_User-Manual_PT.pdf
- GoodWe_EV_ChargeOps_Base_Conhecimento.pdf
- goodwe_carregador.pdf
- goodwe_carregador1.pdf
- goodwe_instalacao.pdf
- goodwe_manualcarregador.pdf
- goodwe_manualdousuario.pdf

### Site Oficial

- https://br.goodwe.com

---

# Funcionalidades Implementadas

## Sprint 1

- Criação da base de conhecimento
- Implementação inicial do RAG
- Integração com GPT-4o-mini
- Busca vetorial
- Testes iniciais

## Sprint 2

- Memória conversacional
- Histórico de mensagens
- Melhoria do contexto do system prompt
- Refinamento das respostas
- Documentação do projeto
- Vídeo demonstrativo

---

# Dependências

Instale as bibliotecas abaixo:

```bash
pip install langchain
pip install langchain-openai
pip install langchain-community
pip install langgraph
pip install langsmith
pip install pypdf
pip install beautifulsoup4
pip install faiss-cpu
pip install tiktoken
```

---

# Variáveis de Ambiente

O projeto utiliza a API da OpenAI.

Configure sua chave de API:

```python
OPENAI_API_KEY="sua_chave"
```

No Google Colab:

```python
from google.colab import userdata

OPENAI_API_KEY = userdata.get("OPENAI_API_KEY")
```

Importante:

- Nunca exponha a API Key no código.
- Utilize Google Colab Secrets ou variáveis de ambiente.

---

# Como Executar

## 1. Carregar os documentos

Importar os PDFs da base de conhecimento.

## 2. Criar embeddings

Gerar os embeddings dos documentos utilizando OpenAI Embeddings.

## 3. Construir a base vetorial

Armazenar os documentos vetorizados.

## 4. Executar o chatbot

Exemplo:

```python
result = graph.invoke(
    {
        "question": "Como configurar limite de kWh por sessão?"
    }
)

print(result["answer"])
```

---

# Memória Conversacional

Foi implementada uma memória simples baseada em histórico de mensagens.

Exemplo:

```python
chat_history = []
```

Após cada interação:

```python
chat_history.append(
    HumanMessage(content=state["question"])
)

chat_history.append(
    AIMessage(content=response.content)
)
```

Isso permite perguntas de continuidade como:

- Explique melhor a resposta anterior.
- Resuma a resposta anterior.
- Qual o próximo passo?
- Existem riscos nessa configuração?

---

# Exemplos de Uso

### Pergunta

```text
Como limitar o consumo máximo por sessão em kWh?
```

### Resposta

```text
No SEMS Portal, ative o limite de energia por sessão nas configurações de recarga e defina o valor máximo em kWh.
```

---

### Pergunta

```text
O que significa o erro E-04?
```

### Resposta

```text
O erro E-04 indica falha na comunicação com o servidor de gerenciamento.
```

---

### Pergunta

```text
Como cadastrar um novo RFID?
```

### Resposta

```text
No SEMS Portal, acesse Gestão de usuários e selecione Adicionar RFID.
```

---

# Estrutura do Repositório

```text
/
├── README.md
├── testechatbot.ipynb
├── system_prompt.txt
├── fluxograma.png
├── testes.md
├── docs/
│   ├── GW_HCA-G2_User-Manual_PT.pdf
│   ├── GoodWe_EV_ChargeOps_Base_Conhecimento.pdf
│   └── demais PDFs
```

---

# Resultados Obtidos

- Chatbot funcional
- Respostas contextualizadas
- Busca baseada em documentação oficial
- Memória conversacional implementada
- Integração com GPT-4o-mini
- Testes realizados com sucesso

---

# Próximos Passos

- Persistência de memória em banco vetorial
- Interface web para usuários finais
- Integração com APIs da GoodWe
- Expansão da base de conhecimento
- Implementação de Function Calling
