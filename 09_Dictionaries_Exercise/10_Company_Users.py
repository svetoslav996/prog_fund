companies = {}

while True:
    input_line = input()
    if input_line == "End":
        break

    company_name, employee_id = input_line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = set()

    companies[company_name].add(employee_id)

# Print the company names and employees' ids
for company, employees in companies.items():
    print(company)
    for employee_id in employees:
        print(f"-- {employee_id}")
