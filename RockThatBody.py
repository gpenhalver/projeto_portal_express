import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 0.6),
        ("I wanna dance in the lights", 2.2),
        ("I wanna ro-", 0.7),
        ("I wanna rock your body", 2.2),
        ("I wanna go-", 0.6),
        ("I wanna go for a ride", 2.2),
        ("Hop in the music and", 2.5),
        ("Rock your body", 0.9),
        ("Rock that body", 0.99),
        ("come on, come on", 0.5),
        ("Rock that body", 1),
        ("(Rock your body)", 0.9),
        ("Rock that body", 1),
        ("come on, come on", 0.9),
        ("Rock that body", 2.6),
    ]

    for frase, atraso in lines:
        total_chars = len(frase)

        
        type_ratio = 0.6
        time_typing = atraso * type_ratio
        time_per_char = time_typing / total_chars

       
        for char in frase:
            print(f"[yellow]{char}[/yellow]", end="")
            sys.stdout.flush()
            sleep(time_per_char)

        print()
        sleep(atraso * (1.2 - type_ratio))

printLyrics()
