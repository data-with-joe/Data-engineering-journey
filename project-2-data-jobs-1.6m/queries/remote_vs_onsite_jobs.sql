-- Remote vs on-site job count
SELECT 
    job_work_from_home,
    COUNT(*) AS job_count
FROM job_postings_fact
GROUP BY job_work_from_home;