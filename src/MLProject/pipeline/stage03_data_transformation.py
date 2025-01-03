from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_transformation import DataTransformation
from MLProject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME}: Starting data transformation process<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME}: Data transformation process completed<<<<<<")
    except Exception as e:
        logger.error(f"{STAGE_NAME}: Exception occurred in data transformation stage: {str(e)}")
        raise e