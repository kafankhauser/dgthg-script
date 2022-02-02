#import dataset
import pandas as pd
df = pd.read_csv("/kc_house_data.csv", dtype = int )

#see columns
for col in df.columns: print(col)

#outcome variable - price

#correlation matrix between the different variables
import seaborn as sn
import matplotlib.pyplot as plt

# Build correlation matrix
correlations = df.corr().unstack().sort_values(ascending=False)

# Convert to dataframe
correlations = pd.DataFrame(correlations).reset_index()

# Label it
correlations.columns = ['col1', 'col2', 'correlation']

# Filter for those that contain 'price'
correlation_price = correlations.query("col1 == 'price' & col2 != 'price'")
correlation_price.sort_values(by = 'correlation', axis=0, ascending=False)


print(type('sqft_living'))




######## linear regression model

# split dataset in test and train set

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

# define Z as predictors 
Z = df [['sqft_living', 'grade', 'sqft_above']]
lm.fit(Z, df['price'])

Y_hat = lm.predict(Z)


# residual plot
import seaborn as sns
width = 12
height = 10
plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.displot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.plot(Y_hat)
