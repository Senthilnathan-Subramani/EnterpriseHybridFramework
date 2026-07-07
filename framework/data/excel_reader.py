from openpyxl import load_workbook
class ExcelReader:
    def read(self,file,sheet):
        return load_workbook(file,data_only=True)[sheet]
