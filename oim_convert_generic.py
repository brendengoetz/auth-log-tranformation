import pandas as pd

data = pd.read_csv('filepath.csv') #read in file
data['timestamp'] = pd.to_datetime(data['TIMESTAMP'], format='%d-%b-%y %I.%M.%S.%f %p') #add column in timestamp format
data['hour'] = pd.DatetimeIndex(data['timestamp']).hour #add new column with hour extracted from timestamp
data['date'] = pd.DatetimeIndex(data['timestamp']).date #add new column with date extracted from timestamp
final = data.groupby(['date', 'hour']).count()['timestamp'] #get count of records by date and hour

final.to_csv('filepath.csv')
