import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('alghost-auto-...json', scope)
gs = gspread.authorize(credentials)
doc = gs.open_by_url('https://....')
# 첫번째 시트 가져오기
ws = doc.get_worksheet(0)
# B1 셀의 데이터를 출력
print(worksheet.acell('B1').value)
