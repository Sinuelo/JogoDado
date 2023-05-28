import random

print("Jogar dado")

jogar = "s"

while jogar == "s":
    numero = random.randint(1, 6)

    if numero == 1:
        print("_________________")
        print("|               |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("|_______________|")

    elif numero == 2:
        print("_________________")
        print("|             O |")
        print("|               |")
        print("|               |")
        print("| O             |")
        print("|_______________|")

    elif numero == 3:
        print("_________________")
        print("|             O |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("| O_____________|")

    elif numero == 4:
        print("_________________")
        print("| O           O |")
        print("|               |")
        print("|               |")
        print("|               |")
        print("| O___________O |")

    elif numero == 5:
        print("_________________")
        print("| O           O |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("| O___________O |")

    elif numero == 6:
        print("_________________")
        print("| O           O |")
        print("|               |")
        print("| O           O |")
        print("|               |")
        print("| O___________O |")
    jogar = input("Pressione (s)  para jogar novamente: ").lower()