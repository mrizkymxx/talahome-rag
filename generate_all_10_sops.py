import os
from build_sops import create_sop

OUT_DIR = "C:/Users/M RIZKY/talahome-rag/data/sops"
os.makedirs(OUT_DIR, exist_ok=True)

# 1. SOP LOG & GRADING
create_sop(
    os.path.join(OUT_DIR, "SOP-01_Penerimaan_dan_Grading_Kayu_Bahan_Baku.pdf"),
    "SOP PENERIMAAN DAN GRADING KAYU LOG & PAPAN MENTAH",
    "TAL-SOP-LOG-01", "Rev 03", "10 Januari 2026", "Logistik & Timber Sourcing",
    [
        ("1. Tujuan dan Ruang Lingkup", [
            "Prosedur ini menetapkan tata cara verifikasi legalitas, penerimaan fisik, pengukuran volume, dan seleksi kualitas (grading) bahan baku kayu jati (Tectona grandis) dan mahoni (Swietenia macrophylla) di area penimbunan kayu (log yard) PT TALAHOME Jepara.",
            "Berlaku untuk seluruh pasokan kayu log bulat maupun kayu gergajian (sawn timber) dari Perum Perhutani dan perkebunan rakyat terverifikasi."
        ]),
        ("2. Verifikasi Dokumen Legalitas (SVLK & V-Legal)", [
            "- Setiap pengiriman wajib disertai Surat Keterangan Sahnya Hasil Hutan Kayu (SKSHHK) atau Faktur Angkutan Kayu resmi.",
            "- Petugas QC Logistik wajib mencocokkan nomor barcode log fisik dengan lembar daftar kayu (DK).",
            "- Kayu tanpa dokumen resmi atau barcode rusak ditolak masuk dan dilarang dibongkar di area pabrik."
        ]),
        ("3. Standar Kriteria Grading Kayu Jati", [
            "Klasifikasi kualitas kayu jati untuk furnitur ekspor terbagi menjadi 3 grade utama:",
            "- Grade A (Export Quality Super): Bebas gubal (sapwood 0%), serat lurus searah, warna cokelat keemasan seragam, bebas mata mati dan retak hati rapuh.",
            "- Grade B (Commercial Quality): Gubal maksimal 10% dari luas permukaan, diperbolehkan mata sehat diameter maks 20 mm, tidak boleh ada lubang kumbang bubuk aktif.",
            "- Grade C (Rustic / Down Grade): Gubal 20-30%, mata kayu alami diperbolehkan untuk lini desain rustic, retak ujung maks 5 cm."
        ]),
        ("4. Cacat Kritis yang Ditolak Total (Reject Mutlak)", [
            "- Serangan kumbang bubuk kayu kering (Lyctus brunneus) aktif dengan ciri serbuk halus putih.",
            "- Hati busuk (heart rot) atau lubang gerowong pada inti log diameter lebih dari 50 mm.",
            "- Retak melintang radial sepanjang lebih dari 150 mm yang membelah serat utama."
        ]),
        ("5. Prosedur Pengukuran Volume dan Labeling", [
            "- Pengukuran diameter log menggunakan tongkat ukur terkalibrasi pada ujung pangkal dan ujung rebah (rata-rata keliling).",
            "- Perhitungan volume log bulat menggunakan rumus baku Brereton metrik.",
            "- Setiap log yang lolos inspeksi wajib dicat ujungnya dengan kode warna: Hijau (Grade A), Kuning (Grade B), Putih (Grade C) dan ditempel QR-Code pelacak batch."
        ])
    ]
)

