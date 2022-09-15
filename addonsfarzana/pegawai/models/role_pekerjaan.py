from odoo import models, fields, api


class Role(models.Model):
    _name = 'pegawai.role'
    _description = 'Absensi Perusahaan'

    pegawai_id = fields.One2many(comodel_name='pegawai.pegawai', inverse_name="role", string="Nama Pegawai")
    name = fields.Char(string='Role Pekerjaan')
    job_desc = fields.Text(string='Job Description')
    req = fields.Text(string='Requirements')
    pegawai_total = fields.Integer(compute='_compute_pegawai', string='Jumlah Pegawai Total')
    pegawai_intern = fields.Integer(compute='_compute_pegawai', string='Jumlah Pegawai Internship')
    pegawai_part = fields.Integer(compute='_compute_pegawai', string='Jumlah Pegawai Part Time')
    pegawai_full = fields.Integer(compute='_compute_pegawai', string='Jumlah Pegawai Full Time')

    @api.depends('pegawai_intern')
    def _compute_pegawai(self):
        print('haloo',self)
        for record in self:
            print('Halooo',record.name)
            record.pegawai_intern = len(self.env['pegawai.pegawai'].search([('status','=','Internship')]))
            record.pegawai_part = len(self.env['pegawai.pegawai'].search([('status','=','Part Time')]))
            record.pegawai_full = len(self.env['pegawai.pegawai'].search([('status','=','Full Time')]))
            record.pegawai_total = record.pegawai_intern + record.pegawai_part + record.pegawai_full

    def act_button(self):
        pass