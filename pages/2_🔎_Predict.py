#Import Library
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

#Konfigurasi page title
st.set_page_config(page_title="stmik-heart-disease", page_icon=":heart:", layout="wide")

#Menampilkan Gambar
image=Image.open('logo_stmik_new.png')
st.image(image, use_column_width=True)

#Judul Display
st.title('Heart Disease Predict Using Machine Learning :heart:')
st.write("---")

#Load Dataset
df=pd.read_csv('heart-20000.csv')

#Menghapus isi fitur
del df['id']
df.drop(df[df['ap_hi']>250].index, inplace = True)
df.drop(df[df['ap_hi']<60].index, inplace = True)
df.drop(df[df['ap_lo']>180].index, inplace = True)
df.drop(df[df['ap_lo']<50].index, inplace = True)

#Menampilkan data sebagai tabel
with st.container():
    st.write("""
                ## Keterangan Data yang Digunakan
                1. Usia: Rentang usia yang akan di prediksi dari umur 10-30
                2. Jenis Kelamin: 1 untuk Laki-Laki dan 2 untuk Perempuan
                3. Tinggi Badan
                4. Berat Badan
                5. ap_hi: Tekanan Darah Sistolik
                6. ap_lo: Tekanan Darah Diastolik
                7. Kolestrol: 1 untuk Rendah, 2 untuk Sedang, dan 3 untuk Tinggi
                8. Gula Darah: 1 untuk Rendah, 2 untuk Sedang, dan 3 untuk Tinggi
                9. Merokok: Jika anda perokok aktif, maka masukkan angka 0 untuk Ya, dan jika Tidak maka masukkan angka 1
                10. Alkohol: Jika anda peminum alkohol aktif, maka masukkan angka 0 untuk Ya, dan jika Tidak maka masukkan angka 1
                11. Aktivitas Fisik: Jika anda sering melakukan kegiatan fisik maka masukkan angka 0 untuk Ya, dan jika Tidak maka masukkan angka 1
                12. *** Target Prediksi ***
                Jika prediksi bernilai 0 maka anda tidak terkena penyakit jantung. 
                Namun jika prediksi bernilai 1 maka anda terkena penyakit jantung.""")
    st.write("---")
    #Menampilkan data dalam bentuk tabel
    st.subheader('Data Informasi:')
    st.dataframe(df)

#Memisahkan X independent and y dependent
X=df.iloc[:, 0:11].values
Y=df.iloc[:, -1].values

#Split data 75% sebagai data training dan 25% sebagai data testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.005, random_state=0)


#Fitur input oleh user
st.sidebar.title('Masukan Data Anda')
def get_user_input():
    Age_in_days = st.sidebar.number_input('Usia/Age')
    Gender = st.sidebar.slider('Jenis Kelamin/Gender', 1, 2, 1)
    Height = st.sidebar.number_input('Tinggi Badan/Height')
    Weight = st.sidebar.number_input('Berat Badan/Weight')
    AP_hi = st.sidebar.number_input('Tekanan Darah Sistolik/ap_hi')
    AP_lo = st.sidebar.number_input('Tekanan Darah Diastolik/ap_lo')
    Cholestrol = st.sidebar.number_input('Kolestrol/Cholestrol', 1, 3, 2)
    Glucose = st.sidebar.number_input('Gula Darah/Glucosa', 1, 3, 2)
    Smoking = st.sidebar.slider('Merokok/Smoke', 0, 1, 0)
    Alcohol = st.sidebar.slider('Alkohol/Alcohol', 0, 1, 0)
    Active = st.sidebar.slider('Aktivitas Fisik/Active', 0, 1, 1)

    #Menyimpan kamus data ke variabel
    user_data = {
        'Usia':Age_in_days,
        'Jenis Kelamin':Gender,
        'Tinggi Badan':Height,
        'Berat Badan':Weight,
        'Darah Tinggi':AP_hi,
        'Darah Rendah':AP_lo,
        'Kolestrol':Cholestrol,
        'Gula Darah':Glucose,
        'Perokok Aktif':Smoking,
        'Alkohol Aktif':Alcohol,
        'Aktivitas Fisik':Active
    }
    #Perulangan untuk kerangka data
    features = pd.DataFrame(user_data, index = [0])
    return features

#Menyimpan data user ke variabel
user_input = get_user_input()

#Menampilkan data input oleh pengguna
st.subheader('Data Input:')
st.write(user_input)

#Membuat dan Melatih Model
classifier = RandomForestClassifier()
classifier.fit(X_train, Y_train)
prediction = classifier.predict(X_test)

#Menampilkan model dalam metrics
st.subheader('Model Test Accuracy Score:')
score = accuracy_score(Y_test, prediction) * 100
st.write(score, '%')

#Menyimpan model prediksi pada variabel
prediction1 = classifier.predict(user_input)

#Menampilkan Hasil Klasifikasi
st.subheader('Hasil Prediksi: ')
st.write(prediction1)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)