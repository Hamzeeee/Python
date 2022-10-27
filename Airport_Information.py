# Learning Python right now... =^._.^= ∫ meow

import requests

api_key = "<INSERT API KEY HERE>"

def flight_direction():
    city_code = input("Insert City code of your Airport: ")

    request = requests.get(f"https://airlabs.co/api/v9/schedules?dep_iata={city_code}&api_key={api_key}").json()

    length = request['response']

    count = input(f"Amount of airplanes you want to see (limit is {len(length)}): ")

    print("[  Status  ]    [  Airline  ]    [  Depart  ]    [  Landing  ]          [  Started  ]                              [  Landed  ]                  [  Flight ID  ]")
    if count == "all":
        count = len(length)

    for x in range(int(count)):
        airline = request['response'][x]['airline_icao']
        status = request['response'][x]['status']
        depart = request['response'][x]['dep_iata']
        arrive = request['response'][x]['arr_iata']
        landed = request['response'][x]['arr_time']
        started = request['response'][x]['dep_time']
        flight_id = request['response'][x]['flight_iata']
        
        # Formatting Text
        if(status == "cancelled"):
            text = f" {status}           {airline}             {depart}              {arrive}              {started}                          {landed}                     {flight_id}"
            print(text)
        if(status == "landed"):
            text = f" {status}              {airline}             {depart}              {arrive}              {started}                          {landed}                     {flight_id}"
            print(text)
        if(status == "redirected"):
            text = f" {status}          {airline}             {depart}              {arrive}              {started}                          {landed}                     {flight_id}"
            print(text)
        
flight_direction()
