import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n===== Employee Salary Prediction System =====")
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Update Salary")
    print("4. Predict Salary")
    print("5. Highest Salary")
    print("6. Average Salary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            df = pd.read_csv("employees.csv")
            print(df)

        elif choice == "2":
            df = pd.read_csv("employees.csv")
            exp = int(input("Enter Experience: "))
            salary = int(input("Enter Salary: "))
            new = pd.DataFrame([[exp, salary]], columns=df.columns)
            df = pd.concat([df, new], ignore_index=True)
            df.to_csv("employees.csv", index=False)
            print("Employee Added Successfully!")

        elif choice == "3":
            df = pd.read_csv("employees.csv")
            exp = int(input("Enter Experience to Update: "))
            salary = int(input("Enter New Salary: "))
            df.loc[df["experience"] == exp, "salary"] = salary
            df.to_csv("employees.csv", index=False)
            print("Salary Updated Successfully!")

        elif choice == "4":
            df = pd.read_csv("employees.csv")
            X = df[["experience"]]
            y = df["salary"]

            model = LinearRegression()
            model.fit(X, y)

            exp = int(input("Enter Experience: "))
            prediction = model.predict([[exp]])
            print("Predicted Salary:", round(prediction[0], 2))

        elif choice == "5":
            df = pd.read_csv("employees.csv")
            print("Highest Salary:")
            print(df[df["salary"] == df["salary"].max()])

        elif choice == "6":
            df = pd.read_csv("employees.csv")
            print("Average Salary:", df["salary"].mean())

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")

    except Exception as e:
        print("Error:", e)