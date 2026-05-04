import streamlit as st
st.title('Calculadora de Reembolso de combustível ⛽')
st.subheader('Escola o combustível ')
# Quando vale a pena escolher etanol ao inves de gasolina?
etanol = 0.36
gasolina = 0.25
opcoes = ['Gasolina','Etanol']
#vEtanol = 0.0
#vGasolina = 0.0
#totalKm = 0.0
escolha = st.selectbox('Escolha o combustível\n',opcoes)


if escolha == 'Etanol':
    vEtanol = st.number_input('Digite o valor do etanol', min_value = 0.0)
    totalKm = st.number_input('Quantos Km você rodou no total? ',min_value =0.0)
    vKm = etanol * vEtanol
#gasolina = st.number_input('Digite o valor da gasolina', min_value = 0.0)
else:
    vGasolina = st.number_input('Digite o valor da Gasolina', min_value = 0.0)
    totalKm = st.number_input('Quantos Km você rodou no total? ',min_value =0.0)
    vKm = gasolina * vGasolina

reembolso = vKm *totalKm
if st.button('Resolver'):
    st.success(f'Valor do reembolso:\n R$ {reembolso:.2f}')
#----------------------------------------------------------------------------
#if gasolina >0:
#   resultado = etanol/gasolina 
#  if resultado <0.70:
#   msg = 'Abasteça com Etanol Chefe 😁✌️'    
#  else:
#   msg = 'Abasteça com gasolina Chefe 😁✌️'
# else:
# st.warning("Digite um valor acima de 0")
# if st.button('Resolver'):
#    st.success(msg)
#----------------------------------------------------------------------------
