schema = "sample_library"
host = "127.0.0.1"
user = "root"
password = "568923Ebru0079." # enter your password for local MySQL server INSIDE the quotes
port = 3306

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'