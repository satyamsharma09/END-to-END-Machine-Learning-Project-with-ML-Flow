from MLProject import logger
from MLProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from MLProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage (STAGE_NAME) started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage (STAGE_NAME) completed <<<<<<")
except Exception as e:
    logger. exception (e)
    raise e



STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage (STAGE_NAME) started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage (STAGE_NAME) completed <<<<<<")
except Exception as e:
    logger. exception (e)
    raise e

logger.info("This is an info message")


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage (STAGE_NAME) started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage (STAGE_NAME) completed <<<<<<")
except Exception as e:
    logger. exception (e)
    raise e

logger.info("This is an info message")