import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:

    def __init__(self, title, scope=None, credentials=None):
        """Initialization
        
        Args:
            title (:obj:`str`): name of spreadsheet
            scope (:obj:`list` of `str`, optional): auth scope. Defaults to None.
            credentials (:obj:`list`, optional): location of credentials file. Defaults to None.
        """

        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(title)

