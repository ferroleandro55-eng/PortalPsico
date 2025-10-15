import streamlit as st
import json, os

st.title("🔑 Recuperar Senha")
DB_FILE = "usuarios.json"

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

usuarios = load_users()

email = st.text_input("Digite seu e-mail cadastrado")
if st.button("Recuperar senha"):
    e_norm = email.strip().lower()
    if e_norm in usuarios:
        senha = usuarios[e_norm]["Senha"]
        st.success(f"Sua senha é: **{senha}**")
    else:
        st.error("E-mail não encontrado.")
