import pickle
import streamlit as st

model = pickle.load(open('estimasi.sav', 'rb'))

st.title('Estimasi Mobil Bekas')

year = st.number_input('Input Tahun Mobil: ')
mileage = st.number_input('Input Kilometer Mobil:')
tax = st.number_input('Input Pajak Mobil: ')
mpg = st.number_input('Input Konsumsi BBM Mobil:')
engineSize =st.number_input('Input Ukuran Mesin Mobil:')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write ('Estimasi Harga Mobil Bekas dalam Pounds: ', predict)
    st.write ('Estimasi Harga Mobil Bekas dalam IDR: ', predict*20000)