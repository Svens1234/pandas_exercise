import pandas as pd

vgs= pd.read_csv(r'C:\Users\German\Desktop\vgsales.csv')
print(vgs.head(10))
print(vgs.info) #информация о файлу vgsales.csv
print(vgs['EU_Sales'].mean()) #среднее месячное
print(vgs['JP_Sales'].max())
print(vgs[vgs['Name'] == 'Brain Age 2: More Training in Minutes a Day']['Genre'])
print(vgs[vgs['Name'] == 'Grand Theft Auto: Vice City ']['Global_Sales'])
print(vgs[vgs['NA_Sales']==vgs['NA_Sales'].max()]['Name'])
print(vgs[vgs['Global_Sales']==vgs['Global_Sales'].min()]['Name'])
print(vgs.groupby('Genre').mean())
print(vgs.groupby('Genre').mean()['JP_Sales'])
print(vgs['Name'].nunique())
print(vgs['Genre'].value_counts().head(3))


def super_in_name(name):
    if 'super' in name.lower().split():
        return True
    else:
        return False


print(vgs['Name'].apply(lambda x: super_in_name(x)))
print(sum(vgs['Name'].apply(lambda x: super_in_name(x))))


