import pandas as pd 
import numpy as np 

data_df = pd.read_csv ('700_sample.csv')

starter_list=np.unique(data_df['starter'].to_numpy())
stop_reason=np.unique(data_df['reason'].to_numpy())

result_df = pd.DataFrame(columns=stop_reason, index=starter_list)
result_df.loc[:,:]=0

for i in range (0  , data_df.shape[0]):
    result_df.loc [data_df['starter'][i],data_df['reason'][i] ]+= data_df['stop_time'][i]

print (result_df)


result_df.to_excel('results.xlsx')
