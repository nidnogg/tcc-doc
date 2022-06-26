import random 

class MutationalFuzzer():    
    def flip_random_character(s):
        """Retorna s com um caractere aleatorio com seu bit modificado."""
        if s == "":
            return s

        pos = random.randint(0, len(s) - 1)
        c = s[pos]
        bit = 1 << random.randint(0, 6)
        new_c = chr(ord(c) ^ bit)
        # print("Flipping", bit, "in", repr(c) + ", giving", repr(new_c))
        return s[:pos] + new_c + s[pos + 1:]

    def delete_random_character(s):
        # Modifica s de forma que um caractere aleatorio seja deletado.
        return s

    def insert_random_character(s):
        # Modifica s de forma que um caractere aleatorio em inserido aleatoriamente
        # na string s.
        return s

    def mutate(self, s: str) -> str:
        """Retorna s com uma mutacao aleatoria aplicada"""
        mutators = [
            self.flip_random_character,
            self.delete_random_character,
            self.insert_random_character
        ]
        mutator = random.choice(mutators)
        return mutator(s)
