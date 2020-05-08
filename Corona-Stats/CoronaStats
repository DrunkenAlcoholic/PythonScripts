#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# CoronaStats
##################################################
# Author: DrunkenAlcoholic
# Copyright: Copyright 2020, CoronaStats
# Credits: https://github.com/sagarkarira/coronavirus-tracker-cli
# Version: 2020.03.04
# Email: DrunkenAlcoholic@protonmail.com
##################################################

import requests
import sys

# Set default country code / country name when using no arguments
countrycode = "au"


def Getdata(xCountryCode):
    # Format the Url to include country code
    weburl = "https://corona-stats.online/" + xCountryCode + "?format=json"

    # Get Json data
    jsondata = requests.get(weburl).json()

    # Extract data from Json based on the country code / country name
    localdata = {
        "Country": jsondata["data"][0]["country"],
        "Cases": jsondata["data"][0]["cases"],
        "Deaths": jsondata["data"][0]["deaths"],
        "CasesToDay": jsondata["data"][0]["todayCases"],
        "DeathsToDay": jsondata["data"][0]["todayDeaths"],
    }

    # Format output colours
    colours = {
        "clRED": "\033[91m",
        "clGREEN": "\033[92m",
        "clEND": "\033[0m",
    }

    # Print Json data based on country code / country name
    print("{clGREEN}{Country}{clEND}\n New Cases:    {clRED}{CasesToDay}{clEND}\n New Deaths:   {clRED}{DeathsToDay}{clEND}\n Total Cases:  {clRED}{Cases}{clEND}\n Total Deaths: {clRED}{Deaths}{clEND}".format(**localdata, **colours))


# Check if country code / country name argument(s) has been passed and loop through if there are any arguments, else use default
if len(sys.argv) >= 2:
    for i in sys.argv[1:]:
        Getdata(i)
else:
    Getdata(countrycode)
