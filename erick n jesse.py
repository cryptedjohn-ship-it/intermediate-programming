"""GROUP PRESENTATION ABOUT DEVELOPING A USEFUL PYTHON PROGRAM
MEMBERS: JESSE LUCAR AND JOHN ERICK ESCRIBA
TOPIC: PATIENT MANAGEMENT
"""

print("================================")
print("     PATIENT MANAGEMENT SYSTEM")
print("================================")

while True:

    patient_name = input("\nEnter patient name: ")
    age = int(input("Enter patient age: "))
    height = float(input("Enter height (meters): "))
    weight = float(input("Enter weight (kg): "))
    temperature = float(input("Enter temperature (°C): "))
    pain_level = int(input("Enter pain level (0-10): "))
    print("[fever] [cough] [headache]")
    symptoms = input("Describe your symptoms: ").lower()

    # Calculate BMI
    bmi = weight / (height ** 2)

    print("\n---------- PATIENT SUMMARY ----------")
    print("Patient Name:", patient_name)
    print("Age:", age)
    print("Height:", height, "m")
    print("Weight:", weight, "kg")
    print("BMI:", round(bmi, 2))
    print("Temperature:", temperature, "°C")
    print("Pain Level:", pain_level)

    # Patient type
    if age < 18:
        print("Patient Type: Pediatric")

        # Nested if-elif-else
        if temperature >= 38:
            print("Priority: High")
            print("Action: Refer to healthcare provider.")

            if pain_level >= 7:
                print("Action: Assess pain and inform healthcare provider.")

        elif pain_level >= 7:
            print("Priority: High")
            print("Action: Assess pain and inform healthcare provider.")

        else:
            print("Priority: Routine")
            print("Action: Continue regular assessment.")

    elif age < 60:
        print("Patient Type: Adult")

        # Nested if-elif-else
        if temperature >= 38:
            print("Priority: High")
            print("Action: Refer to healthcare provider.")

            if pain_level >= 7:
                print("Action: Assess pain and inform healthcare provider.")

        elif pain_level >= 7:
            print("Priority: High")
            print("Action: Assess pain and inform healthcare provider.")

        else:
            print("Priority: Routine")
            print("Action: Continue regular assessment.")

    else:
        print("Patient Type: Senior Citizen")

        # Nested if-elif-else
        if temperature >= 38:
            print("Priority: High")
            print("Action: Refer to healthcare provider.")

            if pain_level >= 7:
                print("Action: Assess pain and monitor closely.")

        elif pain_level >= 7:
            print("Priority: High")
            print("Action: Assess pain and monitor closely.")

        else:
            print("Priority: Routine")
            print("Action: Continue regular assessment.")

    # Check symptoms
    symptoms1 = []

    if "cough" in symptoms:
        symptoms1.append("Cough = Soothe the throat (warm water)")

    if "headache" in symptoms:
        symptoms1.append("Headache = Rest in a Dark, Quiet Room")

    if "fever" in symptoms:
        symptoms1.append("Fever = Rest and Hydrate")

    if symptoms1:
        print("Symptoms:", ", ".join(symptoms1))
    else:
        print("Symptoms not matched yet...")

    # Continue or exit
    choice = input("\nAdd another patient? (yes/no): ")

    if choice.lower() == "no":
        print("\nThank you for using the Patient Management System!")
        break

