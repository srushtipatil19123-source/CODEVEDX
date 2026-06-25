import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n===== Car Price Prediction System =====")
    print("1. View Cars")
    print("2. Add Car")
    print("3. Update Price")
    print("4. Predict Price")
    print("5. Highest Price")
    print("6. Average Price")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            df = pd.read_csv("cars.csv")
            print(df)

        elif choice == "2":
            df = pd.read_csv("cars.csv")

            car_id = len(df) + 1
            brand = input("Enter Brand: ")
            year = int(input("Enter Year: "))
            price = float(input("Enter Price: "))

            new_row = pd.DataFrame({
                "car_id": [car_id],
                "brand": [brand],
                "year": [year],
                "price": [price]
            })

            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv("cars.csv", index=False)
            print("Car Added Successfully!")

        elif choice == "3":
            df = pd.read_csv("cars.csv")

            car_id = int(input("Enter Car ID: "))
            new_price = float(input("Enter New Price: "))

            df.loc[df["car_id"] == car_id, "price"] = new_price
            df.to_csv("cars.csv", index=False)

            print("Price Updated Successfully!")

        elif choice == "4":
            df = pd.read_csv("cars.csv")

            X = df[["year"]]
            y = df["price"]

            model = LinearRegression()
            model.fit(X, y)

            year = int(input("Enter Year: "))
            prediction = model.predict([[year]])

            print("Predicted Price:", round(prediction[0], 2))

        elif choice == "5":
            df = pd.read_csv("cars.csv")
            print("\nCar With Highest Price:")
            print(df[df["price"] == df["price"].max()])

        elif choice == "6":
            df = pd.read_csv("cars.csv")
            print("Average Car Price:", round(df["price"].mean(), 2))

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")

    except Exception as e:
        print("Error:", e)