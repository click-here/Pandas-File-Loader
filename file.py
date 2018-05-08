import sys
import pandas as pd
import os

os.chdir(os.path.dirname(sys.argv[1]))
df = pd.DataFrame()

def read_data(encoding):
    print(sys.argv[1])
    if sys.argv[1].endswith('.csv'):
        df = pd.read_csv(sys.argv[1],encoding=encoding)
        print('done')
    elif sys.argv[1].endswith('.xlsx'):
        sht_count = len(pd.ExcelFile(sys.argv[1]).sheet_names)
        if sht_count > 1:
            dfs = []
            for sht in enumerate(pd.ExcelFile(sys.argv[1]).sheet_names):
                print('Loading sheet ' + str(sht[0]+1) + ' of ' + str(sht_count))
                dfs.append(pd.read_excel(sys.argv[1],sht[1]))
            print(str(sht_count) + ' sheets 0-indexed to be accessed like: dfs[0], dfs[1] etc.')
        else:
            df = pd.read_excel(sys.argv[1])
    else:
        print('File open failed')
    return df

try:
    df = read_data(encoding='utf-8')

except UnicodeDecodeError:
    print('Unicode decode error!')
    print("Trying with 'ISO-8859-1'")
    df = read_data(encoding='ISO-8859-1')
print('Active dir set to ' + os.path.dirname(sys.argv[1]))
