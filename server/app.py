from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import logging
import os

# Initialize Flask app and SocketIO
app = Flask(__name__, template_folder='./gui')
CORS(app)
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Error handler
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Example route to demonstrate logging
@app.route('/ping', methods=['GET'])
def ping():
    logger.info("Ping request received")
    return jsonify({"message": "pong"}), 200

# WebSocket event handler
@socketio.on('connect')
def handle_connect():
    logger.info("Client connected")
    emit('response', {'message': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    logger.info("Client disconnected")

@socketio.on('log_event')
def handle_log_event(json_data):
    logger.info(f"Received log event: {json_data}")
    emit('log_response', {'status': 'Log received'})

if __name__ == "__main__":
    try:
        logger.info("Starting server...")
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        logger.error(f"Error running server: {str(e)}")
        raise
