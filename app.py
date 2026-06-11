import streamlit as st
from FSM import TourismFSM

st.set_page_config(
    page_title="TourismBot Jogja",
    page_icon="🏝️",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #f1f5f9;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1e3a8a 0%,
        #2563eb 50%,
        #06b6d4 100%
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    background: linear-gradient(
        135deg,
        #2563eb,
        #06b6d4
    );
    padding: 50px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}

.feature-card {
    background: white;
    border-radius: 18px;
    padding: 22px;
    min-height: 150px;
    box-shadow:
        0px 4px 15px rgba(0,0,0,0.08);
    transition: 0.3s;
    margin-bottom: 15px;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow:
        0px 10px 25px rgba(0,0,0,0.12);
}

.feature-title {
    font-size: 18px;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 10px;
}

.example-box {
    background: white;
    border-left: 5px solid #2563eb;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 12px;
    box-shadow:
        0px 3px 10px rgba(0,0,0,0.05);
}

[data-testid="stAlert"] {
    border-radius: 15px;
}

[data-testid="stChatMessage"] {
    background: white;
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 10px;
    box-shadow:
        0px 2px 8px rgba(0,0,0,0.05);
}

[data-testid="stChatInput"] {
    border-radius: 15px;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    background-color: #2563eb;
    color: white;
    border: none;
    font-weight: bold;
    padding: 10px;
}

.stButton button:hover {
    background-color: #1d4ed8;
}


h1, h2, h3 {
    color: #0f172a;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SESSION
# =====================================
if "bot" not in st.session_state:
    st.session_state.bot = TourismFSM()
if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# SIDEBAR
# =====================================
with st.sidebar:
    st.title("🏝️ TourismBot Jogja")
    st.markdown("""
Chatbot Pariwisata Yogyakarta berbasis
Finite State Machine (FSM) dan
Natural Language Processing (NLP).
Membantu wisatawan memperoleh
informasi wisata secara cepat dan interaktif.
""")
    st.divider()
    if st.button("🔄 Reset Percakapan"):
        st.session_state.bot = TourismFSM()
        st.session_state.history = []
        st.rerun()

# =====================================
# HERO SECTION
# =====================================
st.markdown("""
<div class="hero">
<h1>🏝️ TourismBot Jogja</h1>
<h3>
Asisten Virtual Pariwisata Yogyakarta
</h3>
<p style="font-size:18px;">
Temukan destinasi wisata, kuliner,
penginapan, dan informasi perjalanan
di Yogyakarta melalui percakapan yang
mudah, cepat, dan interaktif.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# TENTANG
# =====================================
st.subheader("ℹ️ Tentang TourismBot")
st.write("""
TourismBot Jogja merupakan chatbot pariwisata yang dirancang untuk membantu wisatawan menemukan informasi mengenai destinasi wisata, penginapan, kuliner, transportasi, serta rekomendasi perjalanan di Daerah Istimewa Yogyakarta.
""")

# =====================================
# FITUR
# =====================================
st.subheader("✨ Layanan yang tersedia")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
<div class="feature-card">
<div class="feature-title">📍 Berdasarkan Lokasi</div>
Temukan destinasi wisata berdasarkan wilayah di Yogyakarta.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">💰 Berdasarkan Budget</div>
Temukan wisata gratis, murah, hingga premium.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">📝 Informasi Destinasi</div>
Lihat tiket masuk, jam operasional, fasilitas, dan deskripsi wisata.
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature-card">
<div class="feature-title">🏨 Rekomendasi Penginapan</div>
Cari penginapan yang berada dekat dengan destinasi wisata.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">🍜 Rekomendasi Kuliner</div>
Temukan kuliner populer di sekitar lokasi wisata.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">🚌 Rekomendasi Transportasi</div>
Dapatkan informasi akses dan transportasi menuju lokasi wisata.
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="feature-card">
<div class="feature-title">🔥 Wisata Populer</div>
Rekomendasi destinasi favorit wisatawan.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">🕒 Berdasarkan Waktu</div>
Cari wisata yang cocok dikunjungi pagi, siang, sore, atau malam.
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="feature-card">
<div class="feature-title">👨‍👩‍👧‍👦 Teman Perjalanan</div>
Rekomendasi wisata untuk keluarga, pasangan, atau teman.
</div>
""", unsafe_allow_html=True)


# =====================================
# CHATBOT
# =====================================
st.subheader("💬 Mulai Percakapan")
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
prompt = st.chat_input(
    "Tanyakan tentang wisata Yogyakarta..."
)
if prompt:
    st.session_state.history.append({
        "role": "user",
        "content": prompt
    })
    st.session_state.bot.step(prompt)
    reply = st.session_state.bot.get_response()
    st.session_state.history.append({
        "role": "assistant",
        "content": reply
    })
    st.rerun()