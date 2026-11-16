print("===== VOTING ELIGIBILITY SYSTEM =====")

voters_checked = 0
eligible_voters = 0
not_eligible_voters = 0

while True:

    name = input("\nEnter your name: ")

    # Age validation
    while True:
        try:
            age = int(input("Enter your age: "))

            if age >= 0 and age <= 120:
                break
            else:
                print("Invalid age. Age must be between 0 and 120.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    citizen = input("Are you an Indian citizen? (y/n): ").lower()

    while citizen != "y" and citizen != "n":
        print("Please enter y or n.")
        citizen = input("Are you an Indian citizen? (y/n): ").lower()

    voters_checked += 1

    # Checking voting eligibility
    if age >= 18 and citizen == "y":
        print(name, "is eligible to vote.")
        eligible_voters += 1

    elif age < 18:
        print(name, "is not eligible to vote.")
        print("Reason: Age is below 18.")
        print("Years left:", 18 - age)
        not_eligible_voters += 1

    else:
        print(name, "is not eligible to vote.")
        print("Reason: Not an Indian citizen.")
        not_eligible_voters += 1

    another = input("\nCheck another voter? (y/n): ").lower()

    if another != "y":
        break

# Final summary
print("\n===== FINAL SUMMARY =====")
print("Voters checked:", voters_checked)
print("Eligible voters:", eligible_voters)
print("Not eligible voters:", not_eligible_voters)