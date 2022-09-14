CREATE TABLE IF NOT EXISTS test_schema.test_table (
    id INTEGER PRIMARY KEY NOT NULL,
    user_name VARCHAR(250) NOT NULL,
    user_income NUMERIC(10,2) NOT NULL,
    user_description TEXT DEFAULT(NULL),
    created_date date default('2020-01-01'),
    time_stamp timestamp,
    PRIMARY KEY (id)
)