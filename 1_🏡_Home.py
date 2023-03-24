import streamlit as st
from PIL import Image

#Konfigurasi page title
st.set_page_config(page_title="stmik-heart-disease", page_icon=":heart:", layout="wide")

#Menampilkan Gambar
image=Image.open('logo_stmik_new.png')
st.image(image, use_column_width=True)

#Judul Display
st.title('Heart Disease Predict Using Machine Learning :heart:')

#Menampilkan beberapa berita mengenai penyakit jantung
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('download1.jpg')
    with text_column:
        st.subheader("Penyakit Jantung, Gejala, Penyebab, dan Cara Mengobati")
        st.write(
            """
            Penyakit jantung adalah kondisi ketika jantung mengalami gangguan.
            Bentuk gangguan itu sendiri bermacam-macam, bisa berupa gangguan pada pembuluh darah jantung, katup jantung, atau otot jantung. 
            Penyakit jantung juga dapat disebabkan oleh infeksi atau kelainan lahir.
            """
        )
        st.markdown("[Learn More...](https://www.alodokter.com/penyakit-jantung.com)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('heart.jpg')
    with text_column:
        st.subheader("Pencegahan dan Pengobatan Penyakit Jantung")
        st.write(
            """
          Sebelum terkena penyakit jantung, sebaiknya kita mengatur langkah pencegahan penyakit jantung. 
          Kita bisa melakukan tips sederhana dari Yayasan Jantung Indonesia agar tidak terkena penyakit jantung.
            """
        )
        st.markdown("[Learn More...](https://yankes.kemkes.go.id/view_artikel/701/pencegahan-dan-pengobatan-penyakit-jantung-koroner.com)")

# Kontak CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

with st.container():
    st.write("---")
    st.header("Silakan Masukkan Kritik dan Saran")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sekarsetya240@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Masukkan Nama Anda" required>
        <input type="email" name="email" placeholder="Masukkan Email Anda" required>
        <textarea name="message" placeholder="Masukkan Pesan" required></textarea>
        <button type="submit">Kirim</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)