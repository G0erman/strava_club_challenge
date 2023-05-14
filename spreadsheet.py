from dataclasses import dataclass
import gspread

GCP_KEY = 'private/gcp_keys.json'

@dataclass
class Spreadsheet:
    key: str
    worksheet: str

    def __post_init__(self):
        self.gc = gspread.service_account(GCP_KEY)

    def open_sheet(self):
        return self.gc.open_by_key(self.key).worksheet(self.worksheet)

