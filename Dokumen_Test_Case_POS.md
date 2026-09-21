# CONTOH DOKUMEN TEST CASE
# POS SARANA AGRO MAKMUR
## Sistem Kasir / Point of Sale Toko Pertanian

| Kolom | Isi |
|---|---|
| Nama Mahasiswa / Kelompok | ........................................................ |
| NIM / Anggota | ........................................................ |
| Kelas | ........................................................ |
| System Under Test | POS Sarana Agro Makmur |
| Versi / Build SUT | TBD saat baseline build tersedia |
| Versi Dokumen Test Case | 1.0 |
| Metode Pengujian | Black-box / End-to-End melalui browser (aplikasi web yang berjalan di hosting) |

---

## 1. Dasar Penyusunan Test Case

Dokumen ini adalah contoh pengisian test case untuk **POS Sarana Agro Makmur** (Project Based Learning Kelompok 1). Struktur kolom mengikuti materi Bab Test Case dan contoh dokumen TEFA Marketplace: Test Case ID, Requirement ID, precondition, test data, langkah eksekusi, expected result, actual result, status, evidence, dan defect.

**Metode pengujian**: pengujian dilakukan secara **black-box / end-to-end** — tester mengoperasikan aplikasi web melalui browser (aplikasi sudah di-hosting), mengikuti alur sebagai pengguna. Semua langkah uji adalah interaksi di halaman web dan hasil yang diamati adalah **apa yang tampil di layar** (halaman, pesan, data pada form/tabel/struk). Evidence diambil berupa **screenshot halaman web**. Pengujian tidak membahas implementasi internal (fungsi controller, kode, atau database).

Requirement ID diturunkan dari kebutuhan fungsional sistem (modul & rute pada aplikasi) — rincian pemetaannya pada bagian 2. Fitur yang paling direpresentasikan di dokumen ini adalah **Transaksi Penjualan (REQ-008)** karena menyentuh alur inti sistem kasir. Nilai Actual Result dan Evidence belum diisi karena dokumen ini merupakan desain, bukan laporan eksekusi.

### 1.1 Konvensi Status
- **Ready**: desain test case telah cukup jelas untuk dieksekusi.
- **Not Run / Planned**: test case belum dieksekusi.
- **Pass**: actual result sesuai expected result.
- **Fail**: actual result tidak sesuai expected result.
- **Blocked**: eksekusi tidak dapat dilanjutkan karena dependency/environment.

### 1.2 Konvensi Prioritas
Skala prioritas mengikuti contoh dokumen TEFA Marketplace (`P1`–`P2`) dan dipadankan dengan skala umum High/Medium/Low:

| Prioritas | Arti | Padanan Umum |
|---|---|---|
| P1 - Kritis | Gagal pada fitur inti (transaksi, stok, hak akses) → fatal | Critical / High |
| P2 - Tinggi | Gagal signifikan tetapi tidak fatal | High |
| P3 - Menengah | Gagal ringan / fungsi pendukung | Medium |
| P4 - Rendah | Kosmetik / penyempurnaan | Low |

Keterangan: kata **"Kritis"** berarti *Critical* (kegagalan paling berdampak), bukan "krisis".

### 1.3 Konvensi ID
| Artefak | Pola | Contoh | Keterangan |
|---|---|---|---|
| Requirement | REQ-0xx | REQ-008 | Requirement dari analisis kebutuhan |
| Test Scenario | TS-TRS-0xx | TS-TRS-001 | Skenario uji tingkat tinggi |
| Test Case | TC-TRS-0xx | TC-TRS-001 | Kasus uji terperinci |
| Evidence | EV-TC-TRS-001-0x | EV-TC-TRS-001-01 | Bukti eksekusi (screenshot) |
| Defect | BUG-SAM-0xx | BUG-SAM-001 | Defect hasil eksekusi |

---

## 2. Daftar Requirement (Sistem)

Requirement di bawah dirunut dari modul dan menu yang benar-benar ada pada aplikasi POS Sarana Agro Makmur:

