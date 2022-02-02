

#import dataset
import pandas as pd
df = pd.read_csv("/Users/kathi/Desktop/kc_house_data.csv" )

#see columns
for col in df.columns: print(col)

#outcome variable - price

#correlation matrix between the different variables
import seaborn as sns
import matplotlib.pyplot as plt

# Build correlation matrix
correlations = df.corr().unstack().sort_values(ascending=False)

# Convert to dataframe
correlations = pd.DataFrame(correlations).reset_index()

# Label it
correlations.columns = ['col1', 'col2', 'correlation']

# Filter for those that contain 'price'
correlation_price = correlations.query("col1 == 'price' & col2 != 'price'")

#print correlation between predictors and the price columne
correlation_price.sort_values(by = 'correlation', axis=0, ascending=False)




######## model: multiple linear regression

# split dataset in test and train set
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

# define Z as predictors 
Z = df [['sqft_living', 'grade', 'sqft_above']]

#create linear regression model
lm.fit(Z, df['price'])
Y_hat = lm.predict(Z)

# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))

# find the mean square error
from sklearn.metrics import mean_squared_error
print('The mean square error of price and predicted value using multifit is: ',mean_squared_error(df['price'], Y_hat))



### apply neural net using Tensor Flow
# https://www.analyticsvidhya.com/blog/2016/10/an-introduction-to-implementing-neural-networks-using-tensorflow/
