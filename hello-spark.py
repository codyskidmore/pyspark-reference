from pyspark.sql import *

from lib.logger import Logger

if __name__ != "__main__":
    quit()
    #    conf = get_spark_app_config()

# TODO Get this from config instead of hard coding it.
app_name = "Hello Spark"
logger_root = "spark.reference.app"

spark = (SparkSession
         .builder
         .appName(app_name)
         .master("local[3]")
         .getOrCreate())

logger = Logger(spark, logger_root, app_name)

logger.info("Starting HelloSpark")

logger.info("Finished HelloSpark")
spark.stop()
