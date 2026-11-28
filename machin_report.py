def check_user_input(prompt, minimum=0, maximum=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
        if value < minimum:
            print("Error! Parts produced and/or Defective parts cant be less than 0")
            continue
        if maximum is not None and value > maximum:
            print("Error! Parts produced cant be less than defective parts")
            continue
        return value


def check_another_machine():
    while True:
        answer = input("Check another machine? (yes/no): ").strip().lower()
        if answer == "yes":
            return True
        if answer == "no":
            return False
        print("Please answer yes or no.")


checked_machines = 0
total_parts = 0
total_defective_parts = 0

while True:
    parts_produced = check_user_input("Enter the amount of parts the machine produced: ")
    if parts_produced == 0:
        print("No parts Produced today, there are no defective parts")
        defective_parts = 0
    else:
        defective_parts = check_user_input(
            "Enter the amount of defective parts: ",
            minimum=0,
            maximum=parts_produced,
        )
        defect_rate = defective_parts / parts_produced * 100
        print("defect rate is:", defect_rate, "%")

    checked_machines += 1
    total_parts += parts_produced
    total_defective_parts += defective_parts

    if not check_another_machine():
        break

print("Summary:")
print("Machines checked:", checked_machines)
print("Total parts produced:", total_parts)
print("Total defective parts:", total_defective_parts)
if total_parts == 0:
    print("No parts were produced on any machine, so there is no overall defect rate to calculate.")
else:
    overall_defect_rate = total_defective_parts / total_parts * 100
    print("Overall defect rate:", overall_defect_rate, "%")