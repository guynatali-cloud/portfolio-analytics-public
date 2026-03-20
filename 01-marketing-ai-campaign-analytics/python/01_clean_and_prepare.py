import pandas as pd
import numpy as np

RAW_PATH = "../data/raw/global_ads_performance_dataset.csv"
OUT_PATH = "../data/cleaned/marketing_campaign_cleaned.csv"

df = pd.read_csv(RAW_PATH)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)
df["conversion_rate"] = np.where(df["clicks"] > 0, df["conversions"] / df["clicks"], 0)
df["cost_per_1000_impressions"] = np.where(df["impressions"] > 0, df["ad_spend"] / df["impressions"] * 1000, 0)
df["revenue_per_click"] = np.where(df["clicks"] > 0, df["revenue"] / df["clicks"], 0)
df["profit"] = df["revenue"] - df["ad_spend"]
df["profit_margin"] = np.where(df["revenue"] > 0, df["profit"] / df["revenue"], 0)

df["ai_priority_score"] = (
    df["ROAS"].rank(pct=True) * 0.35
    + df["conversion_rate"].rank(pct=True) * 0.30
    + df["CTR"].rank(pct=True) * 0.20
    + (1 - df["CPA"].rank(pct=True)) * 0.15
)

df["ai_recommendation"] = pd.cut(
    df["ai_priority_score"],
    bins=[-1, 0.33, 0.66, 2],
    labels=["Reduce spend", "Monitor / test", "Scale budget"]
)

df.to_csv(OUT_PATH, index=False)
print(f"Saved cleaned file to {OUT_PATH}")
