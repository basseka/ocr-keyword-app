import streamlit as st
from PIL import Image
import easyocr
import numpy as np

# Configuration de la page
st.set_page_config(page_title="🔍 OCR Mobile App", layout="centered", page_icon="📸")

# En-tête avec style
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        color: #2c3e50;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 30px;
    }
    .stTextInput > label {
        font-weight: bold;
    }
    .stFileUploader > label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📸 OCR – Recherche de mot-clé</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Importe ou prends une photo contenant du texte, et nous détecterons le mot-clé !</div>', unsafe_allow_html=True)

# Upload image
uploaded_file = st.file_uploader("🖼️ Importer une image ou prendre une photo :", type=["png", "jpg", "jpeg"])

# Mot-clé
keyword = st.text_input("🔍 Entrez un mot-clé à rechercher")

if uploaded_file is not None and keyword.strip():
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Image sélectionnée", use_container_width=True)

        reader = easyocr.Reader(['fr'], gpu=False)
        result = reader.readtext(np.array(image))

        full_text = " ".join([item[1] for item in result])
        st.markdown("<h4>🧾 Texte détecté :</h4>", unsafe_allow_html=True)
        st.code(full_text)

        if keyword.lower() in full_text.lower():
            st.success(f"✅ Mot-clé trouvé : {keyword}")
        else:
            st.warning("❌ Mot-clé non trouvé dans l’image")

    except Exception as e:
        st.error(f"❌ Une erreur est survenue lors du traitement : {str(e)}")
else:
    st.info("📥 Veuillez importer une image et saisir un mot-clé.")
