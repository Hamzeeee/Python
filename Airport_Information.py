# Learning Python right now... =^._.^= ∫ meow

import requests

api_key = "3cd57689-7cc9-42bb-b666-666f29152812"
city_code = input("Insert City code of your Airport: ")


request = requests.get(f"https://airlabs.co/api/v9/schedules?dep_iata={city_code}&api_key={api_key}").json()

flights = []

lenght = request['response']

count = input(f"Amount of Airplanes you want to see (limit is {len(lenght)}): ")


print("[ Status ]                 [ Airline ]         [ Depart ]         [ Landing ]                 [ Started ]                  [ Landed ]             [ Flight ID ]")
for x in range(int(count)):
    airline = request['response'][x]['airline_icao']
    status = request['response'][x]['status']
    depart = request['response'][x]['dep_iata']
    arrive = request['response'][x]['arr_iata']
    landed = request['response'][x]['arr_time']
    started = request['response'][x]['dep_time']
    flight_id = request['response'][x]['flight_iata']
    print(f"  {status}                       {airline}                 {depart}                {arrive}                  {started}            {landed}              {flight_id}")
