import pandas as pd
import numpy as np
import os


class base_parser:

    @staticmethod
    def parse_file(file_path, **kwargs):
        if not os.path.exists(file_path):
            raise RuntimeError('File does not exist')
        if not file_path.endswith('.csv'):
            raise RuntimeError('File must be a csv')

        df = pd.read_csv(file_path, **kwargs).fillna(0)
        return df


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
