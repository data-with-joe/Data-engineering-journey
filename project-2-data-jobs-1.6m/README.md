# Data Jobs EDA — SQL Project

Exploratory data analysis on 1.6 million job postings using PostgreSQL and TablePlus.

## Business Questions
1. What are the top 10 most in-demand skills?
2. What are the top 10 highest paying skills?
3. Which companies have the most job postings?
4. Remote vs on-site — which has more job postings?
5. What are the top paying job titles and their skills?
6. What are the top 5 skills for Data Engineers specifically?

## Key Findings
- **Python and SQL** are the top 2 most in-demand skills with 1.5M+ job mentions each
- **Fedora, Mongo, Debian** are the highest paying skills averaging $164k-$182k
- **beBee Careers** has the most postings at 32k — a job aggregator
- **90% of jobs are on-site** — only 10% remote
- **Senior Data Scientist** is the highest paying role at $153k avg
- **Top 5 Data Engineer skills:** SQL, Python, AWS, Azure, Spark

## Tools
- PostgreSQL
- TablePlus
- Dataset: Luke Barousse Data Jobs (1.6M rows)

## Tables
- `job_postings_fact` — 1.6M job postings
- `company_dim` — company details
- `skills_job_dim` — job to skill mapping
- `skills_dim` — skill names and categories