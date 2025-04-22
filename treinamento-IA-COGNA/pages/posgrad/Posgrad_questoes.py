import streamlit as st

variaveis = {}

def ler_variaveis(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith("#") or not linha:  # Ignora comentários e linhas em branco
                continue
            if ":" in linha:
                partes = linha.split(":", 1)  # Divide a linha em no máximo 2 partes
                chave = partes[0]
                valor = partes[1] if len(partes) > 1 else ""  # Valor vazio se não houver segundo valor
                variaveis[chave] = valor
    return variaveis

variaveis = ler_variaveis('txt/posgrad/prompts_questoes_posgrad.txt')

st.title("Orientações para Questões")
st.divider()
st.write(variaveis["orientacao"])

st.page_link("pages/Index.py", label="Home", icon="🏠")
