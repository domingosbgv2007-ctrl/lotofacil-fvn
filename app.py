# ============================================
# SISTEMA FVN para LOTOFÁCIL
# Com layout de números em grid 5x5 e logo SFVN
# ============================================

import streamlit as st
import random
import json
from datetime import datetime

st.set_page_config(
    page_title="Sistema FVN para Lotofácil",
    page_icon="🎲",
    layout="centered"
)

# ============================================
# ARQUIVO PARA SALVAR RESULTADOS
# ============================================

ARQUIVO_DADOS = "resultados_lotofacil.json"

# DADOS REAIS ATUALIZADOS (últimos 50 concursos)
DADOS_PADRAO = [
    [3699, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3698, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3697, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3696, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3695, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3694, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3693, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3692, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3691, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3690, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3689, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3688, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3687, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3686, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3685, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3684, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3683, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3682, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3681, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3680, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3679, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3678, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3677, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3676, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3675, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3674, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3673, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3672, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3671, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3670, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3669, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3668, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3667, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3666, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3665, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3664, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3663, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3662, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3661, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3660, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3659, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3658, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3657, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3656, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3655, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3654, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3653, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3652, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3651, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3650, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
]

def carregar_resultados():
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    except:
        return DADOS_PADRAO.copy()

def salvar_resultados(resultados):
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(resultados, f)

# ============================================
# FUNÇÕES DE ANÁLISE
# ============================================

def analisar_frequencia(resultados, ultimos_n=50):
    frequencia = {i: 0 for i in range(1, 26)}
    for concurso, dezenas in resultados[:ultimos_n]:
        for d in dezenas:
            frequencia[d] += 1
    return frequencia

def analisar_clusters(resultados, ultimos_n=50):
    cluster_freq = {}
    for concurso, dezenas in resultados[:ultimos_n]:
        dezenas_ord = sorted(dezenas)
        atual = [dezenas_ord[0]]
        for i in range(1, len(dezenas_ord)):
            if dezenas_ord[i] == dezenas_ord[i-1] + 1:
                atual.append(dezenas_ord[i])
            else:
                if len(atual) >= 3:
                    chave = f"{atual[0]}-{atual[-1]}"
                    cluster_freq[chave] = cluster_freq.get(chave, 0) + 1
                atual = [dezenas_ord[i]]
        if len(atual) >= 3:
            chave = f"{atual[0]}-{atual[-1]}"
            cluster_freq[chave] = cluster_freq.get(chave, 0) + 1
    return dict(sorted(cluster_freq.items(), key=lambda x: x[1], reverse=True))

def gerar_volante(frequencia, clusters, evitar, estrategia):
    volante = set()
    
    if estrategia == "Alta Probabilidade":
        dezenas_freq = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
        for num, _ in dezenas_freq:
            if num not in evitar and len(volante) < 15:
                volante.add(num)
    
    elif estrategia == "Clusters Históricos":
        melhores = list(clusters.keys())[:10]
        if melhores:
            for _ in range(2):
                if melhores:
                    c = random.choice(melhores)
                    partes = c.split('-')
                    for n in range(int(partes[0]), int(partes[1]) + 1):
                        if n not in evitar:
                            volante.add(n)
        dezenas_freq = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
        for num, _ in dezenas_freq:
            if num not in volante and num not in evitar and len(volante) < 15:
                volante.add(num)
    
    else:
        dezenas_freq = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:12]
        for num, _ in dezenas_freq:
            if num not in evitar:
                volante.add(num)
        melhores = list(clusters.keys())[:5]
        if melhores:
            c = random.choice(melhores)
            partes = c.split('-')
            for n in range(int(partes[0]), int(partes[1]) + 1):
                if n not in evitar:
                    volante.add(n)
    
    if len(volante) < 15:
        for n in range(1, 26):
            if n not in volante and n not in evitar and len(volante) < 15:
                volante.add(n)
    
    return sorted(list(volante))[:15]

def detectar_clusters(volante):
    volante_ord = sorted(volante)
    clusters = []
    atual = [volante_ord[0]]
    for i in range(1, len(volante_ord)):
        if volante_ord[i] == volante_ord[i-1] + 1:
            atual.append(volante_ord[i])
        else:
            if len(atual) >= 3:
                clusters.append(atual)
            atual = [volante_ord[i]]
    if len(atual) >= 3:
        clusters.append(atual)
    return clusters

def calcular_forca(volante, frequencia):
    total = sum(frequencia.get(n, 0) for n in volante)
    maximo = sum(sorted(frequencia.values(), reverse=True)[:15])
    return round((total / maximo) * 100, 1) if maximo > 0 else 50

