from pydoc import text
import re

class NLPEngine:
    def __init__(self):
        # DATABASE WISATA
        self.destinations = {
            "keraton yogyakarta": {
                "kategori": "sejarah",
                "lokasi": "kota yogyakarta",
                "tiket": "Rp15.000",
                "jam": "08.00 - 14.00",
                "deskripsi": "istana resmi Kesultanan Ngayogyakarta Hadiningrat yang didirikan oleh Sultan Hamengku Buwono I pada tahun 1755. Berperan sebagai pusat kebudayaan Jawa yang masih hidup (living monument), kompleks arsitektur megah ini memadukan filosofi kraton universal, ornamen ukiran khas Jawa kuno, serta sentuhan kolonial.",
                "fasilitas": "Toilet, Museum, Pemandu Wisata"
            },
            "taman sari": {
                "kategori": "sejarah",
                "lokasi": "kota yogyakarta",
                "tiket": "Rp15.000",
                "jam": "09.00 - 15.00",
                "deskripsi": "situs bekas taman kerajaan atau tempat peristirahatan rahasia Sultan beserta permaisuri yang dibangun pada pertengahan abad ke-18. Keunikan utama Taman Sari terletak pada arsitektur airnya, menara intai, serta bangunan masjid bawah tanah unik bertingkat melingkar (Sumur Gumuling) yang sangat disukai pecinta fotografi sejarah.",
                "fasilitas": "Toilet, Area Foto, Pemandu"
            },
            "candi prambanan": {
                "kategori": "sejarah",
                "lokasi": "sleman",
                "tiket": "Rp50.000",
                "jam": "06.30 - 17.00",
                "deskripsi": "kompleks candi Hindu terbesar di Indonesia yang dibangun pada abad ke-9 oleh dinasti Sanjaya. Arsitekturnya yang ramping dan menjulang setinggi 47 meter melambangkan kemegahan Trimurti (Siwa, Wisnu, Brahma) dengan relief epik Ramayana yang terpahat indah mengitari dinding luar bangunan utama candi.",
                "fasilitas": "Toilet, Mushola, Parkir"
            },
            "museum benteng vredeburg": {
                "kategori": "sejarah",
                "lokasi": "kota yogyakarta",
                "tiket": "Rp15.000",
                "jam": "08.00 - 20.00",
                "deskripsi": "museum perjuangan bangsa Indonesia yang Dibangun pertama kali pada tahun 1765 oleh kolonial Belanda dengan dalih menjaga keraton, bangunan bergaya parit melingkar ini aslinya difungsikan sebagai markas pemantau aktivitas internal kesultanan.",
                "fasilitas": "Museum, Toilet, Parkir"
            },
            "museum sonobudoyo": {
                "kategori": "sejarah",
                "lokasi": "kota yogyakarta",
                "tiket": "Rp10.000",
                "jam": "08.00 - 21.00",
                "deskripsi": "museum sejarah dan kebudayaan Jawa terlengkap kedua di Indonesia setelah Museum Nasional Jakarta. Menyimpan puluhan ribu koleksi artefak bernilai tinggi, mulai dari keris pusaka, topeng klasik, gamelan kuno, hingga naskah manuskrip bersejarah dari tanah Jawa, Madura, Bali, dan Lombok.",
                "fasilitas": "Museum, Bioskop, Toilet"
            },
            "kaliurang": {
                "kategori": "alam",
                "lokasi": "sleman",
                "tiket": "Rp10.000",
                "jam": "24 Jam",
                "deskripsi": "taman botani legendaris seluas 10 hektar di lereng Gunung Merapi yang menawarkan udara sejuk pegunungan. Tempat ini sangat ramah keluarga untuk berpiknik sembari menikmati jalur rimbun bervegetasi kaktus, herbal, serta bunga.",
                "fasilitas": "Parkir, Toilet, Kuliner"
            },
            "hutan pinus mangunan": {
                "kategori": "alam",
                "lokasi": "bantul",
                "tiket": "Rp5.000",
                "jam": "06.00 - 18.00",
                "deskripsi": "Wisata alam dengan hutan pinus yang menyajikan panorama hutan asri dengan jajaran pohon Pinus Sumatra yang menjulang tinggi. Waktu terbaik adalah pagi hari saat kabut tipis menyelimuti area, atau sore hari saat cahaya matahari menembus sela-sela pepohonan secara estetis.",
                "fasilitas": "Toilet, Spot Foto, Parkir"
            },
            "tebing breksi": {
                "kategori": "alam",
                "lokasi": "sleman",
                "tiket": "Rp10.000",
                "jam": "06.00 - 20.00",
                "deskripsi": "kawasan tambang batu kapur aktif menjadi objek wisata. Pasca penutupan karena temuan geologis, dinding batunya dipahat membentuk relief megah bertema cerita pewayangan seperti tokoh Arjuna hingga ukiran naga besar. Dari atas tebing, Anda dapat menyaksikan sunset dan pemandangan landasan Candi Prambanan dari kejauhan.",
                "fasilitas": "Toilet, Parkir, Spot Foto"
            },
            "bukit bintang": {
                "kategori": "alam",
                "lokasi": "gunungkidul",
                "tiket": "Gratis",
                "jam": "24 Jam",
                "deskripsi": "rest area bukit terbuka di perbatasan Bantul-Gunungkidul. Daya tarik utamanya adalah pemandangan bentang kota Yogyakarta dari ketinggian yang terlihat seperti taburan bintang gemerlap (city lights) saat malam hari, sembari menikmati jagung bakar atau wedang ronde hangat.",
                "fasilitas": "Kuliner, Parkir"
            },
            "air terjun sri gethuk": {
                "kategori": "alam",
                "lokasi": "gunungkidul",
                "tiket": "Rp15.000",
                "jam": "08.00 - 16.00",
                "deskripsi": "air terjun setinggi 50 meter yang mengalir indah membelah tebing karst dan langsung bermuara ke Sungai Oyo. Air terjun unik ini mengalir sepanjang tahun tanpa pernah kering meski musim kemarau. Anda bisa menikmati aktivitas berenang menggunakan ban pelampung atau menaiki wahana rafting santai.",
                "fasilitas": "Toilet, Perahu, Parkir"
            },
                "pantai parangtritis": {
                "kategori": "pantai",
                "lokasi": "bantul",
                "tiket": "Rp15.000",
                "jam": "24 Jam",
                "deskripsi": "ikon wisata legendaris yang memiliki pasir hitam pekat khas vulkanik yang membentang sangat luas. Pantai ini sangat terkenal dengan mitos Nyi Roro Kidul dan panorama sunset romantisnya. Wisatawan dilarang keras berenang hingga ke tengah laut karena memiliki karakteristik ombak Samudra Hindia yang besar dan arus bawah laut yang kuat.",
                "fasilitas": "Toilet, Warung Makan, ATV, Bendi, Parkir"
            },
            "pantai indrayanti": {
                "kategori": "pantai",
                "lokasi": "gunungkidul",
                "tiket": "Rp10.000 - Rp15.000",
                "jam": "24 Jam",
                "deskripsi": "pantai pasir putih yang dikelilingi perbukitan karang megah dengan air laut biru jernih. Pantai ini terkenal sebagai salah satu pantai paling bersih dan tertata rapi di Jogja.",
                "fasilitas": "Restoran, Gazebo, Mushola, Toilet, Penginapan"
            },
            "pantai drini": {
                "kategori": "pantai",
                "lokasi": "gunungkidul",
                "tiket": "Rp10.000 - Rp15.000",
                "jam": "24 Jam",
                "deskripsi": "pantai dua wajah dengan ombak tenang di satu sisi dan laut lepas di sisi lainnya. Di sisi barat, ombaknya cenderung tenang dan dangkal sehingga menjadi spot favorit wisatawan untuk bermain air dan mendayung perahu kano. Sedangkan di sisi timur, ombaknya langsung berhadapan dengan laut lepas. Di bagian tengah pantai terdapat sebuah pulau karang kecil yang bisa dinaiki pengunjung melalui jembatan kayu untuk melihat panorama laut dari ketinggian.",
                "fasilitas": "Kano, Gazebo, Warung Makan, Toilet, Mushola"
            },
            "pantai baron": {
                "kategori": "pantai",
                "lokasi": "gunungkidul",
                "tiket": "Rp15.000",
                "jam": "24 Jam",
                "deskripsi": "pantai unik berberntuk teluk yang diapit oleh dua bukit kapur raksasa. Keunikan utama tempat ini adalah adanya pertemuan antara air laut asin dengan aliran sungai bawah tanah air tawar yang bermuara langsung di bibir pantai. Pantai Baron menjadi surga wisata kuliner seafood di Gunungkidul karena wisatawan bisa membeli ikan segar hasil tangkapan nelayan langsung di tempat pelelangan.",
                "fasilitas": "Pasar Ikan, Restoran Seafood, Toilet, Parkir"
            },
            "pantai pok tunggal": {
                "kategori": "pantai",
                "lokasi": "gunungkidul",
                "tiket": "Rp10.000 - Rp15.000",
                "jam": "24 Jam",
                "deskripsi": "pantai pasir putih yang tersembunyi di balik tebing-tebing karang tegak lurus yang menjulang tinggi hingga 50 meter. Lokasinya yang tenang dan asri menjadikannya salah satu spot berkemah (camping ground) paling populer bagi anak muda untuk berburu pemandangan gugusan bintang malam.",
                "fasilitas": "Camping Ground, Gazebo, Toilet, Warung Makan"
            },
            "heha sky view": {
                "kategori": "modern",
                "lokasi": "gunungkidul",
                "tiket": "Rp20.000 - Rp25.000",
                "jam": "08.00 - 21.00",
                "deskripsi": "pelopor wisata swafoto modern di bukit Gunungkidul. Tempat ini menawarkan kombinasi restoran estetik dan taman bertingkat dengan pemandangan lanskap kota Jogja dari ketinggian. Suasana paling magis adalah sore menjelang malam hari saat lampu kota mulai menyala bergantian di bawah bukit.",
                "fasilitas": "Restoran, Sky Glass, Mushola, Toilet, Parkir"
            },
            "obelix hills": {
                "kategori": "modern",
                "lokasi": "sleman",
                "tiket": "Rp20.000 - Rp25.000",
                "jam": "07.00 - 21.00",
                "deskripsi": "wisata perbukitan dengan pemandangan sunset dan spot foto kekinian. Berdiri di atas bukit batu purba kawasan Prambanan, Obelix Hills menyajikan konsep tempat nongkrong terbuka dengan pemandangan matahari terbenam (sunset) yang dramatis. Wisatawan bisa bersantai di atas bean bag sembari menikmati musik dan angin sepoi-sepoi pegunungan.",
                "fasilitas": "Restoran, Bean Bag Area, Live Music, Toilet, Mushola"
            },
            "heha ocean view": {
                "kategori": "modern",
                "lokasi": "gunungkidul",
                "tiket": "Rp20.000 - Rp25.000",
                "jam": "08.00 - 21.00",
                "deskripsi": "destinasi modern yang mengusung gaya bangunan modern ala tebing Santorini Eropa yang kontras dengan latar belakang gulungan ombak laut lepas Samudra Hindia yang biru jernih.",
                "fasilitas": "Restoran, Glamping, Shuttle Bus, Toilet, Mushola"
            },
            "the lost world castle": {
                "kategori": "modern",
                "lokasi": "sleman",
                "tiket": "Rp30.000",
                "jam": "07.00 - 17.00",
                "deskripsi": "wisata kastel unik yang dibangun dari batu sisa erupsi Merapi. Terletak di zona rawan bencana lereng Gunung Merapi, The Lost World Castle dibangun memanfaatkan batu-batu sisa erupsi Merapi menjadi sebuah kastil megah mirip Benteng Takeshi atau kastil abad pertengahan Eropa. Udara di sini sangat sejuk dan sering kali diselimuti kabut tebal yang menambah suasana magis kastil di atas awan.",
                "fasilitas": "Spot Foto, Pujasera, Mushola, Toilet, Parkir"
            },
            "suraloka zoo": {
                "kategori": "modern",
                "lokasi": "sleman",
                "tiket": "Rp30.000",
                "jam": "09.00 - 17.00",
                "deskripsi": "kebun binatang edukasi modern bertaraf interaktif yang sangat bersih dan rapi di kawasan sejuk Kaliurang. Suraloka Zoo dirancang khusus agar anak-anak dan keluarga bisa berinteraksi, menyentuh, serta memberi makan secara langsung berbagai satwa jinak terpilih seperti kambing Merino, kelinci, burung hantu, alpaka, hingga berbagai jenis reptil eksotis.",
                "fasilitas": "Playground, Kafe, Mushola, Toilet, Area Satwa"
            },
            "malioboro": {
                "kategori": "kota",
                "lokasi": "kota yogyakarta",
                "tiket": "Gratis",
                "jam": "24 Jam",
                "deskripsi": "urat nadi pariwisata dan jantung budaya Kota Yogyakarta. Kawasan legendaris ini menyajikan pengalaman berbelanja suvenir, kerajinan, pakaian batik, hingga mencicipi kuliner khas jalanan sembari menikmati penampilan musisi jalanan yang interaktif di sepanjang trotoar.",
                "fasilitas": "Toilet, Bangku Taman, Andong, Becak, ATM"
            },
            "titik nol kilometer": {
                "kategori": "kota",
                "lokasi": "kota yogyakarta",
                "tiket": "Gratis",
                "jam": "24 Jam",
                "deskripsi": "pusat ruang publik terbuka bersejarah. Tempat ini menjadi titik kumpul favorit anak muda dan seniman lokal karena menawarkan latar belakang arsitektur kolonial megah (Indische) yang sangat fotogenik saat lampu kota mulai menyala.",
                "fasilitas": "Area Pedestrian, Bangku, Spot Foto"
            },
            "pasar beringharjo": {
                "kategori": "kota",
                "lokasi": "kota yogyakarta",
                "tiket": "Gratis",
                "jam": "08.30 - 21.00",
                "deskripsi": "pasar tertua di Yogyakarta yang memiliki nilai filosofis tinggi karena menjadi bagian dari Garis Imajiner Kraton. Pasar ini merupakan surga belanja grosir kain batik, pakaian tradisional, jamu herbal tradisional, barang antik, hingga kuliner legendaris seperti Sate Kere dan Pecel Senggol.",
                "fasilitas": "Parkir, Mushola, ATM, Toilet"
            },
            "kampung ketandan": {
                "kategori": "kota",
                "lokasi": "kota yogyakarta",
                "tiket": "Gratis",
                "jam": "24 Jam",
                "deskripsi": "kawasan Pecinan (Chinatown) bersejarah di Yogyakarta yang sudah eksis sejak abad ke-19 atas izin Sultan Hamengku Buwono II. Daya tarik utamanya adalah deretan bangunan berasitektur Tionghoa klasik berpadu gaya kolonial Eropa. Kawasan ini menjadi pusat perayaan tahunan Pekan Budaya Tionghoa Yogyakarta (PBTY) yang meriah.",
                "fasilitas": "Kuliner, Toko Emas, Spot Foto"
            },
            "alun alun kidul": {
                "kategori": "kota",
                "lokasi": "kota yogyakarta",
                "tiket": "Gratis",
                "jam": "24 Jam",
                "deskripsi": "halaman belakang Istana Kraton Ngayogyakarta Hadiningrat yang bertransformasi menjadi pusat hiburan malam rakyat. Aktivitas ikonik di sini adalah ritual Masangin, yaitu mencoba berjalan lurus melewati celah di antara dua pohon beringin kembar dengan mata tertutup. Selain itu, Anda bisa menyewa sepeda atau odong-odong kayuh berhiaskan lampu neon warna-warni untuk mengitari alun-alun.",
                "fasilitas": "Odong-Odong, Kuliner, Toilet, Mushola"
            }
        }

        self.categories = {
            "sejarah": [
                "keraton yogyakarta",
                "taman sari",
                "candi prambanan",
                "museum benteng vredeburg",
                "museum sonobudoyo"
            ],
            "alam": [
                "kaliurang",
                "hutan pinus mangunan",
                "tebing breksi",
                "bukit bintang",
                "air terjun sri gethuk"
            ],
            "pantai": [
                "pantai parangtritis",
                "pantai indrayanti",
                "pantai drini",
                "pantai baron",
                "pantai pok tunggal"
            ],
            "modern": [
                "heha sky view",
                "obelix hills",
                "heha ocean view",
                "the lost world castle",
                "suraloka zoo"
            ],
            "kota": [
                "malioboro",
                "titik nol kilometer",
                "pasar beringharjo",
                "kampung ketandan",
                "alun alun kidul"
            ]
        }

        self.budget = {
            "gratis": [
                "malioboro",
                "titik nol kilometer",
                "pasar beringharjo",
                "kampung ketandan",
                "alun alun kidul",
                "bukit bintang"
            ],
            "murah": [
                "keraton yogyakarta",
                "taman sari",
                "museum benteng vredeburg",
                "museum sonobudoyo",
                "hutan pinus mangunan",
                "tebing breksi",
                "air terjun sri gethuk",
                "pantai parangtritis",
                "pantai indrayanti",
                "pantai drini",
                "pantai baron",
                "pantai pok tunggal",
                "kaliurang"
            ],
            "sedang": [
                "heha sky view",
                "obelix hills",
                "heha ocean view",
                "the lost world castle",
                "suraloka zoo"
            ],
            "premium": [
                "candi prambanan"
            ]
        }

        self.popular_destinations = [
            "malioboro",
            "candi prambanan",
            "keraton yogyakarta",
            "taman sari",
            "pantai parangtritis",
            "heha sky view",
            "obelix hills",
            "tebing breksi",
            "bukit bintang",
            "hutan pinus mangunan"
        ]

        self.visit_time = {
            "pagi": [
                "keraton yogyakarta",
                "candi prambanan",
                "kaliurang",
                "hutan pinus mangunan",
                "pantai indrayanti",
                "pantai baron",
                "pantai drini",
                "pantai pok tunggal",
                "air terjun sri gethuk",
                "suraloka zoo"
            ],
            "siang": [
                "taman sari",
                "museum benteng vredeburg",
                "museum sonobudoyo",
                "pasar beringharjo",
                "pantai baron",
                "the lost world castle",
                "air terjun sri gethuk",
                "suraloka zoo"
            ],
            "sore": [
                "malioboro",
                "candi prambanan",
                "pantai parangtritis",
                "pantai indrayanti",
                "kaliurang",
                "tebing breksi",
                "hutan pinus mangunan",
                "heha sky view",
                "obelix hills",
                "heha ocean view",
                "kampung ketandan",
                "titik nol kilometer"
            ],
            "malam": [
                "malioboro",
                "alun alun kidul",
                "bukit bintang",
                "titik nol kilometer",
                "kampung ketandan",
                "heha sky view",
                "obelix hills",
                "museum sonobudoyo"
            ]
        }

        self.travel_companion = {
            "keluarga": [
                "malioboro",
                "candi prambanan",
                "pantai parangtritis",
                "keraton yogyakarta",
                "kaliurang",
                "alun alun kidul",
                "tebing breksi",
                "pantai indrayanti",
                "pantai baron",
                "pasar beringharjo",
                "museum benteng vredeburg",
                "pantai drini",
                "suraloka zoo"
            ],
            "pasangan": [
                "malioboro",
                "candi prambanan",
                "keraton yogyakarta",
                "taman sari",
                "pantai parangtritis",
                "tebing breksi",
                "heha sky view",
                "obelix hills",
                "heha ocean view",
                "bukit bintang",
                "pantai indrayanti"
            ],
            "teman": [
                "malioboro",
                "candi prambanan",
                "pantai parangtritis",
                "taman sari",
                "kaliurang",
                "alun alun kidul",
                "tebing breksi",
                "heha sky view",
                "titik nol kilometer",
                "pasar beringharjo",
                "hutan pinus mangunan",
                "obelix hills",
                "heha ocean view",
                "the lost world castle",
                "museum sonobudoyo",
                "air terjun sri gethuk",
                "pantai pok tunggal",
                "kampung ketandan"
            ]
        }

        self.hotels = {
            "malioboro": [
                "D'Pavilion Malioboro",
                "Amaris Hotel Malioboro",
                "Grand Malioboro Yogyakarta",
                "Ibis Styles Yogyakarta",
                "Hotel Neo Malioboro"
            ],
            "pasar beringharjo": [
                "KHAS Malioboro Hotel",
                "Malioboro Garden Hotel",
                "D'Pavilion Malioboro",
                "Melia Purosani Yogyakarta",
                "Homestay Beskalan"
            ],
            "kampung ketandan": [
                "Malioboro Garden Hotel",
                "Melia Purosani Yogyakarta",
                "D'Pavilion Malioboro",
                "KHAS Malioboro Hotel",
                "Whiz Hotel Malioboro"
            ],
            "titik nol kilometer": [
                "KHAS Malioboro Hotel",
                "Jambuluwuk Malioboro Hotel",
                "Ndalem Maharani Guest House",
                "Aveta Hotel Malioboro",
                "Ameera Boutique Hotel"
            ],
            "keraton yogyakarta": [
                "Ndalem Maharani Guest House",
                "The Phoenix Hotel",
                "Ndalem Kanoman Guesthouse",
                "Griya Patehan Homestay",
                "KHAS Malioboro Hotel"
            ],
            "museum sonobudoyo": [
                "Ndalem Maharani Guest House",
                "KHAS Malioboro Hotel",
                "Ndalem Kanoman Guesthouse",
                "Jambuluwuk Malioboro Hotel",
                "Aveta Hotel Malioboro"
            ],
            "museum benteng vredeburg": [
                "KHAS Malioboro Hotel",
                "D'Pavilion Malioboro",
                "Melia Purosani Yogyakarta",
                "Amaris Hotel Malioboro",
                "Jambuluwuk Malioboro Hotel"
            ],
            "taman sari": [
                "Kampoeng Djawa Hotel",
                "Ndalem Gamelan Guest House",
                "Griya Patehan Homestay",
                "Ndalem Maharani Guest House",
                "Greenhost Boutique Hotel"
            ],
            "alun alun kidul": [
                "Griya Patehan Homestay",
                "Kampoeng Djawa Hotel",
                "Ndalem Gamelan Guest House",
                "Ndalem Maharani Guest House",
                "Greenhost Boutique Hotel"
            ],
            "kaliurang": [
                "@K Hotel Kaliurang",
                "Griya Persada Resort",
                "D'Kaliurang Resort",
                "Onsen Resort Kaliurang",
                "Villa Bersole Kaliurang"
            ],
            "suraloka zoo": [
                "Griya Persada Resort",
                "D'Kaliurang Resort",
                "Joglo Amirta Resort",
                "Onsen Resort Kaliurang",
                "@K Hotel Kaliurang"
            ],
            "the lost world castle": [
                "Homestay Petung",
                "D'Kaliurang Resort",
                "Griya Persada Resort",
                "Joglo Amirta Resort",
                "@K Hotel Kaliurang"
            ],
            "candi prambanan": [
                "Poeri Devata Resort Hotel",
                "Amaranta Prambanan",
                "VRATA Hotel",
                "Sumberwatu Heritage",
                "Abhayagiri Villa"
            ],
            "tebing breksi": [
                "Amaranta Prambanan",
                "Sumberwatu Heritage",
                "Abhayagiri Villa",
                "Poeri Devata Resort Hotel",
                "VRATA Hotel"
            ],
            "obelix hills": [
                "Homestay Wukirharjo",
                "Sumberwatu Heritage",
                "Amaranta Prambanan",
                "Abhayagiri Villa",
                "Poeri Devata Resort Hotel"
            ],
            "bukit bintang": [
                "Contana Hotel Glamping",
                "HeHa Sky Camping",
                "@Hom Kidul Hotel",
                "Homestay Patuk Indah",
                "Amaranta Prambanan"
            ],
            "heha sky view": [
                "HeHa Sky Camping",
                "Contana Hotel Glamping",
                "@Hom Kidul Hotel",
                "Homestay Patuk Indah",
                "Sumberwatu Heritage"
            ],
            "hutan pinus mangunan": [
                "Mbah Mul Homestay",
                "Homestay Arya Mangunan",
                "Homestay Sukaria Dlingo",
                "Glamping Songgolangit",
                "Adinda Beach Hotel"
            ],
            "air terjun sri gethuk": [
                "Glamping Songgolangit",
                "Hotel Santika Gunungkidul",
                "Homestay Bleberan",
                "Drini Hills Diamond Villa",
                "Contana Hotel Glamping"
            ],
            "pantai parangtritis": [
                "Queen Of The South Resort",
                "Adinda Beach Hotel",
                "Losmen Pantai Depok",
                "Homestay Paris Indah",
                "Mbah Mul Homestay"
            ],
            "heha ocean view": [
                "HeHa Ocean Glamping",
                "Homestay Girikarto",
                "Queen Of The South Resort",
                "Baron Lighthouse Cottage",
                "Drini Hills Diamond Villa"
            ],
            "pantai baron": [
                "Baron Lighthouse Cottage",
                "Drini Hills Diamond Villa",
                "Homestay Kukup Indah",
                "Hotel Santika Gunungkidul",
                "Villa Kopiori"
            ],
            "pantai drini": [
                "Drini Hills Diamond Villa",
                "Baron Lighthouse Cottage",
                "Villa Kopiori",
                "Homestay Kukup Indah",
                "Putra Darma Guest House"
            ],
            "pantai indrayanti": [
                "Villa Kopiori",
                "Putra Darma Guest House",
                "Drini Hills Diamond Villa",
                "Griya Pantai Sundak",
                "Rock Garden Homestay"
            ],
            "pantai pok tunggal": [
                "Putra Darma Guest House",
                "Villa Kopiori",
                "Rock Garden Homestay",
                "Griya Pantai Sundak",
                "Drini Hills Diamond Villa"
            ]
        }

        self.culinary = {
            # ===== KOTA & IKONIK =====
            "malioboro": [
                "Gudeg Yu Djum Wijilan",
                "Gudeg Permata Bu Pudjo",
                "Lumpia Samijaya",
                "Oseng Mercon Bu Narti",
                "Yammie Pathuk"
            ],
            "keraton yogyakarta": [
                "Gudeg Yu Djum Wijilan",
                "Brongkos Handayani",
                "Gudeg Permata Bu Pudjo",
                "Yammie Pathuk"
            ],
            "taman sari": [
                "Brongkos Handayani",
                "Gudeg Yu Djum Wijilan",
                "Soto Tamansari"
            ],
            "museum benteng vredeburg": [
                "Lumpia Samijaya",
                "Gudeg Permata Bu Pudjo",
                "Yammie Pathuk"
            ],
            "museum sonobudoyo": [
                "Lumpia Samijaya",
                "Gudeg Permata Bu Pudjo",
                "Yammie Pathuk"
            ],
            "pasar beringharjo": [
                "Gulai Kambing Beringharjo",
                "Sate Kare Beringharjo",
                "Lumpia Samijaya"
            ],
            "kampung ketandan": [
                "Yammie Pathuk",
                "Gudeg Permata Bu Pudjo",
                "Lumpia Samijaya"
            ],
            "alun alun kidul": [
                "Brongkos Handayani",
                "Gudeg Yu Djum Wijilan",
                "Oseng Mercon Bu Narti"
            ],
            "titik nol kilometer": [
                "Oseng Mercon Bu Narti",
                "Lumpia Samijaya",
                "Gudeg Permata Bu Pudjo"
            ],

            # ===== PRAMBANAN & SEKITARNYA =====
            "candi prambanan": [
                "Soto Sampah Prambanan",
                "Wedang Kopi Prambanan",
                "Suwatu by Mil & Bay",
                "Ayam Goreng Kalasan"
            ],
            "tebing breksi": [
                "Suwatu by Mil & Bay",
                "Wedang Kopi Prambanan",
                "Ayam Goreng Kalasan"
            ],
            "obelix hills": [
                "Suwatu by Mil & Bay",
                "Wedang Kopi Prambanan",
                "Ayam Goreng Kalasan"
            ],

            # ===== KALIURANG & MERAPI =====
            "kaliurang": [
                "Jadah Tempe Mbah Carik",
                "Kopi Klotok",
                "Tongseng Mbah Ganis"
            ],
            "suraloka zoo": [
                "Jadah Tempe Mbah Carik",
                "Kopi Klotok",
                "Tongseng Mbah Ganis"
            ],
            "the lost world castle": [
                "Jadah Tempe Mbah Carik",
                "Kopi Klotok",
                "Tongseng Mbah Ganis"
            ],

            # ===== MANGUNAN =====
            "hutan pinus mangunan": [
                "Thiwul Ayu Eco",
                "Sate Klathak Pak Pong",
                "Sate Klathak Pak Bari"
            ],

            # ===== PANTAI SELATAN BANTUL =====
            "pantai parangtritis": [
                "Gudeg Manggar",
                "Seafood Pantai Depok",
                "Warung Ikan Bakar Parangtritis"
            ],

            # ===== GUNUNGKIDUL =====
            "pantai indrayanti": [
                "Seafood Pantai Indrayanti",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "pantai baron": [
                "Seafood Pantai Baron",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "pantai drini": [
                "Seafood Pantai Drini",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "pantai pok tunggal": [
                "Seafood Pantai Indrayanti",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "bukit bintang": [
                "Bakmi Jawa Piwulang Patuk",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "heha sky view": [
                "Bakmi Jawa Piwulang Patuk",
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum"
            ],
            "heha ocean view": [
                "Seafood Pantai Gesing",
                "Seafood Pantai Baron",
                "Sego Abang Jirak"
            ],
            "air terjun sri gethuk": [
                "Sego Abang Jirak",
                "Gatot dan Thiwul Yu Tum",
                "Bakmi Jawa Piwulang Patuk"
            ]
        }

        self.transportation = {
            # ===== SEJARAH & BUDAYA =====
            "keraton yogyakarta": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Andong",
                "Becak"
            ],
            "taman sari": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Becak"
            ],
            "candi prambanan": [
                "Trans Jogja",
                "KRL Commuter Line",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi"
            ],
            "benteng vredeburg": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Jalan Kaki dari Malioboro"
            ],
            "museum sonobudoyo": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Jalan Kaki dari Titik Nol"
            ],

            # ===== ALAM =====
            "kaliurang": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan",
                "Jeep Lava Tour"
            ],
            "hutan pinus mangunan": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "tebing breksi": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "bukit bintang": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "air terjun sri gethuk": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],

            # ===== PANTAI =====
            "pantai parangtritis": [
                "Bus AKDP",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "pantai indrayanti": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "pantai drini": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "pantai baron": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "pantai pok tunggal": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],

            # ===== REKREASI =====
            "heha sky view": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "obelix hills": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "heha ocean view": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],
            "the lost world castle": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan",
                "Jeep Lava Tour"
            ],
            "suraloka zoo": [
                "Motor Pribadi",
                "Mobil Pribadi",
                "Sewa Kendaraan"
            ],

            # ===== KOTA & IKONIK =====
            "malioboro": [
                "Trans Jogja",
                "KRL Commuter Line",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Andong",
                "Becak"
            ],
            "alun alun kidul": [
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Becak"
            ],
            "titik nol kilometer": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Jalan Kaki dari Malioboro"
            ],
            "pasar beringharjo": [
                "Trans Jogja",
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Jalan Kaki dari Malioboro"
            ],
            "kampung ketandan": [
                "Taksi Online",
                "Motor Pribadi",
                "Mobil Pribadi",
                "Jalan Kaki dari Malioboro"
            ]
        }

        self.alias = {

            # SEJARAH
            "prambanan": "candi prambanan",
            "candi prambanan": "candi prambanan",

            "keraton": "keraton yogyakarta",
            "keraton jogja": "keraton yogyakarta",

            "tamansari": "taman sari",
            "taman sari": "taman sari",

            "vredeburg": "museum benteng vredeburg",
            "benteng vredeburg": "museum benteng vredeburg",

            "sonobudoyo": "museum sonobudoyo",
            "museum sonobudoyo": "museum sonobudoyo",

            # ALAM
            "kaliurang": "kaliurang",

            "pinus mangunan": "hutan pinus mangunan",
            "hutan pinus": "hutan pinus mangunan",
            "mangunan": "hutan pinus mangunan",

            "breksi": "tebing breksi",
            "tebing breksi": "tebing breksi",

            "bukit bintang": "bukit bintang",

            "sri gethuk": "air terjun sri gethuk",
            "air terjun sri gethuk": "air terjun sri gethuk",

            # PANTAI
            "parangtritis": "pantai parangtritis",
            "pantai parangtritis": "pantai parangtritis",

            "indrayanti": "pantai indrayanti",
            "pantai indrayanti": "pantai indrayanti",

            "drini": "pantai drini",
            "pantai drini": "pantai drini",

            "baron": "pantai baron",
            "pantai baron": "pantai baron",

            "pok tunggal": "pantai pok tunggal",
            "pantai pok tunggal": "pantai pok tunggal",

            # MODERN
            "heha sky": "heha sky view",
            "heha sky view": "heha sky view",

            "obelix": "obelix hills",
            "obelix hills": "obelix hills",

            "heha ocean": "heha ocean view",
            "heha ocean view": "heha ocean view",

            "lost world": "the lost world castle",
            "lost world castle": "the lost world castle",

            "suraloka": "suraloka zoo",
            "suraloka zoo": "suraloka zoo",

            # KOTA
            "malioboro": "malioboro",

            "titik nol": "titik nol kilometer",
            "nol kilometer": "titik nol kilometer",
            "titik nol kilometer": "titik nol kilometer",

            "beringharjo": "pasar beringharjo",
            "pasar beringharjo": "pasar beringharjo",

            "ketandan": "kampung ketandan",
            "kampung ketandan": "kampung ketandan",

            "alkid": "alun alun kidul",
            "alun alun kidul": "alun alun kidul",
            "alun-alun kidul": "alun alun kidul"
        }

    def detect_intent(self, text):
        text = text.lower()

        if re.search(r"\b(halo|hai|hi|hello|selamat pagi|selamat siang|selamat sore|selamat malam)\b", text):
            return "GREETING"

        if re.search(r"\b(rekomendasi|saran|suggest|wisata terbaik|wisata wajib|tempat bagus|tempat menarik|jalan jalan kemana|liburan kemana)\b", text):
            return "ASK_RECOMMENDATION"

        if re.search(r"\b(harga tiket|tiket masuk|berapa tiket|harga masuk)\b", text):
            return "ASK_TICKET"

        if re.search(r"\b(jam buka|jam operasional|buka jam|tutup jam)\b", text):
            return "ASK_HOURS"

        if re.search(r"\b(fasilitas|sarana|toilet|parkir|mushola)\b", text):
            return "ASK_FACILITY"

        if re.search(r"\b(lokasi|alamat|ada di mana|dimana|letaknya)\b", text):
            return "ASK_ADDRESS"

        if re.search(r"\b(hotel|penginapan|akomodasi|homestay|villa|resort|guesthouse|guest house|menginap|tempat menginap)\b", text):
            return "ASK_HOTEL"

        if re.search(r"\b(kuliner|makan|makanan|tempat makan|restoran|jajanan|sarapan|makan siang|makan malam|gudeg|bakpia|angkringan|oleh oleh|oleh-oleh)\b", text):
            return "ASK_CULINARY"

        if re.search(r"\b(transportasi|rute|cara ke|cara menuju|akses|naik apa|menuju|perjalanan ke|jalan ke|pergi ke)\b", text):
            return "ASK_TRANSPORT"

        if re.search(r"\b(info|informasi|detail|deskripsi|tiket|harga tiket|jam buka|jam operasional|fasilitas|lokasi|alamat)\b", text):
            return "ASK_INFO"

        if re.search(r"\b(sejarah|budaya|alam|pantai|modern|kota)\b", text):
            return "ASK_CATEGORY"

        if re.search(r"\b(sleman|bantul|gunungkidul|kulon progo|kota yogyakarta)\b", text):
            return "ASK_LOCATION"

        if re.search(r"\b(gratis|murah|hemat|budget|premium)\b", text):
            return "ASK_BUDGET"

        if re.search(r"\b(populer|terkenal|hits|viral|favorit)\b", text):
            return "ASK_POPULAR"

        if re.search(r"\b(pagi|siang|sore|malam|sunrise|sunset)\b", text):
            return "ASK_TIME"

        if re.search(r"\b(keluarga|pasangan|teman|rombongan|anak|honeymoon|bulan madu|couple|romantis)\b", text):
            return "ASK_COMPANION"

        # nama destinasi langsung
        if self.find_destination(text):
            return "ASK_INFO"
        return "UNKNOWN"
    
    def find_destination(self, text):
        text = text.lower()
        for alias, destination in sorted(
            self.alias.items(),
            key=lambda x: len(x[0]),
            reverse=True
        ):
            if alias in text:
                return destination
        return None