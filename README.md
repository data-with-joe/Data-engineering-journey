# Fintech Exchange Rate Pipeline — Medallion Architecture


## Overview
	An independent end-to-end ELT pipeline that ingests live foreign exchange rate data from a public financial API, processes it through a full Medallion architecture (Bronze/Silver/Gold), and serves analytics-ready tables for reporting and BI consumption. Built entirely without guided instruction to demonstrate independent data engineering capability.
## Architecture
	Layer                Description  
	BronzeRaw            exchange rate data ingested as-is from Open Exchange Rates API — 172 currencies 
	SilverCleaned,       enriched and categorised data with derived metrics
	GoldAggregated       analytics tables ready for BI consumptionOrchestrationMaster pipeline notebook orchestrating all layers in sequence
	    
## Tech Stack

	Platform — Databricks Community Edition
	Processing — Apache Spark, PySpark
	Storage — Delta Lake
	Data Source — Open Exchange Rates API (live financial data)
	Language — Python, SQL
	Architecture Pattern — Medallion (Bronze/Silver/Gold)
## Pipeline flow

	Open Exchange Rates API
	        
	01_api_ingestion      > bronze.exchange_rates (172 currency pairs)
	        
	02_silver_transform   > silver.exchange_rates (cleaned + enriched)
	        
	03_gold_aggregations  > gold.category_summary
	                      > gold.strongest_currencies
	                      > gold.weakest_currencies
	        
	00_pipeline_runner    > orchestrates full pipeline end to end




## Transformations Applied (Silver Layer)

	Filtered invalid/zero rates
	Rounded rates to 6 decimal places
	Derived rate_vs_usd — inverse rate showing USD buying power
	Added rate_category — classifies each currency as stronger, weaker, or pegged to USD
	Added processed_at timestamp for auditability


## Gold Layer Tables
	TableDescriptiongold.category_summaryAggregated stats by currency category — avg, min, max ratesgold.strongest_currenciesTop 20 		    currencies stronger than USDgold.weakest_currenciesTop 20 currencies weaker than USD

## Pipeline Orchestration
	The pipeline is scheduled via Databricks Workflows to run daily.
	Tasks execute in the following order:
	1. `01_api_ingestion` — fetches live data from API
	2. `02_silver_transform` — cleans and enriches data  
	3. `03_gold_aggregations` — builds analytics tables
	
## Key Concepts Demonstrated

	Real API ingestion into a data pipeline (not static files)
	ELT design — raw data preserved in Bronze, transformed inside the platform
	Delta Lake for reliable, versioned storage
	Independent pipeline design without guided instruction
	Medallion architecture implementation on Databricks

# NOTE
	This project was built independently as part of my data engineering portfolio, following the completion of a guided Medallion architecture project. It demonstrates the ability to design and build a pipeline from scratch using real financial data.


	
