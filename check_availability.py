import requests
import json
import pandas as pd
from datetime import date


today = date.today()
today_date = today.strftime("%d-%m-%Y")  

district_id = 301 # Alappuzha
show_min_18 = False # Show Min age 18 vac centers
min_availability = 0 # Min Capacity available

try:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, today_date)
    headers = {"User-Agent": "Mozilla"}
    res = requests.get(URL, headers=headers)

    calender_df = pd.DataFrame(json.loads(res.text)["centers"])

    calender_df["from"] = pd.to_datetime(calender_df["from"]).dt.strftime('%H:%M')
    calender_df["to"] = pd.to_datetime(calender_df["to"]).dt.strftime('%H:%M')
    calender_df["Timing"] = calender_df["from"] + " - " + calender_df["to"]
    calender_df.rename(columns={'name': 'Name', 'pincode': 'Pincode',
                                'fee_type': 'Fee type', 'vaccine_fees': "Vaccine charge"}, inplace=True)

    new_df =calender_df.explode("sessions")
    new_df['Min Age Limit'] = new_df.sessions.apply(lambda x: x['min_age_limit'])
    new_df['Available Capacity'] = new_df.sessions.apply(lambda x: x['available_capacity'])
    new_df['Date'] = new_df.sessions.apply(lambda x: x['date'])

    if show_min_18:
        new_df = new_df[new_df["Min Age Limit"] == 18]

    if min_availability:
        new_df = new_df[new_df["Available Capacity"] >= min_availability]

    print(new_df)

except Exception as e:
    print("Error:",str(e))    