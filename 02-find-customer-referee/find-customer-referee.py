from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.testing.utils import assertDataFrameEqual

spark: SparkSession = SparkSession.builder.getOrCreate()

schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("referee_id", StringType(), True),
    ]
)

data = [
    [1, "Will", None],
    [2, "Jane", None],
    [3, "Alex", 2],
    [4, "Bill", None],
    [5, "Zack", 1],
    [6, "Mark", 2],
]

customer_df = spark.createDataFrame(data, schema)

filtered_df = customer_df.filter(
    (F.col("referee_id") != 2) | (F.col("referee_id").isNull())
)

result_df = filtered_df.select("name")

expected_df = [Row("Will"), Row("Jane"), Row("Bill"), Row("Zack")]

assertDataFrameEqual(result_df, expected_df)