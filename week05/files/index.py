def main():
  text_list = read_list("plants.txt")
  print(text_list)

def read_list(filename):
  """Read the contents of a text file into a list and
  return the list. Each element in the list will contain
  one line of text from the text file.
  Parameter filename: the name of the text file to read
  Return: a list of strings
  """

  text_list = []

  with open(filename, mode="rt") as text_file:
    for line in text_file:
      cleared_line = line.strip()
      text_list.append(cleared_line)

  return text_list


   
if __name__ == "__main__":
    main()