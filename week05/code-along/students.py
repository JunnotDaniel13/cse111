import csv

def main():
  I_NUMBER_INDEX = 0
  NAME_INDEX = 1

  students_dict = read_dictionary("students.csv", I_NUMBER_INDEX)

  inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

  inumber = inumber.replace("-", "")

  if not inumber.isdigit():
    print("Invalid character in I-Number")
  else:
    if len(inumber) < 9:
      print("Invalid I-Number: too few digits")
    elif len(inumber) > 9:
      print("Invalid I-Number: too many digits")
    else:
      if inumber not in students_dict:
        print("No such student")
      else:
        value = students_dict[inumber]
        name = value[NAME_INDEX]

        print(name)


def read_dictionary(filename, key_column_index):
  dictionary = {}

  with open(filename, "rt") as csv_file:

    reader = csv.reader(csv_file)

    next(reader)

    for row_list in reader:
      key = row_list[key_column_index]

      dictionary[key] = row_list

  return dictionary

if __name__ == "__main__":
    main()