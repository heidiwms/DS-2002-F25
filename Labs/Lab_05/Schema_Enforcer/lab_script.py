
import csv

import json


students_data = [


    [101, "Computer Science", 3, "Yes", "15.0"],  

    [102, "Biomedical Engineering", 3.7, "No", "12.5"],

    [103, "Psychology", 2, "No", "10.0"], 

    [104, "Mechanical Engineering", 3.95, "No", "9.5"],

    [105, "Computer Science", 4, "Yes", "11.0"],     

]

 


headers = ["student_id", "major", "GPA", "is_cs_major", "credits_taken"]

 

with open("raw_survey_data.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(headers)

    writer.writerows(students_data)


 

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

        "course_id": "BME2220",

        "section": "001",

        "title": "Biomechanics",

        "level": 300,

        "instructors": [

            {"name": "Natasha Sheybani", "role": "Primary"},

        ]

    },

    {

        "course_id": "BME3080",

        "section": "001",

        "title": "IDEAS",

        "level": 300,

        "instructors": [

            {"name": "Tim Allen", "role": "Primary"}

        ]

    },

    {

        "course_id": "STS2600",

        "section": "004",

        "title": "Science, Technology, and Society",

        "level": 300,

        "instructors": [

            {"name": "Sergio Guillen", "role": "Primary"}

        ]

    },

    {

        "course_id": "BME4995",

        "section": "001",

        "title": "Research for Credit",

        "level": 300,

        "instructors": [

            {"name": "William Guilford", "role": "Primary"}

        ]

    },

    {

        "course_id": "BME2102",

        "section": "001",

        "title": "Physiology II",

        "level": 300,

        "instructors": [

            {"name": "Shannon Barker", "role": "Primary"}

        ]

    },

]

 


with open("raw_course_catalog.json", "w") as jsonfile:

    json.dump(courses, jsonfile, indent=4)


 


import pandas as pd



df = pd.read_csv("raw_survey_data.csv")

 

print("\n--- Raw Survey Data ---")

print(df)

 


df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False})

 


df = df.astype({

    "GPA": "float64",

    "credits_taken": "float64"

})

 

print("\n--- Cleaned Survey Data ---")

print(df.dtypes)  

 

df.to_csv("clean_survey_data.csv", index=False)


 

with open("raw_course_catalog.json", "r") as jsonfile:

    course_data = json.load(jsonfile)


df_courses = pd.json_normalize(

    course_data,

    record_path=["instructors"],

    meta=["course_id", "title", "level"]

)

 

print("\n--- Normalized Course Data ---")

print(df_courses)


df_courses.to_csv("clean_course_catalog.csv", index=False)

 