# File where all side effect logs will be stored
log_file = "side_effects.txt"

# List of common side effects the user can choose from
side_effects = [
    "Nausea",
    "Headache",
    "Dizziness",
    "Fatigue",
    "Rash",
    "Insomnia",
    "Diarrhea",
    "Constipation",
    "Dry mouth",
    "Blurred vision",
    "Other"
]


# Let the user choose a side effect from the list.
# If they choose "Other", they can type their own description.
def choose_side_effect():

    while True:

        print("Choose a side effect:")

        for i in range(len(side_effects)):
            print(str(i + 1) + ".", side_effects[i])

        try:

            choice = int(input("Enter a number: "))

            if choice >= 1 and choice <= len(side_effects):

                effect = side_effects[choice - 1]

                if effect == "Other":

                    other = input(
                        "Please describe the other side effect: "
                    )

                    if other != "":
                        return other

                    print("Description cannot be empty.")

                else:
                    return effect

        except ValueError:
            pass

        print("Invalid choice. Please try again.")


# Add a medication and dosage to the medication list
def add_medication(medications):

    name = input("Medication name: ")
    dosage = input("Dosage: ")

    medications.append([name, dosage])

    print("Medication added.")


# Show all medications and return the one selected by the user
def choose_medication(medications):

    if len(medications) == 0:
        print("No medications available.")
        return None

    print("Choose a medication:")

    for i in range(len(medications)):

        print(
            str(i + 1) + ". " +
            medications[i][0] +
            " (" +
            medications[i][1] +
            ")"
        )

    try:

        choice = int(input("Enter a number: "))

        if choice >= 1 and choice <= len(medications):
            return medications[choice - 1]

    except ValueError:
        pass

    print("Invalid choice.")
    return None


# Load previously saved logs from the file
def load_logs():

    logs = []

    try:

        with open(log_file, "r") as file:

            for line in file:

                parts = line.strip().split(",")

                # Each log should contain 5 pieces of information
                if len(parts) == 5:
                    logs.append(parts)

    except:
        print("No previous logs found.")

    return logs


# Save all logs to the file
def save_logs(logs):

    with open(log_file, "w") as file:

        for log in logs:

            # Convert the log list into a comma-separated string
            line = ",".join(log)

            # Write the log to the file and move to a new line
            file.write(line + "\n")


# Create a new side effect log for a medication
def log_side_effect(logs, medications):

    medication_info = choose_medication(medications)

    if medication_info == None:
        return

    medication = medication_info[0]
    dosage = medication_info[1]

    effect = choose_side_effect()

    date = input("Date and time: ")

    notes = input("Notes: ")

    # Store all information for this side effect entry
    new_log = [
        medication,
        dosage,
        effect,
        date,
        notes
    ]

    logs.append(new_log)

    save_logs(logs)

    print("Side effect saved.")


# Allow the user to view all logs or logs for one medication
def view_logs(logs, medications):

    print("View Logs")
    print("1. All medications")
    print("2. Specific medication")

    option = input("Choose an option: ")

    if option == "1":

        if len(logs) == 0:
            print("No logs found.")
            return

        print("Logs:")

        for log in logs:

            print(
                log[0] + " (" +
                log[1] + ") - " +
                log[3] + " - " +
                log[2] + " - " +
                log[4]
            )

    elif option == "2":

        medication_info = choose_medication(medications)

        if medication_info == None:
            return

        medication = medication_info[0]
        dosage = medication_info[1]

        # Track whether any matching logs were found
        found = False

        print("Logs:")

        for log in logs:

            if log[0] == medication and log[1] == dosage:

                print(
                    log[3] + " - " +
                    log[2] + " - " +
                    log[4]
                )

                found = True

        if found == False:
            print("No logs found.")

    else:
        print("Invalid option.")


# Main program
def main():

    print("Medication Side Effect Logger")

    # Load any logs that were saved from previous runs
    logs = load_logs()

    # Store medications added during this session
    medications = []

    running = True

    # Keep showing the menu until the user exits
    while running:

        print()
        print("Menu")
        print("1. Add medication")
        print("2. Log side effect")
        print("3. View logs")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":

            add_medication(medications)

        elif option == "2":

            log_side_effect(logs, medications)

        elif option == "3":

            view_logs(logs, medications)

        elif option == "4":

            running = False
            print("Goodbye.")

        else:

            print("Invalid option.")


main()