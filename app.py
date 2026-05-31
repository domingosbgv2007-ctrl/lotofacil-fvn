# ============================================
# DENTRO DA ABA "CONFERIR RESULTADOS"
# Substitua a parte de seleção das dezenas
# ============================================

st.markdown("### 🎯 Selecione as 15 dezenas sorteadas")

# Layout em grid 5x5
st.markdown("""
<style>
    .numero-grid {
        display: inline-block;
        width: 60px;
        text-align: center;
        margin: 5px;
    }
    .linha-numeros {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Lista para armazenar dezenas selecionadas
dezenas_resultado = []

# Linha 1: 01 a 05
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.checkbox("01", key="conf_01"):
        dezenas_resultado.append(1)
with col2:
    if st.checkbox("02", key="conf_02"):
        dezenas_resultado.append(2)
with col3:
    if st.checkbox("03", key="conf_03"):
        dezenas_resultado.append(3)
with col4:
    if st.checkbox("04", key="conf_04"):
        dezenas_resultado.append(4)
with col5:
    if st.checkbox("05", key="conf_05"):
        dezenas_resultado.append(5)

# Linha 2: 06 a 10
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.checkbox("06", key="conf_06"):
        dezenas_resultado.append(6)
with col2:
    if st.checkbox("07", key="conf_07"):
        dezenas_resultado.append(7)
with col3:
    if st.checkbox("08", key="conf_08"):
        dezenas_resultado.append(8)
with col4:
    if st.checkbox("09", key="conf_09"):
        dezenas_resultado.append(9)
with col5:
    if st.checkbox("10", key="conf_10"):
        dezenas_resultado.append(10)

# Linha 3: 11 a 15
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.checkbox("11", key="conf_11"):
        dezenas_resultado.append(11)
with col2:
    if st.checkbox("12", key="conf_12"):
        dezenas_resultado.append(12)
with col3:
    if st.checkbox("13", key="conf_13"):
        dezenas_resultado.append(13)
with col4:
    if st.checkbox("14", key="conf_14"):
        dezenas_resultado.append(14)
with col5:
    if st.checkbox("15", key="conf_15"):
        dezenas_resultado.append(15)

# Linha 4: 16 a 20
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.checkbox("16", key="conf_16"):
        dezenas_resultado.append(16)
with col2:
    if st.checkbox("17", key="conf_17"):
        dezenas_resultado.append(17)
with col3:
    if st.checkbox("18", key="conf_18"):
        dezenas_resultado.append(18)
with col4:
    if st.checkbox("19", key="conf_19"):
        dezenas_resultado.append(19)
with col5:
    if st.checkbox("20", key="conf_20"):
        dezenas_resultado.append(20)

# Linha 5: 21 a 25
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.checkbox("21", key="conf_21"):
        dezenas_resultado.append(21)
with col2:
    if st.checkbox("22", key="conf_22"):
        dezenas_resultado.append(22)
with col3:
    if st.checkbox("23", key="conf_23"):
        dezenas_resultado.append(23)
with col4:
    if st.checkbox("24", key="conf_24"):
        dezenas_resultado.append(24)
with col5:
    if st.checkbox("25", key="conf_25"):
        dezenas_resultado.append(25)
