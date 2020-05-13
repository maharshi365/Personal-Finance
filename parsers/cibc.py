from base_parser import base_parser
import pandas as pd

class CIBC(base_parser):
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


