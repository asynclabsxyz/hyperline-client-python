import typing_extensions

from hyperline_client.apis.tags import TagValues
from hyperline_client.apis.tags.spark_api import SparkApi
from hyperline_client.apis.tags.user_api import UserApi
from hyperline_client.apis.tags.pipeline_api import PipelineApi
from hyperline_client.apis.tags.file_api import FileApi
from hyperline_client.apis.tags.dataset_api import DatasetApi
from hyperline_client.apis.tags.sql_api import SqlApi
from hyperline_client.apis.tags.api_key_api import ApiKeyApi
from hyperline_client.apis.tags.database_api import DatabaseApi
from hyperline_client.apis.tags.job_api import JobApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SPARK: SparkApi,
        TagValues.USER: UserApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.FILE: FileApi,
        TagValues.DATASET: DatasetApi,
        TagValues.SQL: SqlApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.JOB: JobApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SPARK: SparkApi,
        TagValues.USER: UserApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.FILE: FileApi,
        TagValues.DATASET: DatasetApi,
        TagValues.SQL: SqlApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.DATABASE: DatabaseApi,
        TagValues.JOB: JobApi,
    }
)
