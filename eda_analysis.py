import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("books.csv")

# Data cleanup in case Price column wasn't converted
df["Price"] = df["Price"].replace("Â£", "", regex=True).astype(float)

# View the first few rows
print(df.head())

# Data structure info
print(df.info())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Price distribution
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.show()

# Top-rated books
if 'Rating' in df.columns:
    top_rated = df[df['Rating'] == 5]
    print("Top-rated books:")
    print(top_rated[['Title', 'Price', 'Rating']])
else:
    print("Rating column not found!")

# Average price by category (if Category exists)
if 'Category' in df.columns:
    avg_price_by_cat = df.groupby('Category')['Price'].mean().sort_values(ascending=False)
    avg_price_by_cat.plot(kind='bar')
    plt.title("Average Book Price by Category")
    plt.ylabel("Average Price")
    plt.show()

# Compare average prices by rating
if 'Rating' in df.columns:
    avg_price_by_rating = df.groupby('Rating')['Price'].mean()
    print(avg_price_by_rating)

    # Visualize
    avg_price_by_rating.plot(kind='bar', color='skyblue')
    plt.title("Average Price by Rating")
    plt.ylabel("Price")
    plt.show()

# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())

# Outliers in price
sns.boxplot(x=df['Price'])
plt.title("Boxplot of Book Prices")
plt.xlabel("Price (£)")
plt.show()

# Save cleaned dataset
df_cleaned = df.drop_duplicates()
df_cleaned.to_csv("books_cleaned.csv", index=False)
