# DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit

select * from (
	select floor_num, sum(result) as flr_cnt 
	from hw2.employee natural join hw2.test
	group by floor_num) floor_pos_count 
where flr_cnt = (
	select max(flr_cnt) from (
		select floor_num, sum(result) as flr_cnt 
        from hw2.employee natural join hw2.test
		group by floor_num) floor_pos_count1
);