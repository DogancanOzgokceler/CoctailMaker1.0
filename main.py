#Doğancan Özgökçeler
#𒀀𒀸𒋗𒇷

import random

# Initialize variables to store user's ratings
caffeine_score = 0
fruit_score = 0
spice_score = 0
refreshment_score = 0

# Ingredient options
beverage_options = ["kola", "fanta", "sprite", "soda"]
fruit_options = ["limon suyu", "portakal suyu", "yeşil elma suyu"]
spice_options = ["vanilya", "anason", "karanfil", "zencefil"]
refreshment_options = ["taze nane yaprağı", "limon dilimi"]

# Read user's ratings
caffeine_score = int(input("Kafein puanınızı 5 üzerinden girin: "))
fruit_score = int(input("Meyve puanınızı 5 üzerinden girin: "))
spice_score = int(input("Baharat puanınızı 5 üzerinden girin: "))
refreshment_score = int(input("Ferahlık 5 üzerinden puanınızı girin: "))

# Handle the case when user's rating is more than 5
if caffeine_score > 5:
    print("Sizin kafein için verdiğiniz puan istenen veriden çok fazla olduğu için 5 sayılacak.")
    caffeine_score = 5

if fruit_score > 5:
    print("Sizin meyve için verdiğiniz puan istenen veriden çok fazla olduğu için 5 sayılacak.")
    fruit_score = 5

if spice_score > 5:
    print("Sizin baharat için verdiğiniz puan istenen veriden çok fazla olduğu için 5 sayılacak.")
    spice_score = 5

if refreshment_score > 5:
    print("Sizin ferahlık için verdiğiniz puan istenen veriden çok fazla olduğu için 5 sayılacak.")
    refreshment_score = 5

# Choose ingredients based on user's ratings
if caffeine_score > 3 and fruit_score > 3:
    selected_ingredient = random.choice(fruit_options)
else:
    if spice_score > 3:
        selected_ingredient = random.choice(spice_options)
    else:
        selected_ingredient = random.choice(refreshment_options)

# Choose beverage
selected_beverage = random.choice(beverage_options)

# Create cocktail
cocktail = []
cocktail.append(selected_beverage)
cocktail.append(selected_ingredient)
cocktail.append("buz")

# Print cocktail
print("Özel kokteyliniz:", cocktail)

#THE END 
#21.03.2023 Finish/Bitiş