| Req ID | Modul | Ringkasan Requirement | Menu / Area Aplikasi |
|---|---|---|---|
| REQ-001 | Autentikasi | Login dengan email & password; pengguna diarahkan ke dashboard sesuai role (pemilik / pemilik2 / kasir) | Halaman Login → Dashboard |
| REQ-002 | RBAC / Hak Akses | Pembatasan akses per role: kasir hanya melihat transaksi miliknya sendiri; kelola produk, kategori, diskon, pelanggan, suplier, pembelian, akuntansi, riwayat khusus pemilik | Menu navigasi (sidebar) per role |
| REQ-003 | Kategori Produk | Kelola kategori produk (tambah/ubah/hapus) | Menu Kategori |
| REQ-004 | Produk | Kelola produk (tambah/ubah/hapus, kode otomatis PRD###, harga & stok) | Menu Produk |
| REQ-005 | Diskon | Kelola diskon (besar 1–100%, minimal beli, tanggal aktif, lokasi berlaku) | Menu Diskon |
| REQ-006 | Pelanggan | Kelola data pelanggan | Menu Pelanggan |
| REQ-007 | Suplier | Kelola data suplier | Menu Pengaturan → Suplier |
| REQ-008 | Transaksi Penjualan | Kasir/pemilik membuat transaksi: keranjang minimal 1 item, cek stok, diskon otomatis, pembayaran minimaTotal, cetak struk | Halaman Kasir / Transaksi |
| REQ-009 | Cetak Struk | Kasir mencetak struk transaksi penjualan miliknya | Tombol Cetak/Print Struk pada detail transaksi |
| REQ-010 | Pembelian | Pemilik mencatat pembelian (menambah stok & harga beli) | Menu Pembelian |
| REQ-011 | Transfer Stok | Transfer stok gudang → toko | Menu Produk → Transfer Stok |
| REQ-012 | Laporan | Laporan penjualan/pembelian, filter tanggal, produk terlaris, laba; export CSV khusus pemilik | Menu Laporan |
| REQ-013 | Akuntansi | COA, jurnal, buku besar, beban operasional, laba-rugi, neraca, arus kas | Menu Akuntansi |
| REQ-014 | Pengaturan Akun | Perbarui profil pemilik; tambah/ubah/hapus akun kasir | Menu Pengaturan |
| REQ-015 | Riwayat Aksi | Audit trail aktivitas (login, penjualan, pembelian), filter, hapus riwayat khusus pemilik | Menu Riwayat |

Catatan: fitur komplain/refund tidak ada pada sistem ini (fitur tersebut milik contoh marketplace TEFA), sehingga tidak diuji.

---

## 3. Test Case Register (REQ-008 — Transaksi Penjualan)

Register berikut fokus pada satu requirement utama: **REQ-008 Transaksi Penjualan**. Semua status eksekusi masih **Not Run** karena dokumen ini merupakan desain test case.

| No | Test Case ID | Req ID | Modul/Fitur | Judul Singkat | Prioritas | Jenis | Status |
|---|---|---|---|---|---|---|---|
| 1 | TC-TRS-001 | REQ-008 | Transaksi Penjualan | Transaksi penjualan eceran dengan stok dan pembayaran valid | P1 - Kritis | Positive / End-to-End | Not Run |
| 2 | TC-TRS-002 | REQ-008 | Transaksi Penjualan | Jumlah item melebihi stok toko | P1 - Kritis | Negative | Not Run |
| 3 | TC-TRS-003 | REQ-008 | Transaksi Penjualan | Nominal bayar kurang dari total transaksi | P1 - Kritis | Negative | Not Run |
| 4 | TC-TRS-004 | REQ-008 | Transaksi Penjualan | Jumlah item menghabiskan seluruh stok toko (stok menjadi 0) | P2 - Tinggi | Boundary / Edge | Not Run |
| 5 | TC-TRS-005 | REQ-008 | Transaksi Penjualan | Pembayaran pas tanpa kembalian (bayar = total) | P1 - Kritis | Boundary / Edge | Not Run |
| 6 | TC-TRS-006 | REQ-008 | Transaksi Penjualan | Diskon minimal beli: jumlah tepat sama dengan minimal_beli | P2 - Tinggi | Boundary / Edge | Not Run |

---

## 4. Traceability Ringkas

| Req ID | Ringkasan Requirement | Test Case | Evidence | Defect |
|---|---|---|---|---|
| REQ-001 | Login dan dashboard sesuai role | (kandidat TC-AUTH-*) | TBD | - |
| REQ-002 | RBAC: kasir hanya transaksi sendiri, kelola master khusus pemilik | (kandidat TC-RBAC-*) | TBD | - |
| REQ-003 | Kelola kategori produk | (kandidat TC-KTG-*) | TBD | - |
| REQ-004 | CRUD produk (harga_grosir < harga_satuan, stok >= 0, kode otomatis PRD###) | (kandidat TC-PRD-*) | TBD | - |
| REQ-005 | CRUD diskon (besar 1–100%, minimal beli, tanggal, lokasi) | (kandidat TC-DSK-*) | TBD | - |
| REQ-006 | Kelola pelanggan | (kandidat TC-PLG-*) | TBD | - |
| REQ-007 | Kelola suplier | (kandidat TC-SUP-*) | TBD | - |
| REQ-008 | Transaksi penjualan (cek stok, diskon aktif, bayar >= total) | TC-TRS-001 s.d. TC-TRS-006 | TBD | - |
| REQ-009 | Cetak struk transaksi milik kasir | (kandidat TC-STR-*) | TBD | - |
| REQ-010 | Pembelian (tambah stok gudang & harga_beli) | (kandidat TC-PBL-*) | TBD | - |
| REQ-011 | Transfer stok gudang → toko | (kandidat TC-TRF-*) | TBD | - |
| REQ-012 | Laporan & export CSV (khusus pemilik) | (kandidat TC-LAP-*) | TBD | - |
| REQ-013 | Akuntansi (jurnal, buku besar, laporan keuangan) | (kandidat TC-JRL-*) | TBD | - |
| REQ-014 | Pengaturan akun (pemilik & kasir) | (kandidat TC-AKUN-*) | TBD | - |
| REQ-015 | Riwayat aksi (audit trail, hapus khusus pemilik) | (kandidat TC-RWT-*) | TBD | - |

---

## 5. Detail Test Case

### TEST CASE DETAIL — TC-TRS-001

**Transaksi penjualan eceran dengan stok dan pembayaran valid**

| Test Case ID | TC-TRS-001 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-001 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Positive / End-to-End | Prioritas | P1 - Kritis |
| Sumber | Menu Transaksi / Kasir POS | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi alur pembuatan transaksi penjualan di halaman kasir: kasir menambahkan item, mengisi jumlah dan tipe penjualan, memilih metode bayar, memasukkan nominal bayar, lalu menyimpan — sampai transaksi berhasil tampil di halaman detail dan tercatat pada riwayat.

**Precondition**
- Aplikasi web sudah berjalan di hosting dan dapat diakses melalui browser.
- Tersedia akun kasir yang sudah login.
- Tersedia produk aktif dengan stok cukup (stok tampil lebih dari 0 pada halaman Produk).
- Tidak ada diskon aktif yang memengaruhi produk yang diuji.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Pupuk NPK 50Kg | Stok tampil pada halaman Produk = 10; harga satuan = 120000 |
| Jumlah | 2 | Tipe penjualan: eceran |
| Metode pembayaran | Tunai | Pilihan di form: Tunai / Transfer / Kartu |
| Bayar | 300000 | Nominal uang diterima |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka URL aplikasi dan login dengan akun kasir. | akun kasir | Halaman login tampil; setelah login masuk dashboard kasir. |
| 2 | Buka menu Transaksi / Kasir POS. | - | Halaman kasir tampil: daftar produk, kolom pencarian, dan keranjang kosong. |
| 3 | Pilih produk, isi jumlah 2, pilih tipe eceran, lalu klik Tambah. | Pupuk NPK 50Kg; qty 2 | Item tampil di keranjang dengan subtotal 2 × 120000 = 240000. |
| 4 | Pilih metode pembayaran Tunai. | Tunai | Metode pembayaran terisi pada ringkasan transaksi. |
| 5 | Isi nominal uang yang diterima 300000. | 300000 | Ringkasan menampilkan total 240000 dan kembalian 60000. |
| 6 | Klik tombol Simpan/Proses. | - | Muncul pesan sukses "Transaksi Berhasil!" dan halaman berpindah ke detail transaksi. |
| 7 | Amati halaman detail transaksi. | - | Data transaksi tampil: nama produk, jumlah, harga, total, bayar 300000, kembalian 60000, metode tunai, beserta tombol cetak struk. |
| 8 | Buka menu Riwayat atau Laporan. | - | Transaksi yang baru dibuat muncul pada daftar riwayat penjualan. |

**Expected Result Akhir**

Transaksi berhasil dibuat melalui web: pesan sukses tampil, halaman detail transaksi menampilkan data lengkap, transaksi tercatat pada riwayat penjualan, dan tombol cetak struk tersedia.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Desain test case; screenshot diambil pada tiap langkah kunci saat eksekusi. Stok di halaman Produk dapat dicek sebagai hasil tambahan (berkurang sesuai jumlah terjual).

---

### TEST CASE DETAIL — TC-TRS-002

**Jumlah item melebihi stok toko (eceran)**

| Test Case ID | TC-TRS-002 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-002 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Negative | Prioritas | P1 - Kritis |
| Sumber | Menu Transaksi / Kasir POS | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi bahwa alur pembuatan transaksi ditolak ketika jumlah item (eceran) melebihi stok yang tersedia, dan pesan kesalahan tampil di halaman web.

**Precondition**
- Aplikasi web dapat diakses melalui browser; kasir sudah login.
- Produk yang diuji menampilkan stok toko = 2 pada halaman Produk, dan stok gudang = 12.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Pupuk NPK 50Kg | Stok tampil = 2 (toko); harga satuan = 120000 |
| Jumlah | 3 | Melebihi stok toko yang tampil (2) |
| Tipe | eceran | - |
| Metode pembayaran | Tunai | - |
| Bayar | 500000 | - |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka halaman kasir POS. | - | Halaman kasir tampil. |
| 2 | Pilih produk, isi jumlah 3, tipe eceran, klik Tambah. | qty 3 (stok 2) | Item masuk keranjang berisi jumlah 3. |
| 3 | Isi pembayaran 500000 lalu klik Simpan/Proses. | bayar 500000 | Sistem menolak transaksi. |
| 4 | Perhatikan halaman. | - | Pesan kesalahan tampil di web: "Stok toko Pupuk NPK 50Kg tidak mencukupi." |
| 5 | Buka menu Riwayat / daftar transaksi. | - | Transaksi tersebut tidak tersimpan / tidak muncul di daftar. |

**Expected Result Akhir**

Transaksi ditolak melalui web dengan pesan stok tidak mencukupi yang jelas; transaksi tidak tersimpan dan tidak muncul pada daftar riwayat.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Untuk tipe grosir, pesan serupa menampilkan kapasitas stok gudang ("Stok gudang {nama} tidak mencukupi.") — lihat kandidat TC-TRS-008.

---

### TEST CASE DETAIL — TC-TRS-003

**Nominal bayar kurang dari total transaksi**

| Test Case ID | TC-TRS-003 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-003 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Negative | Prioritas | P1 - Kritis |
| Sumber | Menu Transaksi / Kasir POS | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi bahwa transaksi ditolak ketika nominal uang yang diterima lebih kecil dari total belanja, dan pesan kesalahan tampil di halaman web.

**Precondition**
- Aplikasi web dapat diakses melalui browser; kasir sudah login.
- Produk yang diuji tidak terpengaruh diskon aktif.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Pupuk NPK 50Kg | harga satuan = 120000 |
| Jumlah | 2 | Tipe eceran |
| Total belanja | 240000 | 2 × 120000 |
| Bayar | 100000 | Kurang dari total (240000) |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka halaman kasir dan tambah item qty 2 eceran. | qty 2 | Item tampil di keranjang; total 240000. |
| 2 | Pilih metode Tunai, isi nominal bayar 100000. | 100000 | Ringkasan menunjukkan pembayaran kurang dari total. |
| 3 | Klik Simpan/Proses. | - | Sistem menolak transaksi. |
| 4 | Perhatikan halaman. | - | Pesan kesalahan tampil di web: "Uang bayar tidak cukup." |
| 5 | Buka menu Riwayat / daftar transaksi. | - | Transaksi tidak tersimpan / tidak muncul. |

**Expected Result Akhir**

Transaksi ditolak melalui web dengan pesan "Uang bayar tidak cukup."; tidak ada transaksi yang tersimpan pada daftar.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Total yang dibandingkan adalah total setelah diskon (bila ada), sehingga jika diskon aktif perhitungan di web mengikuti nilai tersebut.

---

### TEST CASE DETAIL — TC-TRS-004

**Jumlah item menghabiskan seluruh stok toko (stok menjadi 0)**

| Test Case ID | TC-TRS-004 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-004 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Boundary / Edge | Prioritas | P2 - Tinggi |
| Sumber | Menu Transaksi / Kasir POS | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi nilai batas: transaksi dengan jumlah persis sama dengan stok tersisa tetap berhasil (stok tampil menjadi 0), sedangkan transaksi berikutnya untuk produk yang sama ditolak.

**Precondition**
- Aplikasi web dapat diakses melalui browser; kasir sudah login.
- Produk yang diuji menampilkan stok toko = 2 pada halaman Produk.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Pupuk NPK 50Kg | Stok tampil = 2 (toko); harga satuan = 120000 |
| Jumlah | 2 | Persis sama dengan stok tersisa |
| Tipe | eceran | - |
| Bayar | 250000 | Cukup untuk total 240000 |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka halaman kasir, tambah item qty 2 eceran. | qty 2 = stok | Kie item tampil; total 240000. |
| 2 | Isi bayar 250000, klik Simpan/Proses. | 250000 | Transaksi berhasil; pesan sukses dan halaman detail tampil. |
| 3 | Buka halaman Produk dan lihat stok produk tsb. | - | Stok toko pada daftar produk menampilkan 0. |
| 4 | Kembali ke kasir, tambah produk yang sama qty 1, simpan. | qty 1, stok 0 | Sistem menolak: pesan stok tidak mencukupi tampil di web. |

**Expected Result Akhir**

Transaksi dengan jumlah = stok tersisa berhasil dan stok pada daftar produk menampilkan 0; penjualan berikutnya untuk produk yang sama ditolak dengan pesan stok tidak mencukupi.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Nilai batas bawah stok: sistem tidak menolak penjualan saat stok menipis, hanya saat jumlah melebihi stok. Filter "Menipis" pada halaman Produk dapat diuji terpisah.

---

### TEST CASE DETAIL — TC-TRS-005

**Pembayaran pas tanpa kembalian (bayar = total)**

| Test Case ID | TC-TRS-005 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-005 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Boundary / Edge | Prioritas | P1 - Kritis |
| Sumber | Menu Transaksi / Kasir POS | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi nilai batas pembayaran: nominal uang yang diterima sama persis dengan total belanja sehingga kembalian tampil 0 dan transaksi tetap berhasil.

**Precondition**
- Aplikasi web dapat diakses melalui browser; kasir sudah login.
- Produk yang diuji tidak terpengaruh diskon aktif.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Bibit Cabai | harga satuan = 15000 |
| Jumlah | 8 | Tipe eceran; total = 8 × 15000 = 120000 |
| Bayar | 120000 | Persis sama dengan total |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka halaman kasir, tambah item qty 8 eceran. | qty 8 | Keranjang menampilkan total 120000. |
| 2 | Isi nominal bayar 120000. | 120000 | Kembalian tampil 0 pada ringkasan. |
| 3 | Klik Simpan/Proses. | - | Transaksi berhasil; halaman detail tampil. |
| 4 | Periksa halaman detail transaksi. | - | Detail menampilkan bayar 120000 dan kembalian 0. |

**Expected Result Akhir**

Transaksi tersimpan dengan nominal pembayaran sama dengan total; halaman detail menampilkan kembalian 0 tanpa pesan error.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Syarat pembayaran minimum adalah bayar ≥ total; test case ini menguji batas bawah yang masih diterima.

---

### TEST CASE DETAIL — TC-TRS-006

**Diskon minimal beli: jumlah tepat sama dengan minimal_beli**

| Test Case ID | TC-TRS-006 | Requirement ID | REQ-008 |
|---|---|---|---|
| Test Scenario ID | TS-TRS-006 | Modul/Fitur | Transaksi Penjualan |
| Jenis Test | Boundary / Edge | Prioritas | P2 - Tinggi |
| Sumber | Menu Transaksi / Kasir POS; Menu Diskon | Status Desain | Ready |

**Tujuan Pengujian**

Memverifikasi aturan diskon berdasarkan batas minimal pembelian: diskon aktif tampil diterapkan (potongan dihitung) ketika jumlah yang dibeli sama dengan minimal beli, dan tidak diterapkan di bawah batas tersebut.

**Precondition**
- Aplikasi web dapat diakses melalui browser; kasir sudah login.
- Pada menu Diskon sudah ada diskon aktif "Promo Pupuk 10%": besar 10%, berlaku untuk lokasi toko, minimal beli 5, rentang tanggal mencakup hari pengujian, produk "Pupuk NPK 50Kg" terpasang.

**Test Data**

| Parameter | Nilai Uji | Keterangan |
|---|---|---|
| Produk | Pupuk NPK 50Kg | harga satuan = 120000; terpasang diskon 10% |
| Jumlah | 5 | Sama dengan minimal beli (5) |
| Tipe | eceran | Diskon lokasi toko |
| Bayar | 550000 | Cukup untuk total 540000 |

**Langkah Eksekusi dan Expected Result**

| Langkah | Aksi / Step (di browser) | Test Data | Expected Result (di layar web) |
|---|---|---|---|
| 1 | Buka halaman kasir, tambah item qty 5 eceran. | qty 5 | Keranjang menampilkan subtotal kotor 600000. |
| 2 | Amati kolom diskon pada keranjang. | jumlah = minimal beli = 5 | Halaman menampilkan potongan 60000 (12000/unit × 5). |
| 3 | Amati total setelah diskon. | - | Total tampil 600000 − 60000 = 540000. |
| 4 | Klik Simpan/Proses dan buka detail transaksi. | - | Halaman detail menampilkan nominal diskon 60000 dan total 540000. |

**Expected Result Akhir**

Diskon tampil diterapkan otomatis saat jumlah = minimal beli; halaman kasir dan detail transaksi menampilkan potongan 60000 dan total 540000.

**Hasil Eksekusi**

| Actual Result | Belum dieksekusi | Status | Not Run / Planned |
|---|---|---|---|
| Evidence ID (Screenshot) | TBD | Defect ID | - |
| Build/Commit | TBD saat eksekusi | Tester | TBD |

**Catatan**

Bila jumlah di bawah minimal beli (misal 4), halaman tidak menampilkan potongan dan total = 480000. Bila ada lebih dari satu diskon berlaku, sistem menerapkan yang terbesar. Diskon lokasi gudang memakai minimal beli grosir.

---

## 6. Kandidat Test Case Tambahan (Modul Lain)

Tabel berikut memberi contoh variasi positive/negative/edge untuk modul lain pada sistem yang dapat dikembangkan (belum ditulis penuh agar dapat berlatih menyusun precondition, test data, steps, dan expected result sendiri).

| TC ID | Req ID | Modul | Skenario (alur di web) | Jenis | Expected Result Ringkas |
|---|---|---|---|---|---|
| TC-TRS-007 | REQ-008 | Transaksi | Penjualan grosir dengan jumlah = minimal grosir | Positive | Pada kasir, harga mengikuti harga grosir; struk/detail menampilkan harga tersebut. |
| TC-TRS-008 | REQ-008 | Transaksi | Penjualan grosir dengan jumlah > stok gudang | Negative | Pesan "Stok gudang {nama} tidak mencukupi." tampil di web. |
| TC-TRS-009 | REQ-008 | Transaksi | Klik Simpan tanpa item di keranjang | Negative | Transaksi ditolak; halaman menampilkan pesan keranjang kosong/wajib minimal 1 item. |
| TC-TRS-010 | REQ-008 | Transaksi | Isi jumlah 0 atau negatif saat tambah item | Negative | Sistem menolak input jumlah tidak valid. |
| TC-RBAC-001 | REQ-002 | Hak Akses | Kasir mengakses menu Produk (/produk) | Negative | Dialihkan ke dashboard dengan pesan tidak punya akses. |
| TC-RBAC-002 | REQ-008 | Hak Akses | Kasir membuka URL detail transaksi milik kasir lain | Negative | Halaman menampilkan data tidak ditemukan / akses ditolak. |
| TC-PRD-001 | REQ-004 | Produk | Tambah produk dengan harga grosir >= harga satuan | Negative | Ditolak; pesan "Harga grosir harus lebih kecil dari harga satuan". |
| TC-PRD-002 | REQ-004 | Produk | Hapus produk yang sudah pernah dipakai di transaksi | Negative | Ditolak; pesan produk tidak bisa dihapus karena sudah dipakai. |
| TC-PRD-003 | REQ-004 | Produk | Tambah produk harga 0 dan stok 0 (nilai minimum) | Boundary | Form diterima; produk tampil di daftar dengan kode PRD###. |
| TC-DSK-001 | REQ-005 | Diskon | Tambah diskon dengan besar > 100 | Negative | Ditolak; pesan besar diskon maksimal 100. |
| TC-DSK-002 | REQ-005 | Diskon | Tanggal selesai sebelum tanggal mulai | Negative | Ditolak; pesan tanggal tidak valid. |
| TC-TRF-001 | REQ-011 | Transfer Stok | Transfer jumlah dus = stok gudang (gudang jadi 0) | Boundary | Berhasil; stok toko bertambah sesuai isi per dus, stok gudang tampil 0. |
| TC-TRF-002 | REQ-011 | Transfer Stok | Transfer jumlah dus > stok gudang | Negative | Ditolak; pesan "Stok tidak cukup! Tersedia: X dus". |
| TC-PBL-001 | REQ-010 | Pembelian | Pembelian valid (stok & harga beli diperbarui) | Positive | Berhasil; stok gudang bertambah dan tercatat pada daftar pembelian. |
| TC-PBL-002 | REQ-010 | Pembelian | Pembelian dengan jumlah 0 / negatif | Negative | Form menolak input jumlah tidak valid. |
| TC-DEL-001 | REQ-008 | Transaksi | Kasir menghapus transaksi miliknya sendiri | Positive | Berhasil; transaksi hilang dari daftar, stok kembali tampil. |
| TC-DEL-002 | REQ-008 | Transaksi | Kasir menghapus transaksi milik kasir lain | Negative | Tidak dapat dihapus; tidak ada perubahan. |
| TC-STR-001 | REQ-009 | Struk | Cetak struk transaksi milik kasir | Positive | Halaman struk tampil sesuai data transaksi. |
| TC-LAP-001 | REQ-012 | Laporan | Export CSV oleh user selain pemilik | Negative | Akses ditolak (halaman 403). |
| TC-AKUN-001 | REQ-014 | Pengaturan | Tambah akun kasir dengan password < 8 karakter | Negative | Ditolak; pesan password minimal 8 karakter. |
| TC-RWT-001 | REQ-015 | Riwayat | Kasir menghapus riwayat aksi | Negative | Ditolak; hanya pemilik yang bisa membersihkan riwayat. |
| TC-AUTH-001 | REQ-001 | Login | Login kredensial valid, masuk dashboard sesuai role | Positive | Masuk ke dashboard sesuai role pemilik/kasir. |
| TC-AUTH-002 | REQ-001 | Login | Login dengan password salah | Negative | Login ditolak dan pesan kesalahan tampil. |

---

## 7. Checklist Review sebelum Eksekusi

- [ ] Test Case ID unik dan konsisten dengan pola penamaan.
- [ ] Setiap test case memiliki Requirement ID yang dapat ditelusuri.
- [ ] Precondition cukup jelas sehingga tester lain dapat menyiapkan kondisi awal yang sama.
- [ ] Test data ditulis eksplisit dan tidak menggunakan credential/data sensitif nyata.
- [ ] Langkah uji berupa alur interaksi di browser dan setiap expected result dapat diamati di layar.
- [ ] Expected result tidak diubah setelah eksekusi hanya untuk membuat test menjadi Pass.
- [ ] Actual Result, Status, Evidence (screenshot), dan Defect ID hanya diisi setelah eksekusi nyata.
- [ ] Skenario P1 seperti transaksi penjualan, stok, dan akses (RBAC) mendapat prioritas eksekusi.