# 2. SOP KILN DRY
create_sop(
    os.path.join(OUT_DIR, "SOP-02_Proses_Pengeringan_Kayu_Kiln_Dry.pdf"),
    "SOP PROSES PENGERINGAN KAYU (KILN DRY OVEN CHAMBER)",
    "TAL-SOP-DRY-02", "Rev 02", "15 Januari 2026", "Kiln Dry & Pengeringan",
    [
        ("1. Tujuan dan Target Parameter", [
            "Memastikan kadar air (Moisture Content - MC) kayu mencapai keseimbangan stabil untuk mencegah deformasi, melengkung (warping), dan retak (cracking) saat furnitur tiba di negara empat musim tujuan ekspor.",
            "- Target MC Pasar Eropa dan Amerika Serikat: 8% hingga 10% (toleransi absolut maks 12%).",
            "- Target MC Pasar Timur Tengah / Australia: 10% hingga 12%.",
            "- Target MC Pasar Domestik / Tropis: 12% hingga 14%."
        ]),
        ("2. Standar Penyusunan Papan (Stacking)", [
            "- Setiap tumpukan papan wajib menggunakan stiker kayu pengganjal (sticker spacer) ukuran seragam 25 x 25 mm berbahan kayu keras kering.",
            "- Jarak antar stiker maksimal 400 mm untuk mencegah papan bergelombang selama proses pengeringan.",
            "- Di atas tumpukan paling atas wajib diberi beban beton penekan (concrete weight) minimal 150 kg/m2."
        ]),
        ("3. Jadwal Siklus Pengeringan (Drying Schedule)", [
            "- Tahap 1 (Pemanasan Awal / Pre-heating): Suhu 45°C - 50°C, Kelembaban Relatif (RH) 85% selama 24 jam untuk melunakkan pori kayu.",
            "- Tahap 2 (Pengeringan Inti / Moisture Reduction): Suhu dinaikkan bertahap hingga 60°C - 65°C, RH diturunkan bertahap dari 70% ke 40% (laju penurunan MC maks 1.5% per hari untuk papan tebal 30 mm).",
            "- Tahap 3 (Pendinginan & Pengkondisian / Conditioning): Suhu 40°C, RH 60% selama 48 jam untuk meredakan tegangan dalam sel kayu (case hardening)."
        ]),
        ("4. Metode Pengujian Kadar Air (Quality Inspection)", [
            "- Petugas KD memeriksa 5 titik acak per stack menggunakan Moisture Meter tusuk tipe pin (Wagner / Delmhorst).",
            "- Jarum pin ditusukkan sedalam 1/3 tebal papan untuk membaca kadar air inti (core moisture), bukan hanya permukaan.",
            "- Jika 1 papan ditemukan MC > 12%, satu batch oven wajib diperpanjang proses conditioning minimal 2x24 jam."
        ]),
        ("5. Waktu Pengistirahatan (Conditioning Resting Period)", [
            "- Papan yang telah keluar dari oven dilarang langsung diproses di mesin serut/potong.",
            "- Wajib diistirahatkan (resting) di gudang transit beratap selama minimal 7 hari (7x24 jam) agar kadar air merata secara higroskopis."
        ])
    ]
)

# 3. SOP PERTUKANGAN & KONSTRUKSI
create_sop(
    os.path.join(OUT_DIR, "SOP-03_Konstruksi_Pertukangan_dan_Perakitan_Mebel.pdf"),
    "SOP KONSTRUKSI PERTUKANGAN DAN PERAKITAN MEBEL KAYU",
    "TAL-SOP-ASM-03", "Rev 04", "18 Januari 2026", "Produksi & Pertukangan",
    [
        ("1. Standar Sambungan Utama (Joinery Standard)", [
            "- Sambungan rangka beban utama (kaki meja, kaki kursi, rangka lemari) WAJIB menggunakan konstruksi Mortise and Tenon (Purus dan Lubang Purus).",
            "- Tebal tenon (purus) minimal 1/3 dari tebal kayu penopang dengan kedalaman masuk minimal 25 mm.",
            "- Celah sambungan (joint gap tolerance) maksimal 0.3 mm untuk menjamin kekuatan rekat film lem."
        ]),
        ("2. Standar Pasak dan Dowel", [
            "- Dowel kayu wajib menggunakan kayu keras beralur spiral (fluted dowel) diameter 10 mm atau 12 mm dengan kadar air 8-10%.",
            "- Dilarang menggunakan paku tembak pada titik sambungan yang menahan beban struktural utama."
        ]),
        ("3. Spesifikasi Lem Kayu Industri (Adhesive)", [
            "- Furnitur Indoor: Menggunakan lem Polyvinyl Acetate (PVAC) tipe Cross-linking D3 standar EN 204.",
            "- Furnitur Outdoor / Garden: Wajib menggunakan lem tipe D4 Waterproof atau Polyurethane (PU) 1-komponen bersertifikasi tahan air mendidih.",
            "- Pelumuran lem harus merata ke seluruh bidang tenon dan lubang mortise, bukan hanya tetesan parsial."
        ]),
        ("4. Prosedur Pengekleman (Clamping) dan Pembersihan", [
            "- Pengekleman rangka wajib menggunakan klem F atau klem pipa hidrolik dengan tekanan minimal 5-7 kg/cm2.",
            "- Waktu tahan klem minimal 45 menit sebelum tekanan dilepas.",
            "- Sisa lelehan lem di sudut sambungan wajib dibersihkan menggunakan kain basah hangat atau kape kayu saat lem masih basah/setengah kering (gel stage). Sisa lem yang membatu akan menolak penyerapan cat finishing."
        ]),
        ("5. Pemasangan Penguat Sudut (Corner Block)", [
            "- Setiap sudut rangka meja dan kursi wajib dipasangi kayu penguat sudut (corner block) segitiga tebal minimal 25 mm.",
            "- Dipasang dengan lem dan 3 titik sekrup ulir baja anti-karat panjang minimal 2 inci."
        ])
    ]
)

