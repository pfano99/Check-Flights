import requests
from secrets_info import api_key

# url = "http://api.aviationstack.com/v1/flights?access_key={}&dep_iata=JNB&limit=10".format(api_key)

url = "http://api.aviationstack.com/v1/cities?access_key={}&search=johannesburg".format(api_key)

# r = requests.get(url)

# print(r.json())
# print(dir(r))


class Flights:
    
    def __init__(self) -> None:
        self.base_url = "http://api.aviationstack.com/v1/flights?access_key={}".format(api_key)


    def get_flights(self, depature_iata, arrival_iata):
        """
            icao is the code that identifies each airport,
            date,
            flight status can be [ scheduled, active, landed, cancelled, incident, diverted ]
        """
        url = self.base_url + "&dep_iata={}&arr_iata={}&limit=10".format(depature_iata, arrival_iata)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(resp.status_code)
            return None

    @staticmethod
    def clean_json(data):
        # data.json())
        results = []
        if data['data']:
            for d in data['data']:
                results.append(
                    { 
                        'flight_date' : d['flight_date'], 
                        'flight_status' : d['flight_status'],
                        'departure' : d['departure']['airport'],
                        'dep_time':d['departure']['estimated'],
                        'arr_time':d['arrival']['estimated'],
                        'arrival' : d['arrival']['airport'],
                        'airline': d['airline']['name'],
                        'flight_no': d['flight']['number']
                    }
                )
        return results


# f = Flights()
# r = f.get_flights('JNB', 'CPT').json()
# print(f.clean_json(r))