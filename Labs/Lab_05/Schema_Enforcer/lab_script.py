import csv
import json
import pandas as pd

data = [
    [101, "Computer Science", 3.8, "Yes", "15.0"],
    [102, "Data Science", 3, "Yes", "12.5"],
    [103, "Mechanical Engineering", 2.9, "No", "14.0"],
    [104, "Psychology", 3, "No", "10.5"],
    [105, "Biomedical Engineering", 3.7, "Yes", "16.0"]
]

headers = ["student_id", "major", "GPA", "is_cs_major", "credits_taken"]

with open("raw_survey_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 2000,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "BME3080",
        "section": "001",
        "title": "Biomedical Engineering Integrated Design and Experimental Analysis (IDEAS)",
        "level": 3000,
        "instructors": [
            {"name": "Allen", "role": "Primary"}
        ]
    },
    {
        "course_id": "BME3310",
        "section": "001",
        "title": "Biomechanics",
        "level": 3000,
        "instructors": [
            {"name": "Dr. Smith", "role": "Primary"}
        ]
    },
    {
        "course_id": "STS1500",
        "section": "002",
        "title": "Science, Technology, and Society",
        "level": 1000,
        "instructors": [
            {"name": "Prof. Johnson", "role": "Primary"}
        ]
    }
]

with open("raw_course_catalog.json", "w") as json_file:
    json.dump(courses, json_file, indent=4)

df = pd.read_csv("raw_survey_data.csv")
df["is_cs_major"] = df["is_cs_major"].map({"Yes": True, "No": False})
