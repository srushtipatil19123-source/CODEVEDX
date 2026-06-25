import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n===== Student Performance Prediction System =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Marks")
    print("4. Predict Performance")
    print("5. Top Performer")
    print("6. Average Marks")
    print("7. Ranking")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            df = pd.read_csv("students.csv")
            print(df)

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            marks = int(input("Enter Marks: "))

            df = pd.read_csv("students.csv")
            df.loc[len(df)] = [student_id, name, marks]
            df.to_csv("students.csv", index=False)

            print("Student added successfully!")

        elif choice == "3":
            student_id = int(input("Enter Student ID to update: "))
            new_marks = int(input("Enter New Marks: "))

            df = pd.read_csv("students.csv")

            if student_id in df["student_id"].values:
                df.loc[df["student_id"] == student_id, "marks"] = new_marks
                df.to_csv("students.csv", index=False)
                print("Marks updated successfully!")
            else:
                print("Student ID not found!")

        elif choice == "4":
            df = pd.read_csv("students.csv")

            X = df[["student_id"]]
            y = df["marks"]

            model = LinearRegression()
            model.fit(X, y)

            future_id = int(input("Enter Student ID to predict: "))
            prediction = model.predict([[future_id]])

            print(f"Predicted Marks: {prediction[0]:.2f}")

        elif choice == "5":
            df = pd.read_csv("students.csv")
            top = df.loc[df["marks"].idxmax()]

            print("\nTop Performer")
            print(f"Name : {top['name']}")
            print(f"Marks: {top['marks']}")

        elif choice == "6":
            df = pd.read_csv("students.csv")
            avg = df["marks"].mean()
            print(f"\nAverage Marks: {avg:.2f}")

        elif choice == "7":
            df = pd.read_csv("students.csv")
            ranked = df.sort_values(by="marks", ascending=False)

            print("\n===== Student Ranking =====")
            print(ranked[["name", "marks"]])

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)
        