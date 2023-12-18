# Final project for 2023's 219114/115 Programming I

* **List of Files**
  * **Python Files**
    - **project_manage.py**
      - Main file to run and test the code
    - **database.py**
      - `class Table` (stores a list of dictionaries)
      - `class DB` (stores a list of `Table` instances with names)
      - `class Read` (for reading and updating CSV files)
      - Test function for this Python file only
    - **roles.py**
      - Random project name for test
      - Keys for each table
      - Check function (only in some situations)
      - Update_all_csv function (update all current version CSV tables)
      - `class Admin` (for user type admin)
        - Command list for an admin role
          1. `add_entry`
             - Add a user to both the login and persons CSV files
          2. `remove_entry`
             - Remove a user from both the login and persons CSV files
          3. `update`
             - Update specific data in the CSV table
      - `class Student` (for user type student e.g. student, lead, member)
        - Command list for a student role
          1. `Become lead`
             - Make project and change role to lead (require new login)
          2. `Check member pending request`
             - Check member pending table that contains the user id
        - Command list for a lead role

* **CSV Files**
  - `persons.csv`
  - `login.csv`
  - `Advisor_pending_request.csv`
  - `Member_pending_request.csv`
  - `Project.csv`

* **Other Files and Folders**
  - `backup_csv_just_in_case`
    - Contains original CSV files
  - (Add other files and folders as needed)


| Header 1     | Header 2     | Header 3     |
|--------------|--------------|--------------|
| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col   |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |

