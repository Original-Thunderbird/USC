DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit

DB Design:
Basically, all and only attributes added to tables are those mentioned in https://bytes.usc.edu/cs585/f21_d--a--ta/hw/HW2/index.html, having the same or similar name.
For table 'meeting', normalization is done due to partial dependency (meeting ID) -> (room number, floor number, meeting start time) to remove redundancy. A table 'attendance' is introduced for an employee's appearance at a meeting.
For table 'test', TINYINT type is used to store test result in attribute 'result'. 0 means negative, 1 means positive.

Q1:
When inserting tupes into table, if the error appears and is like ERROR 1062 (23000): Duplicate entry '00005' for key 'employee.PRIMARY' when inserting tuples in a table, it means there the value for primary key is used in other schema. Please drop that schema if you know where the key is in, or drop all other schemas if you don't know.
# of tuples inserted for table 'employee', 'symptom', 'test', 'scan', 'meeting', 'attendacne' is 17, 14, 13, 14, 6, 16 respectively.

Q2:
The most-self-reported symptom is with symptom ID=3, with 6 occurences. (Check row_ID=1,5,7,11,12,14 in table 'symptom')

Q3
I assume the 'sickest' floor means floor(s) with the most people tested positive for COVID-19. The 'sickest' floor is floor 2, with 5 employees tested positive. (Check employee=00000, 00010, 00011, 00012, 00013 in table 'employee' and 'test').

Q4
The period chosen is from period chosen: Dec. 12th, 2020 (inclusive) to Dec. 18th, 2020 (inclusive).
There are 14 scans (Check 'scan_date' attribute of table 'scan'), 13 tests (Check 'test_date' attribute of table 'test'), 8 positive cases (Check 'result' and 'test_date' attribute of table 'test') and 6 employees who self-reported symptoms (Check 'date_reported' attribute and number of different 'employee_ID' of table 'symptom').
Number of tests and positive cases can both be obtained from table 'test' so they are returned in one table. So only 3 working sheets (term borrowed from Microsoft Excel) are there in the output panel, with one table contains 2 cells.

Q5.
Implements table division. 
Idea:
1. get all attendance record of the 3 employees
2. count occurences of all meetings according to meeting ID
3. pick out those meetings with 3 attendcance records
Check tuple ('00001', 'm00002'), ('00001', 'm00005'), ('00001', 'm00006'), ('00003', 'm00002'), ('00003', 'm00005'), ('00003', 'm00006'), ('00008', 'm00002'), ('00008', 'm00005'), ('00008', 'm00006') in Q1.sql or in MySQL workbench.
For division operation, dividend is the table 'attendance' with 2 attributes, divisor is a column of selected employees represented in their ID, and quotient is a column of meetings they attended together.