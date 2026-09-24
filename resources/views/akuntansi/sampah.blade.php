<x-app-layout>
<x-slot name="header"><h2 class="text-xl font-bold">Sampah Kategori</h2></x-slot>
<div class="bg-white rounded-lg border p-5">
    <a href="{{ route('kategori.index') }}" class="text-sm text-[#2d6a4f]">← Kembali</a>
    <table class="w-full text-sm mt-4">
        <thead><tr class="text-gray-400 text-xs"><th>Nama</th><th>Status</th><th>Aksi</th></tr></thead>
        <tbody>
            @forelse($sampah as $s)
            <tr class="border-b">
                <td class="py-2">{{ $s->nama_kategori }}</td>
                <td><span class="text-xs bg-gray-100 px-2 py-0.5 rounded">Dihapus</span></td>
                <td class="flex gap-2">
                    <form action="{{ route('kategori.pulihkan', $s->id_kategori) }}" method="POST" class="inline">
                        @csrf <button class="px-3 py-1 bg-[#2d6a4f] text-white text-xs rounded">Pulihkan</button>
                    </form>
                    <form action="{{ route('kategori.hapusPermanen', $s->id_kategori) }}" method="POST" class="inline" onsubmit="return confirm('Hapus permanen? Tidak bisa di-undo.')">
                        @csrf @method('DELETE') <button class="px-3 py-1 bg-red-600 text-white text-xs rounded">Hapus Permanen</button>
                    </form>
                </td>
            </tr>
            @empty
            <tr><td colspan="3" class="text-center text-gray-400 py-4">Tidak ada kategori di sampah</td></tr>
            @endforelse
        </tbody>
    </table>
</div>
</x-app-layout>
