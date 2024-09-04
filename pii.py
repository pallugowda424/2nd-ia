import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"D:\\Dataset\\Dataset\\titanic.csv")
age_survived=data[data['survived']==1]['age']
age_not_survived=data[data['survived']==0]['age']
plt.hist(age_survived,color='g',alpha=0.6,label='survived')
plt.hist(age_not_survived,color='k',alpha=0.6,label='Not survived')
plt.xlabel('Age')
plt.ylabel('Frequnecy')
plt.title('Age Distribution of survived and Not survived Passengers')
plt.legend()
plt.show()