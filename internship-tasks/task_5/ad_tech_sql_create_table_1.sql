CREATE TABLE Impressions (
    impressions_id varchar(255) NOT NULL,
    impressions_time TIMESTAMP NOT NULL,
    uder_id INT  NOT NULL,
    app_code INT NOT NULL,
    os_version varchar(255)  NOT NULL,
    is_4G INT,
    is_click INT,
    PRIMARY KEY (impressions_id)
);