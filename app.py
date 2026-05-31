# ============================================
# LOTOFÁCIL - SISTEMA DE PREVISÃO
# Com atualização manual de resultados
# ============================================

import streamlit as st
import random
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Lotofácil - Sistema de Previsão",
    page_icon="🎲",
    layout="centered"
)

# ============================================
# ARQUIVO PARA SALVAR RESULTADOS
# ============================================

ARQUIVO_DADOS = "resultados_lotofacil.json"

# Dados padrão (50 concursos iniciais)
DADOS_PADRAO = [
    [3250, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3251, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3252, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3253, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3254, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3255, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3256, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3257, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3258, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3259, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3260, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3261, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3262, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3263, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3264, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3265, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3266, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3267, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3268, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3269, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3270, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3271, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3272, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3273, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3274, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3275, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3276, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3277, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3278, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3279, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3280, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3281, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3282, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3283, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3284, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3285, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3286, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3287, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3288, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3289, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3290, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
    [3291, [2,4,6,8,10,12,14,16,18,20,22,24,1,3,5]],
    [3292, [5,6,7,8,9,10,15,16,17,18,19,20,21,22,23]],
    [3293, [1,3,5,7,9,11,13,15,17,19,21,23,25,2,4]],
    [3294, [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]],
    [3295, [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]],
    [3296, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]],
    [3297, [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]],
    [3298, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]],
    [3299, [15,16,17,18,19,20,21,22,23,24,25,1,2,3,4]],
    [3300, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]],
]

def carregar_resultados():
    """Carrega resultados do arquivo ou usa padrão"""
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    except:
        return DADOS_PADRAO.copy()

def salvar_resultados(resultados):
    """Salva resultados no arquivo"""
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(resultados, f)

# ============================================
# FUNÇÕES DE ANÁLISE
# ============================================

def analisar_frequencia(resultados, ultimos_n=50):
    """Analisa frequência das dezenas"""
    frequencia = {i: 0 for i in range(1, 26)}
    for concurso, dezenas in resultados[:ultimos_n]:
        for d in dezenas:
            frequencia[d] += 1
    return frequencia

def analisar_clusters(resultados, ultimos_n=50):
    """Identifica clusters que mais apareceram"""
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
    """Gera volante baseado na estratégia escolhida"""
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
    """Detecta sequências de 3+ números"""
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
    """Calcula força do volante (0-100)"""
    total = sum(frequencia.get(n, 0) for n in volante)
    maximo = sum(sorted(frequencia.values(), reverse=True)[:15])
    return round((total / maximo) * 100, 1) if maximo > 0 else 50

# ============================================
# INTERFACE
# ============================================

