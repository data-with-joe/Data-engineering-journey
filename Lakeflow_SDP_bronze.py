# read files
import dlt
import pyspark.sql.functions as F


@dlt.table(
    name="fact_sales",
    comment="ingesting data from landing volume to bronze schema",
    # schema = 'bronze'
)
def fact_sales():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/checkpoints/fact_sales/",
        )
        .option("header", True)
        .load("/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/fact_sales/")
        .withColumn("ingestion_timestamp", F.current_timestamp())
    )


@dlt.table(
    name="dim_products",
    comment="ingest files into bronze schema",
    # schema = 'bronze'
)
def dim_products():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/checkpoints/dim_products/",
        )
        .option("header", True)
        .load("/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/dim_products/")
        .withColumn("ingestion_timestamp", F.current_timestamp())
    )


@dlt.table(
    name="dim_customers",
    comment="ingest files from landing to bronze",
    # schema = 'bronze'
)
def dim_customers():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/checkpoints/dim_customers/",
        )
        .option("header", True)
        .load("/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/dim_customers/")
        .withColumn("ingestion_timestamp", F.current_timestamp())
    )


@dlt.table(
    name="dim_regions",
    comment="ingest files from landing into bronze",
    # schema = 'bronze'
)
def dim_regions():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/checkpoints/dim_regions/",
        )
        .option("header", True)
        .load("/Volumes/lakeflow_pipelines/landing/facts_and_dim_files/dim_regions/")
        .withColumn("ingestion_timestamp", F.current_timestamp())
    )
