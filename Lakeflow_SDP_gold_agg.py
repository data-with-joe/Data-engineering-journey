import dlt
import pyspark.sql.functions as F

@dlt.table(
    name='gold_category_sales_summary',
    comment='aggregated sales summary by product category'
)
def category_sales_summary():
    fact_sales = dlt.read('lakeflow_pipelines.silver.silver_fact_sales').select('sale_id', 'product_id', 'quantity')
    dim_products = dlt.read('lakeflow_pipelines.silver.silver_dim_products').select('product_id', 'category', 'price')

    return (
        fact_sales
            .join(dim_products, on='product_id', how='inner')
            .withColumn('revenue', (F.col('price') * F.col('quantity')).cast('double'))
            .groupBy('category')
            .agg(
                F.sum('revenue').alias('total_revenue'),
                F.countDistinct('sale_id').alias('total_orders'),
                F.sum('quantity').alias('total_quantity')
            )
    )


@dlt.table(
    name='gold_monthly_revenue_trend',
    comment='total revenue aggregated by month'
)
def gold_monthly_revenue_trend():
    fact_sales = dlt.read('lakeflow_pipelines.silver.silver_fact_sales').select('sale_id', 'product_id', 'quantity', 'order_date')
    dim_products = dlt.read('lakeflow_pipelines.silver.silver_dim_products').select('product_id', 'price')

    return (
        fact_sales
            .join(dim_products, on='product_id', how='inner')
            .withColumn('revenue', (F.col('price') * F.col('quantity')).cast('double'))
            .withColumn('month', F.date_format(F.col('order_date'), 'yyyy-MM'))
            .groupBy('month')
            .agg(
                F.sum('revenue').alias('total_revenue'),
                F.countDistinct('sale_id').alias('total_orders')
            )
            .orderBy('month')
    )

@dlt.table(
    name='gold_top_customers_by_revenue',
    comment='total revenue and orders per customer'
)
def gold_top_customers_by_revenue():
    fact_sales = dlt.read('lakeflow_pipelines.silver.silver_fact_sales').select('sale_id', 'customer_id', 'product_id', 'quantity')
    dim_products = dlt.read('lakeflow_pipelines.silver.silver_dim_products').select('product_id', 'price')
    dim_customers = dlt.read('lakeflow_pipelines.silver.silver_dim_customer').select('customer_id', 'first_name', 'last_name')

    return (
        fact_sales
            .join(dim_products, on='product_id', how='inner')
            .join(dim_customers, on='customer_id', how='inner')
            .withColumn('revenue', (F.col('price') * F.col('quantity')).cast('double'))
            .groupBy('customer_id', 'first_name', 'last_name')
            .agg(
                F.sum('revenue').alias('total_revenue'),
                F.countDistinct('sale_id').alias('total_orders')
            )
            .orderBy(F.desc('total_revenue'))
 )

