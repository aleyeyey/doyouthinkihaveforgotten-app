import streamlit as st

st.title("aley's space :>")
st.write(
    "heyyiee, welcome to my space :O"
)
st.image("Snaptik.app_74466485541243159223.jpg")
st.image("1746691690002.jpg", width:200)
st.write("\n")
st.subheader("pacarnya jay mantap yey")
st.write(
    "lagi suka iris by goo goo dolls"
)
st.write(
    """
    - and i'd give up forever to touch you
    - cause i know that you feel me somehow
    """
)
st.header("check nilai ganjil genap katanya")
angka = st.number_input("write a number:", value=0, step=1)

if(angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
    else:
    st.write(f"{angka} adalah bilangan ganjil")
