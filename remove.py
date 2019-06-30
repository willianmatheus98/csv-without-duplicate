import pandas as pd
file_name = "C:\\Users\\Nome do Usuário\\Desktop\\file_with_dupes.csv"
file_name_output = "C:\\Users\\Nome do Usuário\\Desktop\\my_file_without_dupes.csv"
file_name_output2 = "C:\\Users\\Nome do Usuário\\Desktop\\my_file_without_dupes2.csv"

df = pd.read_csv(file_name, sep=",", low_memory=False)
ndf = pd.read_csv(file_name, sep=",", low_memory=False)
# Notes:
# - the `subset=None` means that every column is used
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone
ndf = ndf[ndf.duplicated(subset=['Nome da Coluna'], keep='first')]
df.drop_duplicates(subset=['Nome da Coluna'], inplace=True)


# Write the results to a different file
df.to_csv(file_name_output)
ndf.to_csv(file_name_output2)