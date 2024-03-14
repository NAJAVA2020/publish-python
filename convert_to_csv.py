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
import re
import time
import csv
import sys


def convert_to_csv():
    """
    This function is used to convert the text file to CSV file.
    """
    txt_file = "arduino_messages.txt"

    with open(txt_file, "r") as file:
        data = file.read()

    chem_reg = r"\[\w+-\w+-\w+\s?\w+:\w+:\w+] ------ Received packet (.*)"
    rssi_reg = r" with RSSI (.*)"
    time_reg = r"\[(\w+-\w+-\w+\s?\w+:\w+:\w+)\] ------ Received packet"
    chem_data = {i: data.replace("Chemical: ", "")
                 for i, data in enumerate(re.findall(chem_reg, data))
                 if len(data) > 2}
    rssi_data = dict(enumerate(re.findall(rssi_reg, data)))

    time_data = dict(enumerate(re.findall(time_reg, data)))

    entries = []

    for i, data in chem_data.items():
        time_ = time_data.get(i)
        well_id = dict(enumerate(data.split(" , "))).get(0)
        if len(well_id) > 4:
            well_id = well_id.strip("'")
        pesticide = dict(enumerate(data.split(" , "))).get(1)
        rssi = rssi_data.get(i)
        if not "WELL" in well_id:
            pesticide = well_id
            well_id = "N/A"
        elif not "WELL" in well_id and pesticide:
            well_id = "N/A"

        dict_ = {
            "Time": time_,
            "Well_ID": well_id,
            "Pesticide": pesticide,
            "RSSI": rssi
        }
        entries.append(dict_)

    # create csv file
    csv_file = "data.csv"
    with open(csv_file, "a", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Time", "Well_ID", "Pesticide", "RSSI"])
        writer.writeheader()
        writer.writerows(entries)

    print("[INFO] --- CSV file created successfully --- ")


if _name_ == "_main_":
    convert_to_csv()