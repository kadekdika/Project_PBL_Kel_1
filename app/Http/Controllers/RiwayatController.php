<?php

namespace App\Http\Controllers;

use App\Models\RiwayatAksi;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class RiwayatController extends Controller
{
    public function index(Request $request)
    {
        $q = RiwayatAksi::with('user');

        // Filter rentang tanggal
        $dari = $request->get('dari');
        $sampai = $request->get('sampai');
        if ($dari) $q->whereDate('created_at', '>=', $dari);
        if ($sampai) $q->whereDate('created_at', '<=', $sampai);

        // Filter jenis kejadian → cocokkan prefix aksi
        $kejadian = $request->get('kejadian');
        if (in_array($kejadian, ['penjualan', 'pembelian', 'login'])) {
            $q->where('aksi', 'like', $kejadian . '%');
        }

        // Kata kunci pada label
        $cari = $request->get('cari');
        if ($cari) $q->where('label', 'like', '%' . $cari . '%');

        $riwayat = $q->latest('id_riwayat')->get();

        return view('riwayat.index', compact('riwayat', 'dari', 'sampai', 'kejadian', 'cari'));
    }

    public function destroy($id)
    {
        if (Auth::user()->role !== 'pemilik') {
            return back()->with('error', 'Hanya pemilik yang bisa membersihkan riwayat.');
        }

        RiwayatAksi::findOrFail($id)->delete();
        return back()->with('success', 'Riwayat berhasil dihapus.');
    }
}