import pandas as pd
import datetime
import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import matplotlib.pyplot as plot


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
    return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

def orderDF():
    CLIENT_SECRET_FILE = '/home/tushar/Code/12th IP Project/Restaurant Menu/client_secret.json'
    API_SERVICE_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    gsheetId = '1GTgLvV09DGkMMNSUud9V1RlPM14tREM503Jcv45hwEY'

    s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
    gs = s.spreadsheets()
    rows = gs.values().get(spreadsheetId=gsheetId,range='Test1').execute()
    data = rows.get('values')

    df = pd.DataFrame(data)
    print(df)

    df.to_csv("/home/tushar/Code/12th IP Project/Restaurant Menu/order.csv")
'''    
orderDF()

orders = pd.read_csv("/home/tushar/Code/12th IP Project/Restaurant Menu/order.csv")
print(orders)

val = orders.loc[1:,['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']]
print(val)

value = pd.DataFrame(val)
value = value.to_csv('/home/tushar/Code/12th IP Project/Restaurant Menu/graph.csv')
value = pd.read_csv("/home/tushar/Code/12th IP Project/Restaurant Menu/graph.csv")
x = value.sum(axis=0, skipna=True)
x = list(x)
x.pop(0)
print(x)

dishes = ['CRISPY CHILLI POTATO','PANEER TIKKA','CHICKEN WINGS','FRENCH FRIES','PANEER TIKKA PIZZA','BBQ CHICKEN PIZZA','MARGHERITA PIZZA','CHICKEN KEEMA BURGER','VEG PLATTER' ,'NON VEG PLATTER' ,'BLUEBERRY CHEESECAKE' ,'SOFTY' ,'OREO MOUSSE','SPRITE' ,'COKE']

grph = plot.barh(dishes,x)

plot.xlabel('Frequency of Dishes ordered')
plot.ylabel('Dishes')

plot.grid(True)

plot.tight_layout()
plot.savefig("/home/tushar/Code/12th IP Project/Restaurant Menu/static/images/graph1.jpeg")
plot.show()
'''