# 4. SOP SANDING
create_sop(
    os.path.join(OUT_DIR, "SOP-04_Pengamplasan_Kayu_Mentah_dan_Antar_Lapisan.pdf"),
    "SOP STANDAR PENGAMPLASAN KAYU MENTAH DAN ANTAR LAPISAN",
    "TAL-SOP-SND-04", "Rev 02", "20 Januari 2026", "Persiapan Permukaan & Sanding",
    [
        ("1. Prinsip Dasar Pengamplasan Ekspor", [
            "Pengamplasan bertujuan menutup cacat gores mesin serut, membuka pori secara seragam untuk penyerapan warna (stain), serta meratakan lapisan antar cat.",
            "- ARAH PENGAMPLASAN WAJIB SEARAH SERAT KAYU. Mengamplas melintang serat (cross-grain sanding) dikategorikan cacat fatal."
        ]),
        ("2. Urutan Amplas Mesin (Wide Belt / Stroke Sander)", [
            "- Grid 80 (Amplas Kasar): Meratakan sambungan papan laminasi, menghilangkan sisa lem membatu, dan membuang jejak mata pisau serut.",
            "- Grid 120 (Amplas Sedang): Menghilangkan goresan kasar dari Grid 80 dan menghaluskan permukaan dasar.",
            "- Grid 180 (Amplas Halus): Standar akhir kayu mentah sebelum masuk proses pewarnaan (wood stain) atau base coat."
        ]),
        ("3. Amplas Manual dan Sudut Profil", [
            "- Bagian ukiran, lis profil lengkung, dan sudut kaki wajib diamplas manual menggunakan kertas amplas Grid 180 hingga 240 yang dilapisi bantalan busa (foam sanding block).",
            "- Operator wajib meraba permukaan dengan telapak tangan tanpa sarung tangan untuk mendeteksi gelombang mikro."
        ]),
        ("4. Amplas Antar Lapisan (Intercoat Sanding)", [
            "- Setelah aplikasi Sanding Sealer mengering minimal 2 jam, permukaan wajib diamplas tipis menggunakan Grid 240 atau Grid 320.",
            "- Bertujuan memotong bulu kayu yang mengembang (raised grain) dan menciptakan profil mikro untuk daya rekat lapisan akhir (top coat)."
        ]),
        ("5. Prosedur Dust Cleaning (Pembersihan Debu)", [
            "- Sebelum diaplikasikan cat, seluruh partikel debu kayu wajib ditiup menggunakan air blow gun tekanan udara 6 bar.",
            "- Dilanjutkan dengan pengusapan menggunakan Tack Cloth (kain perekat debu) khusus finishing."
        ])
    ]
)

