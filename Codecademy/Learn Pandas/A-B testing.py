import pandas as pd

ad_clicks = pd.read_csv("ad_clicks.csv")
# print(ad_clicks.head())

print(ad_clicks.groupby("utm_source").user_id.count().reset_index())


ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
# The ~ is a NOT operator

clicks_by_source = (
    ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
)
# print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
    index="utm_source", columns="is_click", values="user_id"
).reset_index()

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (
    clicks_pivot[True] + clicks_pivot[False]
)
# print(clicks_pivot)

# print(ad_clicks.groupby("experimental_group").user_id.count().reset_index())

print(
    ad_clicks.groupby(["experimental_group", "is_click"])
    .user_id.count()
    .reset_index()
    .pivot(index="experimental_group", columns="is_click", values="user_id")
    .reset_index
)

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

a_clicks_pivot = (
    a_clicks.groupby(["is_click", "day"])
    .user_id.count()
    .reset_index()
    .pivot(index="day", columns="is_click", values="user_id")
    .reset_index()
)
a_clicks_pivot["percent_clicked"] = a_clicks_pivot[True] / (
    a_clicks_pivot[True] + a_clicks_pivot[False]
)
print(a_clicks_pivot)
