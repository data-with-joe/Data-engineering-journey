-- Top paying job titles with associated skills
SELECT 
    jpf.job_title_short,
    ROUND(AVG(jpf.salary_year_avg), 2) AS avg_salary,
    STRING_AGG(DISTINCT sd.skills, ', ') AS top_skills
FROM job_postings_fact jpf
JOIN skills_job_dim AS sjd ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd ON sjd.skill_id = sd.skill_id
WHERE jpf.salary_year_avg IS NOT NULL
GROUP BY jpf.job_title_short
ORDER BY avg_salary DESC
LIMIT 10;