superhero = {
    "name": "Batman",
    "alias": "Bruce wayne",
    "gear": [
        "Batbelt"
    ],
    "vehicle": {
        "title": "Batmobile",
        "speed": "Fast mph",
    }
}

hero_name = superhero["name"]
hero_alias = superhero.get("alias")
hero_values = superhero.values()