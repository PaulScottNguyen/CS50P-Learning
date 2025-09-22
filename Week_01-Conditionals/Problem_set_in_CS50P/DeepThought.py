#Ask user the question, their input will be stripped, lowercase after
answer = str(input(f"What is the answer to the greatest question of life, the universe, and everything? ")).strip().lower()
match answer: #Use function match to create two cases
    case "42"|"forty two"|"forty-two":
        print(f"Yes")
    case _:  #All other cases
        print(f"That was not correct! The answer is 42")