import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleDrive:
    def __init__(self):
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]
        json_file_name = 'heroic-bonbon-335210-9521855b3795.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            json_file_name, scope)
        gc = gspread.authorize(credentials)
        spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1udAhvSuJJ8emfOf820jMj_6PImWBbzT3yFVs_SKcYSg/edit#gid=0'
        # 스프레스시트 문서 가져오기
        doc = gc.open_by_url(spreadsheet_url)
        # 시트 선택하기
        self.worksheet = doc.worksheet('시트1')

    def update(self, position, data):
        self.worksheet.update_acell(position, data)
