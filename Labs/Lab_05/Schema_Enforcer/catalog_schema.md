# Course Catalog Data Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `name` | `VARCHAR(50)` | Name of the course instructor. |
| `role` | `VARCHAR(20)` | Instructor’s role in the course (Primary, TA, etc.). |
| `course_id` | `VARCHAR(10)` | Unique identifier for the course. |
| `title` | `VARCHAR(150)` | Official course title. |
| `level` | `INT` | Course level (e.g., 200, 300, 400). |
