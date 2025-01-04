from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_evaluation import ModelEvaluation
from MLProject import logger


STAGE_NAME = "Data Evaluation Stage"
class ModelEvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>{STAGE_NAME}: Starting Model Evaluation Process<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME}: Model evaluation process completed<<<<<<")
    except Exception as e:
        logger.error(f"{STAGE_NAME}: Exception occurred in model training stage: {str(e)}")