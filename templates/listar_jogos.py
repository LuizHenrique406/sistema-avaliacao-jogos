import streamlit as st
import pandas as pd
from views import View
from models.favoritos import Favorito

class ListarJogosUI:
    def main():
        st.title("🎮 Catálogo de jogos")
        st.selectbox("Busque seu jogo pela sua categoria preferida!", View.categoria_listar())
        jogos = View.jogos_listar()
        qtd_cols = len(jogos)
        cards = st.columns(qtd_cols, gap="medium", vertical_alignment="bottom")
        for i, jogo in enumerate(jogos):
            with cards[i]:
                st.write(jogo.get_descricao())
                st.image(jogo.get_imagem(), width="content")
                st.text_area(f"Escreva sua resenha aqui sobre esse jogo aqui", key=jogo.get_descricao())
                if st.button("Favoritar", key="")