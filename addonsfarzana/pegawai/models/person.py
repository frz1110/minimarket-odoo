from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'pegawai.person'
    _description = 'desc'
    
    name = fields.Char(string="Nama Pegawai")
    no_ktp = fields.Char(string="Nomor KTP")
    status = fields.Selection([
        ("Internship","Internship"),
        ("Part Time","Part Time"),
        ("Full Time","Full Time"),
    ],
        string="Tipe Pegawai",
        default = "Full Time"
    )
    alamat = fields.Char(string="Alamat")
    no_hp = fields.Char(string="Nomor HP")
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    role = fields.Many2one(comodel_name='pegawai.role', string="Role Pekerjaan", ondelete='cascade')
    
    @api.constrains('no_hp', 'no_ktp')
    def check_numeric(self):
        for rec in self:
            try:
                if not rec.no_hp.isdigit():
                    raise ValidationError("No HP tidak valid (harus berupa angka)")

                if not rec.no_ktp.isdigit():
                    raise ValidationError("No KTP tidak valid (harus berupa angka)")
            except:
                pass

class Pegawai(models.Model):
    _name = 'pegawai.pegawai'
    _inherit = 'pegawai.person'
    _description = 'Pegawai Perusahaan'

    id_pegawai = fields.Integer(string="ID Pegawai")
    foto = fields.Image(string="Foto")
    jatah_cuti = fields.Integer(string="Jatah Cuti (hari)", default=10)
    absensi_ids = fields.One2many(comodel_name='pegawai.absen', inverse_name="pegawai_id", string="Absensi")
    izin_ids = fields.One2many(comodel_name='pegawai.izin', inverse_name="pegawai_id", string="Izin Pegawai")
    pesan_ids = fields.One2many(comodel_name='pegawai.pesan_pegawai', inverse_name="pegawai_id", string="Pesan untuk HR")
    
    _sql_constraints = [
        ('id_pegawai_unik', 'unique (id_pegawai)', 'ID Pegawai tidak boleh sama !!!')
    ]

class Pelamar(models.Model):
    _name = 'pegawai.pelamar'
    _inherit = 'pegawai.person'
    _description = 'Calon Pegawai Perusahaan'

    id_pelamar = fields.Integer(string="ID Pelamar")
    cv = fields.Binary(string='CV')
    pesan_ids = fields.One2many(comodel_name='pegawai.pesan_pelamar', inverse_name="pelamar_id", string="Pesan untuk HR")
    
    _sql_constraints = [
        ('id_pelamar_unik', 'unique (id_pelamar)', 'ID Pelamar tidak boleh sama !!!')
    ]
    