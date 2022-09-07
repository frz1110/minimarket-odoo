from odoo import models

class SupplierXlsx(models.AbstractModel):
    _name = 'report.farzanamart.supplier_report'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        row, col = 0, 0
        sheet.write(row, col, "Nama Supplier", bold)
        sheet.write(row, col+1, "Alamat", bold)
        sheet.write(row, col+2, "No Telepon", bold)
        for obj in supplier:
            row += 1
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.no_telp)

class BarangXlsx(models.AbstractModel):
    _name = 'report.farzanamart.barang_report'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, barang):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        row, col = 0, 0
        sheet.write(row, col, "Nama Barang", bold)
        sheet.write(row, col+1, "Harga Modal", bold)
        sheet.write(row, col+2, "Harga Jual", bold)
        sheet.write(row, col+3, "Stok", bold)
        sheet.write(row, col+4, "Kelompok Barang", bold)

        for obj in barang:
            row += 1
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.harga_beli)
            sheet.write(row, col+2, obj.harga_jual)
            sheet.write(row, col+3, obj.stok)
            #sheet.write(row, col+4, obj.kelompokbarang_id)
            
            
            