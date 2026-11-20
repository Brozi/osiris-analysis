import pandas as pd

events = pd.read_csv("data/fire-events.csv")
assets = pd.read_csv("data/fire-assets.csv")

print(events.info())
print(assets.info())

df = events.merge(
    assets.drop(columns=["latitude", "longitude"]),
    "left",
    on="asset_id",
    suffixes=("_event", "_asset"),
)

print(df)

df.to_csv("data/fire-events-assets.csv", index=False)

df["event_start_utc"] = pd.to_datetime(df["event_start_utc"], utc=True)
df["first_disclosure_utc"] = pd.to_datetime(df["first_disclosure_utc"], utc=True)
fallback_date = pd.to_datetime(df["event_id"].str.slice(0, 10), utc=True)
