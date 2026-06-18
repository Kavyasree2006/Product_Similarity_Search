import streamlit as st
import pandas as pd
import plotly.express as px
import time
import pickle
import faiss
from huggingface_hub import hf_hub_download 

# Download files from Hugging Face
embeddings_path = hf_hub_download(
    repo_id="kavyasree13/Product_Similarity_Search",
    filename="image_embeddings.pkl",
    repo_type="dataset"
)

faiss_path = hf_hub_download(
    repo_id="kavyasree13/Product_Similarity_Search",
    filename="faiss_index.bin",
    repo_type="dataset"
)

knn_path = hf_hub_download(
    repo_id="kavyasree13/Product_Similarity_Search",
    filename="knn_model.pkl",
    repo_type="dataset"
)

# Load embeddings and image names
with open(embeddings_path, "rb") as f:
    image_embeddings = pickle.load(f)

    # Load FAISS index
index = faiss.read_index(faiss_path)

with open(knn_path, "rb") as f:
    knn_model = pickle.load(f)

# ---------------- Sidebar ----------------

st.sidebar.title("👗 Fashion AI")

st.sidebar.info("""
Deep Learning Based Product Retrieval System
""")

threshold = st.sidebar.slider(
    "Similarity Threshold (%)",
    50,
    100,
    80
)

# ---------------- Search History ----------------

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Main Page ----------------

st.title("🔍 Search Similar Products")

uploaded_file = st.file_uploader(
    "Upload Fashion Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    if uploaded_file.name not in st.session_state.history:
        st.session_state.history.append(uploaded_file.name)

    st.sidebar.subheader("Search History")

    for item in st.session_state.history:
        st.sidebar.write("•", item)

    # Query image

    st.subheader("📷 Query Image")

    st.image(
        uploaded_file,
        width=300
    )

    start_time = time.time()

    with st.spinner("Finding similar products..."):

        # --------------------------------------------------
        # PUT YOUR FEATURE EXTRACTION + KNN SEARCH HERE
        # distances, indices = neighbors.kneighbors(query_feature)
        # --------------------------------------------------

        time.sleep(2)

    end_time = time.time()

    st.success(
        f"Retrieved products in {(end_time-start_time):.2f} sec"
    )

    st.divider()

    st.subheader("⭐ Top-5 Similar Products")

    cols = st.columns(5)

    similarity_scores = [96.8, 95.4, 93.6, 91.7, 89.9]

    product_names = [
        "Product 1",
        "Product 2",
        "Product 3",
        "Product 4",
        "Product 5"
    ]

    for i, col in enumerate(cols):

        with col:

            # Replace with actual image path
            col.image(
                "sample.jpg",
                use_container_width=True
            )

            col.progress(similarity_scores[i]/100)

            col.success(
                f"{similarity_scores[i]}%"
            )

            with col.expander("Product Details"):

                st.write("Category : Apparel")
                st.write("Gender : Men")
                st.write("Season : Summer")
                st.write("Color : Blue")

    st.divider()

    # ---------------- Similarity Chart ----------------

    st.subheader("📊 Similarity Scores")

    chart_df = pd.DataFrame({
        "Product": product_names,
        "Similarity": similarity_scores
    })

    fig = px.bar(
        chart_df,
        x="Product",
        y="Similarity",
        color="Similarity",
        text="Similarity",
        title="Top-5 Similarity Scores"
    )

    fig.update_layout(
        xaxis_title="Products",
        yaxis_title="Similarity (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ---------------- Download Results ----------------

    results_df = pd.DataFrame({
        "Product": product_names,
        "Similarity": similarity_scores
    })

    csv = results_df.to_csv(index=False)

    st.download_button(
        "⬇ Download Results CSV",
        csv,
        file_name="retrieval_results.csv",
        mime="text/csv"
    )

st.divider()

st.caption(
    "Built with ❤️ using Streamlit + ResNet50 + FAISS"
)
