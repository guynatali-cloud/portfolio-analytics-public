import pandas as pd

df = pd.read_csv("../data/cleaned/kev_cleaned.csv", parse_dates=["dateAdded", "dueDate"])

print(df.head())
print(df.info())
print(df.describe(include="all"))
print(df["knownRansomwareCampaignUse"].value_counts(dropna=False))
print(df.groupby("vendorProject").size().sort_values(ascending=False).head(15))
