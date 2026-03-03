age = input("Quel est votre age ? ")
age = int(age)

if age >= 0 and age <= 12:
    print("Vous etes un enfant")
elif age > 12 and age < 18:
    print("Vous etes un adolescent")
elif age >= 18 and age <= 64:
    print("Vous etes un adulte")
else:
    print("Vous etes un senior")