Create Table ViewLog(
    server_time TIMESTAMP NOT NULL,
    server_type varchar(255) NOT NULL,
    session_id INT  NOT NULL,
    user_id INT NOT NULL,
    item_id INT NOT NULL 
);