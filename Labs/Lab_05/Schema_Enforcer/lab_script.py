import csv

import json

import pandas as pd

# Define the data with intentional type inconsistencies
rows = [
    [101, 'Computer Science', 3.5, 'Yes', '15.0'],      # credits_taken as string
    [102, 'Mathematics', 4, 'No', '12.5'],               # GPA as int, credits_taken as string
    [103, 'Physics', 2.8, 'No', '10.5'],                 # credits_taken as string
    [104, 'Computer Science', 3, 'Yes', '18.0'],         # GPA as int, credits_taken as string
    [105, 'Biology', 3.2, 'No', '14.0']                  # credits_taken as string
]

# Write to CSV file
with open('raw_survey_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['student_id', 'major', 'GPA', 'is_cs_major', 'credits_taken'])
    # Write data rows
    writer.writerows(rows)

# Define hierarchical course data
courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "STAT3001",
        "section": "002",
        "title": "Statistical Methods",
        "level": 300,
        "instructors": [
            {"name": "Jane Doe", "role": "Primary"}
        ]
    }
]

# Write hierarchical data to JSON file
with open('raw_course_catalog.json', 'w') as jsonfile:
    json.dump(courses, jsonfile, indent=2)

# --- Task 3: Clean and Validate the CSV Data ---
# Load raw_survey_data.csv into a DataFrame
df = pd.read_csv('raw_survey_data.csv')

# Enforce Boolean Type for is_cs_major
df['is_cs_major'] = df['is_cs_major'].replace({'Yes': True, 'No': False})

# Enforce Numeric Type for credits_taken and GPA
df = df.astype({'credits_taken': 'float64', 'GPA': 'float64'})

# Save cleaned DataFrame
df.to_csv('clean_survey_data.csv', index=False)

# --- Task 4: Normalize the JSON Data ---
# Load raw_course_catalog.json
with open('raw_course_catalog.json', 'r') as jsonfile:
    course_data = json.load(jsonfile)

# Normalize instructors
norm_df = pd.json_normalize(
    course_data,
    record_path=['instructors'],
    meta=['course_id', 'title', 'level']
)

# Save normalized DataFrame
norm_df.to_csv('clean_course_catalog.csv', index=False)
