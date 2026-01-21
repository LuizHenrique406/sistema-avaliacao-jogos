import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de clientes")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente até o momento")
        else:
            list_dic = []
            for cliente in clientes: list_dic.append(cliente.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "senha"])     

    def inserir():
        id = 0
        nome = st.text_input("Nome do cliente")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha")
        if st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, senha)
                st.success("Cliente inserido com sucesso")
                time.sleep(1)
                st.rerun()
            except Exception as error:
                st.error(f"{error}")

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado até o momento")
        else:
            op = st.selectbox("Atualizar clientes", clientes)
            nome = st.text_input("Novo nome",  op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.cliente_atualizar(id, nome, email, senha)
                    st.success("Cliente atualizado com sucesso!")
                    time.sleep(1)
                    st.rerun()
                except Exception as erro:
                    st.error(f"{erro}")

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado até o momento")
        else:
            op = st.selectbox("Excluir Clientes", clientes)
            if op:
                if st.button("Excluir"):
                    id = op.get_id()
                    nome = op.get_nome()
                    email = op.get_email()
                    senha = op.get_senha()
                    View.cliente_excluir(id, nome, email, senha)
                    st.success("Cliente excluído com sucesso!")
                    st.rerun()