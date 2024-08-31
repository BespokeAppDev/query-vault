from flask import request, jsonify
from log_handler import LogHandler
from db_utils import DBUtils
import logging

logger = logging.getLogger(__name__)

def init_routes(app):
    log_handler = LogHandler()
    db_utils = DBUtils()

    @app.route('/log', methods=['POST'])
    def log_query():
        try:
            data = request.json
            log_entry = log_handler.generate_log(
                query=data['query'],
                user_id=data['user_id'],
                metadata=data.get('metadata', {})
            )
            db_utils.save_log(log_entry)
            logger.info(f"Log saved: {log_entry['id']}")
            return jsonify({"message": "Log saved successfully"}), 201
        except Exception as e:
            logger.error(f"Error in /log: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/logs', methods=['GET'])
    def get_logs():
        try:
            user_id = request.args.get('user_id')
            logs = db_utils.retrieve_logs(user_id)
            logger.info(f"Retrieved logs for user: {user_id}")
            return jsonify(logs), 200
        except Exception as e:
            logger.error(f"Error in /logs: {str(e)}")
            return jsonify({"error": str(e)}), 500
