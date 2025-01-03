from MLProject import logger
from MLProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage (STAGE_NAME) started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage (STAGE_NAME) completed <<<<<<")
except Exception as e:
    logger. exception (e)
    raise e


logger.info("This is an info message")