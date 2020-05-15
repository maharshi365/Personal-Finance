from .base_parser import base_parser
import pandas as pd

class Bank(base_parser):
    @staticmethod
    def parse_chequings(file_path):
        df = base_parser.parse_file(
            file_path, names=['Date', 'Name', 'Debit', 'Credit'])
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    @staticmethod
    def parse_savings(file_path):
        df = base_parser.parse_file(
            file_path, names=['Date', 'Name', 'Debit', 'Credit'])
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    @staticmethod
    def parse_credit(file_path):
        df = base_parser.parse_file(
            file_path, names=['Date', 'Name', 'Debit', 'Credit'], usecols=[0, 1, 2, 3])
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    
    @staticmethod
    def clean_data(df):
        df['check'] = df.apply(lambda row: '-'.join(sorted([str(row['Date']), str(row['Debit']), str(row['Credit'])])), axis=1)
        df.drop_duplicates('check', inplace=True)
        df.drop(columns=['check']).to_csv('data/out.csv',index=False,index_label=False)
        


