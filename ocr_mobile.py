import streamlit as st
import numpy as np
from PIL import Image
import easyocr

st.set_page_config(page_title="OCR Mobile", layout="centered")
st.title("📸 OCR – Recherche de mot-clé (EasyOCR)")

uploaded_file = st.file_uploader("Prendre une photo ou choisir une image :", type=["png", "jpg", "jpeg"])
keyword = st.text_input("🔍 Entrez un mot-clé à rechercher")

if uploaded_file is not None and keyword.strip():
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image sélectionnée", use_container_width=True)

        reader = easyocr.Reader(['fr'], gpu=False)
        result = reader.readtext(np.array(image))

        full_text = " ".join([item[1] for item in result])
        st.subheader("🧾 Texte détecté :")
        st.text(full_text)

        if keyword.lower() in full_text.lower():
            st.success(f"✅ Mot-clé trouvé : {keyword}")
        else:
            st.warning("❌ Mot-clé non trouvé dans l’image")

    except Exception as e:
        st.error(f"❌ Une erreur est survenue lors du traitement : {str(e)}")
else:
    st.info("📥 Veuillez importer une image et saisir un mot-clé.")
