-- Which companies have the most job postings?
SELECT 
    cd.name,
    COUNT(jpf.company_id) AS job_count
FROM job_postings_fact AS jpf
JOIN company_dim AS cd ON jpf.company_id = cd.company_id
GROUP BY cd.name
ORDER BY job_count DESC
LIMIT 10;