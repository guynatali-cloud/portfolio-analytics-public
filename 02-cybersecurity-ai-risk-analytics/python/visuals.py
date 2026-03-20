import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned/kev_cleaned.csv", parse_dates=["dateAdded", "dueDate"])
df["days_to_due"] = (df["dueDate"] - df["dateAdded"]).dt.days

top_vendors = df.groupby("vendorProject").size().sort_values(ascending=False).head(15)
top_vendors.sort_values().plot(kind="barh", figsize=(10, 6))
plt.title("Top Vendors in KEV Catalog")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("../outputs/top_vendors.png")
