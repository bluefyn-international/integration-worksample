import os

# interval to wait before re-checking the database for new data
JOB_INTERVAL = int(os.environ.get('JOB_INTERVAL', 5))  # seconds

# at most this amount of executions will run in parallel
MAX_JOB_INSTANCES = int(os.environ.get('MAX_JOB_INSTANCES', 1))

# airbase
AIRBASE_ENDPOINT = os.environ.get(
    'AIRBASE_ENDPOINT', 'api.airtable.com/v0'
)
AIRBASE_DB_ID = os.environ.get('AIRBASE_DB_ID', 'appLLsPEE1KOBefF9')
AIRBASE_TABLE_NAME = os.environ.get('AIRBASE_TABLE_NAME', 'Shipment Tracking')
AIRBASE_KEY = os.environ.get('AIRBASE_KEY', 'keyCB2waCQOZr75sX')

# shipit
SHIP_IT_ENDPOINT = os.environ.get(
    'SHIP_IT_CARRIERS_ENDPOINT', 'http://shipit-api.herokuapp.com/api/carriers'
)
