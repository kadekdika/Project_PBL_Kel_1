<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Jurnal extends Model
{
    protected $table = 'jurnal';
    protected $primaryKey = 'id_jurnal';
    protected $fillable = [
        'no_jurnal', 'tanggal', 'ref_type', 'ref_id',
        'keterangan', 'total', 'id_user',
    ];

    public function detail()
    {
        return $this->hasMany(DetailJurnal::class, 'id_jurnal');
    }

    public function user()
    {
        return $this->belongsTo(User::class, 'id_user');
    }

    public function ref()
    {
        return $this->morphTo();
    }
}
