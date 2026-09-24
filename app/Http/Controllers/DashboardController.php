<?php

namespace App\Http\Controllers;

use App\Models\Transaksi;
use App\Models\DetailTransaksi;
use App\Models\Produk;
use Carbon\Carbon;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request; 

class DashboardController extends Controller
{
    public function index(Request $request)
    {
        $today = Carbon::today();

        $filter = $request->filter ?? 'bulan_ini';
        $now = Carbon::now();

        if ($filter == 'bulan_ini') {
            $start = $now->copy()->startOfMonth();
            $end = $now->copy()->endOfMonth();
        } elseif ($filter == '3_bulan') {
            $start = $now->copy()->subMonths(2)->startOfMonth();
            $end = $now->copy()->endOfMonth();
        } elseif ($filter == '1_tahun') {
            $start = $now->copy()->subYear()->startOfMonth();
            $end = $now->copy()->endOfMonth();
        } else {
            $start = $now->copy()->startOfMonth();
            $end = $now->copy()->endOfMonth();
        }

        // Filter bulan, default bulan ini
        $bulan = $request->bulan ?? Carbon::now()->month;
        $tahun = $request->tahun ?? Carbon::now()->year;

        $selectedDate = Carbon::createFromDate($tahun, $bulan, 1);

        // 4 kartu statistik (tetap hari ini)
        $totalTransaksiHariIni = Transaksi::where('jenis', 'penjualan')
            ->whereBetween('tanggal', [$start, $end])
            ->count();

        $totalPenjualanHariIni = Transaksi::where('jenis', 'penjualan')
            ->whereBetween('tanggal', [$start, $end])
            ->sum('total');

        $produkTerjualHariIni = DetailTransaksi::whereHas('transaksi', function($q) use ($start, $end) {
            $q->where('jenis', 'penjualan')
              ->whereBetween('tanggal', [$start, $end]);
        })->sum('jumlah');

        // Hitung stok menipis
        $stokMenipis = Produk::where(function ($q) {
            $q->where('stok_toko', '<=', 10)
              ->orWhere('stok_gudang', '<=', 5);
        })->count();

        $jumlahStokMenipis = $stokMenipis;

        // Transaksi terakhir
        $transaksiTerakhir = Transaksi::with(['detail.produk', 'pelanggan'])
            ->where('jenis', 'penjualan')
            ->whereBetween('tanggal', [$start, $end])
            ->latest('id_transaksi')
            ->take(5)
            ->get();

        // Produk terlaris
        $produkTerlaris = DetailTransaksi::whereHas('transaksi', function($q) use ($start, $end) {
        $q->where('jenis', 'penjualan')
          ->whereBetween('tanggal', [$start, $end]);
    })
        ->join('produk', 'detail_transaksi.id_produk', '=', 'produk.id_produk')
        ->select('produk.nama_produk', DB::raw('SUM(detail_transaksi.jumlah) as total_terjual'))
        ->groupBy('produk.id_produk', 'produk.nama_produk')
        ->orderByDesc('total_terjual')
        ->take(5)
        ->get();

        // Grafik per hari sesuai bulan yang dipilih
        $grafikDays = $start->diffInDays($end) + 1;
        $grafik = collect(range(0, $grafikDays - 1))->map(function($i) use ($start) {
            $date = $start->copy()->addDays($i);
            return [
                'tanggal' => $date->format('d M'),
                'total'   => Transaksi::where('jenis', 'penjualan')
                                ->whereDate('tanggal', $date)
                                ->sum('total'),
            ];
        });

        // Opsi bulan untuk dropdown
        $opsibulan = collect(range(1, Carbon::now()->month))->map(function($m) {
            $date = Carbon::createFromDate(Carbon::now()->year, $m, 1);
            return [
                'bulan' => $date->month,
                'tahun' => $date->year,
                'label' => $date->translatedFormat('F Y'),
            ];
        })->reverse()->values();

        return view('dashboard', compact(
            'filter', 'start', 'end',
            'totalTransaksiHariIni',
            'totalPenjualanHariIni',
            'produkTerjualHariIni',
            'stokMenipis',
            'jumlahStokMenipis',
            'transaksiTerakhir',
            'produkTerlaris',
            'grafik',
            'opsibulan',
            'bulan',
            'tahun'
        ));
    }
}