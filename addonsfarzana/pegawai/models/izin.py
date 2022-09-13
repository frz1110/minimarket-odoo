from odoo import models, fields, api


class Izin(models.Model):
    _name = 'pegawai.izin'
    _description = 'Pengajuan Izin'

    pegawai_id = fields.Many2one(comodel_name='pegawai.pegawai',string="Nama Pegawai", ondelete='cascade')
    tgl_izin_mulai = fields.Date(string='Tanggal Mulai Izin')
    tgl_izin_akhir = fields.Date(string='Tanggal Berakhir Izin')
    alasan = fields.Char(string='Alasan Tidak Masuk')