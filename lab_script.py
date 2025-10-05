import csv
import json
import pandas as pd

survey_data = [
    {"student_id": 101, "major": "Computer Science", "GPA": 3.5, "is_cs_major": "Yes", "credits_taken": "15.0"},
    {"student_id": 102, "major": "Biomedical Engineering", "GPA": 3, "is_cs_major": "No", "credits_taken": "12.5"},
    {"student_id": 103, "major": "Psychology", "GPA": 2.9, "is_cs_major": "No", "credits_taken": "10.0"},
    {"student_id": 104, "major": "Mechanical Engineering", "GPA": 3, "is_cs_major": "No", "credits_taken": "13.5"},
    {"student_id": 105, "major": "Data Science", "GPA": 3.8, "is_cs_major": "Yes", "credits_taken": "16.0"},
]

with open("raw_survey_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["student_id", "major", "GPA", "is_cs_major", "credits_taken"])
    writer.writeheader()
    writer.writerows(survey_data)

course_catalog = [
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
        "course_id": "BME3080",
        "section": "001",
        "title": "Biomedical Engineering Integrated Design and Experimental Analysis (IDEAS)",
        "level": 300,
        "instructors": [
            {"name": "Allen", "role": "Primary"}
        ]
    },
    {
        "course_id": "BME2102",
        "section": "001",
        "title": "Physiology II",
        "level": 200,
        "instructors": [
            {"name": "Barker", "role": "Primary"}
        ]
    },
    {
        "course_id": "BME2220",
        "section": "001",
        "title": "Biomechanics",
        "level": 200,
        "instructors": [
            {"name": "Sheybani", "role": "Primary"}
        ]
    },
    {
        "course_id": "STS2600",
        "section": "001",
        "title": "Engineering Ethics",
        "level": 200,
        "instructors": [
            {"name": "Sergio", "role": "Primary"}
        ]
    },
    {
        "course_id": "BME4995",
        "section": "001",
        "title": "Research for Credit",
        "level": 400,
        "instructors": [
            {"name": "Guilford", "role": "Primary"}
        ]
    }
]

with open("raw_course_catalog.json", "w") as f:
    json.dump(course_catalog, f, indent=2)

df = pd.read_csv("raw_survey_data.csv")
df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False})
df = df.astype({"GPA": "float64", "credits_taken": "float64"})
df.to_csv("clean_survey_data.csv", index=False)

with open("raw_course_catalog.json") as f:
    data = json.load(f)

df_courses = pd.json_normalize(data, record_path=["instructors"], meta=["course_id", "title", "level"])
df_courses.to_csv("clean_course_catalog.csv", index=False)

survey_schema = """# Survey Data Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for each student. |
| `major` | `VARCHAR(50)` | Student’s declared major or field of study. |
| `GPA` | `FLOAT` | Student’s current grade point average. |
| `is_cs_major` | `BOOL` | Indicates whether the student is a Computer Science major (True/False). |
| `credits_taken` | `FLOAT` | Total number of academic credits completed by the student. |
"""

with open("survey_schema.md", "w") as f:
    f.write(survey_schema)

catalog_schema = """# Course Catalog Data Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `name` | `VARCHAR(50)` | Name of the course instructor. |
| `role` | `VARCHAR(20)` | Instructor’s role in the course (Primary, TA, etc.). |
| `course_id` | `VARCHAR(10)` | Unique identifier for the course. |
| `title` | `VARCHAR(150)` | Official course title. |
| `level` | `INT` | Course level (e.g., 200, 300, 400). |
"""

with open("catalog_schema.md", "w") as f:
    f.write(catalog_schema)
