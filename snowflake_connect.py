import snowflake.connector

# Define your Snowflake connection parameters
# account = 'jq03311.east-us.aws'
# user = 'phanindra2705'
# password = 'Lakshmi@9581'
# warehouse = 'COMPUTE_WH'
# database = 'MY_DATABASE'
# schema = 'MY_SCHEMA'

# Establish the connection
ctx = snowflake.connector.connect(
    user='phanindra2705',
    password='Lakshmi@9581',
    account='kampiws-jq03311',
    warehouse='COMPUTE_WH',
    database='MY_DATABASE',
    schema='MY_SCHEMA'
)

# Create a cursor object
cur = ctx.cursor()

# Execute a simple query
try:
    cur.execute("SELECT CURRENT_VERSION()")
    for row in cur:
        print(row)
finally:
    # Close the cursor and connection
    cur.close()
    ctx.close()
