import os
import json
import pandas as pd

def convert_json_to_csv(directory):
    # Recursively list all JSON files in the specified directory and its subdirectories
    json_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".json"):
                json_files.append(os.path.join(dirpath, filename))
    
    # Initialize an empty DataFrame
    combined_df = pd.DataFrame()

    # Process each JSON file and add its text data to the DataFrame
    for json_file in json_files:
        # Load the JSON file
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract text data
        text_data = [entry.get("text", "") for entry in data]

        # Convert the list into a pandas DataFrame column
        column_name = os.path.splitext(os.path.basename(json_file))[0]  # Use the filename without extension as column name
        combined_df[column_name] = pd.Series(text_data)

    # Save the combined DataFrame to a single CSV file
    combined_csv_filename = os.path.join(directory, "../"+directory+".csv")
    combined_df.to_csv(combined_csv_filename, index=False)

    return combined_csv_filename

# Example usage:
directory_path = "questions_質問"
convert_json_to_csv(directory_path)