# 5. SOP FINISHING
create_sop(
    os.path.join(OUT_DIR, "SOP-05_Finishing_Sistem_PU_dan_Nitrocellulose.pdf"),
    "SOP SISTEM BAHAN KIMIA FINISHING (PU, NC & WATER-BASED)",
    "TAL-SOP-FNS-05", "Rev 03", "22 Januari 2026", "Finishing & Coating Division",
    [
        ("1. Klasifikasi Sistem Finishing Berdasarkan Kategori Produk", [
            "- Produk Indoor Klasik/Modern: Menggunakan sistem Nitrocellulose (NC Lacquer) atau Acid-Curing untuk menghasilkan tampilan serat kayu alami yang hangat (warm feel).",
            "- Produk Outdoor / Garden Furniture: Wajib menggunakan sistem Polyurethane (PU) 2-Komponen berdaya rekat tinggi dengan aditif UV Absorber untuk ketahanan cuaca ekstrem.",
            "- Produk Anak & Kamar Tidur: Wajib menggunakan sistem Water-based bersertifikasi non-toxic EN 71-3 dan bebas timbal (Lead-Free)."
        ]),
        ("2. Formulasi Rasio Pencampuran PU 2K", [
            "- Komponen A (Base Polyurethane): 2 bagian volume.",
            "- Komponen B (Hardener Isocyanate): 1 bagian volume.",
            "- Komponen C (Thinner PU Slow Drying): 1 bagian volume (viskositas 12-14 detik NK-2 cup pada suhu 28°C).",
            "- Pot life campuran: Maksimal 4 jam pada suhu ruang. Campuran melewati 4 jam wajib dibuang karena daya rekat menurun drastis."
        ]),
        ("3. Standar Ketebalan Lapisan Cat (Coating Thickness)", [
            "- Wet Film Thickness (WFT / Ketebalan Basah): 100 hingga 120 mikrometer (diukur dengan Comb Gauge).",
            "- Dry Film Thickness (DFT / Ketebalan Kering): 40 hingga 50 mikrometer setelah pengeringan sempurna 24 jam."
        ]),
        ("4. Pengendalian Lingkungan Spray Booth", [
            "- Tekanan udara kompresor spray gun diatur stabil pada 2.5 - 3.0 bar dengan nozzle 1.5 mm.",
            "- Suhu ruang aplikasi dipertahankan 25°C - 30°C dengan kelembaban udara (RH) maksimal 75%.",
            "- Dilarang melakukan pengecatan saat hujan lebat atau kelembaban udara > 80% karena menyebabkan kabut putih (blushing/blooming)."
        ]),
        ("5. Uji Daya Lekat Cat (Cross-Cut Adhesion Test ISO 2409)", [
            "- Setiap batch produksi mingguan wajib diuji menggunakan pisau cross-hatch cutter membuat 100 kotak kisi (1 mm spacing).",
            "- Ditempel lakban scotch tape khusus dan ditarik cepat pada sudut 60 derajat.",
            "- Standar kelulusan: Class 0 (tidak ada kelupasan sama sekali) atau Class 1 (kelupasan tepi kisi < 5%)."
        ])
    ]
)

# 6. SOP UPHOLSTERY
create_sop(
    os.path.join(OUT_DIR, "SOP-06_Upholstery_Pemasangan_Busa_dan_Kain_Fabric.pdf"),
    "SOP UPHOLSTERY, PEMASANGAN BUSA DAN KAIN PELAPIS JOK",
    "TAL-SOP-UPH-06", "Rev 01", "25 Januari 2026", "Upholstery & Soft Furnishing",
    [
        ("1. Spesifikasi Density Busa Dudukan dan Sandaran", [
            "- Dudukan Kursi / Sofa (Seat Cushion): Wajib menggunakan busa High Resilience (HR Foam) Density minimal D30 hingga D40 (30-40 kg/m3) untuk menjamin elastisitas tidak kempes minimal 5 tahun pemakaian.",
            "- Sandaran Kursi (Backrest): Menggunakan busa Medium Density D24 hingga D28.",
            "- Seluruh lapisan atas busa dilapisi dacron polyester wadding tebal 100-200 gram untuk memberikan efek empuk (crown contour)."
        ]),
        ("2. Standar Uji Ketahanan Kain (Fabric Specification)", [
            "- Uji Gesek Martindale: Kain jok wajib memenuhi minimal 25.000 rubs (commercial grade).",
            "- Ketahanan Luntur Warna (Color Fastness to Light): Minimal Grade 4 standar ISO 105-B02.",
            "- Standar Tahan Api (Fire Retardant): Untuk ekspor ke pasar USA wajib lulus uji TB 117-2013 (CAL 117), untuk pasar UK wajib lulus BS 5852 Source 0 & 1."
        ]),
        ("3. Teknik Pemasangan Lem dan Staples Rangka", [
            "- Perekatan busa ke kayu menggunakan adhesive spray non-flammable water-based bebas racun bau menyengat.",
            "- Penstaplesan kain ke rangka kayu menggunakan staples baja galvanis seri 80/10 atau 80/12 dengan jarak antar staples maksimal 15 mm.",
            "- Kain harus ditarik dengan tegangan simetris untuk mencegah tarikan pola miring (pattern distortion)."
        ]),
        ("4. Standar Penjahitan (Stitching Quality)", [
            "- Benang jahit wajib menggunakan nilon bonded ukuran size 40 atau size 30 tahan getas.",
            "- Kerapatan setikan: 5 hingga 6 jahitan per panjang 1 cm.",
            "- Area sambungan utama wajib menggunakan jahitan ganda (double stitching) dengan jarak garis jahitan 6 mm."
        ])
    ]
)

