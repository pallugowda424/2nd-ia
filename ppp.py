import pandas as pd 
df=pd.read_csv(r'D:\\Dataset\\Dataset\\auto-mpg.csv')
print(df.head())
da={
    "mpg":[18,15,18,17,14,15],
    "cylinder":[8,8,8,8,8,8],
    "Displacement":[130,165,150,140,225,190],
    "weight":[3504,3693,3436,3449,4425,3850],
    "acceleration":[12,11.5,11,10.5,10,8.5],
    "model year":[71,70,72,70,71,70],
    "car name":["chevrolet","skylark","plymouth","ford","pontiac","ambassador"]
     }
df=pd.DataFrame(da)
m1=df['horsepower'].mean()
print(m1)
m2=df['acceleration'].std
print(m2)
m3=df.grouply('model year')['model year'].count()
print(m3)

