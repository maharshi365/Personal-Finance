from parsers.bank import Bank
import pandas as pd

chq = Bank.parse_chequings('data/Chequing.csv')
sav = Bank.parse_savings('data/Savings.csv')
cre = Bank.parse_credit('data/Visa.csv')

out = pd.concat([chq,sav,cre])

Bank.clean_data(out)