# 7. SOP QC FINAL
create_sop(
    os.path.join(OUT_DIR, "SOP-07_Quality_Control_Final_dan_Inspeksi_Pra_Kirim.pdf"),
    "SOP QUALITY CONTROL FINAL DAN INSPEKSI PRA-KIRIM (PDI)",
    "TAL-SOP-QC-07", "Rev 03", "27 Januari 2026", "Quality Assurance & QC",
    [
        ("1. Metode Penarikan Sampel Inspeksi (AQL Standard)", [
            "Inspeksi pra-kirim (Pre-Shipment Inspection) mengacu pada standar internasional ISO 2859-1 (MIL-STD-105E) General Inspection Level II:",
            "- Critical Defect (Cacat Kritis Fungsi / K3): AQL 0 (Toleransi 0 unit gagal).",
            "- Major Defect (Cacat Utama / Retak / Warna Belang): AQL 1.0.",
            "- Minor Defect (Cacat Kecil / Gores Halus < 5 mm): AQL 2.5."
        ]),
        ("2. Pengujian Stabilitas dan Keseimbangan Kaki (Rocking Test)", [
            "- Setiap unit kursi dan meja diletakkan di atas meja granit uji kerataan standar toleransi 0.1 mm.",
            "- Celah goyang (rocking gap) kaki kursi/meja yang diperbolehkan maksimal 1.0 mm.",
            "- Seluruh kaki wajib dipasangi adjuster foot glide atau bantalan felt pad tebal 3 mm anti-gores lantai."
        ]),
        ("3. Uji Beban Statis dan Dinamis Kursi", [
            "- Uji Beban Duduk: Kursi diberikan beban vertikal statis 150 kg di tengah dudukan selama 60 detik (tidak boleh ada keretakan atau suara patah).",
            "- Uji Sandaran: Sandaran didorong gaya horizontal 45 kg sebanyak 10 siklus berturut-turut."
        ]),
        ("4. Uji Ketahanan Permukaan Meja (Resistance Test)", [
            "- Uji Tahan Panas Kering: Cangkir berisi air mendidih 90°C diletakkan di atas permukaan meja selama 15 menit tanpa menimbulkan noda lingkar putih.",
            "- Uji Tahan Bahan Kimia Rumah Tangga: Tetesan alkohol 48% dan cuka makan dibiarkan selama 1 jam, kemudian dilap bersih (lapisan cat tidak boleh melunak atau berubah warna)."
        ]),
        ("5. Stempel Lolos QC dan Pelabelan Barcode", [
            "- Unit yang lolos 100% pemeriksaan ditempel stempel bertinta perak 'QC PASSED TALAHOME' beserta tanggal dan inisial inspektur di bawah dudukan/sisi tak terlihat.",
            "- Ditempel barcode nomor seri produksi untuk melacak riwayat tukang dan bahan baku."
        ])
    ]
)

