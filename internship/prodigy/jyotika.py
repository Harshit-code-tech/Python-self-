import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

HouseDF = pd.read_csv('/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/train.csv')

HouseDF.head()

HouseDF.info()

HouseDF.describe()
print(HouseDF.isnull().sum())



sns.pairplot(HouseDF)

sns.heatmap(HouseDF.corr(), annot=True)

correlation_matrix = HouseDF.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

X = HouseDF[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
             'floors', 'waterfront', 'view', 'condition', 'sqft_above',
             'sqft_basement', 'yr_built', 'yr_renovated', ]]

y = HouseDF[['price']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lm = LinearRegression()

print(X_train, y_train)
lm.fit(X_train, y_train)

coeff_df = pd.DataFrame(lm.coef_.reshape(-1, 1), X.columns, columns=['Coefficient'])


predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)

sns.distplot((y_test - predictions), bins=50);
