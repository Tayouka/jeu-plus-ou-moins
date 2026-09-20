import random
import streamlit as st

# Configuration de la page pour smartphone
st.set_page_config(page_title="Plus ou Moins", page_icon="🎮", layout="centered")

# Style sombre personnalisé
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    h1 { text-align: center; color: #ffffff; }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #238636;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎮 PLUS OU MOINS")
st.write("Je pense à un nombre entre 1 et 100. Devine lequel !")

# Initialisation des variables de jeu
if "nombre_secret" not in st.session_state:
    st.session_state.nombre_secret = random.randint(1, 100)
    st.session_state.essais = 0
    st.session_state.meilleur_score = "--"

# Champ de saisie pour le téléphone
proposition = st.number_input("Ton essai :", min_value=1, max_value=100, step=1, key="input_nombre")

# Boutons d'action
col1, col2 = st.columns(2)

with col1:
    if st.button("Valider 🚀"):
        st.session_state.essais += 1
        secret = st.session_state.nombre_secret
        
        if proposition < secret:
            st.warning("C'est **PLUS** ! ▲")
        elif proposition > secret:
            st.error("C'est **MOINS** ! ▼")
        else:
            st.success(f"🎉 **BRAVO !** Trouvé en {st.session_state.essais} coups !")
            if st.session_state.meilleur_score == "--" or st.session_state.essais < st.session_state.meilleur_score:
                st.session_state.meilleur_score = st.session_state.essais

with col2:
    if st.button("Recommencer 🔄"):
        st.session_state.nombre_secret = random.randint(1, 100)
        st.session_state.essais = 0
        st.rerun()

# Affichage des statistiques
st.divider()
st.info(f"**Tentatives :** {st.session_state.essais}  |  **Meilleur score :** {st.session_state.meilleur_score}")