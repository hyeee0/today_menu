import pandas as pd
import glob

data_paths = glob.glob('./crawling_data_1/*')
df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df_temp = df_temp.drop_duplicates(subset=['menu_titles'])
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df = df.drop_duplicates(subset=['menu_titles'])
df.info()
# print(len(df.titles.value_counts()))
df.to_csv('./crawling_data/menu_recipes_01-25_1.csv', index=False)