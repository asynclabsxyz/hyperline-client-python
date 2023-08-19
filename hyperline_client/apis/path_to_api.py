import typing_extensions

from hyperline_client.paths import PathValues
from hyperline_client.apis.paths.api_keys import ApiKeys
from hyperline_client.apis.paths.database_schema import DatabaseSchema
from hyperline_client.apis.paths.datasets import Datasets
from hyperline_client.apis.paths.datasets_metadata import DatasetsMetadata
from hyperline_client.apis.paths.datasets_preview import DatasetsPreview
from hyperline_client.apis.paths.datasets_explorer import DatasetsExplorer
from hyperline_client.apis.paths.datasets_explorer_details import DatasetsExplorerDetails
from hyperline_client.apis.paths.code import Code
from hyperline_client.apis.paths.files import Files
from hyperline_client.apis.paths.files_metadata import FilesMetadata
from hyperline_client.apis.paths.files_preview import FilesPreview
from hyperline_client.apis.paths.files_content import FilesContent
from hyperline_client.apis.paths.files_samples import FilesSamples
from hyperline_client.apis.paths.jobs import Jobs
from hyperline_client.apis.paths.pipeline_backfill import PipelineBackfill
from hyperline_client.apis.paths.pipeline_edit import PipelineEdit
from hyperline_client.apis.paths.pipelines import Pipelines
from hyperline_client.apis.paths.pipelines_pipeline_name import PipelinesPipelineName
from hyperline_client.apis.paths.pipelines_pipeline_name_delete import PipelinesPipelineNameDelete
from hyperline_client.apis.paths.pipelines_pipeline_name_deploy import PipelinesPipelineNameDeploy
from hyperline_client.apis.paths.pipelines_pipeline_name_pause import PipelinesPipelineNamePause
from hyperline_client.apis.paths.pipelines_pipeline_name_trigger import PipelinesPipelineNameTrigger
from hyperline_client.apis.paths.pipelines_pipeline_name_runs import PipelinesPipelineNameRuns
from hyperline_client.apis.paths.pipelines_pipeline_name_runs_run_id import PipelinesPipelineNameRunsRunId
from hyperline_client.apis.paths.pipelines_pipeline_name_runs_run_id_stages import PipelinesPipelineNameRunsRunIdStages
from hyperline_client.apis.paths.pipelines_pipeline_name_runs_run_id_stages_stage_name_logs_try_number import PipelinesPipelineNameRunsRunIdStagesStageNameLogsTryNumber
from hyperline_client.apis.paths.spark import Spark
from hyperline_client.apis.paths.spark_job_id import SparkJobId
from hyperline_client.apis.paths.spark_job_id_cancel import SparkJobIdCancel
from hyperline_client.apis.paths.spark_job_id_output import SparkJobIdOutput
from hyperline_client.apis.paths.spark_job_id_save import SparkJobIdSave
from hyperline_client.apis.paths.spark_jobs_saved import SparkJobsSaved
from hyperline_client.apis.paths.sparksql import Sparksql
from hyperline_client.apis.paths.sparksql_edit import SparksqlEdit
from hyperline_client.apis.paths.sql import Sql
from hyperline_client.apis.paths.sql_edit import SqlEdit
from hyperline_client.apis.paths.sql_jobs import SqlJobs
from hyperline_client.apis.paths.sql_jobs_job_id_status import SqlJobsJobIdStatus
from hyperline_client.apis.paths.sql_jobs_job_id_output import SqlJobsJobIdOutput
from hyperline_client.apis.paths.sql_queries import SqlQueries
from hyperline_client.apis.paths.user import User

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_KEYS: ApiKeys,
        PathValues.DATABASE_SCHEMA: DatabaseSchema,
        PathValues.DATASETS: Datasets,
        PathValues.DATASETS_METADATA: DatasetsMetadata,
        PathValues.DATASETS_PREVIEW: DatasetsPreview,
        PathValues.DATASETS_EXPLORER: DatasetsExplorer,
        PathValues.DATASETS_EXPLORER_DETAILS: DatasetsExplorerDetails,
        PathValues.CODE: Code,
        PathValues.FILES: Files,
        PathValues.FILES_METADATA: FilesMetadata,
        PathValues.FILES_PREVIEW: FilesPreview,
        PathValues.FILES_CONTENT: FilesContent,
        PathValues.FILES_SAMPLES: FilesSamples,
        PathValues.JOBS: Jobs,
        PathValues.PIPELINE_BACKFILL: PipelineBackfill,
        PathValues.PIPELINE_EDIT: PipelineEdit,
        PathValues.PIPELINES: Pipelines,
        PathValues.PIPELINES_PIPELINE_NAME: PipelinesPipelineName,
        PathValues.PIPELINES_PIPELINE_NAME_DELETE: PipelinesPipelineNameDelete,
        PathValues.PIPELINES_PIPELINE_NAME_DEPLOY: PipelinesPipelineNameDeploy,
        PathValues.PIPELINES_PIPELINE_NAME_PAUSE: PipelinesPipelineNamePause,
        PathValues.PIPELINES_PIPELINE_NAME_TRIGGER: PipelinesPipelineNameTrigger,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS: PipelinesPipelineNameRuns,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID: PipelinesPipelineNameRunsRunId,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID_STAGES: PipelinesPipelineNameRunsRunIdStages,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID_STAGES_STAGE_NAME_LOGS_TRY_NUMBER: PipelinesPipelineNameRunsRunIdStagesStageNameLogsTryNumber,
        PathValues.SPARK: Spark,
        PathValues.SPARK_JOB_ID: SparkJobId,
        PathValues.SPARK_JOB_ID_CANCEL: SparkJobIdCancel,
        PathValues.SPARK_JOB_ID_OUTPUT: SparkJobIdOutput,
        PathValues.SPARK_JOB_ID_SAVE: SparkJobIdSave,
        PathValues.SPARK_JOBS_SAVED: SparkJobsSaved,
        PathValues.SPARKSQL: Sparksql,
        PathValues.SPARKSQL_EDIT: SparksqlEdit,
        PathValues.SQL: Sql,
        PathValues.SQL_EDIT: SqlEdit,
        PathValues.SQL_JOBS: SqlJobs,
        PathValues.SQL_JOBS_JOB_ID_STATUS: SqlJobsJobIdStatus,
        PathValues.SQL_JOBS_JOB_ID_OUTPUT: SqlJobsJobIdOutput,
        PathValues.SQL_QUERIES: SqlQueries,
        PathValues.USER: User,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_KEYS: ApiKeys,
        PathValues.DATABASE_SCHEMA: DatabaseSchema,
        PathValues.DATASETS: Datasets,
        PathValues.DATASETS_METADATA: DatasetsMetadata,
        PathValues.DATASETS_PREVIEW: DatasetsPreview,
        PathValues.DATASETS_EXPLORER: DatasetsExplorer,
        PathValues.DATASETS_EXPLORER_DETAILS: DatasetsExplorerDetails,
        PathValues.CODE: Code,
        PathValues.FILES: Files,
        PathValues.FILES_METADATA: FilesMetadata,
        PathValues.FILES_PREVIEW: FilesPreview,
        PathValues.FILES_CONTENT: FilesContent,
        PathValues.FILES_SAMPLES: FilesSamples,
        PathValues.JOBS: Jobs,
        PathValues.PIPELINE_BACKFILL: PipelineBackfill,
        PathValues.PIPELINE_EDIT: PipelineEdit,
        PathValues.PIPELINES: Pipelines,
        PathValues.PIPELINES_PIPELINE_NAME: PipelinesPipelineName,
        PathValues.PIPELINES_PIPELINE_NAME_DELETE: PipelinesPipelineNameDelete,
        PathValues.PIPELINES_PIPELINE_NAME_DEPLOY: PipelinesPipelineNameDeploy,
        PathValues.PIPELINES_PIPELINE_NAME_PAUSE: PipelinesPipelineNamePause,
        PathValues.PIPELINES_PIPELINE_NAME_TRIGGER: PipelinesPipelineNameTrigger,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS: PipelinesPipelineNameRuns,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID: PipelinesPipelineNameRunsRunId,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID_STAGES: PipelinesPipelineNameRunsRunIdStages,
        PathValues.PIPELINES_PIPELINE_NAME_RUNS_RUN_ID_STAGES_STAGE_NAME_LOGS_TRY_NUMBER: PipelinesPipelineNameRunsRunIdStagesStageNameLogsTryNumber,
        PathValues.SPARK: Spark,
        PathValues.SPARK_JOB_ID: SparkJobId,
        PathValues.SPARK_JOB_ID_CANCEL: SparkJobIdCancel,
        PathValues.SPARK_JOB_ID_OUTPUT: SparkJobIdOutput,
        PathValues.SPARK_JOB_ID_SAVE: SparkJobIdSave,
        PathValues.SPARK_JOBS_SAVED: SparkJobsSaved,
        PathValues.SPARKSQL: Sparksql,
        PathValues.SPARKSQL_EDIT: SparksqlEdit,
        PathValues.SQL: Sql,
        PathValues.SQL_EDIT: SqlEdit,
        PathValues.SQL_JOBS: SqlJobs,
        PathValues.SQL_JOBS_JOB_ID_STATUS: SqlJobsJobIdStatus,
        PathValues.SQL_JOBS_JOB_ID_OUTPUT: SqlJobsJobIdOutput,
        PathValues.SQL_QUERIES: SqlQueries,
        PathValues.USER: User,
    }
)
