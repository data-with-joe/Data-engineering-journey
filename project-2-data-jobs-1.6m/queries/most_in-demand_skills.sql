-- What are the top 10 most in-demand skills?
SELECT 
    sd.skills,
    COUNT(sjd.job_id) AS job_count
FROM skills_dim sd
JOIN skills_job_dim AS sjd ON sd.skill_id = sjd.skill_id
GROUP BY sd.skills
ORDER BY job_count DESC
LIMIT 10