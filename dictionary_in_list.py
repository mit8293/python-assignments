travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,num_of_visits,states):
    new = {}
    new["country"] = country
    new["visits"] = num_of_visits
    new["cities"] = states
    travel_log.append(new)





add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
