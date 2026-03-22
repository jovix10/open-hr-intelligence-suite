import streamlit as st
from datetime import datetime
from modules.recruiter_ia import run_recruiter

# Configuração da Página
st.set_page_config(page_title="Open-HR Intelligence", page_icon="🎯", layout="wide")

# CSS Minimalista e Seguro
st.markdown("""
    <style>
    .wa-link {
        display: block;
        background-color: #25D366;
        color: white !important;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("🎯 Open-HR")
        st.caption("v1.0.0 | Open Source")
        st.write("---")
        
        menu = ["🏠 Dashboard", "🔍 Recrutador IA", "📝 Onboarding", "📈 Engajamento"]
        choice = st.sidebar.radio("Navegação", menu)
        
        st.write("---")
        st.write("**Precisa de ajuda?**")
        wa_url = "https://wa.me/5568999066746?text=Suporte%20Open-HR"
        st.markdown(f'<a href="{wa_url}" target="_blank" class="wa-link">💬 WhatsApp</a>', unsafe_allow_html=True)

    # Conteúdo Principal
    if choice == "🏠 Dashboard":
        st.header("Painel de Controle")
        st.write(f"Bem-vindo. Hoje é {datetime.now().strftime('%d/%m/%Y')}")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Análises", "150", "+5")
        c2.metric("Vagas", "8", "0")
        c3.metric("Eficiência", "92%", "+2%")
        
        st.info("Este é um projeto público focado em automação de RH.")

    elif choice == "🔍 Recrutador IA":
        run_recruiter()

    else:
        st.header(choice)
        st.warning("Este módulo está em desenvolvimento pela comunidade.")

if __name__ == "__main__":
    main()