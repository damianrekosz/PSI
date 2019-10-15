import random

students = (random.randrange(100000,999999), random.randrange(100000,999999), random.randrange(100000,999999),
            random.randrange(100000,999999), random.randrange(100000,999999), random.randrange(100000,999999),
            "jan kowalski", "adam zakrzewski", "wiktor wiśniewski", "marta dąbrowska", "iwona kłosińska", "józef śliwowski")

print("indexy:")
print(students[:6])
print("nazwiska:")
print(students[6:])
