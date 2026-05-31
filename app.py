# ============================================
# APP LOTOFÁCIL FVN - STREAMLIT
# Sistema Anti-Caos com Estratégia Híbrida
# ============================================

import streamlit as st
import random
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Lotofácil FVN",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# ESTILO PERSONALIZADO
# ============================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5em;
    }
    .main-header p {
        color: rgba(255,255,255,0.9);
        margin-top: 10px;
    }
    .volante-card {
        background: #1e1e2e;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border-left: 5px solid #667eea;
        transition: transform 0.2s;
    }
    .volante-card:hover {
        transform: translateY(-3px);
    }
    .numero {
        display: inline-block;
        width: 42px;
        height: 42px;
        text-align: center;
        line-height: 42px;
        margin: 3px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 14px;
    }
    .numero-cluster-grande { background: #fef3c7; color: #d97706; }
    .numero-cluster-medio { background: #dbeafe; color: #2563eb; }
    .numero-cluster-pequeno { background: #dcfce7; color: #16a34a; }
    .numero-normal { background: #334155; color: #cbd5e1; }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        width: 100%;
        border: none;
        border-radius: 12px;
        padding: 12px;
    }
    .stButton button:hover {
        transform: scale(1.02);
        opacity: 0.95;
    }
    .stat-card {
        background: #1e1e2e;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
    .stDownloadButton button {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# BANCOS DE CLUSTERS
# ============================================

CLUSTERS_GRANDES = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,10],
    [5,6,7,8,9,10,11,12,13],
    [10,11,12,13,14,15,16,17],
    [11,12,13,14,15,16,17,18,19,20],
    [12,13,14,15,16,17,18,19,20],
    [15,16,17,18,19,20,21,22,23,24,25],
    [16,17,18,19,20,21,22,23,24,25],
    [18,19,20,21,22,23,24,25],
    [19,20,21,22,23,24,25],
    [20,21,22,23,24,25],
]

CLUSTERS_MEDIOS = [
    [1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7],
    [6,7,8,9,10], [7,8,9,10,11],
    [10,11,12,13,14], [11,12,13,14,15], [12,13,14,15,16],
    [15,16,17,18,19], [16,17,18,19,20], [17,18,19,20,21],
    [18,19,20,21,22], [19,20,21,22,23], [20,21,22,23,24],
    [21,22,23,24,25], [22,23,24,25], [1,2,3,4],
    [8,9,10,11], [14,15,16,17],
]

CLUSTERS_PEQUENOS = [
    [1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7],
    [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12],
    [11,12,13], [12,13,14], [13,14,15], [14,15,16], [15,16,17],
    [16,17,18], [17,18,19], [18,19,20], [19,20,21], [20,21,22],
    [21,22,23], [22,23,24], [23,24,25],
]

# ============================================
# FUNÇÕES PRINCIPAIS
# ============================================

def detectar_clusters(volante):
    """Detecta sequências de 3+ números consecutivos"""
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

def gerar_volante(tipo):
    """Gera um volante baseado no tipo de estratégia"""
    volante = set()
    
    if tipo == 'GRANDE':
        cluster = random.choice(CLUSTERS_GRANDES)
        volante.update(cluster)
    elif tipo == 'MÉDIO':
        clusters = random.sample(CLUSTERS_MEDIOS, 2)
        for c in clusters:
            volante.update(c)
    else:
        clusters = random.sample(CLUSTERS_PEQUENOS, 3)
        for c in clusters:
            volante.update(c)
    
    if len(volante) < 15:
        restantes = [n for n in range(1, 26) if n not in volante]
        random.shuffle(restantes)
        while len(volante) < 15 and restantes:
            volante.add(restantes.pop())
    
    if len(volante) > 15:
        volante = set(random.sample(list(volante), 15))
    
    return sorted(list(volante))

def gerar_volantes(qtd_g, qtd_m, qtd_p, evitar_01):
    """Gera a bateria completa de volantes"""
    volantes = []
    
    # Gera volantes GRANDES
    for _ in range(qtd_g):
        v = gerar_volante('GRANDE')
        if not evitar_01 or 1 not in v:
            volantes.append(('GRANDE', v))
    
    # Gera volantes MÉDIOS
    for _ in range(qtd_m):
        v = gerar_volante('MÉDIO')
        if not evitar_01 or 1 not in v:
            volantes.append(('MÉDIO', v))
    
    # Gera volantes PEQUENOS
    for _ in range(qtd_p):
        v = gerar_volante('PEQUENO')
        if not evitar_01 or 1 not in v:
            volantes.append(('PEQUENO', v))
    
    # Completa se faltar por causa da restrição do 01
    while len(volantes) < qtd_g + qtd_m + qtd_p:
        falta_g = max(0, qtd_g - sum(1 for t,_ in volantes if t == 'GRANDE'))
        falta_m = max(0, qtd_m - sum(1 for t,_ in volantes if t == 'MÉDIO'))
        falta_p = max(0, qtd_p - sum(1 for t,_ in volantes if t == 'PEQUENO'))
        
        for _ in range(falta_g):
            v = gerar_volante('GRANDE')
            if not evitar_01 or 1 not in v:
                volantes.append(('GRANDE', v))
        for _ in range(falta_m):
            v = gerar_volante('MÉDIO')
            if not evitar_01 or 1 not in v:
                volantes.append(('MÉDIO', v))
        for _ in range(falta_p):
            v = gerar_volante('PEQUENO')
            if not evitar_01 or 1 not in v:
                volantes.append(('PEQUENO', v))
    
    random.shuffle(volantes)
    return volantes

def formatar_volante(tipo, volante, indice):
    """Formata um volante como HTML"""
    clusters = detectar_clusters(volante)
    
    # Identifica a qual cluster cada número pertence
    nums_cluster_grande = set()
    nums_cluster_medio = set()
    nums_cluster_pequeno = set()
    
    for c in clusters:
        if len(c) >= 6:
            nums_cluster_grande.update(c)
        elif len(c) >= 4:
            nums_cluster_medio.update(c)
        else:
            nums_cluster_pequeno.update(c)
    
    # Gera HTML dos números
    numeros_html = ""
    for num in volante:
        if num in nums_cluster_grande:
            classe = "numero-cluster-grande"
        elif num in nums_cluster_medio:
            classe = "numero-cluster-medio"
        elif num in nums_cluster_pequeno:
            classe = "numero-cluster-pequeno"
        else:
            classe = "numero-normal"
        
        numeros_html += f'<span class="numero {classe}">{num:02d}</span>'
    
    # Gera texto dos clusters
    cluster_text = ""
    if clusters:
        seq = []
        for c in clusters:
            if len(c) >= 6:
                seq.append(f"⭐ {c[0]}-{c[-1]} ({len(c)})")
            elif len(c) >= 4:
                seq.append(f"🔷 {c[0]}-{c[-1]} ({len(c)})")
            else:
                seq.append(f"🔹 {c[0]}-{c[-1]} ({len(c)})")
        cluster_text = " | ".join(seq)
    else:
        cluster_text = "⚠️ Sem clusters de 3+ números"
    
    # Ícone do tipo
    tipo_icone = {"GRANDE": "🏆", "MÉDIO": "📌", "PEQUENO": "🔸"}[tipo]
    
    return f"""
    <div class="volante-card">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <strong>{tipo_icone} Volante {indice:02d}</strong>
            <span style="font-size: 11px; padding: 3px 10px; border-radius: 20px; background: #2d2d3d;">{tipo}</span>
        </div>
        <div>{numeros_html}</div>
        <div style="font-size: 11px; color: #888; margin-top: 10px; padding-top: 8px; border-top: 1px solid #2d2d3d;">
            🔗 {cluster_text}
        </div>
    </div>
    """

# ============================================
# INTERFACE DO APP
# ============================================

# Cabeçalho
st.markdown("""
<div class="main-header">
    <h1>🎰 LOTOFÁCIL FVN</h1>
    <p>Sistema Anti-Caos com Estratégia Híbrida • Clusters Grandes + Médios + Pequenos</p>
    <p style="font-size: 14px; margin-top: 10px;">Baseado em análise de resultados reais da Lotofácil</p>
</div>
""", unsafe_allow_html=True)

# Sidebar com controles
with st.sidebar:
    st.markdown("## ⚙️ CONFIGURAÇÕES")
    st.markdown("---")
    
    qtd_grande = st.slider("🏆 Clusters GRANDES (6-10 números)", 0, 20, 10)
    qtd_medio = st.slider("📌 Clusters MÉDIOS (4-5 números)", 0, 20, 10)
    qtd_pequeno = st.slider("🔸 Clusters PEQUENOS (3 números)", 0, 20, 10)
    
    st.markdown("---")
    
    evitar_01 = st.checkbox("⚠️ Evitar número 01", value=True)
    
    st.markdown("---")
    st.markdown("### 📊 ESTRATÉGIA")
    st.info("""
    **🏆 GRANDES:** 1 cluster de 6-10 números consecutivos
    
    **📌 MÉDIOS:** 2 clusters de 4-5 números consecutivos
    
    **🔸 PEQUENOS:** 3 clusters de 3 números consecutivos
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 LEGENDA")
    st.markdown("""
    - ⭐ = cluster 6+ números
    - 🔷 = cluster 4-5 números  
    - 🔹 = cluster 3 números
    - 🏆 = estratégia GRANDE
    - 📌 = estratégia MÉDIO
    - 🔸 = estratégia PEQUENO
    """)

# Botões principais
col1, col2 = st.columns(2)
with col1:
    gerar = st.button("🎲 GERAR VOLANTES", use_container_width=True)
with col2:
    novos = st.button("🔄 NOVOS VOLANTES", use_container_width=True)

# Estado da sessão (mantém os volantes entre interações)
if 'volantes' not in st.session_state or gerar or novos:
    with st.spinner("🔄 Gerando volantes otimizados... Isso leva apenas alguns segundos"):
        st.session_state.volantes = gerar_volantes(qtd_grande, qtd_medio, qtd_pequeno, evitar_01)

volantes = st.session_state.volantes

# ============================================
# ESTATÍSTICAS
# ============================================

total = len(volantes)
total_g = sum(1 for t,_ in volantes if t == 'GRANDE')
total_m = sum(1 for t,_ in volantes if t == 'MÉDIO')
total_p = sum(1 for t,_ in volantes if t == 'PEQUENO')

st.markdown("---")
st.markdown("## 📊 ESTATÍSTICAS")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🎯 Total de Volantes", total)
with col2:
    st.metric("🏆 Grandes", total_g)
with col3:
    st.metric("📌 Médios", total_m)
with col4:
    st.metric("🔸 Pequenos", total_p)

# ============================================
# EXIBIÇÃO DOS VOLANTES
# ============================================

st.markdown("---")
st.markdown("## 📋 SEUS VOLANTES")

# Organiza em 2 colunas para melhor visualização
cols = st.columns(2)

for i, (tipo, volante) in enumerate(volantes, 1):
    with cols[(i-1) % 2]:
        st.markdown(formatar_volante(tipo, volante, i), unsafe_allow_html=True)

# ============================================
# BOTÃO PARA COPIAR/BAIXAR
# ============================================

st.markdown("---")

# Gera texto para download
texto_copia = "=" * 60 + "\n"
texto_copia += f"VOLANTES LOTOFÁCIL FVN\n"
texto_copia += f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
texto_copia += "=" * 60 + "\n\n"

for i, (tipo, volante) in enumerate(volantes, 1):
    volante_str = " ".join(f"{n:02d}" for n in volante)
    texto_copia += f"[{i:02d}] {tipo}: {volante_str}\n"

texto_copia += "\n" + "=" * 60 + "\n"
texto_copia += "🏆 GRANDES = cluster 6-10 números\n"
texto_copia += "📌 MÉDIOS = cluster 4-5 números\n"
texto_copia += "🔸 PEQUENOS = cluster 3 números\n"
texto_copia += "=" * 60

st.download_button(
    label="📥 BAIXAR VOLANTES (TXT)",
    data=texto_copia,
    file_name=f"lotofacil_fvn_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
    mime="text/plain",
    use_container_width=True
)

# ============================================
# RODAPÉ
# ============================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 11px; padding: 20px;">
    ⚠️ Este sistema é baseado em análises estatísticas e padrões identificados em resultados anteriores.<br>
    Não há garantia de acertos. Jogue com responsabilidade.
</div>
""", unsafe_allow_html=True)