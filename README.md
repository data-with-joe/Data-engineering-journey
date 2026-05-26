# Azure Databricks — Medallion Architecture Pipeline

## Overview
An end-to-end data engineering pipeline built on Azure and Databricks, implementing the Medallion Architecture (Bronze/Silver/Gold) pattern for scalable data transformation and analytics.

## Architecture
∙	Landing layer: Raw source files ingested into ADLS
∙	Bronze layer: Raw data loaded as-is into databricks
∙	Silver Layer: Data cleaned and transformed using Apache Spark
∙	Gold Layer: Aggregated analytics-ready data for BI consumption

## Tech Stack
	∙	Cloud — Microsoft Azure
	∙	Storage — Azure Data Lake Storage (ADLS)
	∙	Processing — Apache Spark (PySpark)
	∙	Platform — Databricks
	∙	Table Format — Delta Lake
	∙	Pipeline Framework — Delta Live Tables (DLT)
	∙	Architecture Pattern — Medallion (Bronze/Silver/Gold)
## Concepts Demonstrated
	∙	ELT pipeline design (load raw, transform inside the platform)
	∙	Incremental data processing
	∙	Data lake organization and layer separation
	∙	Spark-based transformations at scale
	∙	Pipeline orchestration via Databricks Workflows (Jobs & Tasks)
	∙	Declarative pipeline management with Delta Live Tables
# Notes
I built this as part of my data engineering learning journey, following industry-standard patterns used in modern cloud data stacks.
