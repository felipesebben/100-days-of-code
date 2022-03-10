travel_log = [
    {
        "country_visited": "France",
        "times_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country_visited": "Germany",
        "times_visited": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country_visited(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)

    print(f"You've visited {country_visited} {times_visited} times.")
    print(f"\nYou've been to {cities_visited[0]} and {cities_visited[1]}.")


add_new_country_visited("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
