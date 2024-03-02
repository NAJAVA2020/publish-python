#!/usr/bin/env python
"""
This script is used to push the changes to the git repository in CSV format.
Columns:
=======
- Time
- Well ID
- Pesticide detected
- Received Signal Strength Indicator (RSSI)
"""
import os
import secrets
import re
import time
import csv


txt_file = "arduino_messages.txt"

with open(txt_file, "r") as file:
    data = file.read()


chem_reg = r"Received packet (.*)"
rssi_reg = r" with RSSI -(.*)"

chem_data = {i: data.replace("Chemical: ", "")
             for i, data in enumerate(re.findall(chem_reg, data))
             if len(data) > 2}
rssi_data = dict(enumerate(re.findall(rssi_reg, data)))

entries = []
for i, data in chem_data.items():
    dict_ = {
        "Time": time.ctime(),
        "Well_ID": dict(enumerate(data.split(" , "))).get(0),
        "Pesticide": dict(enumerate(data.split(" , "))).get(1),
        "RSSI": rssi_data.get(i)
    }
    entries.append(dict_)

# create csv file
csv_file = "data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["Time", "Well_ID", "Pesticide", "RSSI"])
    writer.writeheader()
    writer.writerows(entries)


# def push_to_git():
#     """
#     This function is used to push the changes to the git repository.
#     """
#     os.system("git add .")
#     os.system(f"git commit -m 'Updated the files{secrets.token_hex(4)}'")
#     os.system("git push origin master")
