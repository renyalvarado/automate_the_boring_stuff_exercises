#! /usr/bin/env python3
# Using Google Docs API
# Code based on https://developers.google.com/sheets/api/quickstart/python

from __future__ import print_function
import pickle
import os.path
import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import tabulate

if len(sys.argv) < 2:
    print("Error. Program needs a DOCUMENT_ID", file=sys.stderr)
    exit(1)

if len(sys.argv) < 3:
    print("Error. Program needs a RANGE", file=sys.stderr)
    exit(1)

if len(sys.argv) < 4:
    print("Error. Program needs a CELL_TO_UPDATE", file=sys.stderr)
    exit(1)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = sys.argv[1]
SAMPLE_RANGE_NAME = sys.argv[2]
CELL_TO_UPDATE = sys.argv[3]


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = None
    # The file token.pickle stores the user"s access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    service = build("sheets", "v4", credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
    else:
        print(tabulate.tabulate(values))

    values = [["New Header2"]]
    body = {"values": values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=CELL_TO_UPDATE,
        valueInputOption="RAW", body=body).execute()
    print(f"{result.get('updatedCells')} cells updated.")


if __name__ == "__main__":
    main()
