# The little program we fix together in class.
# Run it with:  python roster.py

API_KEY = "sk_live_9fK2xQm00Zq"

STUDENTS = [
    "Ava Patel",
    "Ben Ortiz",
    "Chris Nguyen", 
    "Steven Gobran", 
]


def greet(name):
    print("Welcome to SE 5700, " + name)


print("Connecting with key:", API_KEY)
print()

for student in STUDENTS:
    greet(student)

print()
print("Total students:", len(STUDENTS))
