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
                        - Remove a user from both the login and persons CSV
                          files
                    3. `update`
                        - Update specific data in the CSV table
            - `class Student` (for user type student e.g. student, lead,
              member)
                - Command list for a student role
                    1. `Become lead`
                        - Make project and change role to lead (require new
                          login)
                    2. `Check member pending request`
                        - Check the member pending table that contains the user
                          id accept or don't do anything
                - Command list for a lead role
                    1. `Send invitation to member/s`
                        - Send request to students to be a member of the team
                    2. `Change update project`
                        - Update project detail or name
                    3. `Send request for advisor`
                        - Send request for advisor one at a time
                    4. `Submit project for evaluation`
                        - Submit the ongoing project and change it to pending
                    5. `Check status`
                        - Check the status of the project
                - Command list for a member role
                    1. `Change update project`
                        - Update project detail or name
                    2. `Check status`
                        - Check the status of the project
            - `class Faculty` (For user type faculty)
                - Command list for both faculty and advisor
                    1. `Check advisor pending request`
                        - Check the advisor pending table that contains the
                          user id accept or deny
                    2. `Evaluate projects`
                        - Evaluate one of the pending project files
                    3. `See all projects`
                        - See all student project files
* **How to run my project**
    * Proceed to project_manage.py and run that file
    * Enter username
    * Enter password
    * Select option
    * If finished continue use 'y', else stop and exit use 'n'

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

| Role            | Action                                                                           | Method                   | Class   | Completion |
|-----------------|----------------------------------------------------------------------------------|--------------------------|---------|-----------:|
| admin           | Begins admin role command and provide options for admin                          | admin                    | Admin   |       100% |
| admin           | Add entry for new user to the table                                              | add_entry                | Admin   |       100% |
| admin           | Remove entry of user from the table                                              | remove_entry             | Admin   |       100% |
| admin           | Update a specific value in the table                                             | admin_update             | Admin   |       100% |
| dev_only        | Show a table for admin update action                                             | show_table               | Admin   |       100% |
| student         | Begins student role command and provide options for student                      | student                  | Student |       100% |
| student         | Change from lead role while create a new project only use by student as option 1 | add_project              | Student |       100% |
| student         | Check the table of user invitation to accept or leave it                         | check_member_request     | Student |       100% |
| lead            | Begins lead role command and provide options for lead                            | lead                     | Student |       100% |
| lead            | Send an invitation to a student that doesn't belong in any project               | send_invite_member       | Student |       100% |
| lead            | Send an invitation to a faculty only one at a time                               | send_invite_advisor      | Student |       100% |
| lead            | Submit project and change status to pending                                      | submit_project           | Student |       100% |
| lead/member     | Update a name or the detail of your project                                      | update_project           | Student |       100% |
| lead/member     | Check own project status e.g. pending, ongoing, number of A                      | check_stat               | Student |       100% |
| member          | Begins member role command and provide options for member                        | member                   | Student |       100% |
| faculty/advisor | Begins faculty/advisor role command and provide options for faculty staff        | faculty                  | Faculty |       100% |
| faculty/advisor | Check the table of user invitation to accept or deny it                          | check_faculty_request    | Faculty |       100% |
| dev_only        | Find project of the group you want using id                                      | project_find_id_consider | Faculty |       100% |
| faculty/advisor | Evaluation step:                                                                 | evaluate                 | Faculty |       100% |
|                 | 1. Let faculties pick the project to evaluate and approve                        |                          |         |            |
|                 | 2. Check the detail and vote for A (Approve) or D (Decline)                      |                          |         |            |
|                 | 3. For the project to be complete requirement is 2 A                             |                          |         |            |
| faculty/advisor | Show all projects                                                                | show_project_table       | Faculty |       100% |


* **Missing function**
    - I don't know what else to write, probably none
    - When I tested it there are no bugs