st.markdown("""
<style>
    .header {
        text-align: center;
        padding: 20px;
        background: #1e3c72;
        border-radius: 12px;
        margin-bottom: 25px;
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
    .volante {
        background: #1e1e2e;
        border-radius: 10px;
        padding: 12px;
        margin: 8px 0;
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
    .badge {
        display: inline-block;
        background: #2a5298;
        color: white;
        padding: 2px 10px;
        border-radius: 15px;
        font-size: 11px;
    }
    .success {
        background: #10b981;
        color: white;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
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
    .tab {
        padding: 10px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("""
<div class="header">
    <h1>🎲 LOTOFÁCIL</h1>
    <p>Sistema de Previsão por Análise Estatística</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# ABAS PRINCIPAIS
# ============================================

aba1, aba2 = st.tabs(["🎯 GERAR VOLANTES", "📝 ATUALIZAR RESULTADOS"])

# ============================================
# ABA 1 - GERAR VOLANTES
# ============================================

with aba1:
    # Carregar dados atuais
    resultados = carregar_resultados()
    ultimo_concurso = resultados[0][0] if resultados else 3300
    
    st.caption(f"📊 Base de dados: {len(resultados)} concursos | Último: {ultimo_concurso}")
    
    with st.sidebar:
        st.markdown("### ⚙️ Configurar")
        
        qtd_analise = st.slider("Análise (últimos concursos)", 10, min(50, len(resultados)), 25)
        
        st.markdown("---")
        
        estrategia = st.selectbox("Estratégia", [
            "Alta Probabilidade",
            "Clusters Históricos",
            "Misto"
        ])
        
        st.markdown("---")
        
        evitar_opcao = st.radio("Excluir números", ["Nenhum", "Apenas 01", "Escolher"])
        
        numeros_evitar = []
        if evitar_opcao == "Apenas 01":
            numeros_evitar = [1]
        elif evitar_opcao == "Escolher":
            numeros_evitar = st.multiselect("Selecione", list(range(1, 26)), [])
        
        st.markdown("---")
        
        qtd_volantes = st.slider("Quantidade", 5, 50, 30)
        
        st.markdown("---")
        st.caption("Clusters = sequências de 3+ números")
    
    # Botão gerar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        gerar = st.button("🎲 GERAR VOLANTES", use_container_width=True)
    
    # Processar
    if 'volantes' not in st.session_state or gerar:
        with st.spinner("Analisando dados..."):
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
    
    volantes = st.session_state.volantes
    
    # Exibir
    st.markdown("---")
    
    for i, (vol, forca, cls) in enumerate(volantes, 1):
        if i == 1:
            st.markdown('<div class="jogo-ouro">', unsafe_allow_html=True)
            st.markdown(f"### 🏆 JOGO DE OURO #{i}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        elif i == 2:
            st.markdown('<div class="jogo-ouro">', unsafe_allow_html=True)
            st.markdown(f"### 🥈 JOGO DE OURO #{i}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"### Volante {i:02d}")
            st.markdown(f"<span class='badge'>Força: {forca}%</span>", unsafe_allow_html=True)
        
        # Números
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
        
        # Clusters
        if cls:
            txt = " | ".join([f"{c[0]}-{c[-1]} ({len(c)})" for c in cls])
            st.caption(f"Sequências: {txt}")
        
        if i in [1, 2]:
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
    # Download
    if volantes:
        texto = f"LOTOFÁCIL - {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        texto += f"Base: {len(resultados)} concursos | Análise: últimos {qtd_analise}\n"
        texto += f"Estratégia: {estrategia}\n"
        texto += "=" * 50 + "\n\n"
        
        for i, (vol, forca, _) in enumerate(volantes, 1):
            if i <= 2:
                texto += f"[{i:02d}] JOGO DE OURO ({forca}%): "
            else:
                texto += f"[{i:02d}] ({forca}%): "
            texto += " ".join(f"{n:02d}" for n in vol) + "\n"
        
        st.download_button("📥 Baixar volantes", texto, file_name=f"lotofacil_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")

# ============================================
# ABA 2 - ATUALIZAR RESULTADOS
# ============================================

with aba2:
    st.markdown("### 📝 Adicionar novo resultado")
    
    resultados = carregar_resultados()
    ultimo = resultados[0][0] if resultados else 3300
    
    st.info(f"Último concurso registrado: **{ultimo}**")
    
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
        st.markdown("### 📋 Dezenas sorteadas")
        st.markdown("Selecione as 15 dezenas:")
    
    # Seleção das 15 dezenas
    dezenas_selecionadas = []
    
    # Mostrar botões organizados
    cols = st.columns(5)
    for i in range(1, 26):
        idx = (i - 1) % 5
        with cols[idx]:
            if st.checkbox(f"{i:02d}", key=f"num_{i}"):
                dezenas_selecionadas.append(i)
    
    st.caption(f"Selecionadas: {len(dezenas_selecionadas)} de 15")
    
    # Botão para adicionar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        adicionar = st.button("➕ ADICIONAR RESULTADO", use_container_width=True)
    
    if adicionar:
        if len(dezenas_selecionadas) != 15:
            st.error(f"Você selecionou {len(dezenas_selecionadas)} dezenas. Precisam ser exatamente 15.")
        else:
            dezenas_ord = sorted(dezenas_selecionadas)
            novo_resultado = [novo_concurso, dezenas_ord]
            
            # Adiciona no início (mais recente primeiro)
            resultados.insert(0, novo_resultado)
            
            # Remove o mais antigo se tiver mais de 100
            if len(resultados) > 100:
                removido = resultados.pop()
                st.warning(f"Removido concurso {removido[0]} (limite de 100)")
            
            salvar_resultados(resultados)
            
            st.success(f"✅ Concurso {novo_concurso} adicionado com sucesso!")
            st.balloons()
            
            # Mostrar o que foi adicionado
            st.markdown(f"**Dezenas:** {' '.join(f'{n:02d}' for n in dezenas_ord)}")
            
            # Limpar estado
            st.rerun()
    
    st.markdown("---")
    
    # Exibir últimos resultados
    st.markdown("### 📜 Últimos resultados registrados")
    
    if resultados:
        mostrar = st.slider("Quantidade para exibir", 5, min(30, len(resultados)), 10)
        
        for i in range(mostrar):
            concurso, dezenas = resultados[i]
            dezenas_str = " ".join(f"{n:02d}" for n in dezenas)
            st.text(f"Concurso {concurso}: {dezenas_str}")
    
    # Botão para resetar
    st.markdown("---")
    st.warning("⚠️ Cuidado: resetar remove todos os resultados personalizados!")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        resetar = st.button("🔄 RESETAR PARA DADOS PADRÃO", use_container_width=True)
    
    if resetar:
        salvar_resultados(DADOS_PADRAO)
        st.success("✅ Dados resetados para o padrão!")
        st.rerun()

# ============================================
# RODAPÉ
# ============================================

st.markdown("---")
st.caption("⚠️ Sistema baseado em análise estatística. Não há garantia de acertos. Jogue com responsabilidade.")
