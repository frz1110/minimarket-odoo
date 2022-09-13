from odoo import models, fields, api


class Absensi(models.Model):
    _name = 'pegawai.absen'
    _description = 'Absensi Perusahaan'

    pegawai_id = fields.Many2one(comodel_name='pegawai.pegawai',string="Nama Pegawai", ondelete='cascade')
    tanggal = fields.Date(string='Tanggal')
    jam_masuk = fields.Float(string='Jam Masuk')
    jam_keluar = fields.Float(string='Jam Keluar')
    durasi_kerja = fields.Char(string='Durasi Kerja')

    @api.onchange('jam_masuk', 'jam_keluar')
    def _compute_durasi_kerja(self):
        if self.jam_keluar and self.jam_masuk:
            count = self.jam_keluar  - self.jam_masuk
            print("c", count, type(count))
            self.durasi_kerja = f"{count}"

class Lembur(models.Model):
    _name = 'pegawai.lembur'
    _inherit = 'pegawai.absen'
    _description = 'New Description'





