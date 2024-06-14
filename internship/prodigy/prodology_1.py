import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
# Load the dataset
try:
    checkprice = pd.read_csv(
        '/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/house/train.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)
except Exception as e:
    print("An error occurred while loading the dataset:", e)
    exit(1)
# Check if 'SalePrice' is present in the dataset
if 'SalePrice' not in checkprice.columns:
    print("Error: 'SalePrice' column not found in the dataset.")
    exit(1)
# Define features and target variable
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
target = 'SalePrice'
X = checkprice[features]
y = checkprice[target]
if X.empty or y.empty:
    print("No data available after preprocessing. Please check your dataset.")
    exit(1)
# Split the data into training and testing sets
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
except ValueError as ve:
    print(ve)
    exit(1)
# Model Training
model = LinearRegression()
model.fit(X_train, y_train)
# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Load the test dataset with IDs
try:
    test_data = pd.read_csv(
        '/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/house/test.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)
except Exception as e:
    print("An error occurred while loading the test dataset:", e)
    exit(1)

# Predict prices for test data
test_X = test_data[features]
test_data['PredictedPrice'] = model.predict(test_X)

# Sort the test data by PredictedPrice in ascending order
sorted_test_data = test_data[['Id', 'PredictedPrice']].sort_values(by='PredictedPrice', ascending=True)

# Save sorted test data to a new CSV file
try:
    sorted_test_data.to_csv(
        '/home/harshit/Desktop/c and java and python programming/python/ai_ml practise/ml/internship/house/sorted_test_data.csv',
        index=False)
    print("Data saved to csv file at given path")
except Exception as e:
    print("An error occurred while saving the sorted test data:", e)
    exit(1)

# Display the first few rows of sorted test data
print(sorted_test_data.head())
