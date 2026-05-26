-- running total: calculate the running total of previous job title 

select job_title_short, 
		salary_year_avg,
		sum (salary_year_avg) over(
		PARTITION BY job_title_short
		order by job_posted_date
		) as running_total 

from job_postings_fact
where salary_year_avg is not NULL;