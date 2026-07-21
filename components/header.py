import streamlit as st
import base64

def carregar_imagem_base64(caminho_da_imagem):
    """Lê um arquivo de imagem e converte para Base64 (texto seguro para HTML)."""
    try:
        with open(caminho_da_imagem, "rb") as arquivo:
            return base64.b64encode(arquivo.read()).decode()
    except FileNotFoundError:
        return None

def desenhar_header(cor_da_empresa="#069782", caminho_logo="logo.png"):
    """
    Desenha o topo (banner) personalizado com a marca da empresa e o título centralizado.
    """
    logo_base64 = carregar_imagem_base64(caminho_logo)

    if logo_base64:
        html_banner = f"""<div style="
background-color: {cor_da_empresa}; 
padding: 15px 30px; 
border-radius: 10px; 
display: flex; 
align-items: center; 
justify-content: space-between; 
margin-bottom: 45px;
">
<img src="data:image/png;base64,{logo_base64}" style="height: 55px; max-width: 180px; object-fit: contain;">
<div style="text-align: center; margin: 0 auto;">
<h1 style="color: white; margin: 0; font-family: sans-serif; font-size: 24px; line-height: 1.2;">PORTAL DE SISTEMAS & PROCESSOS</h1>
<p style="color: #E0E0E0; margin: 5px 0 0 0; font-family: sans-serif; font-size: 13px;">Identidade, Organização e Autonomia para a Gestão</p>
</div>
<div style="width: 180px;"></div>
</div>"""
    else:
        html_banner = f"""<div style="background-color: {cor_da_empresa}; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 45px;">
<h1 style="color: white; margin: 0; font-family: sans-serif; font-size: 24px;">PORTAL DE SISTEMAS & PROCESSOS</h1>
<p style="color: #E0E0E0; margin: 5px 0 0 0; font-family: sans-serif; font-size: 13px;">Identidade, Organização e Autonomia para a Gestão</p>
</div>"""

    # Renderiza o topo na tela do Streamlit
    st.markdown(html_banner, unsafe_allow_html=True)