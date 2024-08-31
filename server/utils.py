import logging

logger = logging.getLogger(__name__)

class Utils:
    @staticmethod
    def setup_logging():
        """
        Configures logging for the application.
        """
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        return logger

    @staticmethod
    def handle_error(error):
        """
        Handles errors by logging them and returning a JSON response.
        """
        logger.error(f"An error occurred: {str(error)}")
        return {"error": str(error)}, 500
