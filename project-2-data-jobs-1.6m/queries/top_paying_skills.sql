-- What are the top 10 highest paying skills?
SELECT 
    sd.skills,
    ROUND(AVG(jpf.salary_year_avg), 2) AS avg_salary
FROM job_postings_fact AS jpf
JOIN skills_job_dim AS sjd ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd ON sjd.skill_id = sd.skill_id
WHERE jpf.salary_year_avg IS NOT NULL
GROUP BY sd.skills
ORDER BY avg_salary DESC
LIMIT 10;