Thoughts are first given based on each of 8 business rules, then comments on overall design are left at the end.

1. The entity 'Employee' can be added. Clearly 'employee_id' is the primary key. 'smartphone_num' shall not be left NULL for any employee.

2. Whether an employee has any symptom doesn't really matter. The company only need to know if an employee is finally tested positive or not. 'status' of 'Employees' will potentially be changed according to the result, which shall not be NULL.

3. The place of test occurs doesn't matter either, yet the (date and) time for testing should be recorded (assuming this is mandatory in the self-report process) in the 'test-time' attribute of 'TestResults' entity. I also assume that time for an onsite testing will also be recorded in the system and so-called 'time' includes date and time.

5. The entity 'Meeting' can be added. Called as 'Meeting', this entity actually describes appearance of an 'employee_id' at the room defined by 'room_num' and 'floor' at 'start_time'. For close contact, we only need to find all 'employee_id's that appear at the same room & time. Each participation of a meeting is identified by the person's id and info of the meeting itself, so 'Meeting' shal be a weak entity.

6. Personally I think it's unnecessary to keep an entity specifically for the purpose of message sending. Targets for close contact notification can be found be using 'Meetings' entity, and those on the same floor can be found by 'floor' attribute, which value cannot be NULL, in 'Employees' entity. However, if the company wants to make a log of notification sending history (I assume so) then fine, it is worthy to add it.
Each row in the 'Notification' entity shall be identified by foreign key 'employee_id', the 'medium' that it is sent (mobile/email), and 'sent_time', so this shall be a weak entity. 'medium' is needed in the key as notifications may be sent to an employee via SMS and email at the same time.

7. Attribute 'status' in entity 'Employee' should have domain {'well', 'sick', 'hospitalized' and 'deceased'} and its value shall not be NULL, thus it alone should be sufficient to see if an employee is tested positive and consequently, cannot be granted access to the building. No attribute like 'is_covid_positive' or 'entrance_allowed' is needed anymore.

8. Here we see that notifications need to be of 2 levels, one is for close contacts, message for them should be like 'test needed'; the other for employees at the same floor and the message should be like 'test recommanded'. So 'Notification' entity should have an attribute 'msg_lvl' with domain of (say,) {'test needed', 'test recommanded'}. 
Attribute 'floor' is needed for entity 'Employee' for selecting employees working on the same floor for message sending. The name is 'floor' as its meaning is the same as the one of the entity 'Meeting'. Same name shall be used to avoid causing synonyms.

Overall Comments:
Entity 'TestResult' will have composite primary key 'employee_id' (also foreign key) and 'test_time'. A person cannot take more than one test at the same time so these are enough for identification. 'test_time' is added to the entity 'TestResult'  to help narrow down potential tracing targets. Say if a person gets negative result for the 1st test and get positive for the second, then with the test time recorded, we only need to inform those who had close contact with the patient during his/her 1st and 2nd test.

An employee can be sent 0 to many notifications, yet a notification is designed for a specific employee, so relationship between 'Employee' and 'Notification' is one and only one to optional many. The same applies for 'TestResults'.
An employee can attend zero to many meetings, having 0 to many participation record, yet a record in the 'Meeting' entity is only available for exactly one employee (assuming E-R diagram does not support list datatype, and if the participation record doesn't contain a specific employee, then the record is meaningless). so relationship 'TestResult' and 'Meeting' is also one and only one to optional many. 

