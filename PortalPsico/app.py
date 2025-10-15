import streamlit as st
import json, os

st.set_page_config(page_title="PortalPsico", page_icon="🧠")

st.title("🔐 RELATÓRIOS PSICOPEDAGÓGICOS")
st.caption("Sistema local — usuários em arquivo JSON — relatórios em PDF na pasta relatorios/")

DB_FILE = "usuarios.json"

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

usuarios = load_users()

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
tipo = st.selectbox("Entrar como", ["Pais", "Admin / Mestre"])
entrar = st.button("Entrar")

if entrar:
    email_norm = email.strip().lower()
    if tipo == "Admin / Mestre" and email_norm == "admin@portal.com" and senha == "12345":
        st.success("✅ Logado como Admin Mestre")
    elif email_norm in usuarios and usuarios[email_norm]["Senha"] == senha:
        st.success(f"✅ Bem-vindo(a), {usuarios[email_norm]['Nome']}!")
    else:
        st.error("❌ E-mail ou senha incorreta.")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 PortalPsico — Desenvolvido por Leandro Ferro. Todos os direitos reservados.")
