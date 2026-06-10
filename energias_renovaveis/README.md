# GoodCharge AI — Smart EV Charging Optimization

Sistema inteligente de otimização de carregamento para veículos elétricos baseado na disponibilidade de energia solar.

Projeto acadêmico inspirado em soluções de gerenciamento energético aplicadas à mobilidade elétrica sustentável.

---

# Integrantes

* André Felix — RM 571691
* Davi Pacheco — RM 569487
* Gabriel Silveira — RM 568910
* Henrique Aragão — RM 570529
* João Vitor Jun — RM 572079

Turma: 1CCPQ

---

# Sobre o Projeto

O crescimento da mobilidade elétrica traz novos desafios para a infraestrutura energética de empresas, condomínios e estações de carregamento.

O GoodCharge AI foi desenvolvido como uma Prova de Conceito (PoC) capaz de demonstrar como um sistema inteligente pode otimizar o carregamento de veículos elétricos utilizando prioritariamente energia proveniente de fontes renováveis.

A solução monitora a disponibilidade de energia solar simulada e ajusta automaticamente o modo de carregamento dos veículos de acordo com a geração disponível.

Dessa forma, o sistema contribui para:

* maior aproveitamento da energia solar;
* redução do consumo da rede elétrica convencional;
* aumento da eficiência energética;
* redução de desperdícios;
* incentivo à mobilidade sustentável.

---

# Objetivo

Desenvolver um protótipo funcional capaz de demonstrar a viabilidade técnica de um sistema inteligente de gerenciamento de carregamento para veículos elétricos baseado na disponibilidade de energia renovável.

A proposta busca:

* maximizar o uso de energia solar;
* reduzir a dependência da rede elétrica;
* evitar desperdícios energéticos;
* aplicar conceitos de Smart Grid;
* demonstrar automação voltada à sustentabilidade.

---

# Problema Proposto

Em sistemas convencionais, os veículos elétricos podem ser carregados sem considerar a disponibilidade de geração renovável.

Como consequência:

* ocorre maior dependência da rede elétrica;
* aumentam os custos energéticos;
* há menor aproveitamento da energia solar produzida localmente.

O GoodCharge AI propõe uma estratégia de carregamento adaptativo, utilizando a disponibilidade de energia solar como critério para definir a potência de carregamento.

---

# Conceito da Solução

O sistema simula uma estação de carregamento de veículos elétricos instalada em um prédio comercial equipado com painéis solares.

A geração solar é representada por um sensor LDR que detecta diferentes níveis de luminosidade.

O Arduino realiza a leitura do sensor e determina automaticamente o modo de carregamento adequado.

A condição operacional é representada por LEDs que indicam visualmente o estado do sistema.

---

# Arquitetura do Sistema

```text
Painel Solar (Simulado)
           │
           ▼
      Sensor LDR
           │
           ▼
     Arduino Uno
           │
           ▼
Sistema de Decisão Inteligente
           │
           ▼
Controle do Carregamento EV
           │
           ▼
 LEDs Indicadores de Status
```

---

# Fluxo de Funcionamento

```text
Início
   │
   ▼
Leitura do Sensor LDR
   │
   ▼
Valor > 900 ?
   │
 ┌─Sim────────────────────┐
 │                        │
 ▼                        │
Modo Carregamento Máximo  │
LED Verde                 │
 │                        │
 └────────────────────────┘

Não
 │
 ▼
Valor > 200 ?
 │
 ┌─Sim────────────────────┐
 │                        │
 ▼                        │
Modo Econômico            │
LED Amarelo               │
 │                        │
 └────────────────────────┘

Não
 │
 ▼
Modo Reduzido
LED Vermelho
 │
 ▼
Repetir Processo
```

---

# Componentes Utilizados

| Componente  | Função                                  |
| ----------- | --------------------------------------- |
| Arduino Uno | Controle principal do sistema           |
| Sensor LDR  | Simulação da geração solar              |
| LEDs        | Indicação visual dos estados do sistema |
| Resistores  | Proteção e controle elétrico            |
| Protoboard  | Montagem do circuito                    |
| Tinkercad   | Simulação virtual do protótipo          |

---

# Justificativa Técnica

## Arduino Uno

Foi escolhido por ser uma plataforma de baixo custo, amplamente utilizada em sistemas embarcados e adequada para aplicações de automação e monitoramento.

## Sensor LDR

Representa a disponibilidade de energia solar por meio da intensidade luminosa incidente, permitindo simular diferentes cenários de geração fotovoltaica.

## LEDs Indicadores

Facilitam a visualização do estado operacional do sistema e representam os diferentes modos de carregamento do veículo elétrico.

