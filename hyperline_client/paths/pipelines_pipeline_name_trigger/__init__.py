# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from hyperline_client.paths.pipelines_pipeline_name_trigger import Api

from hyperline_client.paths import PathValues

path = PathValues.PIPELINES_PIPELINE_NAME_TRIGGER