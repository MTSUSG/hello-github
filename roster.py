# The little program we fix together in class.
# Run it with:  python roster.py

import os


def load_env(path=".env"):
    """Read KEY=value lines out of .env and into the environment."""
    for line in open(path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key] = value


load_env()
API_KEY = os.environ["API_KEY"]

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
