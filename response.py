bug = "Infinite Loop"
programmer = "Stressed Coder"

while True:
    print(f"{programmer}: 'Why won't you leave me alone, {bug}?!'")
    print(f"{bug}: 'Because I love you too much!' ")
    response = input("Fix the bug? (yes/no): ").strip().lower()
    if response == "yes":
        print(f"{bug}: 'Nooo! I'll miss you!' ")
        break
    elif response == "no":
        print(f"{bug}: 'Hehe, I'm here forever! '")
    else:
        print(f"{programmer}: 'What kind of answer is that?!' ")
