import os

SETUP = "The congressman who drafted the Digital Assets Act \u2014 the law that will govern every crypto exchange in America \u2014"
PUNCH = "just asked his aide to print his email so he could scan it back into a PDF."

ENTRY = SETUP + " " + PUNCH


def write_entry(text):
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
