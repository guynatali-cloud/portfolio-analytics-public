import pandas as pd

PATH = "../data/cleaned/marketing_campaign_cleaned.csv"
df = pd.read_csv(PATH)

summary = (
    df.groupby("platform")
    .agg(
        ad_spend=("ad_spend", "sum"),
        revenue=("revenue", "sum"),
        clicks=("clicks", "sum"),
        impressions=("impressions", "sum"),
        conversions=("conversions", "sum"),
    )
    .reset_index()
)

summary["ROAS"] = summary["revenue"] / summary["ad_spend"]
summary["conversion_rate"] = summary["conversions"] / summary["clicks"]
summary["CTR"] = summary["clicks"] / summary["impressions"]
summary["CPA"] = summary["ad_spend"] / summary["conversions"]

summary["score"] = (
    (summary["ROAS"] / summary["ROAS"].max()) * 0.60
    + (summary["conversion_rate"] / summary["conversion_rate"].max()) * 0.40
)

summary["recommended_share"] = summary["score"] / summary["score"].sum()
total_budget = summary["ad_spend"].sum()
summary["recommended_budget"] = summary["recommended_share"] * total_budget
summary["budget_shift"] = summary["recommended_budget"] - summary["ad_spend"]

print(summary[["platform", "ad_spend", "recommended_budget", "budget_shift", "ROAS", "conversion_rate"]])
