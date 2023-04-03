# DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit

# select meetings that employee with ID 00001, 00003 and 00008 all attended
select meeting_ID from (
	select meeting_ID, COUNT(meeting_ID) as cnt from (
		select * from hw2.attendance 
        where employee_ID IN ('00001', '00003', '00008')
	) jntersection 
    group by meeting_ID
) meeting_cnt 
where cnt = 3;