import random
from classes import Pokemon, Move
from battle import Battle
import ascii_art


def create_pokemon(name, pokemon_type, level, max_hp, attack, defense, speed, moves):
    pokemon = Pokemon(name, pokemon_type, level, max_hp, attack, defense, speed)
    for move in moves:
        pokemon.add_move(move)
    return pokemon


def build_starters():
    # ---- Moves ----
    ember = Move("Ember", "Fire", 40, 100, 25)
    flamethrower = Move("Flamethrower", "Fire", 60, 90, 15)

    water_gun = Move("Water Gun", "Water", 40, 100, 25)
    hydro_pump = Move("Hydro Pump", "Water", 65, 80, 10)

    vine_whip = Move("Vine Whip", "Grass", 40, 100, 25)
    razor_leaf = Move("Razor Leaf", "Grass", 55, 95, 15)

    thunder_shock = Move("Thunder Shock", "Electric", 40, 100, 25)
    thunderbolt = Move("Thunderbolt", "Electric", 60, 90, 15)

    # ---- Pokemon ----
    charmander = create_pokemon(
        "Charmander", "Fire", 12, 90, 45, 38, 65,
        [ember, flamethrower]
    )

    squirtle = create_pokemon(
        "Squirtle", "Water", 12, 95, 42, 45, 55,
        [water_gun, hydro_pump]
    )

    bulbasaur = create_pokemon(
        "Bulbasaur", "Grass", 12, 92, 43, 42, 58,
        [vine_whip, razor_leaf]
    )

    pikachu = create_pokemon(
        "Pikachu", "Electric", 12, 80, 40, 30, 90,
        [thunder_shock, thunderbolt]
    )

    return {
        "1": charmander,
        "2": squirtle,
        "3": bulbasaur,
        "4": pikachu,
    }


def choose_player_pokemon(starters):
    print("\nChoose your Pokemon:")
    print("1. Charmander (Fire)")
    print("2. Squirtle (Water)")
    print("3. Bulbasaur (Grass)")
    print("4. Pikachu (Electric)")

    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        if choice in starters:
            return starters[choice]
        print("Invalid choice! Try again.")


def main():
    ascii_art.print_banner()

    starters = build_starters()

    player_pokemon = choose_player_pokemon(starters)

    remaining = [p for key, p in starters.items() if p is not player_pokemon]
    enemy_pokemon = random.choice(remaining)

    print(f"\nYou chose {player_pokemon.name}!")
    print(f"Wild {enemy_pokemon.name} appeared!")

    player_pokemon.display_info()
    enemy_pokemon.display_info()

    battle = Battle(player_pokemon, enemy_pokemon)
    battle.start()

    ascii_art.print_result(
        winner_name=player_pokemon.name if player_pokemon.is_alive() else enemy_pokemon.name,
        is_player=player_pokemon.is_alive()
    )


if __name__ == "__main__":
    main()