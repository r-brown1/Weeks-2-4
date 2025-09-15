from src import data_cleaner
from src import utils

if __name__ == "__main__":
    print("Starting data cleaning pipeline...\n")
    data = data_cleaner.get_df_from_csv("./data/data.csv")
    print("Successfully retrieved raw data\n")

    # MISSING VALUE REPORT
    print("Generating missing value report...\n")
    print("Successfully generated missing value report\n")
    print(data_cleaner.generate_missing_values_report(data))

    # HANDLE MISSING VALUES
    print("Handling missing values...\n")
    data = data_cleaner.handle_missing_values(data, ["age", "status"])
    print("Successfully handled missing values\n")

    # CLEANING DATA
    print("Cleaning data...\n")
    data = data_cleaner.standardize_string_values(data, ["gender", "experience", "date", "city", "name"])
    print("Successfully standardized string values\n")
    data = data_cleaner.standardize_num_values(data, ["price", "height" ,"age", "sales"])
    print("Successfully standardized numeric values\n")

    # NORMALIZING DATA
    print("Normalizing data...\n")
    data_cleaner.min_max_normalize(data, "score")
    print("Successfully normalized scores\n")

    # HANDLE OUTLIERS
    print("Handling outliers...\n")
    data = utils.drop_income_outliers(data)
    data = utils.flag_expense_outliers(data)
    print(utils.handle_salary_outliers(data))

    # HANDLE ONE-HOT ENCODING
    print("Adding one-hot encoding columns...\n")
    data = utils.one_hot_encode(data, ["department"])

    # SAVING CLEANED DATA
    print("Saving data...\n")
    data.to_csv("./cleaned_data/cleaned_data.csv", index=False)
    print("Successfully saved cleaned data\n")


