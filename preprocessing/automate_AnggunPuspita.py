import pandas as pd
import os


def preprocess_data():
    input_path = "../dataset_raw/titanic.csv"
    output_folder = "data_preprocessing"

    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_csv(input_path)

    # Missing Value Handling
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Drop columns
    df = df.drop(
        ["PassengerId", "Name", "Ticket", "Cabin"],
        axis=1
    )

    # Encoding
    df = pd.get_dummies(
        df,
        columns=["Sex", "Embarked"],
        drop_first=True
    )

    output_path = os.path.join(
        output_folder,
        "titanic_preprocessed.csv"
    )

    df.to_csv(output_path, index=False)

    print("Preprocessing selesai!")
    print(f"File tersimpan di: {output_path}")


if __name__ == "__main__":
    preprocess_data()