class Pokemon:
    def __init__(self,name,pokemon_type,level,max_hp,attack,defense,speed):
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level

        self.max_hp = max_hp
        self.current_hp = max_hp

        self.attack = attack
        self.defense = defense
        self.speed = speed

        self.moves =[]
        self.status = None

    def display_info(self):
        print("-" * 35)
        print(f"{self.name}")
        print(f"Type      : {self.pokemon_type}")
        print(f"Level     : {self.level}")
        print(f"HP        : {self.current_hp}/{self.max_hp}")
        print(f"Attack    : {self.attack}")
        print(f"Defense   : {self.defense}")
        print(f"Speed     : {self.speed}")

        print("\nMoves:")
        if self.moves:
            for index, move in enumerate(self.moves, start=1):
                print(f"{index}. {move.name}")
        else:
            print("No moves assigned.")

        print("-" * 35)

    def add_move(self, move):
        if not isinstance(move, Move):
            print("Only Move objects can be added.")
            return
        
        if len(self.moves) < 4:
            self.moves.append(move)
        else:
            print(f"{self.name} already has 4 moves.")

    def take_damage(self,damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def heal(self, amount):
        if not self.is_alive():
            print(f"{self.name} has fainted and cannot be healed.")
            return

        self.current_hp += amount

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

        print(f"{self.name} recovered {amount} HP!")
        print(f"HP: {self.current_hp}/{self.max_hp}")
    
    def is_alive(self):
        return self.current_hp > 0
    
    def show_moves(self):
        print(f"\n{self.name}'s Moves")

        for index, move in enumerate(self.moves, start=1):
            print(
            f"{index}. {move.name}"
            f" ({move.move_type})"
            f" PP {move.current_pp}/{move.max_pp}"
        )
            
    def choose_move(self):
        while True:
            self.show_moves()
            try:
                choice = int(input("\nChoose a move (1-4): "))

                if 1 <= choice <= len(self.moves):
                    move = self.moves[choice - 1]

                    if move.current_pp > 0:
                        return move
                    else:
                        print("\nThat move has no PP left!")

                else:
                    print("\nInvalid choice!")

            except ValueError:
                print("\nPlease enter a valid number.")
    




class Move:
    def __init__(self, name, move_type, power, accuracy, pp):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy

        self.max_pp = pp
        self.current_pp = pp

    def display_move(self):
        print("-" * 30)
        print(f"Move      : {self.name}")
        print(f"Type      : {self.move_type}")
        print(f"Power     : {self.power}")
        print(f"Accuracy  : {self.accuracy}%")
        print(f"PP        : {self.current_pp}/{self.max_pp}")
        print("-" * 30)

    def use_pp(self):
        if self.current_pp > 0:
            self.current_pp -=1
            return True
        
        return False
            