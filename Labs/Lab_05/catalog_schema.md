# Course Catalog Data Schema

| Column Name    | Required Data Type | Brief Description |
| :---           | :---              | :---             |
| `name`         | `VARCHAR(50)`     | Instructor's full name. |
| `role`         | `VARCHAR(20)`     | Instructor's role in the course (e.g., Primary, TA). |
| `course_id`    | `VARCHAR(10)`     | Unique identifier for the course. |
| `title`        | `VARCHAR(100)`    | Title of the course. |
| `level`        | `INT`             | Course level (e.g., 200, 300). |
