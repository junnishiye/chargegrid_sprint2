# ChargeGrid Intelligence

## Integrantes

* André Felix — RM 571691
* Davi Pacheco — RM 569487
* Gabriel Silveira — RM 568910
* Henrique Aragão — RM 570529
* João Vitor Jun — RM 572079

Turma: 1CCPQ

---

## Descrição do Projeto

O ChargeGrid Intelligence é uma prova de conceito desenvolvida para o GoodWe Challenge com o objetivo de demonstrar uma solução para gerenciamento inteligente de estações de recarga de veículos elétricos.

O sistema foi projetado para monitorar a demanda de energia de múltiplos veículos conectados simultaneamente, redistribuindo a potência disponível quando a capacidade da instalação é ultrapassada.

Além disso, a solução apresenta conceitos relacionados à tarifação, interoperabilidade entre equipamentos e previsão de demanda baseada em dados históricos.

---

## Problema

Com o crescimento da mobilidade elétrica, estações de recarga podem enfrentar situações em que a demanda total de energia supera a capacidade disponível da infraestrutura.

Sem um gerenciamento adequado, isso pode causar:

* Sobrecarga da rede elétrica;
* Redução da eficiência operacional;
* Limitações na expansão dos pontos de recarga;
* Aumento dos custos de operação.

---

## Solução Proposta

A solução ChargeGrid Intelligence realiza o gerenciamento inteligente da potência disponível na estação.

Quando a soma das potências solicitadas pelos veículos ultrapassa o limite da instalação, o sistema redistribui automaticamente a energia entre os carregadores, mantendo a operação dentro da capacidade disponível.

Além disso, a plataforma demonstra:

* Controle inteligente de demanda;
* Simulação de tarifação por consumo;
* Integração baseada em protocolos abertos;
* Previsão de demanda utilizando dados históricos.

---

## Funcionalidades

### Controle Inteligente de Demanda

A aplicação monitora a potência solicitada pelos veículos conectados e verifica se a demanda total ultrapassa o limite da instalação.

Caso seja identificada uma situação de sobrecarga, a potência é redistribuída automaticamente entre os veículos.

### Tarifação e Pagamento

O sistema realiza uma simulação de cobrança baseada no consumo de energia e no valor da tarifa configurada pelo usuário.

### Inteligência Artificial

A prova de conceito utiliza um histórico de demanda para gerar uma previsão simples de utilização futura da estação.

### Interoperabilidade

A arquitetura proposta considera a integração entre diferentes componentes utilizando protocolos amplamente utilizados no setor de energia e mobilidade elétrica.

---

## Arquitetura da Solução

```text
Carregadores EV
        │
        ▼
      OCPP
        │
        ▼
ChargeGrid Intelligence
        │
        ▼
     MODBUS
        │
        ▼
Inversores GoodWe
Baterias
Medidores
```

### OCPP

Protocolo utilizado para comunicação entre carregadores e a plataforma de gerenciamento.

### MODBUS

Protocolo utilizado para integração com inversores, medidores e dispositivos de automação.

---

## Tecnologias Utilizadas

* Python
* Streamlit
* Pandas

---

## Estrutura do Projeto

```text
ChargeGrid-Intelligence/

main.py
requirements.txt
README.md
```

---

## Como Executar

### 1. Instalar as dependências

```bash
pip install streamlit pandas
```

### 2. Executar a aplicação

```bash
streamlit run main.py
```

### 3. Acessar no navegador

```text
http://localhost:8501
```

---

## Demonstração

A aplicação permite:

* Configurar a potência solicitada por cada veículo;
* Simular situações de sobrecarga;
* Visualizar a redistribuição automática de potência;
* Calcular valores de cobrança;
* Analisar previsão de demanda;
* Compreender a arquitetura proposta para integração dos equipamentos.

---

## Evolução da Sprint 1

Na Sprint 1 foi realizada a pesquisa e definição conceitual da solução.

Na Sprint 2 a proposta evoluiu para uma prova de conceito funcional, permitindo a demonstração prática do gerenciamento de demanda, da tarifação, da interoperabilidade e da utilização de dados para apoio à tomada de decisão.

---

## Conclusão

O ChargeGrid Intelligence demonstra como técnicas de gerenciamento inteligente podem contribuir para a operação eficiente de estações de recarga de veículos elétricos.

A prova de conceito evidencia a aplicação prática dos conceitos estudados ao longo do desafio, apresentando uma solução escalável e alinhada às necessidades atuais da mobilidade elétrica.
