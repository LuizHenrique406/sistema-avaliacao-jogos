import streamlit as st
import pandas as pd
import time
from views import View

class ListarResenhaUI:
    def main():
        
        tab1, tab2, tab3 = st.tabs(["Listar", "Atualizar", "Excluir"])
        with tab1: ListarResenhaUI.listar_resenha()
        with tab2: ListarResenhaUI.atualizar_resenha()
        with tab3: ListarResenhaUI.excluir_resenha()

    def listar_resenha():
        resenhas = View.resenha_listar()
        if len(resenhas) == 0: st.write("Nenhuma resenha salva até o momento")
        else:
            list_dic = []
            for resenha in resenhas: list_dic.append(resenha.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "idCliente", "idJogo", "resenha"])
    
    def atualizar_resenha():
        resenhas = View.resenha_listar()
        if len(resenhas) == 0: st.write("Nenhuma resenha salva até o momento")
        else:
            op = st.selectbox("Atualizar resenha", resenhas)
            r = st.text_input("Nova resenha",  op.get_resenha())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.resenha_atualizar(id, r)
                    st.success("Categoria atualizada com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as erro:
                    st.error(f"{erro}")
    def excluir_resenha():
        resenhas = View.categoria_listar()
        if len(resenhas) == 0: st.write("Nenhum resenha cadastrada até o momento")
        else:
            op = st.selectbox("Excluir resenhas", resenhas)
            if op:
                if st.button("Excluir"):
                    id = op.get_id()
                    descricao = op.get_resenha()
                    View.categoria_excluir(id, descricao)
                    st.success("Categoria excluído com sucesso!")
                    st.rerun()