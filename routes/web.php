<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\{
    ProfileController, ProdukController, KategoriController,
    PelangganController, TransaksiController, SuplierController,
    LaporanController, DashboardController,
    PengaturanController, DiskonController, LandingPageController,
    AkuntansiController, LaporanKeuanganController, RiwayatController
};

// Internal: tanpa halaman welcome/landing — root langsung arahkan ke login,
// kalau sudah login lempar ke dashboard.
Route::get('/', function () {
    return Auth::check() ? redirect()->route('dashboard') : redirect()->route('login');
});

// --- 1. ROUTE LOGIN UMUM ---
Route::middleware(['auth', 'verified'])->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// --- 2. ROUTE AKSES BERSAMA (Pemilik & Kasir) ---
Route::middleware(['auth', 'role:pemilik,kasir,pemilik2'])->group(function () {
    Route::get('/laporan', [LaporanController::class, 'index'])->name('laporan.index');
    Route::get('/laporan/export', [LaporanController::class, 'exportExcel'])->name('laporan.export');
});

// --- 3. ROUTE PENJUALAN (Kasir + Pemilik) ---
// Semua role boleh input transaksi supaya akun pemilik (default) tetap bisa
// menjalankan POS. Controller transaksi sudah membatasi hanya transaksi milik
// user yang login (id_user), jadi kasir tidak bisa lihat/ubah transaksi kasir lain.
Route::middleware(['auth', 'role:kasir,pemilik,pemilik2'])->group(function () {
    Route::get('/transaksi/stok-terkini', [TransaksiController::class, 'stokTerkini'])->name('transaksi.stokTerkini');
    Route::resource('transaksi', TransaksiController::class)->only(['index', 'create', 'store', 'show', 'destroy']);
    Route::get('/transaksi/{id}/print', [TransaksiController::class, 'printStruk'])->name('transaksi.print');
});

