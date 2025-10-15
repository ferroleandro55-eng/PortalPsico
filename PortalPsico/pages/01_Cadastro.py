import streamlit as st
import json, os

st.title("👥 Cadastro e Remoção de Usuários")
DB_FILE = "usuarios.json"

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

usuarios = load_users()

st.subheader("➕ Cadastrar novo usuário")
with st.form("form_cadastro"):
    nome = st.text_input("Nome completo")
    email = st.text_input("E-mail (ex: pai@email.com)")
    senha = st.text_input("Senha", type="password")
    tipo = st.selectbox("Tipo de usuário", ["Pais", "Admin / Mestre"])
    status = st.selectbox("Status", ["Ativo", "Inativo"])
    sub = st.form_submit_button("Cadastrar usuário")
    if sub:
        e_norm = email.strip().lower()
        if not nome or not email or not senha:
            st.warning("⚠️ Preencha todos os campos!")
        elif e_norm in usuarios:
            st.error("❌ Este e-mail já está cadastrado.")
        else:
            usuarios[e_norm] = {"Nome": nome, "Senha": senha, "Tipo": tipo, "Status": status}
            save_users(usuarios)
            st.success(f"✅ Usuário '{nome}' cadastrado!")

st.subheader("🗑 Remover usuário")
if usuarios:
    sel = st.selectbox("Selecione um usuário", list(usuarios.keys()))
    if st.button("Remover usuário selecionado"):
        usuarios.pop(sel, None)
        save_users(usuarios)
        st.success("Usuário removido!")
else:
    st.info("Nenhum usuário cadastrado ainda.")
