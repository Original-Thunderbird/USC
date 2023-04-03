# DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit

select sym_type from (
	select sym_type, count(sym_type) as sym_count 
	from hw2.symptom 
    group by sym_type) sym_count_view
where sym_count = (
	select max(sym_count) from (
		select sym_type, count(sym_type) as sym_count 
		from hw2.symptom 
        group by sym_type) sym_count_view1
);