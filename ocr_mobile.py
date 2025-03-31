import streamlit as st
from PIL import Image
import easyocr
import numpy as np

st.set_page_config(page_title="🔍 OCR Mobile App", layout="centered", page_icon="📸")

# CSS custom pour style
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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📸 OCR – Recherche de mot-clé</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Importe ou prends une photo contenant du texte, et nous détecterons le mot-clé !</div>', unsafe_allow_html=True)

# Sélection de la langue
lang = st.selectbox("🌐 Choisir la langue du texte :", ['fr', 'en', 'es', 'de'])

# Upload image
uploaded_file = st.file_uploader("🖼️ Importer une image ou prendre une photo :", type=["png", "jpg", "jpeg"])

# Mot-clé
keyword = st.text_input("🔍 Entrez un mot-clé à rechercher")

# Bouton de réinitialisation
if st.button("🧹 Réinitialiser"):
    st.experimental_rerun()

if uploaded_file is not None and keyword.strip():
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Image sélectionnée", use_container_width=True)

        reader = easyocr.Reader([lang], gpu=False, verbose=False)
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
