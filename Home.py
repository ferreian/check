import streamlit as st
import pandas as pd

# Função para carregar os dados do Excel
def carregar_dados(nome_arquivo):
    try:
        return pd.read_excel(nome_arquivo)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Interface do usuário no Streamlit
def main():
    st.title('Verificador de Material')
    
    # Upload do arquivo Excel no sidebar
    arquivo = st.sidebar.file_uploader("Carregue a lista de materiais (formato Excel)", type=['xlsx'])
    
    if arquivo is not None:
        # Carregar dados do Excel
        df = carregar_dados(arquivo)
        
        if df is not None:
            # Mostrar a tabela de materiais carregada
            st.write("Lista de Materiais:", df)
            
            # Campo para inserir o nome do material a ser verificado
            material_a_verificar = st.text_input("Digite o nome do material a verificar:")
            
            if material_a_verificar:
                # Verificar se o material está na lista (case insensitive)
                material_a_verificar_lower = material_a_verificar.lower()
                materiais_na_lista_lower = [str(mat).lower() for mat in df.values.flatten()]
                
                if material_a_verificar_lower in materiais_na_lista_lower:
                    st.success(f"Material '{material_a_verificar}' encontrado na lista!")
                    st.write("O material está disponível para retirada.")
                else:
                    st.error(f"Material '{material_a_verificar}' NÃO encontrado na lista.")
                    st.write("O material não está disponível.")
            else:
                st.info("Digite o nome do material para verificar a disponibilidade.")
            
if __name__ == "__main__":
    main()
