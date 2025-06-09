def main():
  provinces = read_file("provinces.txt")

  print(provinces)

  provinces.pop(0)

  provinces.pop()

  province_name = "Alberta"

  for index, province in enumerate(provinces):
    if province.lower() == "AB".lower():
      provinces[index] = province_name

  count = provinces.count(province_name)

  print(f"{province_name} occurs {count} times in the modified list.")

def read_file(filename):
  data = []
  with open(filename, mode='rt') as data_file:
    for row in data_file:
      cleared_row = row.strip()
      data.append(cleared_row)

  return data


if __name__ == "__main__":
  main()