// --- 4. ROUTE KHUSUS PEMILIK ---
Route::middleware(['auth', 'role:pemilik,pemilik2'])->group(function () {
    // Sampah routes (kategori, produk, diskon, pelanggan, suplier)
    Route::get('/kategori/sampah', [KategoriController::class, 'sampah'])->name('kategori.sampah');
    Route::post('/kategori/sampah/{id}/pulihkan', [KategoriController::class, 'pulihkan'])->name('kategori.pulihkan');
    Route::delete('/kategori/sampah/{id}/hapus', [KategoriController::class, 'hapusPermanen'])->name('kategori.hapusPermanen');
    Route::get('/produk/sampah', [ProdukController::class, 'sampah'])->name('produk.sampah');
    Route::post('/produk/sampah/{id}/pulihkan', [ProdukController::class, 'pulihkan'])->name('produk.pulihkan');
    Route::delete('/produk/sampah/{id}/hapus', [ProdukController::class, 'hapusPermanen'])->name('produk.hapusPermanen');
    Route::get('/diskon/sampah', [DiskonController::class, 'sampah'])->name('diskon.sampah');
    Route::post('/diskon/sampah/{id}/pulihkan', [DiskonController::class, 'pulihkan'])->name('diskon.pulihkan');
    Route::delete('/diskon/sampah/{id}/hapus', [DiskonController::class, 'hapusPermanen'])->name('diskon.hapusPermanen');
    Route::get('/pelanggan/sampah', [PelangganController::class, 'sampah'])->name('pelanggan.sampah');
    Route::post('/pelanggan/sampah/{id}/pulihkan', [PelangganController::class, 'pulihkan'])->name('pelanggan.pulihkan');
    Route::delete('/pelanggan/sampah/{id}/hapus', [PelangganController::class, 'hapusPermanen'])->name('pelanggan.hapusPermanen');

    Route::resource('pelanggan', PelangganController::class);
    Route::resource('produk', ProdukController::class);
    // create/show mati agar /kategori/tambah dll 404 bersih, tidak nyelot ke method show yang tidak ada
    Route::resource('kategori', KategoriController::class)->except(['create', 'show']);
    Route::resource('diskon', DiskonController::class);

    // Pembelian (lewat TransaksiController)
    Route::get('/pembelian', [TransaksiController::class, 'indexPembelian'])->name('pembelian.index');
    Route::get('/pembelian/create', [TransaksiController::class, 'createPembelian'])->name('pembelian.create');
    Route::post('/pembelian', [TransaksiController::class, 'storePembelian'])->name('pembelian.store');
    Route::get('/pembelian/{id}', [TransaksiController::class, 'showPembelian'])->name('pembelian.show');
    Route::delete('/pembelian/{id}', [TransaksiController::class, 'destroyPembelian'])->name('pembelian.destroy');

    // Kustomisasi visual (kini hanya login, halaman depan sudah dihapus)
    Route::prefix('pengaturan')->group(function () {
        Route::get('/landing', [LandingPageController::class, 'index'])->name('landing.index');
        Route::post('/landing/update', [LandingPageController::class, 'update'])->name('landing.update');
    });

    Route::post('/produk/{id}/transfer-stok', [ProdukController::class, 'transferStok'])->name('produk.transferStok');

    // Riwayat — audit immutabel, tidak bisa dihapus (destroy dimatikan)
    Route::get('/riwayat', [RiwayatController::class, 'index'])->name('riwayat.index');
    // ponytail: destroy disabled
    // Route::delete('/riwayat/{id}', [RiwayatController::class, 'destroy'])->name('riwayat.destroy');

    // ponytail: akuntansi disabled — UI disembunyi, code tetap ada. Restore: uncomment blok ini + sidebar di app.blade.php + JurnalService calls di TransaksiController.
    // // Akuntansi (COA, Jurnal, Buku Besar, Beban, Laporan Keuangan)
    // Route::prefix('akuntansi')->name('akuntansi.')->group(function () {
    //     Route::get('/coa', [AkuntansiController::class, 'coa'])->name('coa');
    //     Route::post('/coa', [AkuntansiController::class, 'coaStore'])->name('coa.store');
    //     Route::delete('/coa/{id}', [AkuntansiController::class, 'coaDestroy'])->name('coa.destroy');
    //     Route::get('/buku-besar', [AkuntansiController::class, 'bukuBesar'])->name('buku-besar');
    //     Route::get('/jurnal', [AkuntansiController::class, 'jurnal'])->name('jurnal');
    //     Route::post('/jurnal', [AkuntansiController::class, 'jurnalStore'])->name('jurnal.store');
    //     Route::delete('/jurnal/{id}', [AkuntansiController::class, 'jurnalDestroy'])->name('jurnal.destroy');
    //     Route::get('/beban', [AkuntansiController::class, 'beban'])->name('beban');
    //     Route::post('/beban', [AkuntansiController::class, 'bebanStore'])->name('beban.store');
    //     Route::delete('/beban/{id}', [AkuntansiController::class, 'bebanDestroy'])->name('beban.destroy');
    //     Route::get('/laba-rugi', [LaporanKeuanganController::class, 'labaRugi'])->name('laba-rugi');
    //     Route::get('/neraca', [LaporanKeuanganController::class, 'neraca'])->name('neraca');
    //     Route::get('/arus-kas', [LaporanKeuanganController::class, 'arusKas'])->name('arus-kas');
    // });

    // Pengaturan Akun & User
    Route::prefix('pengaturan')->name('pengaturan.')->group(function () {
        Route::get('/pemilik', [PengaturanController::class, 'pemilikIndex'])->name('pemilik');
        Route::put('/pemilik/update', [PengaturanController::class, 'pemilikUpdate'])->name('pemilik.update');

        Route::get('/kasir', [PengaturanController::class, 'kasir'])->name('kasir');
        Route::post('/kasir', [PengaturanController::class, 'kasirStore'])->name('kasir.store');
        Route::get('/kasir/{id}/edit', [PengaturanController::class, 'kasirEdit'])->name('kasir.edit');
        Route::put('/kasir/{id}', [PengaturanController::class, 'kasirUpdate'])->name('kasir.update');
        Route::delete('/kasir/{id}', [PengaturanController::class, 'kasirDestroy'])->name('kasir.destroy');

        // Suplier — semua di bawah prefix pengaturan, nama route pengaturan.suplier.*
        Route::get('/suplier/sampah', [SuplierController::class, 'sampah'])->name('suplier.sampah');
        Route::post('/suplier/sampah/{id}/pulihkan', [SuplierController::class, 'pulihkan'])->name('suplier.pulihkan');
        Route::delete('/suplier/sampah/{id}/hapus', [SuplierController::class, 'hapusPermanen'])->name('suplier.hapusPermanen');

        Route::get('/suplier', [SuplierController::class, 'index'])->name('suplier');
        Route::post('/suplier', [SuplierController::class, 'store'])->name('suplier.store');
        Route::get('/suplier/{id}/edit', [SuplierController::class, 'edit'])->name('suplier.edit');
        Route::put('/suplier/{id}', [SuplierController::class, 'update'])->name('suplier.update');
        Route::delete('/suplier/{id}', [SuplierController::class, 'destroy'])->name('suplier.destroy');
    });
});

require __DIR__.'/auth.php';

