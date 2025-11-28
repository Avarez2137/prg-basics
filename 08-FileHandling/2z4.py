# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(position_file, "w") as new_file:
    with open(employees_file, "r") as file:
        content = file.readlines()
        print(content)
        for line in content:
            if job_title in line:
                new_file.write(line)
