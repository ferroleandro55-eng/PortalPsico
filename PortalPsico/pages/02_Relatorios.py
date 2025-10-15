import streamlit as st
import os, json
from datetime import datetime

st.title("📁 Enviar e Excluir Relatórios")
PASTA_RELATORIOS = "relatorios"
MAP_FILE = "relatorios_map.json"
os.makedirs(PASTA_RELATORIOS, exist_ok=True)

def load_map():
    if os.path.exists(MAP_FILE):
        with open(MAP_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_map(m):
    with open(MAP_FILE, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=4, ensure_ascii=False)

mapa = load_map()

st.subheader("📤 Enviar Relatório (PDF)")
with st.form("upload_form"):
    nome = st.text_input("Nome do destinatário")
    pdf = st.file_uploader("Selecione o PDF", type=["pdf"])
    sub = st.form_submit_button("Enviar")
    if sub and pdf:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S_") + pdf.name
        path = os.path.join(PASTA_RELATORIOS, ts)
        with open(path, "wb") as f:
            f.write(pdf.getbuffer())
        mapa[ts] = nome
        save_map(mapa)
        st.success(f"Relatório '{pdf.name}' enviado para {nome}.")

st.subheader("📂 Relatórios no Servidor")
if mapa:
    for fname, dono in mapa.items():
        fpath = os.path.join(PASTA_RELATORIOS, fname)
        with open(fpath, "rb") as f:
            st.download_button(f"⬇️ {fname} ({dono})", f, file_name=fname)
        if st.button(f"🗑 Excluir {fname}"):
            os.remove(fpath)
            mapa.pop(fname)
            save_map(mapa)
            st.experimental_rerun()
else:
    st.info("Nenhum relatório enviado ainda.")
