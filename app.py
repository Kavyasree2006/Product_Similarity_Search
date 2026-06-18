
import streamlit as st

st.title("Fashion Product Similarity Search")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg","jpeg","png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Query Image")
    st.write("Top-5 similar products will be displayed here.")
