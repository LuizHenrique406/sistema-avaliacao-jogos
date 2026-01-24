import streamlit as st
import pandas as pd
import base64
import os
from views import View
import time

SAVE_DIR = "images" 
os.makedirs(SAVE_DIR, exist_ok=True)

class ManterJogosUI:
    def main():
        st.header("Cadastro de jogos")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterJogosUI.listar()
        with tab2: ManterJogosUI.inserir()
        with tab3: ManterJogosUI.atualizar()
        with tab4: ManterJogosUI.excluir()

    def listar():
        jogos = View.jogos_listar()
        if len(jogos) == 0: st.write("Nenhum jogo até o momento")
        else:
            list_dic = []
            for jogos in jogos: list_dic.append(jogos.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao", "idCategoria", "imagem"])     

    def inserir():
        id = 0
        descricao = st.text_input("Descrição do produto")
        categoria = st.selectbox("Categoria", View.categoria_listar())
        imagem = st.file_uploader("Adicione a imagem do jogo", type=None) 
        if imagem is not None:
            save_path = os.path.join(SAVE_DIR, imagem.name)
            with open(save_path, "wb") as f: 
                f.write(imagem.getbuffer())
        if len(View.categoria_listar()) > 0 and st.button("Inserir"): 
            try:
                View.jogos_inserir(id, descricao, categoria.get_id(), save_path)
                st.success("Jogo adicionado com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as erro:
                st.error(f"{erro}")

    def atualizar():
        jogos = View.jogos_listar()
        if len(jogos) == 0: st.write("Nenhum jogo até o momento")
        else:
            op = st.selectbox("Atualizar Jogos", jogos)
            descricao = st.text_input("Nova descrição",  op.get_descricao())
            categorias = st.selectbox("Nova categoria", View.categoria_listar())
            imagem = st.file_uploader("Adicione a nova imagem do jogo", type=None)
            if len(View.categoria_listar()) > 0 and st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.jogos_atualizar(id, descricao, categorias.get_id())
                    st.success("Jogo atualizado com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as erro:
                    st.error(f"{erro}")
    
    def excluir():
        jogos = View.jogos_listar()
        if len(jogos) == 0: st.write("Nenhum jogo até o momento")
        else:
            op = st.selectbox("Excluir jogos", jogos)
            if op:
                if st.button("Excluir"):
                    id = op.get_id()
                    descricao = op.get_descricao()
                    idCategoria = op.get_idCategoria()
                    imagem = op.get_imagem()
                    View.jogos_excluir(id, descricao, idCategoria, imagem)
                    st.success("Jogo excluído com sucesso!")
                    time.sleep(1)
                    st.rerun()