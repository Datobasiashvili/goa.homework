# 1) ისწავლეთ random-ი პითონში(ბიბლოეთეკა)

import random

age = random.randint(0, 100)

print(age)

if age == 0:
    print("You were just born.")
elif age < 12 and age > 1:
    print("You are a kid")
elif age >= 12 and age <= 19:
    print("You are a teenager.")
elif age >= 18 and age < 70:
    print("You are an adult.")
elif age >= 70 and age < 100:
    print("You are a pensioner.")

