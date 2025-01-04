from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_trainer import ModelTrainer
from MLProject import logger
from pathlib import Path


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME}: Starting Modeal Training Process<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME}: Model training process completed<<<<<<")
    except Exception as e:
        logger.error(f"{STAGE_NAME}: Exception occurred in model training stage: {str(e)}")