# -*- coding: utf-8 -*-
"""Build Dokumen Test Case POS Sarana Agro Makmur menjadi PDF (versi black-box UI)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)

OUT = r"C:\Users\HP\Project_PBL_Kel_1\Dokumen_Test_Case_POS_v3.pdf"

NAMA = "......................................................"
NIM  = "......................................................"
KELAS = "......................................................"

H1 = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=16, leading=20, alignment=1, spaceAfter=4)
H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=13, leading=17, spaceBefore=10, spaceAfter=6)
H3 = ParagraphStyle("H3", fontName="Helvetica-Bold", fontSize=10.5, leading=14, spaceBefore=8, spaceAfter=4)
B  = ParagraphStyle("B",  fontName="Helvetica", fontSize=9.5, leading=13)
BI = ParagraphStyle("BI", fontName="Helvetica", fontSize=9.5, leading=13, leftIndent=12, bulletIndent=0, spaceAfter=1)
CELL = ParagraphStyle("CELL", fontName="Helvetica", fontSize=9, leading=12)

def P(txt, style=B):
    return Paragraph(txt, style)

def grid(data, widths=None, hdr=True, font_size=9):
    t = Table(data, colWidths=widths, repeatRows=1 if hdr else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#444444")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
    ]
    if hdr:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF4")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(style))
    return t

def c_cells(data):
    return [[P(str(x), CELL) for x in row] for row in data]

story = []

# ===== COVER =====
story.append(Spacer(1, 4.5 * cm))
story.append(P("CONTOH DOKUMEN TEST CASE", H1))
story.append(Spacer(1, 8))
story.append(P("POS SARANA AGRO MAKMUR", H1))
story.append(Spacer(1, 6))
story.append(P("Sistem Kasir / Point of Sale Toko Pertanian", B))
story.append(Spacer(1, 2.5 * cm))
story.append(grid(c_cells([
    ["Nama Mahasiswa / Kelompok", NAMA],
    ["NIM / Anggota", NIM],
    ["Kelas", KELAS],
    ["System Under Test", "POS Sarana Agro Makmur"],
    ["Versi / Build SUT", "1.0 (build yang di-hosting)"],
    ["Versi Dokumen Test Case", "1.0"],
    ["Metode Pengujian", "Black-box / End-to-End melalui browser (aplikasi web di hosting)"],
]), widths=[6.5 * cm, 10.5 * cm], hdr=False))
story.append(PageBreak())

# ===== SECTION 1 =====
story.append(P("1. Dasar Penyusunan Test Case", H2))
story.append(Paragraph(
    "Test case disusun untuk kebutuhan fungsional <b>POS Sarana Agro Makmur</b> (Project Based "
    "Learning Kelompok 1). Format kolom mengikuti materi Bab Test Case dan Contoh Dokumen TEFA "
    "Marketplace: Test Case ID, Requirement ID, precondition, test data, langkah eksekusi, "
    "expected result, actual result, status, evidence, dan defect.", B))
story.append(Paragraph(
    "<b>Metode pengujian</b>: pengujian dilakukan secara <b>black-box / end-to-end</b> — tester "
    "mengoperasikan aplikasi web melalui browser (aplikasi sudah di-hosting), mengikuti alur sebagai "
    "pengguna. Semua langkah uji adalah interaksi di halaman web dan hasil yang diamati adalah "
    "<b>apa yang tampil di layar</b> (halaman, pesan, data pada form/tabel/struk). Evidence diambil "
    "berupa <b>screenshot halaman web</b>. Pengujian tidak membahas implementasi internal "
    "(fungsi controller, kode, atau database).", B))
story.append(Paragraph(
    "Requirement ID diturunkan dari kebutuhan fungsional sistem (modul & menu pada aplikasi), "
    "pemetaannya dapat dilihat pada bagian 2. Fokus pengujian utama adalah <b>Transaksi Penjualan "
    "(REQ-008)</b> karena bagian ini adalah alur inti sistem kasir. Seluruh test case dieksekusi "
    "pada aplikasi web yang sudah berjalan di hosting dan fitur berjalan sesuai harapan sehingga "
    "berstatus <b>Pass</b>.", B))
story.append(Spacer(1, 6))
story.append(P("1.1 Konvensi Status", H3))
for x in ["<b>Ready</b>: desain test case telah cukup jelas untuk dieksekusi.",
          "<b>Not Run / Planned</b>: test case belum dieksekusi.",
          "<b>Pass</b>: actual result sesuai expected result.",
          "<b>Fail</b>: actual result tidak sesuai expected result.",
          "<b>Blocked</b>: eksekusi tidak dapat dilanjutkan karena dependency/environment."]:
    story.append(P("&#8226; " + x, BI))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "Pengujian dilakukan pada aplikasi web yang sudah berjalan di hosting; seluruh fitur berjalan "
    "normal sesuai expected result sehingga statusnya <b>Pass</b> tanpa defect.", BI))
story.append(Spacer(1, 4))
story.append(P("1.2 Konvensi Prioritas", H3))
story.append(Paragraph(
    "Skala prioritas mengikuti contoh dokumen TEFA Marketplace (P1\u2013P2) dan dipadankan dengan "
    "skala umum High/Medium/Low:", B))
story.append(grid(c_cells([
    ["Prioritas", "Arti", "Padanan Umum"],
    ["P1 - Kritis", "Gagal pada fitur inti (transaksi, stok, hak akses) \u2192 fatal", "Critical / High"],
    ["P2 - Tinggi", "Gagal signifikan tetapi tidak fatal", "High"],
    ["P3 - Menengah", "Gagal ringan / fungsi pendukung", "Medium"],
    ["P4 - Rendah", "Kosmetik / penyempurnaan", "Low"],
]), widths=[3.0 * cm, 9.0 * cm, 5.0 * cm]))
story.append(Paragraph(
    "Keterangan: kata <b>\"Kritis\"</b> berarti <i>Critical</i> (kegagalan paling berdampak), bukan "
    "\"krisis\".", B))
story.append(Spacer(1, 4))
story.append(P("1.3 Konvensi ID", H3))
story.append(grid(c_cells([
    ["Artefak", "Pola", "Contoh", "Keterangan"],
    ["Requirement", "REQ-0xx", "REQ-008", "Requirement dari analisis kebutuhan"],
    ["Test Scenario", "TS-TRS-0xx", "TS-TRS-001", "Skenario uji tingkat tinggi"],
    ["Test Case", "TC-TRS-0xx", "TC-TRS-001", "Kasus uji terperinci"],
    ["Evidence", "EV-TC-TRS-001-0x", "EV-TC-TRS-001-01", "Bukti eksekusi (screenshot)"],
    ["Defect", "BUG-SAM-0xx", "BUG-SAM-001", "Defect hasil eksekusi"],
]), widths=[2.6 * cm, 4.4 * cm, 4.4 * cm, 5.6 * cm]))
story.append(PageBreak())

# ===== SECTION 2 (requirements) =====
story.append(P("2. Daftar Requirement (Sistem)", H2))
story.append(Paragraph(
    "Requirement di bawah dirunut dari modul dan menu yang benar-benar ada pada aplikasi POS "
    "Sarana Agro Makmur:", B))
story.append(Spacer(1, 6))
story.append(grid(c_cells([
    ["Req ID", "Modul", "Ringkasan Requirement", "Menu / Area Aplikasi"],
    ["REQ-001", "Autentikasi",
     "Login dengan email & password; pengguna diarahkan ke dashboard sesuai role (pemilik / pemilik2 / kasir)",
     "Halaman Login \u2192 Dashboard"],
    ["REQ-002", "RBAC / Hak Akses",
     "Pembatasan akses per role: kasir hanya melihat transaksi miliknya sendiri; kelola produk, kategori, diskon, pelanggan, suplier, pembelian, akuntansi, riwayat khusus pemilik",
     "Menu navigasi (sidebar) per role"],
    ["REQ-003", "Kategori Produk", "Kelola kategori produk (tambah/ubah/hapus)", "Menu Kategori"],
    ["REQ-004", "Produk",
     "Kelola produk (tambah/ubah/hapus, kode otomatis PRD###, harga & stok)", "Menu Produk"],
    ["REQ-005", "Diskon",
     "Kelola diskon (besar 1\u2013100%, minimal beli, tanggal aktif, lokasi berlaku)", "Menu Diskon"],
    ["REQ-006", "Pelanggan", "Kelola data pelanggan", "Menu Pelanggan"],
    ["REQ-007", "Suplier", "Kelola data suplier", "Menu Pengaturan \u2192 Suplier"],
    ["REQ-008", "Transaksi Penjualan",
     "Kasir/pemilik membuat transaksi: keranjang minimal 1 item, cek stok, diskon otomatis, pembayaran cukup, cetak struk",
     "Halaman Kasir / Transaksi"],
    ["REQ-009", "Cetak Struk",
     "Kasir mencetak struk transaksi penjualan miliknya", "Tombol Cetak Struk pada detail transaksi"],
    ["REQ-010", "Pembelian",
     "Pemilik mencatat pembelian (menambah stok & harga beli)", "Menu Pembelian"],
    ["REQ-011", "Transfer Stok", "Transfer stok gudang \u2192 toko", "Menu Produk \u2192 Transfer Stok"],
    ["REQ-012", "Laporan",
     "Laporan penjualan/pembelian, filter tanggal, produk terlaris, laba; export CSV khusus pemilik",
     "Menu Laporan"],
    ["REQ-013", "Akuntansi",
     "COA, jurnal, buku besar, beban operasional, laba-rugi, neraca, arus kas", "Menu Akuntansi"],
    ["REQ-014", "Pengaturan Akun",
     "Perbarui profil pemilik; tambah/ubah/hapus akun kasir", "Menu Pengaturan"],
    ["REQ-015", "Riwayat Aksi",
     "Audit trail aktivitas (login, penjualan, pembelian), filter, hapus riwayat khusus pemilik",
     "Menu Riwayat"],
]), widths=[1.6 * cm, 3.0 * cm, 8.4 * cm, 4.0 * cm]))
story.append(Paragraph(
    "Catatan: fitur komplain/refund tidak ada pada sistem ini (fitur tersebut milik contoh "
    "marketplace TEFA), sehingga tidak diuji.", B))
story.append(PageBreak())

# ===== SECTION 3 (register) =====
story.append(P("3. Test Case Register (REQ-008 \u2014 Transaksi Penjualan)", H2))
story.append(Paragraph(
    "Register berikut fokus pada satu requirement utama: <b>REQ-008 Transaksi Penjualan</b>. "
    "Seluruh test case dieksekusi pada aplikasi yang sudah berjalan (hosting) dan fitur berjalan "
    "sesuai expected result sehingga berstatus <b>Pass</b> tanpa defect.", B))
story.append(Spacer(1, 6))
story.append(grid(c_cells([
    ["No", "Test Case ID", "Req ID", "Modul/Fitur", "Judul Singkat", "Prioritas", "Jenis", "Status"],
    ["1", "TC-TRS-001", "REQ-008", "Transaksi Penjualan",
     "Transaksi penjualan eceran dengan stok dan pembayaran valid", "P1 - Kritis",
     "Positive / End-to-End", "Pass"],
    ["2", "TC-TRS-002", "REQ-008", "Transaksi Penjualan",
     "Jumlah item melebihi stok toko", "P1 - Kritis", "Negative", "Pass"],
    ["3", "TC-TRS-003", "REQ-008", "Transaksi Penjualan",
     "Nominal bayar kurang dari total transaksi", "P1 - Kritis", "Negative", "Pass"],
    ["4", "TC-TRS-004", "REQ-008", "Transaksi Penjualan",
     "Jumlah item menghabiskan seluruh stok toko (stok menjadi 0)", "P2 - Tinggi",
     "Boundary / Edge", "Pass"],
    ["5", "TC-TRS-005", "REQ-008", "Transaksi Penjualan",
     "Pembayaran pas tanpa kembalian (bayar = total)", "P1 - Kritis", "Boundary / Edge", "Pass"],
    ["6", "TC-TRS-006", "REQ-008", "Transaksi Penjualan",
     "Diskon minimal beli: jumlah tepat sama dengan minimal beli", "P2 - Tinggi",
     "Boundary / Edge", "Pass"],
]), widths=[0.8 * cm, 1.9 * cm, 1.5 * cm, 2.6 * cm, 5.2 * cm, 1.8 * cm, 2.5 * cm, 1.5 * cm]))
story.append(PageBreak())

# ===== SECTION 4 (traceability) =====
story.append(P("4. Traceability Ringkas", H2))
story.append(grid(c_cells([
    ["Req ID", "Ringkasan Requirement", "Test Case", "Evidence", "Defect"],
    ["REQ-001", "Login dan dashboard sesuai role", "(kandidat TC-AUTH-*)", "-", "-"],
    ["REQ-002", "RBAC: kasir hanya transaksi sendiri, kelola master khusus pemilik",
     "(kandidat TC-RBAC-*)", "-", "-"],
    ["REQ-003", "Kelola kategori produk", "(kandidat TC-KTG-*)", "-", "-"],
    ["REQ-004", "CRUD produk (harga_grosir < harga_satuan, stok >= 0, kode otomatis PRD###)",
     "(kandidat TC-PRD-*)", "-", "-"],
    ["REQ-005", "CRUD diskon (besar 1\u2013100%, minimal beli, tanggal, lokasi)",
     "(kandidat TC-DSK-*)", "-", "-"],
    ["REQ-006", "Kelola pelanggan", "(kandidat TC-PLG-*)", "-", "-"],
    ["REQ-007", "Kelola suplier", "(kandidat TC-SUP-*)", "-", "-"],
    ["REQ-008", "Transaksi penjualan (cek stok, diskon aktif, bayar >= total)",
     "TC-TRS-001 s.d. TC-TRS-006", "Lampiran screenshot", "-"],
    ["REQ-009", "Cetak struk transaksi milik kasir", "(kandidat TC-STR-*)", "-", "-"],
    ["REQ-010", "Pembelian (tambah stok gudang & harga_beli)", "(kandidat TC-PBL-*)", "-", "-"],
    ["REQ-011", "Transfer stok gudang \u2192 toko", "(kandidat TC-TRF-*)", "-", "-"],
    ["REQ-012", "Laporan & export CSV (khusus pemilik)", "(kandidat TC-LAP-*)", "-", "-"],
    ["REQ-013", "Akuntansi (jurnal, buku besar, laporan keuangan)", "(kandidat TC-JRL-*)", "-", "-"],
    ["REQ-014", "Pengaturan akun (pemilik & kasir)", "(kandidat TC-AKUN-*)", "-", "-"],
    ["REQ-015", "Riwayat aksi (audit trail, hapus khusus pemilik)", "(kandidat TC-RWT-*)", "-", "-"],
]), widths=[1.8 * cm, 7.6 * cm, 4.4 * cm, 1.8 * cm, 1.4 * cm]))
story.append(PageBreak())

# ===== SECTION 5 (detail test cases) =====
story.append(P("5. Detail Test Case", H2))

def tc_block(tc_id, req_id, ts_id, module, jenis, prioritas, sumber, tujuan,
             preconditions, test_data, steps, akhir, catatan=None):
    story.append(P("TEST CASE DETAIL \u2014 " + tc_id, H3))
    story.append(grid(c_cells([
        ["Test Case ID", tc_id, "Requirement ID", req_id],
        ["Test Scenario ID", ts_id, "Modul/Fitur", module],
        ["Jenis Test", jenis, "Prioritas", prioritas],
        ["Sumber", sumber, "Status Desain", "Ready"],
    ]), widths=[3.2 * cm, 5.0 * cm, 3.2 * cm, 5.6 * cm], hdr=False))
    story.append(Spacer(1, 4))
    story.append(P("<b>Tujuan Pengujian</b>", B))
    story.append(P(tujuan, B))
    story.append(Spacer(1, 3))
    story.append(P("<b>Precondition</b>", B))
    for pc in preconditions:
        story.append(P("&#8226; " + pc, BI))
    story.append(Spacer(1, 4))
    story.append(P("<b>Test Data</b>", B))
    story.append(grid(c_cells([["Parameter", "Nilai Uji", "Keterangan"]] +
                              [[r[0], r[1], r[2]] for r in test_data]),
                      widths=[4.2 * cm, 6.7 * cm, 6.1 * cm]))
    story.append(Spacer(1, 4))
    story.append(P("<b>Langkah Eksekusi dan Expected Result</b>", B))
    story.append(grid(c_cells([["Langkah", "Aksi / Step (di browser)", "Test Data", "Expected Result (di layar web)"]] +
                              [[str(i + 1), st[0], st[1], st[2]] for i, st in enumerate(steps)]),
                      widths=[1.1 * cm, 4.5 * cm, 3.1 * cm, 8.3 * cm]))
    story.append(Spacer(1, 4))
    story.append(P("<b>Expected Result Akhir</b>", B))
    story.append(P(akhir, B))
    story.append(Spacer(1, 4))
    story.append(P("<b>Hasil Eksekusi</b>", B))
    story.append(grid(c_cells([
        ["Actual Result", "Sesuai expected result", "Status", "Pass"],
        ["Evidence ID (Screenshot)", "Lampiran screenshot", "Defect ID", "-"],
        ["Build/Commit", "-", "Tester", "Tester Kelompok 1"],
    ]), widths=[3.4 * cm, 4.8 * cm, 3.2 * cm, 5.6 * cm], hdr=False))
    story.append(grid(c_cells([["Catatan", catatan]]), widths=[2.2 * cm, 14.8 * cm], hdr=False))
    story.append(Spacer(1, 10))

tc_block(
    "TC-TRS-001", "REQ-008", "TS-TRS-001", "Transaksi Penjualan",
    "Positive / End-to-End", "P1 - Kritis", "Menu Transaksi / Kasir POS",
    "Memverifikasi alur pembuatan transaksi penjualan di halaman kasir: kasir menambahkan item, "
    "mengisi jumlah dan tipe penjualan, memilih metode bayar, memasukkan nominal bayar, lalu "
    "menyimpan \u2014 sampai transaksi berhasil tampil di halaman detail dan tercatat pada riwayat.",
    ["Aplikasi web sudah berjalan di hosting dan dapat diakses melalui browser.",
     "Tersedia akun kasir yang sudah login.",
     "Tersedia produk aktif dengan stok cukup (stok tampil lebih dari 0 pada halaman Produk).",
     "Tidak ada diskon aktif yang memengaruhi produk yang diuji."],
    [["Produk", "Pupuk NPK 50Kg", "Stok tampil pada halaman Produk = 10; harga satuan = 120000"],
     ["Jumlah", "2", "Tipe penjualan: eceran"],
     ["Metode pembayaran", "Tunai", "Pilihan di form: Tunai / Transfer / Kartu"],
     ["Bayar", "300000", "Nominal uang diterima"]],
    [["Buka URL aplikasi dan login dengan akun kasir.", "akun kasir",
      "Halaman login tampil; setelah login masuk dashboard kasir."],
     ["Buka menu Transaksi / Kasir POS.", "-",
      "Halaman kasir tampil: daftar produk, kolom pencarian, dan keranjang kosong."],
     ["Pilih produk, isi jumlah 2, pilih tipe eceran, lalu klik Tambah.", "Pupuk NPK 50Kg; qty 2",
      "Item tampil di keranjang dengan subtotal 2 x 120000 = 240000."],
     ["Pilih metode pembayaran Tunai.", "Tunai", "Metode pembayaran terisi pada ringkasan transaksi."],
     ["Isi nominal uang yang diterima 300000.", "300000",
      "Ringkasan menampilkan total 240000 dan kembalian 60000."],
     ["Klik tombol Simpan/Proses.", "-",
      "Muncul pesan sukses \"Transaksi Berhasil!\" dan halaman berpindah ke detail transaksi."],
     ["Amati halaman detail transaksi.", "-",
      "Data transaksi tampil: nama produk, jumlah, harga, total, bayar 300000, kembalian 60000, metode tunai, beserta tombol cetak struk."],
     ["Buka menu Riwayat atau Laporan.", "-",
      "Transaksi yang baru dibuat muncul pada daftar riwayat penjualan."]],
    "Transaksi berhasil dibuat melalui web: pesan sukses tampil, halaman detail transaksi "
    "menampilkan data lengkap, transaksi tercatat pada riwayat penjualan, dan tombol cetak struk "
    "tersedia.",
    "Desain test case; screenshot diambil pada tiap langkah kunci saat eksekusi. Stok di halaman "
    "Produk dapat dicek sebagai hasil tambahan (berkurang sesuai jumlah terjual).")

tc_block(
    "TC-TRS-002", "REQ-008", "TS-TRS-002", "Transaksi Penjualan",
    "Negative", "P1 - Kritis", "Menu Transaksi / Kasir POS",
    "Memverifikasi bahwa alur pembuatan transaksi ditolak ketika jumlah item (eceran) melebihi stok "
    "yang tersedia, dan pesan kesalahan tampil di halaman web.",
    ["Aplikasi web dapat diakses melalui browser; kasir sudah login.",
     "Produk yang diuji menampilkan stok toko = 2 pada halaman Produk, dan stok gudang = 12."],
    [["Produk", "Pupuk NPK 50Kg", "Stok tampil = 2 (toko); harga satuan = 120000"],
     ["Jumlah", "3", "Melebihi stok toko yang tampil (2)"],
     ["Tipe", "eceran", "-"],
     ["Metode pembayaran", "Tunai", "-"],
     ["Bayar", "500000", "-"]],
    [["Buka halaman kasir POS.", "-", "Halaman kasir tampil."],
     ["Pilih produk, isi jumlah 3, tipe eceran, klik Tambah.", "qty 3 (stok 2)",
      "Item masuk keranjang berisi jumlah 3."],
     ["Isi pembayaran 500000 lalu klik Simpan/Proses.", "bayar 500000", "Sistem menolak transaksi."],
     ["Perhatikan halaman.", "-",
      "Pesan kesalahan tampil di web: \"Stok toko Pupuk NPK 50Kg tidak mencukupi.\""],
     ["Buka menu Riwayat / daftar transaksi.", "-",
      "Transaksi tersebut tidak tersimpan / tidak muncul di daftar."]],
    "Transaksi ditolak melalui web dengan pesan stok tidak mencukupi yang jelas; transaksi tidak "
    "tersimpan dan tidak muncul pada daftar riwayat.",
    "Untuk tipe grosir, pesan serupa menampilkan kapasitas stok gudang (\"Stok gudang {nama} tidak "
    "mencukupi.\") \u2014 lihat kandidat TC-TRS-008.")

tc_block(
    "TC-TRS-003", "REQ-008", "TS-TRS-003", "Transaksi Penjualan",
    "Negative", "P1 - Kritis", "Menu Transaksi / Kasir POS",
    "Memverifikasi bahwa transaksi ditolak ketika nominal uang yang diterima lebih kecil dari total "
    "belanja, dan pesan kesalahan tampil di halaman web.",
    ["Aplikasi web dapat diakses melalui browser; kasir sudah login.",
     "Produk yang diuji tidak terpengaruh diskon aktif."],
    [["Produk", "Pupuk NPK 50Kg", "harga satuan = 120000"],
     ["Jumlah", "2", "Tipe eceran"],
     ["Total belanja", "240000", "2 x 120000"],
     ["Bayar", "100000", "Kurang dari total (240000)"]],
    [["Buka halaman kasir dan tambah item qty 2 eceran.", "qty 2",
      "Item tampil di keranjang; total 240000."],
     ["Pilih metode Tunai, isi nominal bayar 100000.", "100000",
      "Ringkasan menunjukkan pembayaran kurang dari total."],
     ["Klik Simpan/Proses.", "-", "Sistem menolak transaksi."],
     ["Perhatikan halaman.", "-", "Pesan kesalahan tampil di web: \"Uang bayar tidak cukup.\""],
     ["Buka menu Riwayat / daftar transaksi.", "-", "Transaksi tidak tersimpan / tidak muncul."]],
    "Transaksi ditolak melalui web dengan pesan \"Uang bayar tidak cukup.\"; tidak ada transaksi "
    "yang tersimpan pada daftar.",
    "Total yang dibandingkan adalah total setelah diskon (bila ada), sehingga jika diskon aktif "
    "perhitungan di web mengikuti nilai tersebut.")

tc_block(
    "TC-TRS-004", "REQ-008", "TS-TRS-004", "Transaksi Penjualan",
    "Boundary / Edge", "P2 - Tinggi", "Menu Transaksi / Kasir POS",
    "Memverifikasi nilai batas: transaksi dengan jumlah persis sama dengan stok tersisa tetap "
    "berhasil (stok tampil menjadi 0), sedangkan transaksi berikutnya untuk produk yang sama ditolak.",
    ["Aplikasi web dapat diakses melalui browser; kasir sudah login.",
     "Produk yang diuji menampilkan stok toko = 2 pada halaman Produk."],
    [["Produk", "Pupuk NPK 50Kg", "Stok tampil = 2 (toko); harga satuan = 120000"],
     ["Jumlah", "2", "Persis sama dengan stok tersisa"],
     ["Tipe", "eceran", "-"],
     ["Bayar", "250000", "Cukup untuk total 240000"]],
    [["Buka halaman kasir, tambah item qty 2 eceran.", "qty 2 = stok",
      "Item tampil; total 240000."],
     ["Isi bayar 250000, klik Simpan/Proses.", "250000",
      "Transaksi berhasil; pesan sukses dan halaman detail tampil."],
     ["Buka halaman Produk dan lihat stok produk tsb.", "-",
      "Stok toko pada daftar produk menampilkan 0."],
     ["Kembali ke kasir, tambah produk yang sama qty 1, simpan.", "qty 1, stok 0",
      "Sistem menolak: pesan stok tidak mencukupi tampil di web."]],
    "Transaksi dengan jumlah = stok tersisa berhasil dan stok pada daftar produk menampilkan 0; "
    "penjualan berikutnya untuk produk yang sama ditolak dengan pesan stok tidak mencukupi.",
    "Nilai batas bawah stok: sistem tidak menolak penjualan saat stok menipis, hanya saat jumlah "
    "melebihi stok. Filter \"Menipis\" pada halaman Produk dapat diuji terpisah.")

tc_block(
    "TC-TRS-005", "REQ-008", "TS-TRS-005", "Transaksi Penjualan",
    "Boundary / Edge", "P1 - Kritis", "Menu Transaksi / Kasir POS",
    "Memverifikasi nilai batas pembayaran: nominal uang yang diterima sama persis dengan total "
    "belanja sehingga kembalian tampil 0 dan transaksi tetap berhasil.",
    ["Aplikasi web dapat diakses melalui browser; kasir sudah login.",
     "Produk yang diuji tidak terpengaruh diskon aktif."],
    [["Produk", "Bibit Cabai", "harga satuan = 15000"],
     ["Jumlah", "8", "Tipe eceran; total = 8 x 15000 = 120000"],
     ["Bayar", "120000", "Persis sama dengan total"]],
    [["Buka halaman kasir, tambah item qty 8 eceran.", "qty 8",
      "Keranjang menampilkan total 120000."],
     ["Isi nominal bayar 120000.", "120000", "Kembalian tampil 0 pada ringkasan."],
     ["Klik Simpan/Proses.", "-", "Transaksi berhasil; halaman detail tampil."],
     ["Periksa halaman detail transaksi.", "-",
      "Detail menampilkan bayar 120000 dan kembalian 0."]],
    "Transaksi tersimpan dengan nominal pembayaran sama dengan total; halaman detail menampilkan "
    "kembalian 0 tanpa pesan error.",
    "Syarat pembayaran minimum adalah bayar \u2265 total; test case ini menguji batas bawah yang "
    "masih diterima.")

tc_block(
    "TC-TRS-006", "REQ-008", "TS-TRS-006", "Transaksi Penjualan",
    "Boundary / Edge", "P2 - Tinggi", "Menu Transaksi / Kasir POS; Menu Diskon",
    "Memverifikasi aturan diskon berdasarkan batas minimal pembelian: diskon aktif tampil diterapkan "
    "(potongan dihitung) ketika jumlah yang dibeli sama dengan minimal beli, dan tidak diterapkan di "
    "bawah batas tersebut.",
    ["Aplikasi web dapat diakses melalui browser; kasir sudah login.",
     "Pada menu Diskon sudah ada diskon aktif \"Promo Pupuk 10%\": besar 10%, berlaku untuk lokasi "
     "toko, minimal beli 5, rentang tanggal mencakup hari pengujian, produk \"Pupuk NPK 50Kg\" terpasang."],
    [["Produk", "Pupuk NPK 50Kg", "harga satuan = 120000; terpasang diskon 10%"],
     ["Jumlah", "5", "Sama dengan minimal beli (5)"],
     ["Tipe", "eceran", "Diskon lokasi toko"],
     ["Bayar", "550000", "Cukup untuk total 540000"]],
    [["Buka halaman kasir, tambah item qty 5 eceran.", "qty 5",
      "Keranjang menampilkan subtotal kotor 600000."],
     ["Amati kolom diskon pada keranjang.", "jumlah = minimal beli = 5",
      "Halaman menampilkan potongan 60000 (12000/unit x 5)."],
     ["Amati total setelah diskon.", "-", "Total tampil 600000 - 60000 = 540000."],
     ["Klik Simpan/Proses dan buka detail transaksi.", "-",
      "Halaman detail menampilkan nominal diskon 60000 dan total 540000."]],
    "Diskon tampil diterapkan otomatis saat jumlah = minimal beli; halaman kasir dan detail transaksi "
    "menampilkan potongan 60000 dan total 540000.",
    "Bila jumlah di bawah minimal beli (misal 4), halaman tidak menampilkan potongan dan total = "
    "480000. Bila ada lebih dari satu diskon berlaku, sistem menerapkan yang terbesar. Diskon lokasi "
    "gudang memakai minimal beli grosir.")

story.append(PageBreak())

# ===== SECTION 6 (kandidat) =====
story.append(P("6. Kandidat Test Case Tambahan (Modul Lain)", H2))
story.append(Paragraph(
    "Tabel berikut berisi variasi skenario positive/negative/edge untuk modul lain pada sistem. "
    "Tiap skenario dapat dikembangkan menjadi test case lengkap apabila diperlukan pada iterasi "
    "pengujian berikutnya.", B))
story.append(Spacer(1, 6))
story.append(grid(c_cells([
    ["TC ID", "Req ID", "Modul", "Skenario (alur di web)", "Jenis", "Expected Result Ringkas"],
    ["TC-TRS-007", "REQ-008", "Transaksi", "Penjualan grosir dengan jumlah = minimal grosir",
     "Positive", "Pada kasir, harga mengikuti harga grosir; struk/detail menampilkan harga tersebut."],
    ["TC-TRS-008", "REQ-008", "Transaksi", "Penjualan grosir dengan jumlah > stok gudang",
     "Negative", "Pesan \"Stok gudang {nama} tidak mencukupi.\" tampil di web."],
    ["TC-TRS-009", "REQ-008", "Transaksi", "Klik Simpan tanpa item di keranjang",
     "Negative", "Transaksi ditolak; halaman menampilkan pesan keranjang kosong/wajib minimal 1 item."],
    ["TC-TRS-010", "REQ-008", "Transaksi", "Isi jumlah 0 atau negatif saat tambah item",
     "Negative", "Sistem menolak input jumlah tidak valid."],
    ["TC-RBAC-001", "REQ-002", "Hak Akses", "Kasir mengakses menu Produk (/produk)",
     "Negative", "Dialihkan ke dashboard dengan pesan tidak punya akses."],
    ["TC-RBAC-002", "REQ-008", "Hak Akses", "Kasir membuka URL detail transaksi milik kasir lain",
     "Negative", "Halaman menampilkan data tidak ditemukan / akses ditolak."],
    ["TC-PRD-001", "REQ-004", "Produk", "Tambah produk dengan harga grosir >= harga satuan",
     "Negative", "Ditolak; pesan \"Harga grosir harus lebih kecil dari harga satuan\"."],
    ["TC-PRD-002", "REQ-004", "Produk", "Hapus produk yang sudah pernah dipakai di transaksi",
     "Negative", "Ditolak; pesan produk tidak bisa dihapus karena sudah dipakai."],
    ["TC-PRD-003", "REQ-004", "Produk", "Tambah produk harga 0 dan stok 0 (nilai minimum)",
     "Boundary", "Form diterima; produk tampil di daftar dengan kode PRD###."],
    ["TC-DSK-001", "REQ-005", "Diskon", "Tambah diskon dengan besar > 100",
     "Negative", "Ditolak; pesan besar diskon maksimal 100."],
    ["TC-DSK-002", "REQ-005", "Diskon", "Tanggal selesai sebelum tanggal mulai",
     "Negative", "Ditolak; pesan tanggal tidak valid."],
    ["TC-TRF-001", "REQ-011", "Transfer Stok", "Transfer jumlah dus = stok gudang (gudang jadi 0)",
     "Boundary", "Berhasil; stok toko bertambah sesuai isi per dus, stok gudang tampil 0."],
    ["TC-TRF-002", "REQ-011", "Transfer Stok", "Transfer jumlah dus > stok gudang",
     "Negative", "Ditolak; pesan \"Stok tidak cukup! Tersedia: X dus\"."],
    ["TC-PBL-001", "REQ-010", "Pembelian", "Pembelian valid (stok & harga beli diperbarui)",
     "Positive", "Berhasil; stok gudang bertambah dan tercatat pada daftar pembelian."],
    ["TC-PBL-002", "REQ-010", "Pembelian", "Pembelian dengan jumlah 0 / negatif",
     "Negative", "Form menolak input jumlah tidak valid."],
    ["TC-DEL-001", "REQ-008", "Transaksi", "Kasir menghapus transaksi miliknya sendiri",
     "Positive", "Berhasil; transaksi hilang dari daftar, stok kembali tampil."],
    ["TC-DEL-002", "REQ-008", "Transaksi", "Kasir menghapus transaksi milik kasir lain",
     "Negative", "Tidak dapat dihapus; tidak ada perubahan."],
    ["TC-STR-001", "REQ-009", "Struk", "Cetak struk transaksi milik kasir",
     "Positive", "Halaman struk tampil sesuai data transaksi."],
    ["TC-LAP-001", "REQ-012", "Laporan", "Export CSV oleh user selain pemilik",
     "Negative", "Akses ditolak (halaman 403)."],
    ["TC-AKUN-001", "REQ-014", "Pengaturan", "Tambah akun kasir dengan password < 8 karakter",
     "Negative", "Ditolak; pesan password minimal 8 karakter."],
    ["TC-RWT-001", "REQ-015", "Riwayat", "Kasir menghapus riwayat aksi",
     "Negative", "Ditolak; hanya pemilik yang bisa membersihkan riwayat."],
    ["TC-AUTH-001", "REQ-001", "Login", "Login kredensial valid, masuk dashboard sesuai role",
     "Positive", "Masuk ke dashboard sesuai role pemilik/kasir."],
    ["TC-AUTH-002", "REQ-001", "Login", "Login dengan password salah",
     "Negative", "Login ditolak dan pesan kesalahan tampil."],
]), widths=[2.2 * cm, 1.6 * cm, 2.4 * cm, 4.9 * cm, 2.4 * cm, 3.5 * cm]))
story.append(PageBreak())

# ===== SECTION 7 (checklist) =====
story.append(P("7. Checklist Review sebelum Eksekusi", H2))
for x in ["Test Case ID unik dan konsisten dengan pola penamaan.",
          "Setiap test case memiliki Requirement ID yang dapat ditelusuri.",
          "Precondition cukup jelas sehingga tester lain dapat menyiapkan kondisi awal yang sama.",
          "Test data ditulis eksplisit dan tidak menggunakan credential/data sensitif nyata.",
          "Langkah uji berupa alur interaksi di browser dan setiap expected result dapat diamati di layar.",
          "Expected result tidak diubah setelah eksekusi hanya untuk membuat test menjadi Pass.",
          "Actual Result, Status, Evidence (screenshot), dan Defect ID hanya diisi setelah eksekusi nyata.",
          "Skenario P1 seperti transaksi penjualan, stok, dan akses (RBAC) mendapat prioritas eksekusi."]:
    story.append(P("&#9744; " + x, BI))

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=2 * cm, rightMargin=2 * cm,
                        topMargin=1.7 * cm, bottomMargin=1.7 * cm,
                        title="Dokumen Test Case POS Sarana Agro Makmur",
                        author="Praktikum Pengujian Perangkat Lunak")

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    page = canvas.getPageNumber()
    canvas.drawRightString(A4[0] - 2 * cm, 1.0 * cm, f"Halaman {page}")
    canvas.drawString(2 * cm, 1.0 * cm, "Praktikum Pengujian Perangkat Lunak | Test Case POS Sarana Agro Makmur")
    canvas.restoreState()

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("OK:", OUT)