import streamlit as st
from views import View
import pandas as pd
from models.favoritos import Favorito

class ManterFavoritoUI:
    def main():

        st.title("Meus jogos favoritos")

        tab1, tab2, = st.tabs(["Ver meus favoritos", "Desfavoritar"])
        with tab1: ManterFavoritoUI.meus_favoritos()
        with tab2: ManterFavoritoUI.desfavoritar()


    def desfavoritar():
        idCliente = st.session_state["cliente_id"]
        produtos_fav = View.produtos_favoritos(idCliente)
        if produtos_fav == None:
            st.write("Nenhum jogo favoritado até o momento.")
        else:
            if produtos_fav: 
                op = st.selectbox("Selecione o jogo que você deseja desfavoritar", produtos_fav)
                idJogo = op["idJogo"]
                c = Favorito(idJogo, idCliente)
                if op and st.button("Desfavoritar"):
                    View.desfavoritar(c)
                    st.success("Jogo desfavoritado com sucesso!")
                    st.rerun()
        
    def meus_favoritos():
        idCliente = st.session_state["cliente_id"]
        favoritos = View.produtos_favoritos(idCliente)
        if favoritos == None:
            st.write("Nenhum jogo favoritado até o momento.")
        else:
            df = pd.DataFrame(favoritos)
            st.dataframe(df, hide_index=True, column_order=["idJogo", "Jogo"])