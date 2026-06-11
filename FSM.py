from enum import Enum, auto
from engine import NLPEngine

class State(Enum):
    IDLE = auto()

class TourismFSM:
    def __init__(self):
        self.state = State.IDLE
        self.nlp = NLPEngine()
        self.response = ""
    def get_response(self):
        return self.response
    def step(self, user_input=""):
        user_input = user_input.lower().strip()
        intent = self.nlp.detect_intent(user_input)

        # =========================
        # GREETING
        # =========================
        if intent == "GREETING":
            self.response = """
                Halo 👋
                Selamat datang di Chatbot Pariwisata Yogyakarta.\n
                Saya dapat membantu:\n
                🏞️ Rekomendasi wisata\n
                📍 Wisata berdasarkan lokasi\n
                💰 Wisata berdasarkan budget\n
                📝 Informasi destinasi\n
                🏨 Penginapan terdekat\n
                🍜 Kuliner terdekat\n
                🚌 Transportasi menuju wisata\n
                🔥 Wisata populer\n
                🕒 Wisata berdasarkan waktu kunjungan\n
                👨‍👩‍👧‍👦 Wisata berdasarkan teman perjalanan\n
                Silakan tanyakan apa saja tentang wisata Jogja.
                """
            
        # =========================
        # KATEGORI
        # =========================
        elif intent == "ASK_CATEGORY":
            found = False
            for kategori, wisata in self.nlp.categories.items():
                if kategori in user_input:
                    self.response = f"""
                        🏞️ Jika Anda menyukai wisata {kategori}, berikut beberapa destinasi yang dapat dikunjungi:
                        """
                    for item in wisata:
                        self.response += f"\n• {item.title()}\n"
                    self.response += "\nSemoga salah satu destinasi tersebut sesuai dengan rencana perjalanan Anda 😊"
                    found = True
                    break
            if not found:
                self.response = """
                    Kategori wisata yang tersedia:
                    • Sejarah
                    • Alam
                    • Pantai
                    • Modern
                    • Kota
                    \n Silakan sebutkan kategori wisata yang Anda minati untuk mendapatkan rekomendasi destinasi yang sesuai.
                    """

        # =========================
        # LOKASI
        # =========================
        elif intent == "ASK_LOCATION":
            lokasi_dicari = None
            lokasi_list = [
                "sleman",
                "bantul",
                "gunungkidul",
                "kota yogyakarta"
            ]
            for lokasi in lokasi_list:
                if lokasi in user_input:
                    lokasi_dicari = lokasi
                    break
            if lokasi_dicari:
                hasil = []
                for nama, data in self.nlp.destinations.items():
                    if data["lokasi"] == lokasi_dicari:
                        hasil.append(nama)
                self.response = f"""
                    📍 Berikut beberapa destinasi wisata yang berada di wilayah {lokasi_dicari.title()}:
                    """
                for item in hasil:
                    self.response += f"\n• {item.title()}\n"
                self.response += "\nAnda dapat memilih destinasi yang paling sesuai dengan minat dan waktu kunjungan Anda."
            else:
                self.response = """
                    Pilih lokasi:
                    • Sleman
                    • Bantul
                    • Gunungkidul
                    • Kota Yogyakarta
                    \n Silakan sebutkan nama wilayah untuk mendapatkan rekomendasi destinasi wisata yang berada di sana.
                    """

        # =========================
        # BUDGET
        # =========================
        elif intent == "ASK_BUDGET":
            found = False
            for budget, wisata in self.nlp.budget.items():
                if budget in user_input:
                    self.response = f"""
                        💰 Jika Anda mencari wisata dengan budget {budget}, berikut rekomendasi yang dapat dipertimbangkan:
                        """
                    for item in wisata:
                        self.response += f"\n• {item.title()}\n"
                    self.response += "\nDestinasi tersebut cukup ramah di kantong dan tetap menarik untuk dikunjungi."
                    found = True
                    break
            if not found:
                self.response = """
                    Pilih Kategori budget:
                    • Gratis
                    • Murah
                    • Sedang
                    • Premium
                    \n Silakan sebutkan kategori budget untuk mendapatkan rekomendasi destinasi wisata yang sesuai dengan anggaran Anda.
                    """

        # =========================
        # INFO DESTINASI
        # =========================
        elif intent == "ASK_INFO":
            destination = self.nlp.find_destination(user_input)
            if destination:
                data = self.nlp.destinations[destination]
                self.response = f"""
                    🏛️ {destination.title()} adalah {data['deskripsi']}\n
                    Berikut informasi lengkapnya:\n
                    📍 Lokasi:
                    {data['lokasi'].title()}\n
                    🎟️ Tiket Masuk:
                    {data['tiket']}\n
                    🕒 Jam Operasional:
                    {data['jam']}\n
                    🏢 Fasilitas:
                    {data['fasilitas']}\n
                    Semoga informasi ini membantu merencanakan kunjungan Anda 😊
                """
            else:
                self.response = "Silakan sebutkan nama destinasi yang ingin diketahui informasinya."

        elif intent == "ASK_TICKET":
            destination = self.nlp.find_destination(user_input)
            if destination:
                data = self.nlp.destinations[destination]
                self.response = f"""
                    🎟️ Harga tiket masuk {destination.title()} adalah {data['tiket']}.
                    Silakan datang sesuai jam operasional yang berlaku.
                    """

        elif intent == "ASK_HOURS":
            destination = self.nlp.find_destination(user_input)
            if destination:
                data = self.nlp.destinations[destination]
                self.response = f"""
                    🕒 {destination.title()} buka pada pukul:
                    {data['jam']}
                    Pastikan datang sebelum jam tutup agar dapat menikmati wisata dengan nyaman.
                    """

        elif intent == "ASK_FACILITY":
            destination = self.nlp.find_destination(user_input)
            if destination:
                data = self.nlp.destinations[destination]
                self.response = f"""
                    🏢 Fasilitas yang tersedia di {destination.title()}:
                    {data['fasilitas']}
                    """

        elif intent == "ASK_ADDRESS":
            destination = self.nlp.find_destination(user_input)
            if destination:
                data = self.nlp.destinations[destination]
                self.response = f"""
                    📍 {destination.title()} berada di wilayah {data['lokasi'].title()}, Daerah Istimewa Yogyakarta.
                    """

        # =========================
        # HOTEL
        # =========================
        elif intent == "ASK_HOTEL":
            destination = self.nlp.find_destination(user_input)
            if destination and destination in self.nlp.hotels:
                self.response = f"""
                🏨 Jika Anda berencana berkunjung ke {destination.title()}, berikut beberapa penginapan yang dapat dipertimbangkan:\n
                """
                for hotel in self.nlp.hotels[destination]:
                    self.response += f"\n• {hotel}\n"
                self.response += "\nSemoga membantu menemukan tempat menginap yang nyaman 😊"
            else:
                self.response = "Sebutkan destinasi wisata yang ingin dicari penginapannya."

        # =========================
        # KULINER
        # =========================
        elif intent == "ASK_CULINARY":
            destination = self.nlp.find_destination(user_input)
            if destination and destination in self.nlp.culinary:
                self.response = f"""
                🍜 Setelah berwisata di {destination.title()}, Anda bisa mencoba kuliner berikut:
                """
                for item in self.nlp.culinary[destination]:
                    self.response += f"\n• {item}\n"
                self.response += "\nKuliner tersebut cukup populer dan mudah dijangkau dari lokasi wisata."
            else:
                self.response = "Sebutkan destinasi wisata yang ingin dicari kulinernya."

        # =========================
        # TRANSPORTASI
        # =========================
        elif intent == "ASK_TRANSPORT":
            destination = self.nlp.find_destination(user_input)
            if destination and destination in self.nlp.transportation:
                self.response = f"""
                🚌 Untuk menuju {destination.title()}, Anda dapat menggunakan beberapa pilihan transportasi berikut:
                """
                for item in self.nlp.transportation[destination]:
                    self.response += f"\n• {item}\n"
                self.response += "\nPilih transportasi yang paling sesuai dengan kebutuhan dan lokasi keberangkatan Anda."
            else:
                self.response = "Sebutkan destinasi wisata yang ingin dituju."

        # =========================
        # POPULER
        # =========================
        elif intent == "ASK_POPULAR":
            self.response = """
                🔥 Berikut beberapa destinasi wisata yang paling populer di Yogyakarta:
                """
            for wisata in self.nlp.popular_destinations:
                self.response += f"\n• {wisata.title()}\n"
            self.response += """
                \nDestinasi tersebut menjadi favorit wisatawan karena memiliki daya tarik dan pengalaman yang unik.
                """

        # =========================
        # REKOMENDASI UMUM
        # =========================
        elif intent == "ASK_RECOMMENDATION":
            self.response = """
                🌟 Rekomendasi wisata paling populer di Yogyakarta:
                🏛️ Candi Prambanan\n
                🏙️ Malioboro\n
                🏰 Keraton Yogyakarta\n
                🌊 Pantai Parangtritis\n
                🌇 HeHa Sky View\n
                ⛰️ Obelix Hills\n
                📸 Tebing Breksi\n
                Jika Anda ingin rekomendasi yang lebih spesifik, silakan sebutkan:
                • Budget
                • Lokasi
                • Waktu kunjungan
                • Teman perjalanan
                """

        # =========================
        # WAKTU KUNJUNGAN
        # =========================
        elif intent == "ASK_TIME":
            # mapping kata khusus
            if "sunset" in user_input:
                user_input += " sore"
            if "sunrise" in user_input:
                user_input += " pagi"
            found = False
            for waktu, wisata in self.nlp.visit_time.items():
                if waktu in user_input:
                    if waktu == "pagi":
                        title = "🌅 Rekomendasi wisata pagi hari"
                    elif waktu == "siang":
                        title = "☀️ Rekomendasi wisata siang hari"
                    elif waktu == "sore":
                        title = "🌇 Rekomendasi wisata sore hari / sunset"
                    else:
                        title = "🌙 Rekomendasi wisata malam hari"
                    self.response = f"{title}:\n\n"
                    for item in wisata:
                        self.response += f"• {item.title()}\n"
                    self.response += "\nSemoga membantu menyusun itinerary perjalanan Anda 😊"
                    found = True
                    break
            if not found:
                self.response = """
                    Saya dapat memberikan rekomendasi berdasarkan waktu kunjungan.
                    Pilihan yang tersedia:\n
                    🌅 Pagi\n
                    ☀️ Siang\n
                    🌇 Sore / Sunset\n
                    🌙 Malam\n
                    Contoh:
                    • Wisata pagi di Jogja
                    • Tempat melihat sunset
                    • Wisata malam yang ramai
                    """

        # =========================
        # TEMAN PERJALANAN
        # =========================
        elif intent == "ASK_COMPANION":
            if any(word in user_input for word in [
                "romantis",
                "honeymoon",
                "bulan madu",
                "couple"
            ]):
                user_input += " pasangan"
            found = False
            for tipe, wisata in self.nlp.travel_companion.items():
                if tipe in user_input:
                    self.response = f"""
                    👨‍👩‍👧‍👦 Jika Anda berlibur bersama {tipe}, berikut beberapa destinasi yang cocok untuk dikunjungi:
                    """
                    for item in wisata:
                        self.response += f"\n• {item.title()}\n"
                    self.response += "\nTempat-tempat tersebut memiliki fasilitas yang cukup lengkap dan nyaman untuk dinikmati bersama."
                    found = True
                    break
            if not found:
                self.response = """
                    Pilihan teman perjalanan:
                    • Keluarga
                    • Pasangan
                    • Teman
                    """

        # =========================
        # DEFAULT
        # =========================
        else:
            self.response = """
                Maaf, saya belum memahami pertanyaan Anda.
                Contoh pertanyaan:
                • Apa saja wisata sejarah di Jogja?
                • Wisata alam di Sleman
                • Wisata murah untuk keluarga
                • Berapa tiket masuk Prambanan?
                • Hotel dekat Malioboro
                • Kuliner dekat Pantai Baron
                • Cara menuju Kaliurang
                • Wisata populer di Jogja
                • Wisata malam di Jogja
                • Wisata romantis untuk pasangan
                """