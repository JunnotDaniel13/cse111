import csv

COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 3
NUM_PATIENTS_INDEX = 4
def main():
  with open("dentists.csv", mode="rt") as file:

    reader = csv.reader(file)
    next(reader)

    running_max = 0
    most_office = None

    for row_list in reader:
      company = row_list[COMPANY_NAME_INDEX]
      num_employees = int(row_list[NUM_EMPS_INDEX])
      num_patients = int(row_list[NUM_PATIENTS_INDEX])
      
      patients_per_emp = num_patients / num_employees

      if patients_per_emp > running_max:
          running_max = patients_per_emp
          most_office = company

  print(f"{most_office} has {running_max:.1f} patients per employee")

  
if __name__ == '__main__':
  main()