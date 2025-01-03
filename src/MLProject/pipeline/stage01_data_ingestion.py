from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_ingestion import DataIngestion
from MLProject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main (self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    #     self.config_manager = ConfigurationManager()
    #     self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
    #     self.data_ingestion = DataIngestion(self.data_ingestion_config)

    # def execute(self):
    #     logger.info(f"{STAGE_NAME}: Starting data ingestion process")
    #     self.data_ingestion.download_file()
    #     self.data_ingestion.extract_zip_file()
    #     logger.info(f"{STAGE_NAME}: Data ingestion process completed")
    #     return self.data_ingestion_config.unzip_dir


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME}: Starting data ingestion process<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME}: Data ingestion process completed<<<<<<")
    except Exception as e:
        logger.error(f"{STAGE_NAME}: Exception occurred in data ingestion stage: {str(e)}")
        raise e