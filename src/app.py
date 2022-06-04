import pokebase as pb

pokemon_game = 'y'

version = pb.version(pokemon_game)
version_group = pb.version_group(version.version_group.name)
pokedexes = [pb.pokedex(dex.name) for dex in version_group.pokedexes]

for pokedex in pokedexes:
    print()
    print(pokedex.name)
    for pokemon in pokedex.pokemon_entries:
        nb = pokemon.entry_number
        pokemon = pb.pokemon(pokemon.pokemon_species.name)
        print()
        print(pokemon.name)
        if not hasattr(pokemon, 'location_area_encounters'):
            continue
        
        for location in pokemon.location_area_encounters:
            for details in location.version_details:
                if details.version.name != pokemon_game:
                    continue
                    
                print(location.location_area.name)
