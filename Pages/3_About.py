
import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ",
    layout="wide"
)

st.title("ℹ About The Project")

st.markdown("""
# 👗 Fashion Product Similarity Search System

An AI-powered visual recommendation system that retrieves fashion products visually similar to a query image using Deep Learning and Similarity Search techniques.
""")

st.divider()

# ================= Project Overview =================

st.header("📌 Project Overview")

st.info("""
This project uses image embeddings extracted from a pre-trained ResNet50 model and performs similarity search using FAISS and K-Nearest Neighbors to recommend visually similar fashion products.
""")

# ================= Tech Stack =================

st.header("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### Deep Learning
- TensorFlow
- Keras
- ResNet50
""")

with col2:
    st.success("""
### Machine Learning
- Scikit-Learn
- KNN
- FAISS
""")

with col3:
    st.success("""
### Dashboard
- Streamlit
- Plotly
- Pandas
""")

st.divider()

# ================= Features =================

st.header("🚀 Features")

st.markdown("""
✅ Deep Image Feature Extraction

✅ Visual Similarity Search

✅ Top-5 Product Recommendations

✅ FAISS-based Fast Retrieval

✅ Interactive Dashboard

✅ Product Analytics

✅ Search History

✅ Similarity Score Visualization

✅ Download Results

✅ Dataset Insights
""")

st.divider()

# ================= Workflow =================

st.header("⚙ Workflow")

st.code("""
Input Image
      ↓
Image Preprocessing
      ↓
ResNet50 Feature Extraction
      ↓
2048-Dimensional Embeddings
      ↓
FAISS + KNN Similarity Search
      ↓
Top-5 Similar Products
      ↓
Interactive Dashboard
""")

st.divider()

# ================= Dataset =================

st.header("📂 Dataset Information")

st.info("""
Dataset: Fashion Product Images Dataset

Source: Kaggle

Total Images: 44,441+

Contains:
- Apparel
- Footwear
- Accessories
- Multiple Colors
- Men, Women and Kids Fashion
""")

st.divider()

# ================= Model =================

st.header("🧠 Model Architecture")

col1, col2 = st.columns(2)

with col1:
    st.metric("Embedding Size", "2048")

    st.metric("Top Recommendations", "5")

with col2:
    st.metric("Base Model", "ResNet50")

    st.metric("Similarity Engine", "FAISS + KNN")

st.divider()

# ================= Learning Objectives =================

st.header("🎯 Learning Objectives")

st.markdown("""
- Understand Image Similarity Search
- Learn Feature Extraction using CNNs
- Build Recommendation Systems
- Work with Image Embeddings
- Implement Nearest Neighbor Search
- Develop End-to-End AI Applications
""")

st.divider()

# ================= Author =================

st.header("👨‍💻 Author")

st.success("""
Name: Kavya

Role: Engineering Student

Project: Fashion Product Similarity Search System

Built using Deep Learning and Computer Vision
""")

st.divider()

# ================= Footer =================

st.caption(
    "Built with ❤️ using TensorFlow, ResNet50, FAISS and Streamlit"
)
