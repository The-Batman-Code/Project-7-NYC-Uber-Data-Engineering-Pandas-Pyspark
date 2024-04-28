if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test
from pyspark.sql import SparkSession
import requests
from pyspark.sql import SparkSession
import requests
import os


@data_loader
def load_data_from_api(*args, **kwargs):
    spark = SparkSession.builder.appName("test").getOrCreate()

    url = r"https://storage.googleapis.com/uber-analytics-03/uber_data.csv"
    response = requests.get(url)

    # Get the absolute path of the current working directory
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "uber_data.csv")

    with open(file_path, "wb") as f:
        f.write(response.content)

    # Read the local CSV file into a Spark DataFrame with column names
    df = (
        spark.read.option("inferSchema", "true")
        .option("header", "true")
        .csv(f"file:///{file_path}")
    )

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
