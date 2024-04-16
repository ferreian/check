import streamlit as st
import pandas as pd

# Função para carregar os dados do Excel
def carregar_dados(nome_arquivo):
    return pd.read_excel(nome_arquivo)

# Interface do usuário no Streamlit
def main():
    st.title('Verificador de Material')
    
    # Upload do arquivo Excel no sidebar
    arquivo = st.sidebar.file_uploader("Carregue a lista de materiais (formato Excel)", type=['xlsx'])
    
    if arquivo is not None:
        # Carregar dados do Excel
        df = carregar_dados(arquivo)
        
        # Mostrar a tabela de materiais carregada
        st.write("Lista de Materiais:", df)
        
        # Campo para inserir o nome do material a ser verificado
        material_a_verificar = st.text_input("Digite o nome do material a verificar:")
        
        if material_a_verificar:
            # Verificar se o material está na lista
            resultado = material_a_verificar in df.values
            
            # Mostrar resultado da verificação e abrir pop-up
            if resultado:
                st.success(f"Material '{material_a_verificar}' encontrado na lista!")
                st.write("O material está disponível para retirada.")
            else:
                st.error(f"Material '{material_a_verificar}' NÃO encontrado na lista.")
                st.write("O material não está disponível.")
            
if __name__ == "__main__":
    main()
