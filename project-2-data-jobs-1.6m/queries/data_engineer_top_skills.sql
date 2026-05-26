-- Top 5 skills for Data Engineer roles
SELECT 
    sd.skills,
    COUNT(sjd.job_id) AS skill_count
FROM job_postings_fact AS jpf
JOIN skills_job_dim AS sjd ON jpf.job_id = sjd.job_id
JOIN skills_dim AS sd ON sjd.skill_id = sd.skill_id
WHERE jpf.job_title_short = 'Data Engineer'
GROUP BY sd.skills
ORDER BY skill_count DESC
LIMIT 5;