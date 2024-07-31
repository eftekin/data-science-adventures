from datetime import datetime

import pandas as pd
import pytz
import requests
import streamlit as st
from bs4 import BeautifulSoup


def parse_url(url_list):
    weekdays_list = {}

    for url, label in url_list:
        data = requests.get(url).text
        # create BeautifulSoup object
        soup = BeautifulSoup(data, "html.parser")

        # looking for the table with the class line-table
        table = soup.find("table", class_="line-table")

        for row in table.tbody.find_all("tr"):
            # find all data for each column
            columns = row.find_all("td")
            weekdays_list.update({columns[0].text.strip(): label})
    return weekdays_list


# Downloading contents of the web page
urls = [
    ("https://otobussaatleri.net/50l-alibeykoy-metro-besiktas-otobus-saatleri/", "50L"),
    ("https://otobussaatleri.net/50t-alibeykoy-metro-taksim-otobus-saatleri/", "50T"),
]
weekdays_hour_list = parse_url(urls)
# sort weekdays list
weekdays_hour_list_sorted = dict(sorted(weekdays_hour_list.items()))

# get current time
turkey_timezone = pytz.timezone("Europe/Istanbul")
utc_now = datetime.utcnow()
turkey_now = utc_now.replace(tzinfo=pytz.utc).astimezone(tz=turkey_timezone)
current_time = turkey_now.strftime("%H:%M")

# print title
page_title = "Weekday Bus Schedule: Alibeyköy to Bomonti (50L and 50T)"
st.markdown(f"<h1 style='text-align:center;'>{page_title}</h1>", unsafe_allow_html=True)


# Function to convert hours to minutes to compare bus times with current_time
def convert_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


# print bus schedule
bus_found = False
for time, label in weekdays_hour_list_sorted.items():
    if int(convert_to_minutes(current_time)) <= int(convert_to_minutes(time)):
        st.markdown(
            f"<h3 style='text-align:center; font-size:24px;'>{time} <span style='color:slategray; font-style:italic;'> &ensp; ({label})</span></h3>",
            unsafe_allow_html=True,
        )
        bus_found = True

# print no_bus_message if bus not found
no_bus_message = "No bus available right now."
if not bus_found:
    st.markdown(
        f"<h3 style='text-align:center;'>{no_bus_message}</h3>", unsafe_allow_html=True
    )
