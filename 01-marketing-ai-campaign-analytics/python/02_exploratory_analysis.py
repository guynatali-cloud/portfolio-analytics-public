import pandas as pd

PATH = "../data/cleaned/marketing_campaign_cleaned.csv"
df = pd.read_csv(PATH)

platform_summary = (
    df.groupby("platform")
    .agg(
        impressions=("impressions", "sum"),
        clicks=("clicks", "sum"),
        ad_spend=("ad_spend", "sum"),
        conversions=("conversions", "sum"),
        revenue=("revenue", "sum"),
    )
    .reset_index()
)

platform_summary["CTR"] = platform_summary["clicks"] / platform_summary["impressions"]
platform_summary["conversion_rate"] = platform_summary["conversions"] / platform_summary["clicks"]
platform_summary["CPC"] = platform_summary["ad_spend"] / platform_summary["clicks"]
platform_summary["CPA"] = platform_summary["ad_spend"] / platform_summary["conversions"]
platform_summary["ROAS"] = platform_summary["revenue"] / platform_summary["ad_spend"]
platform_summary["profit"] = platform_summary["revenue"] - platform_summary["ad_spend"]

print(platform_summary.sort_values("ROAS", ascending=False))
