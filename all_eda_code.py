import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("dataset/netflix_titles.csv")

# ==================================================
# FIRST 5 ROWS
# ==================================================

print("First 5 Rows:")
print(df.head())

# ==================================================
# DATASET SHAPE
# ==================================================

print("\nDataset Shape:")
print(df.shape)

# ==================================================
# COLUMN NAMES
# ==================================================

print("\nColumn Names:")
print(df.columns)

# ==================================================
# DATA TYPES
# ==================================================

print("\nData Types:")
print(df.dtypes)

# ==================================================
# MISSING VALUES
# ==================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==================================================
# DUPLICATE ROWS
# ==================================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==================================================
# MOVIES VS TV SHOWS
# ==================================================

print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.savefig("visuals/movies_vs_tvshows.png")
plt.show()

# ==================================================
# TOP 10 COUNTRIES
# ==================================================

top_countries = df['country'].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visuals/top_10_countries.png")
plt.show()

# ==================================================
# TOP 10 GENRES
# ==================================================

top_genres = df['listed_in'].value_counts().head(10)

print("\nTop 10 Genres:")
print(top_genres)

plt.figure(figsize=(12,6))
top_genres.plot(kind='bar')

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visuals/top_10_genres.png")
plt.show()

# ==================================================
# CONTENT GROWTH BY RELEASE YEAR
# ==================================================

content_by_year = df['release_year'].value_counts().sort_index()

print("\nContent Growth by Release Year:")
print(content_by_year.tail(15))

plt.figure(figsize=(12,6))
content_by_year.plot(kind='line')

plt.title("Netflix Content Released Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visuals/content_growth_by_year.png")
plt.show()

# ==================================================
# RATINGS DISTRIBUTION
# ==================================================

rating_counts = df['rating'].value_counts()

print("\nRatings Distribution:")
print(rating_counts)

plt.figure(figsize=(10,5))
rating_counts.plot(kind='bar')

plt.title("Netflix Content Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visuals/ratings_distribution.png")
plt.show()

# ==================================================
# CONTENT ADDED BY YEAR
# ==================================================

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

added_year = df['date_added'].dt.year.value_counts().sort_index()

print("\nContent Added By Year:")
print(added_year)

plt.figure(figsize=(12,6))
added_year.plot(kind='line')

plt.title("Content Added to Netflix by Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("visuals/content_added_by_year.png")
plt.show()