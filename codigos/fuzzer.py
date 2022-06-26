import random

def fuzzer(max_length: int = 100, char_start: int = 32, char_range: int = 32) -> str:
    """String com um tamanho `max_length` de caracteres
       no intervalo [`char_start`, `char_start` + `char_range`)"""
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

fuzzer()
# A saida e a string aleatoria: '!7#%"*#0=)$;%6*;>638:*>80"=</>(/*:-(2<4 !:5*6856&?""11<7+%<%7,4.8,*+&,,$,."'