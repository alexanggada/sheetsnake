import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_client():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'approval-automation-keyfile.json', scope
    )
    return gspread.authorize(credentials)


def get_worksheet(client, spreadsheet_name, worksheet_name):
    spreadsheet = client.open(spreadsheet_name)
    return spreadsheet.worksheet(worksheet_name)


def get_grid_values(worksheet):
    return worksheet.batch_get(['B4:M15'])[0]


def update_grid_values(worksheet, values):
    worksheet.batch_update([{
        'range': 'B4:M15',
        'values': values
    }])


def update_status(worksheet, new_status):
    return worksheet.update_acell('H17', new_status)


def get_score(worksheet):
    return worksheet.get('H18')[0][0]


def update_score(worksheet, new_score):
    return worksheet.update_acell('H18', new_score)


def get_direction(worksheet):
    return worksheet.get('H19')[0][0]


def update_direction(worksheet, new_direction):
    return worksheet.update_acell('H19', new_direction)
