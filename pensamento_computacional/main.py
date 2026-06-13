import streamlit as st
import pandas as pd

st.set_page_config(page_title="ChargeGrid Intelligence", layout="wide")

st.title("ChargeGrid Intelligence")
st.caption(
    "Sistema inteligente para gerenciamento de recarga de veículos elétricos baseado em controle de demanda, tarifação, interoperabilidade e análise de dados."
)
st.subheader("Sprint 2 - GoodWe Challenge")

st.markdown("""
Prova de conceito de uma plataforma para gerenciamento inteligente de recarga
de veículos elétricos em ambiente comercial.

A solução demonstra:

- Controle inteligente de demanda
- Tarifação de sessões
- Interoperabilidade (OCPP e MODBUS)
- Uso de dados para previsão de demanda
""")

st.divider()

st.header("1. Controle Inteligente de Demanda")

st.write("Simulação de distribuição automática de potência entre veículos conectados.")

limite_total = st.slider(
    "Limite total disponível da instalação (kW)",
    min_value=50,
    max_value=200,
    value=100
)

col1, col2 = st.columns(2)

with col1:
    veiculo_a = st.slider("Veículo A", 0, 50, 40)
    veiculo_b = st.slider("Veículo B", 0, 50, 35)

with col2:
    veiculo_c = st.slider("Veículo C", 0, 50, 30)
    veiculo_d = st.slider("Veículo D", 0, 50, 20)

potencias_solicitadas = [veiculo_a, veiculo_b, veiculo_c, veiculo_d]
veiculos = ["Veículo A", "Veículo B", "Veículo C", "Veículo D"]

demanda_total = sum(potencias_solicitadas)

st.metric("Demanda Total Solicitada", f"{demanda_total} kW")
if demanda_total > limite_total:
    excesso = demanda_total - limite_total

    st.error(
        f"Demanda excedida em {excesso:.1f} kW. Balanceamento necessário."
    )

if demanda_total <= limite_total:
    potencias_distribuidas = potencias_solicitadas.copy()
    st.success("A demanda está dentro da capacidade da instalação.")
else:
    fator = limite_total / demanda_total
    potencias_distribuidas = [round(p * fator, 1) for p in potencias_solicitadas]
    st.warning("Sobrecarga detectada. O sistema redistribuiu automaticamente a potência.")

df = pd.DataFrame({
    "Veículo": veiculos,
    "Potência Solicitada (kW)": potencias_solicitadas,
    "Potência Distribuída (kW)": potencias_distribuidas
})

st.dataframe(df, use_container_width=True)

st.bar_chart(
    df.set_index("Veículo")[
        ["Potência Solicitada (kW)", "Potência Distribuída (kW)"]
    ]
)

utilizacao = round((sum(potencias_distribuidas) / limite_total) * 100, 1)
st.metric("Utilização da Infraestrutura", f"{utilizacao}%")

st.divider()

st.header("2. Tarifação e Pagamento")

tarifa = st.number_input(
    "Tarifa por kWh (R$)",
    min_value=0.10,
    max_value=5.00,
    value=0.90,
    step=0.10
)

veiculo_escolhido = st.selectbox("Selecionar veículo", veiculos)
indice = veiculos.index(veiculo_escolhido)

consumo = potencias_distribuidas[indice]
valor = consumo * tarifa

col3, col4 = st.columns(2)

with col3:
    st.metric("Energia Considerada", f"{consumo:.1f} kWh")

with col4:
    st.metric("Valor Estimado da Sessão", f"R$ {valor:.2f}")

st.info(
    "Em uma implementação real, o valor poderia considerar horário, perfil do usuário, descontos e regras comerciais."
)

st.divider()

st.header("3. Inteligência Artificial")

historico = pd.DataFrame({
    "Dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
    "Demanda (kW)": [62, 70, 68, 75, 80, 85, 78]
})

st.line_chart(historico.set_index("Dia"))

previsao = round(historico["Demanda (kW)"].mean(), 1)

st.metric("Demanda Prevista para o Próximo Dia", f"{previsao} kW")

if previsao >= 80:
    st.warning("Previsão de alta demanda. Recomenda-se preparar a infraestrutura.")
else:
    st.success("Demanda prevista dentro da faixa normal de operação.")

st.divider()

st.header("4. Interoperabilidade")

st.code(
"""Carregadores EV
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
Medidores""",
    language="text"
)

st.info(
    "OCPP é utilizado para comunicação entre carregadores e a plataforma central. MODBUS permite integração com inversores, medidores e dispositivos de automação."
)

st.divider()

st.header("Conclusão")

st.success(
    "A prova de conceito demonstra gerenciamento inteligente de demanda, tarifação, interoperabilidade e uso de dados para apoio à tomada de decisão."
)
