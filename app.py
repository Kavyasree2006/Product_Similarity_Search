import streamlit as st

st.set_page_config(
    page_title="Fashion Similarity Search",
    page_icon="👗",
    layout="wide"
)

# CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("👗 Fashion Product Similarity Search")

st.markdown("""
Discover visually similar fashion products using Deep Learning, ResNet50 and FAISS.
""")

# Metrics
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Images",
    "44,441"
)

col2.metric(
    "Embedding Size",
    "2048"
)

col3.metric(
    "Model",
    "ResNet50"
)

col4.metric(
    "Top-K",
    "5"
)

st.divider()

st.image(
    "https://images.unsplash.com/photo-1445205170230-053b83016050",
    use_container_width=True
)

st.markdown("""
### Features

✅ Deep Learning Embeddings

✅ FAISS Similarity Search

✅ Top-5 Recommendations

✅ Interactive Analytics

✅ Product Retrieval Dashboard
""")