# 8. SOP PACKAGING
create_sop(
    os.path.join(OUT_DIR, "SOP-08_Pengemasan_Ekspor_dan_Pemuatan_Kontainer.pdf"),
    "SOP PENGEMASAN STANDAR EKSPOR DAN PEMUATAN KONTAINER",
    "TAL-SOP-PKG-08", "Rev 04", "01 Februari 2026", "Packing, Warehouse & Shipping",
    [
        ("1. Spesifikasi Lapisan Kemasan (4-Layer Protection)", [
            "Setiap unit mebel wajib dikemas dengan urutan 4 lapis perlindungan:",
            "- Lapisan 1: Foam sheet busa polyethylene tebal 2 mm menyelimuti 100% permukaan kayu untuk mencegah gesekan abrasif.",
            "- Lapisan 2: Corner protector (pelindung sudut) dari karton tebal 5-ply bentuk L lebar 50 x 50 mm tebal 5 mm pada seluruh sudut tajam.",
            "- Lapisan 3: Single face corrugated wrap tebal 3 mm di sekeliling badan furnitur.",
            "- Lapisan 4: Master Box karton double-wall 5-layer K150/M150/K150 B/C Flute dengan kekuatan tekan ledak minimal 275 lbs/sq-in (Bursting Test)."
        ]),
        ("2. Pencegahan Kelembaban dan Jamur (Mold Prevention)", [
            "- Di dalam setiap kardus kemasan WAJIB dimasukkan Silica Gel Desiccant Clay ukuran 50 gram sebanyak 2 kantong (total 100 gram per box).",
            "- Pada saat stuffing ke dalam kontainer, wajib digantungkan Container Dry Bag berat 1 kg sebanyak minimal 4 kantong di dinding kontainer 20ft (atau 8 kantong untuk kontainer 40ft HC)."
        ]),
        ("3. Prosedur Uji Jatuh Kemasan (ISTA 1A Drop Test)", [
            "- Produk kemasan baru wajib lulus simulasi drop test dari ketinggian 76 cm ke lantai beton:",
            "- Tahapan: 1 kali jatuh pada sudut paling lemah, 3 kali jatuh pada rusuk terpendek/sedang/terpanjang, dan 6 kali jatuh pada masing-masing sisi rata.",
            "- Hasil: Isi mebel di dalam kardus tidak boleh mengalami retak, lecet cat, atau pergeseran sambungan."
        ]),
        ("4. Standar Pemuatan Kontainer (Container Stuffing)", [
            "- Kardus barang berat (meja, lemari) diletakkan di lantai kontainer paling bawah, kursi dan aksesoris di tumpukan atas.",
            "- Batas maksimal tumpukan kardus adalah 4 susun.",
            "- Sela kosong antar palet wajib diisi bantalan udara (Dunnage Air Bag) tekanan 0.2 bar agar muatan tidak bergeser saat ombak laut."
        ])
    ]
)

# 9. SOP K3
create_sop(
    os.path.join(OUT_DIR, "SOP-09_Keselamatan_Kesehatan_Kerja_K3_Pabrik_Kayu.pdf"),
    "SOP KESELAMATAN DAN KESEHATAN KERJA (K3) BENGKEL MEBEL",
    "TAL-SOP-K3-09", "Rev 02", "05 Februari 2026", "HSE & Manajemen Fasilitas",
    [
        ("1. Kebijakan Alat Pelindung Diri (APD) per Zona Kerja", [
            "- Area Pemotongan Kayu (Sawmill & Ripsaw): Wajib memakai kacamata pelindung (Safety Goggles), pelindung telinga (Ear Plug) reduksi suara min 25 dB, dan sepatu keselamatan ujung besi (Steel Toe Boot). Dilarang memakai sarung tangan kain longgar dekat mata pisau putar.",
            "- Area Finishing (Spray Booth): Wajib memakai masker respirator half-face dilengkapi filter uap organik tipe A2P3, kacamata kimia, dan pakaian kerja lengan panjang.",
            "- Area Gudang Logistik: Wajib mengenakan rompi visibilitas tinggi (Hi-Vis Vest) dan helm pengaman jika ada operasional forklift."
        ]),
        ("2. Pengendalian Bahaya Debu Kayu (Dust Control)", [
            "- Sistem Blower Dust Collector sentral wajib dinyalakan minimal 10 menit sebelum mesin serut dioperasikan.",
            "- Pembersihan serbuk gergaji dilakukan harian menggunakan vacuum cleaner industri bertenaga hisap tinggi, dilarang menyapu kering yang menerbangkan debu ke udara bebas."
        ]),
        ("3. Pencegahan Bahaya Kebakaran dan Bahan Mudah Terbakar", [
            "- AREA PABRIK TALAHOME ADALAH KAWASAN BEBAS ROKOK. Merokok hanya diizinkan di Gazebo K3 khusus di luar gerbang pagar pabrik.",
            "- Kain perca sisa pembersih tiner dan lem wajib dimasukkan ke dalam tong sampah besi tertutup rapat berisi air untuk mencegah pembakaran spontan (spontaneous combustion).",
            "- Alat Pemadam Api Ringan (APAR) jenis Dry Chemical Powder 6 kg dan CO2 5 kg dipasang di setiap tiang dengan radius jangkauan maksimal 15 meter."
        ]),
        ("4. Prosedur Tanggap Darurat dan Pertolongan Pertama (P3K)", [
            "- Kotak P3K standar Tipe B Permenaker wajib tersedia di setiap mandor lini kerja.",
            "- Setiap kecelakaan kerja, baik luka sayat ringan maupun kejadian nyaris celaka (near-miss), wajib dilaporkan kepada Koordinator HSE dalam waktu 1x24 jam untuk investigasi akar masalah."
        ])
    ]
)

