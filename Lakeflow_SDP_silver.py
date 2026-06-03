# facts sales transformation

import dlt
import pyspark.sql.functions as F

# silver fact_sales cleaning 

@dlt.table(
    name='silver_fact_sales',
    comment='cleaned and transformed fact_sales data'
)
def silver_fact_sales():
    return (
        dlt.read('lakeflow_pipelines.bronze.fact_sales')
            # cast columns
            .withColumn('sale_id', F.col('sale_id').cast('integer'))
            .withColumn('order_date', F.to_date(F.col('order_date'), 'dd/MM/yyyy'))
            .withColumn('customer_id', F.col('customer_id').cast('integer'))
            .withColumn('product_id', F.col('product_id').cast('integer'))
            .withColumn('quantity', F.col('quantity').cast('integer'))
            .withColumn('discount', F.col('discount').cast('integer'))
            .withColumn('region_id', F.col('region_id').cast('integer'))
            .withColumn('channel', F.col('channel').cast('string'))
            .withColumn('promo_code', F.col('promo_code').cast('string'))
            # handle nulls - fill
            .fillna({
                'quantity': 0,
                'discount': 0.0,
                'channel': 'unknown',
                'promo_code': 'none'
            })
            # handle nulls - drop
            .dropna(subset=['sale_id', 'order_date', 'customer_id', 'product_id', 'region_id'])
    )




#silver dim products cleaning

@dlt.table(
    name = 'silver_dim_products',
    comment= 'cleaning and transformed dim products table'
)
def silver_dim_products():
    return(

        dlt.read('lakeflow_pipelines.bronze.dim_products')
                .withColumn('product_id', F.col('product_id').cast('integer'))
                .withColumn('product_name', F.col('product_name').cast('string'))
                .withColumn('category', F.col('category').cast('string'))
                .withColumn('price', F.col('price').cast('double'))
                .withColumn('in_stock', F.col('in_stock').cast('integer'))
                .fillna({'in_stock': 0})
                .fillna('Unknown', subset=['product_name', 'category' ])
                .dropna(subset = ['product_id', 'price'])
    
    )

# silver customer dim cleaning
#customer_id,first_name,last_name,email,join_date,vip

@dlt.table(
    name = 'silver_dim_customer',
    comment = 'cleaning and transforming dim customers'
)
def silver_dim_customer():
    return(
        dlt.read('lakeflow_pipelines.bronze.dim_customers')
            .withColumn('customer_id', F.col('customer_id').cast('integer'))
            .withColumn('first_name', F.col('first_name').cast('string'))
            .withColumn('last_name', F.col('last_name').cast('string'))
            .withColumn('email', F.col('email').cast('string'))
            .withColumn('join_date', F.to_date(F.col('join_date'), 'dd/MM/yyyy'))
            .withColumn('vip', F.col('vip').cast('boolean'))
            .fillna({
                'first_name': 'Unknown',
                'last_name': 'Unknown',
                'email': 'Unknown',
                'vip': False
            })
            .dropna(subset = ['customer_id', 'join_date'])
    )


# cleaning region dim

#region_id,region_name,country

@dlt.table(
    name='silver_dim_regions',
    comment= 'transforming and cleaning regions dim'
)
def silver_dim_regions():
    return(
    dlt.read('lakeflow_pipelines.bronze.dim_regions')
        .withColumn('region_id', F.col('region_id').cast('integer'))
        .withColumn('region_name', F.col('region_name').cast('string'))
        .withColumn('country', F.col('country').cast('string'))

    )
























