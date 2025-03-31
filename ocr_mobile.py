import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="OCR Mobile", layout="centered")
st.title("📸 OCR – Recherche de mot-clé")

# Uploader compatible mobile (caméra)
uploaded_file = st.file_uploader("Prendre une photo ou choisir une image :", type=["png", "jpg", "jpeg"])

keyword = st.text_input("🔍 Entrez un mot-clé à rechercher")

if uploaded_file and keyword:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image sélectionnée", use_column_width=True)

    # OCR
    text = pytesseract.image_to_string(image)
    st.subheader("🧾 Texte détecté :")
    st.text(text)

    if keyword.lower() in text.lower():
        st.success(f"✅ Mot-clé trouvé : {keyword}")
    else:
        st.warning("❌ Mot-clé non trouvé dans l’image")
