import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n===== House Price Prediction System =====")
    print("1. View Houses")
    print("2. Add House")
    print("3. Update Price")
    print("4. Predict Price")
    print("5. Highest Price")
    print("6. Average Price")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            df = pd.read_csv("houses.csv")
            print(df)

        elif choice == "2":
            df = pd.read_csv("houses.csv")
            area = int(input("Enter House Area (sq ft): "))
            price = int(input("Enter House Price: "))
            new_house = pd.DataFrame([[area, price]], columns=df.columns)
            df = pd.concat([df, new_house], ignore_index=True)
            df.to_csv("houses.csv", index=False)
            print("House Added Successfully!")

        elif choice == "3":
            df = pd.read_csv("houses.csv")
            area = int(input("Enter Area to Update: "))
            new_price = int(input("Enter New Price: "))
            df.loc[df["area"] == area, "price"] = new_price
            df.to_csv("houses.csv", index=False)
            print("Price Updated Successfully!")

        elif choice == "4":
            df = pd.read_csv("houses.csv")

            X = df[["area"]]
            y = df["price"]

            model = LinearRegression()
            model.fit(X, y)

            area = int(input("Enter House Area: "))
            prediction = model.predict([[area]])

            print("Predicted House Price:", round(prediction[0], 2))

        elif choice == "5":
            df = pd.read_csv("houses.csv")
            print("\nHouse with Highest Price:")
            print(df[df["price"] == df["price"].max()])

        elif choice == "6":
            df = pd.read_csv("houses.csv")
            print("Average House Price:", round(df["price"].mean(), 2))

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")

    except Exception as e:
        print("Error:", e)