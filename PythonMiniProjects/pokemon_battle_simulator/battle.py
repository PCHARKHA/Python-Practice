import random
class Battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.turn = 1
        self.battle_log = []

    def display_status(self):
        print("\n" + "=" * 45)
        print(f"{self.player.name} (Lv.{self.player.level})")
        print(f"HP: {self.player.current_hp}/{self.player.max_hp}")

        print()

        print(f"{self.enemy.name} (Lv.{self.enemy.level})")
        print(f"HP: {self.enemy.current_hp}/{self.enemy.max_hp}")
        print("=" * 45)

    def first_attacker(self):
        if self.player.speed >= self.enemy.speed:
            return self.player, self.enemy
        return self.enemy, self.player

    def calculate_damage(self, attacker, defender, move):
        # Base Damage
        damage = ((attacker.attack * move.power) // defender.defense)

        # Random Damage (90% - 110%)
        damage = int(damage * random.uniform(0.9, 1.1))

        # Critical Hit (10% chance)
        critical = False
        if random.randint(1, 100) <= 10:
            damage *= 2
            critical = True

        # Type Effectiveness
        multiplier = self.type_multiplier(move.move_type, defender.pokemon_type)
        damage = int(damage * multiplier)

        damage = max(1, damage)

        return damage, critical, multiplier

    def type_multiplier(self, attack_type, defender_type):

        chart = {
            ("Fire", "Grass"): 2,
            ("Fire", "Water"): 0.5,
            ("Fire", "Fire"): 0.5,

            ("Water", "Fire"): 2,
            ("Water", "Grass"): 0.5,
            ("Water", "Water"): 0.5,

            ("Grass", "Water"): 2,
            ("Grass", "Fire"): 0.5,
            ("Grass", "Grass"): 0.5,

            ("Electric", "Water"): 2,
            ("Electric", "Grass"): 0.5,
            ("Electric", "Electric"): 0.5,
        }

        return chart.get((attack_type, defender_type), 1)

    def accuracy_check(self, move):
        return random.randint(1, 100) <= move.accuracy

    def attack(self, attacker, defender, move):

        if not move.use_pp():
            print(f"{move.name} has no PP left!")
            return

        print(f"\n{attacker.name} used {move.name}!")

        if not self.accuracy_check(move):
            print(f"{attacker.name}'s attack missed!")
            self.battle_log.append(
                f"{attacker.name} used {move.name} but missed."
            )
            return

        damage, critical, multiplier = self.calculate_damage(
            attacker,
            defender,
            move
        )

        if critical:
            print("Critical Hit!")

        if multiplier > 1:
            print("It's super effective!")

        elif multiplier < 1:
            print("It's not very effective...")

        defender.take_damage(damage)

        self.battle_log.append(
            f"{attacker.name} used {move.name} and dealt {damage} damage."
        )

    def player_turn(self):
        move = self.player.choose_move()
        self.attack(self.player, self.enemy, move)

    def enemy_turn(self):

        available_moves = [
            move for move in self.enemy.moves
            if move.current_pp > 0
        ]

        if not available_moves:
            print(f"{self.enemy.name} has no moves left!")
            return

        move = random.choice(available_moves)

        self.attack(self.enemy, self.player, move)

    def battle_over(self):

        if not self.player.is_alive():
            print(f"\n{self.player.name} fainted!")
            print(f"\n🏆 {self.enemy.name} wins!")
            return True

        if not self.enemy.is_alive():
            print(f"\n{self.enemy.name} fainted!")
            print(f"\n🏆 {self.player.name} wins!")
            return True

        return False

    def show_battle_log(self):
        print("\n" + "=" * 45)
        print("BATTLE SUMMARY")
        print("=" * 45)

        for event in self.battle_log:
            print(event)

    def start(self):

        print("=" * 45)
        print(f"{self.player.name} VS {self.enemy.name}")
        print("=" * 45)

        while self.player.is_alive() and self.enemy.is_alive():

            print(f"\n========== Turn {self.turn} ==========")

            self.display_status()

            first, second = self.first_attacker()

            if first == self.player:
                self.player_turn()

                if self.enemy.is_alive():
                    self.enemy_turn()

            else:
                self.enemy_turn()

                if self.player.is_alive():
                    self.player_turn()

            self.turn += 1

        self.battle_over()
        self.show_battle_log()