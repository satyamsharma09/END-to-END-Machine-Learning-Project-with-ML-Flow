from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_validation import DataValiadtion
from MLProject import logger


STAGE_NAME = "Data Validation stage"
class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        # try:
        #     logger.info(f"{STAGE_NAME} started")
        #     config_manager = ConfigurationManager()
        #     config = config_manager.get_data_validation_config()
        #     data_validation = DataValiadtion(config)
        #     data_validation.validate_all_columns()
        #     logger.info(f"{STAGE_NAME} completed")
        # except Exception as e:
        #     logger.error(f"{STAGE_NAME} failed")
        #     raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME}: Starting data validation process<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME}: Data validation process completed<<<<<<")
    except Exception as e:
        logger.error(f"{STAGE_NAME}: Exception occurred in data validation stage: {str(e)}")
        raise e

        
