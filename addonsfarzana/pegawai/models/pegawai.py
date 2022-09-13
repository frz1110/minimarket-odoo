from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pegawai(models.Model):
    _name = 'pegawai.pegawai'
    _description = 'Pegawai Perusahaan'

    name = fields.Char(string="Nama Pegawai")
    id_pegawai = fields.Integer(string="ID Pegawai")
    no_ktp = fields.Char(string="Nomor KTP")
    status = fields.Selection([
        ("Internship","Internship"),
        ("Part Time","Part Time"),
        ("Full TIme","Full TIme"),
    ],
        string="Status"
    )
    alamat = fields.Char(string="Alamat")
    no_hp = fields.Char(string="Nomor HP")
    absensi_ids = fields.One2many(comodel_name='pegawai.absen', inverse_name="pegawai_id", string="Absensi")
    role = fields.Char(string="Role Pekerjaan")
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')
    jatah_cuti = fields.Integer(string="Jatah Cuti", default=10)


    @api.constrains('no_hp', 'no_ktp')
    def check_numeric(self):
        for rec in self:
            print(rec.no_hp)
            print(rec.no_hp.isdigit())
            if not rec.no_hp.isdigit():
                raise ValidationError("No HP tidak valid (harus berupa angka)")

            if not rec.no_ktp.isdigit():
                raise ValidationError("No KTP tidak valid (harus berupa angka)")

    _sql_constraints = [
        ('id_pegawai_unik', 'unique (id_pegawai)', 'ID Pegawai tidak boleh sama !!!')
    ]
    