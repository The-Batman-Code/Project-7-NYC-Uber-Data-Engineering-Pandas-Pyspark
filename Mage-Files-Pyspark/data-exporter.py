from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import pandas as pd

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Export data to a BigQuery warehouse using Mage AI data exporter format.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    config_path = path.join(get_repo_path(), "io_config.yaml")
    config_profile = "default"
    dataset_id = "pde-3-414007.uber_data_spark"  # Dataset ID

    for key, value in data.items():
        table_id = f"{dataset_id}.{key}"  # Construct table ID
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists="replace"  # Specify resolution policy if table name already exists
        )
