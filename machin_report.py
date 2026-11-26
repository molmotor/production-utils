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
    answer=input("Check another machine? : ").strip().lower()
    



parts_produced = check_user_input("Enter the amount of parts the machine produced: ")
if parts_produced == 0:
    print("No parts Produced today, there are no defective parts")
else:
    defective_parts = check_user_input(
        "Enter the amount of defective parts: ",
        minimum=0,
        maximum=parts_produced,
    )
    defect_rate = defective_parts / parts_produced * 100
    print("defect rate is:", defect_rate, "%")