## Simulação em Tinkercad

Permite validar a lógica do projeto sem a necessidade de equipamentos físicos, reduzindo custos e acelerando o desenvolvimento da Prova de Conceito.

---

# Lógica de Funcionamento

A tomada de decisão é baseada na leitura analógica do sensor LDR.

## Regras de Decisão

```cpp
Se valorLuz > 900
    Carregamento Máximo

Se valorLuz > 200
    Carregamento Econômico

Caso contrário
    Carregamento Reduzido
```

---

# Modos de Operação

| LED         | Disponibilidade Solar | Modo de Carregamento |
| ----------- | --------------------- | -------------------- |
| 🟢 Verde    | Alta                  | Máximo               |
| 🟡 Amarelo  | Moderada              | Econômico            |
| 🔴 Vermelho | Baixa                 | Reduzido             |

---

# Dados Gerados pela Simulação

Durante os testes realizados no Tinkercad foram observados os seguintes comportamentos:

| Leitura LDR | Disponibilidade Solar | Estado   | Potência Simulada |
| ----------- | --------------------- | -------- | ----------------- |
| 980         | Alta                  | Verde    | 100%              |
| 920         | Alta                  | Verde    | 100%              |
| 700         | Moderada              | Amarelo  | 60%               |
| 500         | Moderada              | Amarelo  | 60%               |
| 180         | Baixa                 | Vermelho | 20%               |
| 100         | Baixa                 | Vermelho | 20%               |

Os dados demonstram que o sistema é capaz de adaptar automaticamente o modo de carregamento conforme a disponibilidade energética simulada.

---

# Código Principal

```cpp
int ldr = A0;

int ledVerde = 7;
int ledAmarelo = 5;
int ledVermelho = 6;

void setup() {

  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  int valorLuz = analogRead(ldr);

  Serial.println(valorLuz);

  if (valorLuz > 900) {

    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVermelho, LOW);

  }

  else if (valorLuz > 200) {

    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarelo, HIGH);
    digitalWrite(ledVermelho, LOW);

  }

  else {

    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarelo, LOW);
    digitalWrite(ledVermelho, HIGH);

  }

  delay(500);
}
```

---

# Relação com Smart Grids

O projeto aplica conceitos fundamentais de Smart Grid ao ajustar dinamicamente o consumo energético de acordo com a disponibilidade de geração renovável.

Em um cenário real, essa estratégia permite:

* reduzir picos de demanda;
* otimizar recursos energéticos;
* aumentar a eficiência operacional;
* melhorar a integração entre geração e consumo.

---

# Sustentabilidade Aplicada

O GoodCharge AI está diretamente relacionado aos princípios de sustentabilidade estudados durante o semestre.

A solução:

* prioriza o uso de energia renovável;
* reduz desperdícios energéticos;
* diminui a dependência da rede elétrica;
* incentiva a mobilidade elétrica sustentável;
* contribui para uma gestão energética mais eficiente.

---

# Resultados Obtidos

A Prova de Conceito demonstrou com sucesso:

* monitoramento da disponibilidade energética simulada;
* tomada de decisão automatizada;
* alteração dinâmica dos modos de carregamento;
* aplicação prática de conceitos de energia renovável;
* viabilidade técnica inicial da solução.

---

# Tecnologias Utilizadas

* Arduino IDE
* Linguagem C++
* Tinkercad
* Arduino Uno
* Sistemas Embarcados
* Smart Grid
* Eficiência Energética
* Mobilidade Elétrica

---

# Demonstração

## Vídeo do Projeto

[LINK]

## Projeto Tinkercad

https://www.tinkercad.com/things/fz1yFlzDWq7-sprint-2-goodcharge-ai/editel?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard%2Fdesigns%2Fcircuits&sharecode=15kn7KNMOgplobzf-iAMaGiyH4WtySW56uzaWSSIk9I

---

# Repositório

https://github.com/junnishiye/chargegrid_sprint2/tree/main/energias_renovaveis

---

# Conclusão

O GoodCharge AI demonstrou a viabilidade técnica de um sistema inteligente de gerenciamento de carregamento para veículos elétricos baseado na disponibilidade de energia solar.

A Prova de Conceito comprova que estratégias de carregamento adaptativo podem contribuir para uma utilização mais eficiente dos recursos energéticos, incentivando o uso de fontes renováveis e promovendo maior sustentabilidade no contexto da mobilidade elétrica.

Como evolução futura, o sistema poderá integrar sensores reais de geração fotovoltaica, medidores de potência e algoritmos de otimização mais avançados para aplicações em ambientes corporativos e residenciais.
