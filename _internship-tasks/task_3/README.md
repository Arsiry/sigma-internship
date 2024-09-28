# TASK 3
## Collect data and Provide EDA

Created a database to ingest millions of simulated Ad Campaign events from a Kafka workspace.

Data are collected more then 3 days

Use a dashboard tool Metabase to connect to the database to visualize and analyze the event data.

Created python notebooks which is connect to database using mysql.connector and ORM SQLAlchemy. 

EDA is conducted

## Content
* `AdTech_Database.pdf`, screenshots of database 
* `AdTech_Dashboard.pdf`, metabase dashboard
* `connect_to_db_mysql_connector.ipynb`,`connect_to_db_mysql_connector_v2.ipynb` - python notebook - This Python script connects to a SingleStore(MySQL) database using mysql.connector, download data about campaigns and events to local files *.csv. - `campaigns_data.csv`, `events_data.csv`.
* `connect_to_db_sqlalchemy.ipynb` - python notebook - This Python script connects to a SingleStore(MySQL) using ORM SQLAlchemy
* `eda.ipynb` - python notebook - EDS is conducted

