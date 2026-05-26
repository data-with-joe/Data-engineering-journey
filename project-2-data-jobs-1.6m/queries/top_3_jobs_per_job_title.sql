-- top 3 ranked jobs per job title based max salary

with ranked_jobs as (

select job_title_short, salary_year_avg, RANK () 
	over (
		partition by job_title_short
			order by salary_year_avg DESC
		 ) as rank
from job_postings_fact
where salary_year_avg is not NULL

)
select * from ranked_jobs 
where rank <=3 