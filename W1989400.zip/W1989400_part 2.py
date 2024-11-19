# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: W1989400
 # Date: 21st of April

# Creating variables to store credits
pass_credit = 0
defer_credit = 0
fail_credit = 0

# Creating variables to store data in list
progression_data = []

# Creating variables to count the progression
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
total_count = 0

# Range of marks
credit_marks = [0, 20, 40, 60, 80, 100, 120]

# Getting the inputs in try and except and handling errors
while True:
    try:
        pass_credit = int(input("Enter your total credits at pass: "))
        if pass_credit not in credit_marks:
            print("Invalid marks")
            continue
    except ValueError:
        print("Integer required, Please try again!")
        continue

    try:
        defer_credit = int(input("Enter your total credits at defer: "))
        if defer_credit not in credit_marks:
            print("Invalid marks")
            continue
    except ValueError:
        print("Integer required, Please try again!")
        continue

    try:
        fail_credit = int(input("Enter your total credit at fail: "))
        if fail_credit not in credit_marks:
            print("Invalid marks")
            continue
    except ValueError:
        print("Integer required, Please try again!")
        continue

    # Using conditional statements for predicting the progression outcomes
    if pass_credit + defer_credit + fail_credit != 120:
        print("Total incorrect")

    elif pass_credit == 120:
        print("Progress")
        progress_count += 1
        progression_data.append(("Progress", pass_credit, defer_credit, fail_credit)) #reference- www.w3schools.com

    elif pass_credit >= 100 and defer_credit <= 20:
        print("Progress (module trailer)")
        trailer_count += 1
        progression_data.append(("Progress (module trailer)", pass_credit, defer_credit, fail_credit))


    elif fail_credit <= 60:
        print("Do not progress (module retriever)")
        retriever_count += 1
        progression_data.append(("Do not progress (module retriever)", pass_credit, defer_credit, fail_credit))

    else:
        print("Exclude")
        exclude_count += 1
        progression_data.append(("Exclude", pass_credit, defer_credit, fail_credit))

    # Getting feedback from the user to see if they want to quit or resume their program and displaying a histogram for the progression outcome
    user_input = input("Enter 'y' for yes or 'q' to quit and view results: ")
    if user_input == "q":
        print("\nHistogram")
        print("---------------------------------------------------------------")
        print("Progress  {} : {}".format(progress_count, "*" * progress_count))
        print("Trailer   {} : {}".format(trailer_count, "*" * trailer_count))
        print("Retriever {} : {}".format(retriever_count, "*" * retriever_count))
        print("Excluded  {} : {}".format(exclude_count, "*" * exclude_count))
        print(
            "\n{} outcomes in total.".format(
                progress_count + trailer_count + retriever_count + exclude_count
            )
        )
        print("---------------------------------------------------------------")
        break
    elif user_input != "y":
        print("\nInvalid choice, terminating program!")
        break
    try:
        user_input = str(user_input)
    except ValueError:
        print("Please enter your input again!")

# Printing Progression data in lists
print("part 2")
for data in progression_data:
    print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}") #references-www.w3schools.com