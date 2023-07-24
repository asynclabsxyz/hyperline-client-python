# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hyperline_client.paths.spark_job_id_save import Api

from hyperline_client.paths import PathValues

path = PathValues.SPARK_JOB_ID_SAVE