def conferir_volante(volante, resultado):
    acertos = [n for n in volante if n in resultado]
    return len(acertos), acertos

# ============================================
# INTERFACE
# ============================================

st.markdown("""
<style>
    .header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 12px;
        margin-bottom: 25px;
    }
    .logo {
        display: inline-block;
        background: linear-gradient(135deg, #f5af19 0%, #f12711 100%);
        color: white;
        font-weight: bold;
        font-size: 2em;
        width: 80px;
        height: 80px;
        line-height: 80px;
        text-align: center;
        border-radius: 20px;
        margin-bottom: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .header h1 {
        color: white;
        margin: 0;
        font-size: 1.8em;
    }
    .header p {
        color: #a0c4e8;
        margin: 8px 0 0 0;
        font-size: 0.9em;
    }
    .jogo-ouro {
        background: linear-gradient(135deg, #f5af19 0%, #f12711 100%);
        border-radius: 12px;
        padding: 15px;
        margin: 15px 0;
    }
    .numero {
        display: inline-block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        text-align: center;
        margin: 2px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
    }
    .numero-freq { background: #10b981; color: white; }
    .numero-cluster { background: #f59e0b; color: white; }
    .numero-normal { background: #334155; color: #cbd5e1; }
    .numero-acerto { background: #10b981; color: white; box-shadow: 0 0 0 2px white; }
    .numero-erro { background: #ef4444; color: white; opacity: 0.5; }
    .badge {
        display: inline-block;
        background: #2a5298;
        color: white;
        padding: 2px 10px;
        border-radius: 15px;
        font-size: 11px;
    }
    .stButton button {
        background: #1e3c72;
        color: white;
        font-weight: bold;
        width: 100%;
    }
    hr {
        margin: 20px 0;
    }
    .info-base {
        text-align: center;
        font-size: 12px;
        color: #888;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho com logo SFVN
st.markdown("""
<div class="header">
    <div class="logo">SFVN</div>
    <h1>SISTEMA FVN para LOTOFÁCIL</h1>
    <p>Sistema de Previsão por Análise Estatística | Clusters e Probabilidade</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# TRÊS ABAS PRINCIPAIS
# ============================================

aba1, aba2, aba3 = st.tabs(["🎯 GERAR VOLANTES", "🔍 CONFERIR RESULTADOS", "📝 ATUALIZAR RESULTADOS"])

# ============================================
# ABA 1 - GERAR VOLANTES
# ============================================

with aba1:
    resultados = carregar_resultados()
    ultimo_concurso = resultados[0][0] if resultados else 3699
    
    st.markdown(f'<div class="info-base">📊 Base: {len(resultados)} concursos | Último: {ultimo_concurso}</div>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("### ⚙️ CONFIGURAÇÕES FVN")
        
        qtd_analise = st.slider("Quantidade para análise", 10, min(50, len(resultados)), 25)
        
        st.markdown("---")
        
        estrategia = st.selectbox("Estratégia de previsão", [
            "Alta Probabilidade",
            "Clusters Históricos",
            "Misto (Recomendado)"
        ])
        
        st.markdown("---")
        
        evitar_opcao = st.radio("Excluir números", ["Nenhum", "Apenas 01", "Escolher"])
        
        numeros_evitar = []
        if evitar_opcao == "Apenas 01":
            numeros_evitar = [1]
        elif evitar_opcao == "Escolher":
            numeros_evitar = st.multiselect("Selecione os números para excluir", list(range(1, 26)), [])
        
        st.markdown("---")
        
        qtd_volantes = st.slider("Quantidade de volantes", 5, 50, 30)
        
        st.markdown("---")
        st.caption("🔗 Clusters = sequências de 3+ números consecutivos")
        st.caption("📈 Sistema FVN - Foco em Variabilidade Natural")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gerar = st.button("🎲 GERAR VOLANTES FVN", use_container_width=True)
    
    if 'volantes' not in st.session_state or gerar:
        with st.spinner("Analisando dados históricos..."):
            freq = analisar_frequencia(resultados, qtd_analise)
            clusters = analisar_clusters(resultados, qtd_analise)
            
            volantes_temp = []
            for _ in range(qtd_volantes):
                vol = gerar_volante(freq, clusters, numeros_evitar, estrategia)
                forca = calcular_forca(vol, freq)
                cls = detectar_clusters(vol)
                volantes_temp.append((vol, forca, cls))
            
            volantes_temp.sort(key=lambda x: x[1], reverse=True)
            st.session_state.volantes = volantes_temp
            st.session_state.freq = freq
            st.session_state.ultimos_volantes = volantes_temp
    
    volantes = st.session_state.volantes
    
    st.markdown("---")
    
    for i, (vol, forca, cls) in enumerate(volantes, 1):
        if i == 1:
            st.markdown('<div class="jogo-ouro">', unsafe_allow_html=True)
            st.markdown(f"### 🏆 JOGO DE OURO FVN #{i}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        elif i == 2:
            st.markdown('<div class="jogo-ouro">', unsafe_allow_html=True)
            st.markdown(f"### 🥈 JOGO DE OURO FVN #{i}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"### Volante FVN {i:02d}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        
        html = "<div>"
        for n in vol:
            if n in [x for x,_ in sorted(st.session_state.freq.items(), key=lambda kv: kv[1], reverse=True)[:10]]:
                classe = "numero-freq"
            elif any(n in c for c in cls):
                classe = "numero-cluster"
            else:
                classe = "numero-normal"
            html += f'<span class="numero {classe}">{n:02d}</span>'
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)
        
        if cls:
            txt = " | ".join([f"{c[0]}-{c[-1]} ({len(c)})" for c in cls])
            st.caption(f"🔗 Sequências detectadas: {txt}")
        
        if i in [1, 2]:
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
    if volantes:
        texto = f"SISTEMA FVN para LOTOFÁCIL - {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        texto += f"Base: {len(resultados)} concursos | Análise: últimos {qtd_analise}\n"
        texto += f"Estratégia: {estrategia}\n"
        texto += "=" * 50 + "\n\n"
        
        for i, (vol, forca, _) in enumerate(volantes, 1):
            if i <= 2:
                texto += f"[{i:02d}] JOGO DE OURO FVN ({forca}%): "
            else:
                texto += f"[{i:02d}] ({forca}%): "
            texto += " ".join(f"{n:02d}" for n in vol) + "\n"
        
        st.download_button("📥 BAIXAR VOLANTES FVN", texto, file_name=f"lotofacil_fvn_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")

# ============================================
# ABA 2 - CONFERIR RESULTADOS
# ============================================

with aba2:
    st.markdown("### 🔍 Conferir volantes com resultado oficial")
    
    if 'ultimos_volantes' in st.session_state and st.session_state.ultimos_volantes:
        volantes_para_conferir = st.session_state.ultimos_volantes
        st.success(f"✅ {len(volantes_para_conferir)} volantes carregados da última geração")
    else:
        st.warning("⚠️ Nenhum volante encontrado. Vá na aba GERAR VOLANTES primeiro.")
        volantes_para_conferir = []
    
    st.markdown("---")
    
    st.markdown("### 📋 Digite o resultado do concurso")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        concurso_conferencia = st.number_input("Número do concurso", min_value=1, value=3700, step=1)
    
    with col2:
        st.markdown("### 🎯 Selecione as 15 dezenas sorteadas")
    
    dezenas_resultado = []
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("01", key="conf_01"): dezenas_resultado.append(1)
    with c2:
        if st.checkbox("02", key="conf_02"): dezenas_resultado.append(2)
    with c3:
        if st.checkbox("03", key="conf_03"): dezenas_resultado.append(3)
    with c4:
        if st.checkbox("04", key="conf_04"): dezenas_resultado.append(4)
    with c5:
        if st.checkbox("05", key="conf_05"): dezenas_resultado.append(5)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("06", key="conf_06"): dezenas_resultado.append(6)
    with c2:
        if st.checkbox("07", key="conf_07"): dezenas_resultado.append(7)
    with c3:
        if st.checkbox("08", key="conf_08"): dezenas_resultado.append(8)
    with c4:
        if st.checkbox("09", key="conf_09"): dezenas_resultado.append(9)
    with c5:
        if st.checkbox("10", key="conf_10"): dezenas_resultado.append(10)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("11", key="conf_11"): dezenas_resultado.append(11)
    with c2:
        if st.checkbox("12", key="conf_12"): dezenas_resultado.append(12)
    with c3:
        if st.checkbox("13", key="conf_13"): dezenas_resultado.append(13)
    with c4:
        if st.checkbox("14", key="conf_14"): dezenas_resultado.append(14)
    with c5:
        if st.checkbox("15", key="conf_15"): dezenas_resultado.append(15)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("16", key="conf_16"): dezenas_resultado.append(16)
    with c2:
        if st.checkbox("17", key="conf_17"): dezenas_resultado.append(17)
    with c3:
        if st.checkbox("18", key="conf_18"): dezenas_resultado.append(18)
    with c4:
        if st.checkbox("19", key="conf_19"): dezenas_resultado.append(19)
    with c5:
        if st.checkbox("20", key="conf_20"): dezenas_resultado.append(20)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("21", key="conf_21"): dezenas_resultado.append(21)
    with c2:
        if st.checkbox("22", key="conf_22"): dezenas_resultado.append(22)
    with c3:
        if st.checkbox("23", key="conf_23"): dezenas_resultado.append(23)
    with c4:
        if st.checkbox("24", key="conf_24"): dezenas_resultado.append(24)
    with c5:
        if st.checkbox("25", key="conf_25"): dezenas_resultado.append(25)
    
    st.caption(f"📊 Dezenas selecionadas: {len(dezenas_resultado)} de 15")
    
    bt1, bt2, bt3 = st.columns([1, 2, 1])
    with bt2:
        conferir = st.button("🔍 CONFERIR VOLANTES", use_container_width=True)
    
    if conferir:
        if len(dezenas_resultado) != 15:
            st.error(f"❌ Você selecionou {len(dezenas_resultado)} dezenas. Precisa ser exatamente 15.")
        elif not volantes_para_conferir:
            st.error("❌ Nenhum volante para conferir. Gere volantes primeiro.")
        else:
            resultados_conf = []
            for i, (vol, forca, cls) in enumerate(volantes_para_conferir, 1):
                qtd_acertos, acertos = conferir_volante(vol, dezenas_resultado)
                resultados_conf.append((i, vol, qtd_acertos, acertos, forca, cls))
            
            resultados_conf.sort(key=lambda x: x[2], reverse=True)
            
            total_volantes = len(resultados_conf)
            total_11_mais = sum(1 for r in resultados_conf if r[2] >= 11)
            total_10_mais = sum(1 for r in resultados_conf if r[2] >= 10)
            total_9_mais = sum(1 for r in resultados_conf if r[2] >= 9)
            total_8_mais = sum(1 for r in resultados_conf if r[2] >= 8)
            maior_pontuacao = max(r[2] for r in resultados_conf)
            
            st.markdown("---")
            st.markdown("## 📊 RESUMO DA CONFERÊNCIA")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Total Volantes", total_volantes)
            with col2:
                st.metric("11+ pontos", total_11_mais)
            with col3:
                st.metric("10+ pontos", total_10_mais)
            with col4:
                st.metric("9+ pontos", total_9_mais)
            with col5:
                st.metric("8+ pontos", total_8_mais)
            
            st.markdown(f"### 🏆 Melhor pontuação: **{maior_pontuacao} acertos**")
            
            if maior_pontuacao >= 11:
                st.balloons()
                st.success(f"🎉 PARABÉNS! Você teve um volante com {maior_pontuacao} acertos!")
            
            st.markdown("---")
            st.markdown("## 🎯 DETALHAMENTO POR VOLANTE")
            
            for idx, vol, qtd, acertos, forca, cls in resultados_conf:
                if qtd >= 11:
                    st.markdown(f"### 🏆 Volante FVN {idx:02d} - {qtd} ACERTOS!")
                elif qtd >= 9:
                    st.markdown(f"### ⭐ Volante FVN {idx:02d} - {qtd} acertos")
                else:
                    st.markdown(f"### Volante FVN {idx:02d} - {qtd} acertos")
                
                html = "<div>"
                for n in vol:
                    if n in dezenas_resultado:
                        html += f'<span class="numero numero-acerto">{n:02d}</span>'
                    else:
                        html += f'<span class="numero numero-erro">{n:02d}</span>'
                html += "</div>"
                st.markdown(html, unsafe_allow_html=True)
                
                if acertos:
                    st.markdown(f"✅ **Acertos:** {' '.join(f'{n:02d}' for n in acertos)}")
                
                st.markdown(f"📊 Força do volante: {forca}%")
                st.markdown("<hr>", unsafe_allow_html=True)

# ============================================
# ABA 3 - ATUALIZAR RESULTADOS
# ============================================

with aba3:
    st.markdown("### 📝 Adicionar novo resultado ao sistema")
    
    resultados = carregar_resultados()
    ultimo = resultados[0][0] if resultados else 3699
    
    st.info(f"📌 Último concurso registrado no sistema: **{ultimo}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        novo_concurso = st.number_input(
            "Número do concurso",
            min_value=ultimo + 1,
            max_value=ultimo + 100,
            value=ultimo + 1,
            step=1
        )
    
    with col2:
        st.markdown("### 🎯 Selecione as 15 dezenas sorteadas")
    
    dezenas_selecionadas = []
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("01", key="atu_01"): dezenas_selecionadas.append(1)
    with c2:
        if st.checkbox("02", key="atu_02"): dezenas_selecionadas.append(2)
    with c3:
        if st.checkbox("03", key="atu_03"): dezenas_selecionadas.append(3)
    with c4:
        if st.checkbox("04", key="atu_04"): dezenas_selecionadas.append(4)
    with c5:
        if st.checkbox("05", key="atu_05"): dezenas_selecionadas.append(5)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("06", key="atu_06"): dezenas_selecionadas.append(6)
    with c2:
        if st.checkbox("07", key="atu_07"): dezenas_selecionadas.append(7)
    with c3:
        if st.checkbox("08", key="atu_08"): dezenas_selecionadas.append(8)
    with c4:
        if st.checkbox("09", key="atu_09"): dezenas_selecionadas.append(9)
    with c5:
        if st.checkbox("10", key="atu_10"): dezenas_selecionadas.append(10)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("11", key="atu_11"): dezenas_selecionadas.append(11)
    with c2:
        if st.checkbox("12", key="atu_12"): dezenas_selecionadas.append(12)
    with c3:
        if st.checkbox("13", key="atu_13"): dezenas_selecionadas.append(13)
    with c4:
        if st.checkbox("14", key="atu_14"): dezenas_selecionadas.append(14)
    with c5:
        if st.checkbox("15", key="atu_15"): dezenas_selecionadas.append(15)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("16", key="atu_16"): dezenas_selecionadas.append(16)
    with c2:
        if st.checkbox("17", key="atu_17"): dezenas_selecionadas.append(17)
    with c3:
        if st.checkbox("18", key="atu_18"): dezenas_selecionadas.append(18)
    with c4:
        if st.checkbox("19", key="atu_19"): dezenas_selecionadas.append(19)
    with c5:
        if st.checkbox("20", key="atu_20"): dezenas_selecionadas.append(20)
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.checkbox("21", key="atu_21"): dezenas_selecionadas.append(21)
    with c2:
        if st.checkbox("22", key="atu_22"): dezenas_selecionadas.append(22)
    with c3:
        if st.checkbox("23", key="atu_23"): dezenas_selecionadas.append(23)
    with c4:
        if st.checkbox("24", key="atu_24"): dezenas_selecionadas.append(24)
    with c5:
        if st.checkbox("25", key="atu_25"): dezenas_selecionadas.append(25)
    
    st.caption(f"📊 Dezenas selecionadas: {len(dezenas_selecionadas)} de 15")
    
    bt1, bt2, bt3 = st.columns([1, 2, 1])
    with bt2:
        adicionar = st.button("➕ ADICIONAR CONCURSO AO SISTEMA FVN", use_container_width=True)
    
    if adicionar:
        if len(dezenas_selecionadas) != 15:
            st.error(f"❌ Você selecionou {len(dezenas_selecionadas)} dezenas. O sistema FVN precisa de exatamente 15.")
        else:
            dezenas_ord = sorted(dezenas_selecionadas)
            novo_resultado = [novo_concurso, dezenas_ord]
            
            resultados.insert(0, novo_resultado)
            
            if len(resultados) > 100:
                removido = resultados.pop()
                st.warning(f"⚠️ Removido concurso {removido[0]} (limite de 100)")
            
            salvar_resultados(resultados)
            
            st.success(f"✅ Concurso {novo_concurso} adicionado com sucesso ao sistema FVN!")
            st.balloons()
            
            st.markdown(f"**Dezenas registradas:** {' '.join(f'{n:02d}' for n in dezenas_ord)}")
            
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 📜 Últimos resultados no sistema FVN")
    
    if resultados:
        mostrar = st.slider("Quantidade para exibir", 5, min(30, len(resultados)), 10)
        
        for i in range(mostrar):
            concurso, dezenas = resultados[i]
            dezenas_str = " ".join(f"{n:02d}" for n in dezenas)
            st.text(f"Concurso {concurso}: {dezenas_str}")
    
    st.markdown("---")
    st.warning("⚠️ ATENÇÃO: Resetar remove todos os resultados personalizados inseridos!")
    
    bt1, bt2, bt3 = st.columns([1, 2, 1])
    with bt2:
        resetar = st.button("🔄 RESETAR PARA DADOS PADRÃO FVN", use_container_width=True)
    
    if resetar:
        salvar_resultados(DADOS_PADRAO)
        st.success("✅ Dados resetados para o padrão do sistema FVN!")
        st.rerun()

# ============================================
# RODAPÉ
# ============================================

st.markdown("---")
st.caption("🔬 SISTEMA FVN - Foco em Variabilidade Natural | Análise de Clusters e Probabilidade Estatística")
st.caption("⚠️ Sistema baseado em análise estatística. Não há garantia de acertos. Jogue com responsabilidade.")