# 10. SOP KLAIM BUYER
create_sop(
    os.path.join(OUT_DIR, "SOP-10_Penanganan_Klaim_Kerusakan_dan_Garansi_Buyer.pdf"),
    "SOP PENANGANAN KLAIM KERUSAKAN DAN GARANSI MUTU BUYER",
    "TAL-SOP-CLM-10", "Rev 02", "10 Februari 2026", "Customer Service & Legal Ekspor",
    [
        ("1. Kebijakan Garansi Produk PT TALAHOME", [
            "- Garansi Struktural Rangka Kayu: Berlaku selama 24 bulan sejak tanggal Bill of Lading (B/L) untuk cacat manufaktur (sambungan purus lepas, rangka retak alami, atau cacat bubuk kayu laten).",
            "- Garansi Lapisan Finishing: Berlaku selama 12 bulan terhadap perubahan warna ekstrem, pengelupasan (delaminasi cat), atau retak seribu (crazing).",
            "- Pengecualian Garansi (Exclusions): Garansi gugur jika produk mengalami benturan fisik akibat kesalahan handling forwarder, penyimpanan di ruangan dengan kelembaban abnormal (< 30% atau > 80% RH), atau paparan sinar matahari langsung untuk produk berlabel indoor."
        ]),
        ("2. Persyaratan Kelengkapan Berkas Klaim Buyer", [
            "Buyer wajib menyampaikan laporan klaim selambat-lambatnya 14 hari kalender setelah peti kemas kontainer dibuka di pelabuhan/gudang tujuan dengan melampirkan:",
            "- Formulir Resmi Claim Notification Form (TAL-FRM-CLM) yang ditandatangani.",
            "- Nomor Kontainer dan Nomor Purchase Order (PO).",
            "- Foto identitas stempel QC PASSED di bagian bawah produk.",
            "- Minimal 3 lembar foto detail kerusakan resolusi tinggi dari berbagai sudut.",
            "- Rekaman video continuous minimal 15 detik yang memperlihatkan kondisi cacat fisik."
        ]),
        ("3. Klasifikasi Solusi dan Kompensasi Finansial", [
            "- Kategori Klaim Minor (< $300): Diterbitkan Credit Note (CN) instan yang dipotongkan pada invoice order produksi berikutnya.",
            "- Kategori Kerusakan Komponen Lepas: PT TALAHOME mengirimkan suku cadang/komponen pengganti (replacement parts) melalui ekspedisi udara kurir ekspres maksimal 7 hari kerja.",
            "- Kategori Kerusakan Berat Struktural (> $1,000): Opsi penggantian unit 100% pada kontainer berikutnya atau refund transfer dana setelah persetujuan Direktur Operasional."
        ]),
        ("4. Tindakan Korektif Internal (CAPA Report)", [
            "- Setiap klaim yang disetujui wajib diterbitkan dokumen Corrective and Preventive Action (CAPA) oleh Departemen QA.",
            "- Rapat evaluasi teknis dipimpin General Manager dalam waktu 3 hari kerja untuk memastikan cacat serupa tidak berulang pada batch produksi berikutnya."
        ])
    ]
)

print("[COMPLETE] All 10 SOPs generated successfully in:", OUT_DIR)
