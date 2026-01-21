import streamlit as st
import pandas as pd
from views import View

class ListarJogosUI:
    def main():
        st.title("🎮 Catálogo de jogos")
        st.selectbox("Busque seu jogo pela sua categoria preferida!", View.categoria_listar())
        jogos = View.jogos_listar()
        if len(jogos) == 0: st.write("Nenhum produto até o momento")
        else:
            list_dic = []
            for jogos in jogos: list_dic.append(jogos.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao", "idCategoria", "imagem"])