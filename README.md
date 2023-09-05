# hyperline-client
DO NOT EDIT THIS FILE!


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://asynclabs.xyz](http://asynclabs.xyz)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/asynclabsxyz/hyperline-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/asynclabsxyz/hyperline-client-python.git`)

Then import the package:
```python
import hyperline_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hyperline_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import hyperline_client
from hyperline_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.ApiKeyApi(api_client)

    try:
        # Create an API key
        api_response = api_instance.create_api_key()
        print("The response of ApiKeyApi->create_api_key:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */api/v1beta*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiKeyApi* | [**create_api_key**](docs/ApiKeyApi.md#create_api_key) | **POST** /api_keys | Create an API key
*ApiKeyApi* | [**get_api_key**](docs/ApiKeyApi.md#get_api_key) | **GET** /api_keys | Get an API key info
*CodeApi* | [**create_code_file**](docs/CodeApi.md#create_code_file) | **POST** /code | Create a file
*CodeApi* | [**list_code_files**](docs/CodeApi.md#list_code_files) | **GET** /code | List code files
*DatabaseApi* | [**get_database_schema**](docs/DatabaseApi.md#get_database_schema) | **GET** /database/schema | Get database schema
*DatasetApi* | [**get_dataset_metadata**](docs/DatasetApi.md#get_dataset_metadata) | **GET** /datasets/metadata | Get dataset metadata
*DatasetApi* | [**get_dataset_preview**](docs/DatasetApi.md#get_dataset_preview) | **GET** /datasets/preview | Get dataset preview
*DatasetApi* | [**list_datasets**](docs/DatasetApi.md#list_datasets) | **GET** /datasets | List datasets
*DatasetApi* | [**list_explorer_datasets**](docs/DatasetApi.md#list_explorer_datasets) | **GET** /datasets/explorer | List datasets for web explorer
*DatasetApi* | [**list_explorer_datasets_details**](docs/DatasetApi.md#list_explorer_datasets_details) | **GET** /datasets/explorer/details | List datasets details for web explorer
*FileApi* | [**create_file**](docs/FileApi.md#create_file) | **POST** /files | Create a file
*FileApi* | [**get_file_content**](docs/FileApi.md#get_file_content) | **GET** /files/content | Get file content
*FileApi* | [**get_file_metadata**](docs/FileApi.md#get_file_metadata) | **GET** /files/metadata | Get file metadata
*FileApi* | [**get_file_preview**](docs/FileApi.md#get_file_preview) | **GET** /files/preview | Get file preview
*FileApi* | [**get_samples**](docs/FileApi.md#get_samples) | **GET** /files/samples | Get sample files
*FileApi* | [**list_files**](docs/FileApi.md#list_files) | **GET** /files | List files
*JobApi* | [**list_jobs**](docs/JobApi.md#list_jobs) | **GET** /jobs | List user jobs
*PipelineApi* | [**backfill_pipeline**](docs/PipelineApi.md#backfill_pipeline) | **POST** /pipeline/backfill | Backfill a pipeline
*PipelineApi* | [**create_pipeline**](docs/PipelineApi.md#create_pipeline) | **POST** /pipelines | Create a pipeline
*PipelineApi* | [**delete_pipeline**](docs/PipelineApi.md#delete_pipeline) | **POST** /pipelines/{pipeline_name}/delete | Delete a pipeline
*PipelineApi* | [**deploy_pipeline**](docs/PipelineApi.md#deploy_pipeline) | **POST** /pipelines/{pipeline_name}/deploy | Deploy a pipeline
*PipelineApi* | [**edit_pipeline**](docs/PipelineApi.md#edit_pipeline) | **POST** /pipeline/edit | Edit a pipeline
*PipelineApi* | [**get_pipeline**](docs/PipelineApi.md#get_pipeline) | **GET** /pipelines/{pipeline_name} | Get a pipeline
*PipelineApi* | [**get_pipeline_run**](docs/PipelineApi.md#get_pipeline_run) | **GET** /pipelines/{pipeline_name}/runs/{run_id} | Get information of a pipeline run
*PipelineApi* | [**get_stage_instances**](docs/PipelineApi.md#get_stage_instances) | **GET** /pipelines/{pipeline_name}/runs/{run_id}/stages | Get stage instances of a pipeline
*PipelineApi* | [**get_stage_log**](docs/PipelineApi.md#get_stage_log) | **GET** /pipelines/{pipeline_name}/runs/{run_id}/stages/{stage_name}/logs/{try_number} | Get the logs of a pipeline stage instance
*PipelineApi* | [**list_pipeline_runs**](docs/PipelineApi.md#list_pipeline_runs) | **GET** /pipelines/{pipeline_name}/runs | List runs of a pipeline
*PipelineApi* | [**list_pipelines**](docs/PipelineApi.md#list_pipelines) | **GET** /pipelines | List pipelines
*PipelineApi* | [**pause_pipeline**](docs/PipelineApi.md#pause_pipeline) | **POST** /pipelines/{pipeline_name}/pause | Pause a pipeline
*PipelineApi* | [**trigger_pipeline**](docs/PipelineApi.md#trigger_pipeline) | **POST** /pipelines/{pipeline_name}/trigger | Delete a pipeline
*SparkApi* | [**spark_cancel_job**](docs/SparkApi.md#spark_cancel_job) | **POST** /spark/{job_id}/cancel | Cancel a Spark job
*SparkApi* | [**spark_check_job**](docs/SparkApi.md#spark_check_job) | **GET** /spark/{job_id} | Check a Spark job status
*SparkApi* | [**spark_get_job_output**](docs/SparkApi.md#spark_get_job_output) | **GET** /spark/{job_id}/output | Get Spark job output
*SparkApi* | [**spark_get_sql**](docs/SparkApi.md#spark_get_sql) | **GET** /sparksql/edit | Get user Spark SQL query cache
*SparkApi* | [**spark_list_jobs**](docs/SparkApi.md#spark_list_jobs) | **GET** /spark | List Spark jobs
*SparkApi* | [**spark_list_saved_jobs**](docs/SparkApi.md#spark_list_saved_jobs) | **GET** /spark/jobs/saved | List saved spark jobs
*SparkApi* | [**spark_save_job**](docs/SparkApi.md#spark_save_job) | **POST** /spark/{job_id}/save | Save a spark job for pipeline
*SparkApi* | [**spark_submit_job**](docs/SparkApi.md#spark_submit_job) | **POST** /spark | Submit a Spark job
*SparkApi* | [**spark_submit_sql**](docs/SparkApi.md#spark_submit_sql) | **POST** /sparksql | Submit a Spark SQL job
*SparkApi* | [**spark_update_sql**](docs/SparkApi.md#spark_update_sql) | **POST** /sparksql/edit | Update user Spark SQL query cache
*SqlApi* | [**check_sql_job**](docs/SqlApi.md#check_sql_job) | **GET** /sql/jobs/{job_id}/status | Check the status of a SQL job
*SqlApi* | [**execute_sql_query**](docs/SqlApi.md#execute_sql_query) | **POST** /sql | Execute a SQL query
*SqlApi* | [**get_sql_cache**](docs/SqlApi.md#get_sql_cache) | **GET** /sql/edit | Get user SQL query cache
*SqlApi* | [**get_sql_job_output**](docs/SqlApi.md#get_sql_job_output) | **GET** /sql/jobs/{job_id}/output | Get the output of a SQL job
*SqlApi* | [**get_sql_queries**](docs/SqlApi.md#get_sql_queries) | **GET** /sql/queries | Get user SQL queries
*SqlApi* | [**submit_sql_job**](docs/SqlApi.md#submit_sql_job) | **POST** /sql/jobs | Submit a SQL job
*SqlApi* | [**update_sql_cache**](docs/SqlApi.md#update_sql_cache) | **POST** /sql/edit | Update user SQL query cache
*SqlApi* | [**update_sql_query**](docs/SqlApi.md#update_sql_query) | **POST** /sql/queries | Update user SQL query cache
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create a user
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user | Get user info


## Documentation For Models

 - [ApiKey](docs/ApiKey.md)
 - [BadUserRequest](docs/BadUserRequest.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetCollection](docs/DatasetCollection.md)
 - [DatasetTable](docs/DatasetTable.md)
 - [DatasetTableColumn](docs/DatasetTableColumn.md)
 - [Error](docs/Error.md)
 - [ExplorerViewDataset](docs/ExplorerViewDataset.md)
 - [ExplorerViewDatasetCollection](docs/ExplorerViewDatasetCollection.md)
 - [File](docs/File.md)
 - [FileCollection](docs/FileCollection.md)
 - [FileCreateRequest](docs/FileCreateRequest.md)
 - [Job](docs/Job.md)
 - [JobCollection](docs/JobCollection.md)
 - [Pipeline](docs/Pipeline.md)
 - [PipelineBackfillRequest](docs/PipelineBackfillRequest.md)
 - [PipelineMetadata](docs/PipelineMetadata.md)
 - [PipelineMetadataCollection](docs/PipelineMetadataCollection.md)
 - [PipelineRun](docs/PipelineRun.md)
 - [PipelineRunCollection](docs/PipelineRunCollection.md)
 - [SavedJob](docs/SavedJob.md)
 - [SavedJobCollection](docs/SavedJobCollection.md)
 - [SparkJob](docs/SparkJob.md)
 - [SparkJobCollection](docs/SparkJobCollection.md)
 - [SparkJobOutput](docs/SparkJobOutput.md)
 - [SparkJobStatus](docs/SparkJobStatus.md)
 - [SparkJobSubmitRequest](docs/SparkJobSubmitRequest.md)
 - [SqlColumn](docs/SqlColumn.md)
 - [SqlExecuteResponse](docs/SqlExecuteResponse.md)
 - [SqlFieldSchema](docs/SqlFieldSchema.md)
 - [SqlJobStatistics](docs/SqlJobStatistics.md)
 - [SqlJobStatus](docs/SqlJobStatus.md)
 - [SqlQuery](docs/SqlQuery.md)
 - [SqlQueryCollection](docs/SqlQueryCollection.md)
 - [SqlSchema](docs/SqlSchema.md)
 - [SqlTable](docs/SqlTable.md)
 - [Stage](docs/Stage.md)
 - [StageInstance](docs/StageInstance.md)
 - [StageInstanceCollection](docs/StageInstanceCollection.md)
 - [User](docs/User.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication


## Author

dev@asynclabs.xyz


