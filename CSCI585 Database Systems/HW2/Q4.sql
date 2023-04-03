# DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit
# period chosen: Dec. 12th, 2020 (inclusive) - Dec. 18th, 2020 (inclusive)

# number of scans
SELECT count(scan_ID) as scan_count FROM hw2.scan where scan_date>='2020-12-12' and scan_date<='2020-12-18';

# number of tests, number of positive casestest
SELECT count(test_ID) as test_count, sum(result) as positive_cases FROM hw2.test where test_date>='2020-12-12' and test_date<='2020-12-18';

# number of employees who self-reported symptoms
SELECT count(DISTINCT employee_ID) as employee_count FROM hw2.symptom where date_reported>='2020-12-12' and date_reported <='2020-12-18';