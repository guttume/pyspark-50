from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark: SparkSession = SparkSession.builder.appName("pyspark-50").master("local[*]").getOrCreate()

schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("low_fats", StringType(), True),
    StructField("recyclable", StringType(), True)
])

data = [
    (0, "Y", "N"),
    (1, "Y", "Y"),
    (2, "N", "Y"),
    (3, "Y", "Y"),
    (4, "N", "N"),
]

product_df = spark.createDataFrame(data, schema)

filtered_df = product_df.filter((f.col("low_fats") == "Y") & (f.col("recyclable") == "Y"))

result_df = filtered_df.select("product_id")

result_df.show()

