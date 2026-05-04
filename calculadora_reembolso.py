import streamlit as st
st.title('Calculadora de Reembolso de combustível ⛽')
#st.subheader('Calza')
# Quando vale a pena escolher etanol ao inves de gasolina?
etanol = 0.36
gasolina = 0.25
#vEtanol = 0.0
#vGasolina = 0.0
#totalKm = 0.0

vEtanol = st.number_input('Digite o valor do etanol', min_value = 0.0)
totalKm = st.number_input('Quantos Km você rodou no total? ',min_value =0.0)
#gasolina = st.number_input('Digite o valor da gasolina', min_value = 0.0)

vKm = etanol * vEtanol
reembolso = vKm *totalKm
if st.button('Resolver'):
    st.success(f'{reembolso:.2f}')
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