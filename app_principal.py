import streamlit as st
from components.header import desenhar_header

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Portal de Sistemas e Processos",
    page_icon="🖥️",
    layout="wide"
)

# 2. FUNÇÃO AUXILIAR DE SEGURANÇA (Evita que o app quebre se o arquivo de secrets não existir)
def obter_secret(chave, valor_padrao="N/A"):
    try:
        return st.secrets.get(chave, valor_padrao)
    except Exception:
        return valor_padrao

# 3. DESENHA O TOPO DA LOGCARE
desenhar_header(cor_da_empresa="#069782", caminho_logo="logo.png")

# 4. MENSAGEM DE AUTONOMIA
st.info(
    "👋 **Olá, pessoal!** Este portal foi criado para que você tenha total autonomia. "
    "Aqui você encontra os links diretos, locais de funcionamento e os responsáveis "
    "de cada sistema da nossa operação, sem a necessidade de acionar a equipe fora do horário."
)

# 5. CABEÇALHO DO PORTAL
st.subheader("Guia rápido de acessos e documentações para a gestão.")
st.markdown("---")

# 6. DIVIDINDO A TELA EM COLUNAS
col_operacao, col_financeiro = st.columns(2)

# --- COLUNA 1: OPERAÇÕES & LOGÍSTICA ---
with col_operacao:
    st.header("📦 Operações & Logística")
    
    # Sistema 1: Portal 99
    with st.expander("🌐 Portal 99 (Atendimento / Planejamento / Bases)"):
        st.write("**Tipo de Acesso:** Web (Nuvem)")
        st.write("**Link direto:** [Acessar Portal 99](https://intranet.profilelog.com.br/99pedidos/index.php)")
        st.write("**Responsável Principal:** Equipe Atendimento")
        st.write("**Suporte Técnico:** Alessandro")
        st.info("💡 *Este sistema pode ser acessado de qualquer computador ou celular com internet.*")

    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("PORTAL99_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("PORTAL99_PASS", "senha_padrao"), language="text")

    # Sistema 2: QR Code
    with st.expander("🏷️ Sistema de QR Code (Atendimento / Planejamento)"):
        st.write("**Tipo de Acesso:** Web & Google Drive")
        st.write("**Link do Sistema:** [Gerador de QR Code](https://logcareetiquetaqrcode.streamlit.app/)")
        st.write("**Link do Banco de Dados (Logs):** [Pasta do Google Drive](https://docs.google.com/spreadsheets/d/1qJf9Hdjqci847ANvKLtqJiiv7wnSuRHM1fHsc1xkwmQ/edit?gid=0#gid=0)")
        st.write("**Responsável Principal:** Equipe Atendimento")
        st.write("**Suporte Técnico:** Paulo")
        st.info("💡 *Este sistema pode ser acessado de qualquer computador ou celular com internet.*")

    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("QRCODE_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("QRCODE_PASS", "senha_padrao"), language="text")

    # Sistema 3: Ortobom
    with st.expander("🏷️ Sistema de Gestão Ortobom (Transporte / Planejamento)"):
        st.write("**Tipo de Acesso:** Web & Google Drive")
        st.write("**Link do Sistema:** [Acessar Sistema Ortobom](https://logcarecarretasortobom.streamlit.app/)")
        st.write("**Link do Banco de Dados (Logs):** [Pasta do Google Drive](https://docs.google.com/spreadsheets/d/1l2XTVGgNxCapZDy052z2986RmoQU66XxmLOFzGegoDc/edit?gid=0#gid=0)")
        st.write("**Responsável Principal:** Equipe Transporte")
        st.write("**Suporte Técnico:** Paulo")
        st.info("💡 *Este sistema pode ser acessado de qualquer computador ou celular com internet.*")
    
    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("ORTOBOM_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("ORTOBOM_PASS", "senha_padrao"), language="text")

    # Sistema 4: WMS & TMS
    with st.expander("🖥️ WMS / TMS (Sistemas de Base - Locais)"):
        st.error("⚠️ **Atenção: Sistemas Locais (DDS)**")
        st.write("**Onde roda:** Instalado em computador individual físico na empresa.")
        st.write("**Responsável Principal:** Equipe de Atendimento")
        st.write("**Suporte Técnico:** Equipe DDS")
        st.write("💡 **Como acessar:** Requer estar fisicamente na máquina ou acesso via área de trabalho remota autorizada.")

    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("WMS_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("WMS_PASS", "senha_padrao"), language="text")


# --- COLUNA 2: FINANCEIRO, COMERCIAL & GESTÃO ---
with col_financeiro:
    st.header("💼 Administrativo & Estratégico")
    
    # Sistema 5: Faturas
    with st.expander("🧾 Sistema de Faturas (Financeiro / Bases)"):
        st.write("**Tipo de Acesso:** Web")
        st.write("**Link direto:** [Acessar Sistema de Faturas](https://logcarebasefatura.pythonanywhere.com/)")
        st.write("**Responsável Principal:** Departamento Financeiro")
        st.write("**Suporte Técnico:** Paulo")
        st.info("💡 *Este sistema pode ser acessado de qualquer computador ou celular com internet.*")

        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("FINANCEIRO_USER", "usuario_gestao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("FINANCEIRO_PASS", "senha_padrao_123"), language="text")

    # Sistema 6: Gerador de Propostas
    with st.expander("✍️ Gerador de Propostas (Comercial / Gerência)"):
        st.write("**Tipo de Acesso:** Web")
        st.write("**Link direto:** [Acessar Gerador](https://link-gerador-propostas.com)")
        st.write("**Como acessar:** Requer estar fisicamente na máquina ou acesso via área de trabalho remota autorizada.")
        st.write("**Responsável Principal:** Equipe Comercial")
        st.write("**Suporte Técnico:** Paulo")
        st.info("💡 *Este sistema pode ser acessado de qualquer computador ou celular com internet.*")

    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("PROPOSTA_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("PROPOSTA_PASS", "senha_padrao"), language="text")

    # Sistema 7: Power BI
    with st.expander("📊 Power BI (Painéis de Gestão)"):
        st.warning("⏳ **Status: Em Breve**")
        st.write("Estamos desenvolvendo os painéis unificados de planejamento e gerência.")
        st.write("**Responsável Principal:** Equipe Planejamento")
        st.write("**Suporte Técnico:** Paulo")

    # MOLDE DE CREDENCIAIS (Basta mudar a chave do secret!)
        st.markdown("---")
        st.caption("🔑 **Credenciais de Acesso da Gestão**")
    
        col_user, col_pass = st.columns(2)
        with col_user:
            st.write("**Usuário:**")
            st.code(obter_secret("SUA_CHAVE_USER", "usuario_padrao"), language="text")
            
        with col_pass:
            st.write("**Senha:**")
            st.code(obter_secret("SUA_CHAVE_PASS", "senha_padrao"), language="text")