# Simple Dictionary.
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# Nesting a List in a Dictionary.
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Stuttgart', 'Hamburg']
}

# Nesting a dictionary in a dictionary. What about labeling cities?

travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'],
               'total_visits': 12,
               'castles_visited': {
                   'north': 'Chantilly',
                   'south': 'Bourgignon',
                }},
    'Germany': {'cities_visited': ['Berlin', 'Stuttgart', 'Hamburg'],
                'total_visits': 5},
}


# Nesting a dictionary in a list.
travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12,
        'castles_visited': {
                   'north': 'Chantilly',
                   'south': 'Bourgignon',
                }
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Stuttgart', 'Hamburg'],
        'total_visits': 5
    },
]
