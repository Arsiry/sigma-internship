# TASK 5
## Database Postgres 

Design the DB for a task in AdTech domain. Make queries for data ingestion, extraction, aggregation.

I used BD in AdTech domain from Task 1:
* `train.csv`, the impression logs     
* `viewlog.csv`, view log of users    
* `item_data.csv`, products descriptions

## Content
* `AdTech_DatabaseModel_SimpleSchema.pdf`, Lucidchart, Visual data model diagram, Simple Schema 
* `AdTech_DatabaseModel_DatabaseSchema.pdf`, Lucidchart, Visual data model diagram
* `PostgreSQL_Database`, Postgres (Valentina Studio) screenshots
* `ad_tech_sql_create_table_1.sql` - Create table query - Creating table Impressions (train.csv)
* `ad_tech_sql_create_table_2.sql` - Create table query - Creating table ViewLog (viewlog.csv)
* `ad_tech_sql_create_table_3.sql` - Create table query - Creating table ItemData (item_data.csv)
* `ad_tech_sql_collecting_data_1.sql` - Select query - This query fetches impressions for users and compares them to their previous impressions. It calculates how many days have passed between the impressions, but only includes pairs of impressions where the time difference is 7 days or less. This query was saved as view df_impressions_before.
* `ad_tech_sql_collecting_data_2.sql` - Select query - This query counts how many previous impressions exist for each current impression by grouping the results by impressions_id. This query was saved as view df_impressions_before_count.
* `ad_tech_sql_collecting_data_3.sql` - Select query - This query retrieves detailed information about current impressions and includes a count of previous impressions for each current impression.
* `connect_to_db_psycopg2.ipynb` - python notebook - This Python script connects to a PostgreSQL database using psycopg2, executes multiple SQL queries.
* `connect_to_db_sqlalchemy.ipynb` - python notebook - This Python script connects to a PostgreSQL database using ORM SQLAlchemy, executes multiple SQL queries.