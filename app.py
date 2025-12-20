import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace
from scipy.spatial.distance import cosine
from PIL import Image

st.set_page_config(page_title="Verificador Facial com Máscara", layout="wide")
st.title("🎭 Verificação Facial: Foto vs. Máscara")

def process_face(img_pil):
    img_array = np.array(img_pil.convert('RGB'))
    img_cv2 = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    return img_cv2

col1, col2 = st.columns(2)

with col1:
    st.subheader("Foto de Referência (Base)")
    file1 = st.file_uploader("Upload Foto A", type=['jpg', 'png', 'jpeg'], key="1")
    if file1:
        img1 = Image.open(file1)
        st.image(img1, caption="Referência", use_container_width=True)

with col2:
    st.subheader("Foto com Máscara (Teste)")
    file2 = st.file_uploader("Upload Foto B", type=['jpg', 'png', 'jpeg'], key="2")
    if file2:
        img2 = Image.open(file2)
        st.image(img2, caption="Teste (Máscara)", use_container_width=True)

if file1 and file2:
    if st.button("Verificar se é a mesma pessoa"):
        with st.spinner("Analisando biometria facial..."):
            try:
                face1 = process_face(img1)
                face2 = process_face(img2)

                emb1 = DeepFace.represent(face1, model_name='ArcFace', enforce_detection=False)[0]["embedding"]
                emb2 = DeepFace.represent(face2, model_name='ArcFace', enforce_detection=False)[0]["embedding"]

                distancia = cosine(emb1, emb2)
                
                threshold = 0.65 
                is_same = distancia < threshold

                st.divider()
                if is_same:
                    st.success(f"✅ Identidade Confirmada! (Distância: {distancia:.4f})")
                    st.balloons()
                else:
                    st.error(f"❌ Identidades Diferentes. (Distância: {distancia:.4f})")
                
                st.info(f"O limite de similaridade é {threshold}. Resultados abaixo disso são considerados a mesma pessoa.")

            except Exception as e:
                st.error(f"Erro no processamento: {e}")