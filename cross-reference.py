import pandas as pd

fire_events = pd.read_csv("data/fire-events.csv")
fire_assets = pd.read_csv("data/fire-assets.csv")

print(fire_events.info())
print(fire_assets.info())

fire_events_assets = fire_events.merge(
    fire_assets.drop(columns=["latitude", "longitude"]),
    "left",
    on="asset_id",
    suffixes=("_event", "_asset"),
)

print(fire_events_assets)

fire_events_assets.to_csv("data/fire-events-assets.csv", index=False)
