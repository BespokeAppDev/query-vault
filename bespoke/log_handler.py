import json
import uuid
from datetime import datetime

def generate_log(query, user_id, metadata=None):
    """
    Generates a structured log entry in JSON format.

    Args:
        query (str): The user query to be logged.
        user_id (str): The ID of the user making the query.
        metadata (dict, optional): Additional information to log.

    Returns:
        dict: The log entry formatted as a dictionary.
    """
    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "query": query,
        "metadata": metadata or {}
    }
    return log_entry

def log_to_json(log_entry):
    """
    Converts a log entry dictionary to a JSON string.

    Args:
        log_entry (dict): The log entry to convert.

    Returns:
        str: The JSON string representation of the log.
    """
    return json.dumps(log_entry, indent=2)
