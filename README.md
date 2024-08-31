query-vault
logging system to capture, store, and manage user query logs from GUI 


QueryLogWarehouse

Overview

QueryLogWarehouse is a robust logging system designed to capture, store, and manage user query logs from a GUI interface. It leverages PostgreSQL on AWS for warehousing logs as JSON objects, enabling efficient data storage and retrieval. This system is built to support model evaluation, analytics, and other use cases by securely storing and accessing query data.

Features

- Log Generation**: Automatically generates structured logs for user queries.
- JSON Storage**: Logs are stored as JSON objects in a PostgreSQL database.
- Real-time Logging**: Supports real-time logging and retrieval via WebSocket.
- Scalable Design**: Designed to scale and manage large volumes of data.

Setup Instructions

Prerequisites

- Python 3.8+
- PostgreSQL database instance on AWS
- Virtual environment (optional but recommended)

Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/QueryLogWarehouse.git
    cd QueryLogWarehouse
    ```

2. Set Up Virtual Environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set Up Environment Variables:
    - Create a `.env` file in the root directory with your database credentials.
    ```plaintext
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=5432
    ```

5. Run Database Migration:
    - Execute the SQL script in `migrations/create_log_table.sql` to create the necessary table.
    ```bash
    psql -h your_db_host -U your_db_user -d your_db_name -f migrations/create_log_table.sql
    ```

6. Start the Server:
    ```bash
    python server/app.py
    ```

Front-End Usage

GUI folder left empty for more practiced hands

Usage

Logging Queries

- Use the `/log` endpoint to log user queries:
    ```bash
    curl -X POST http://localhost:5000/log -H "Content-Type: application/json" -d '{"query": "example query", "user_id": "user123"}'
    ```

Retrieving Logs

- Use the `/logs` endpoint to retrieve logs:
    ```bash
    curl http://localhost:5000/logs?user_id=user123
    ```



