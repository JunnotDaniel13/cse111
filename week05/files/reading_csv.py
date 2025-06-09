import csv


def main():
  with open("hymns.csv", mode="rt") as file:

    reader = csv.reader(file)

    for row in reader:
      print(row)


if __name__ == "__main__":
  main()