# SQL using Python HR database

This repository contains code examples for interacting with an HR database using Python and SQL.

## Getting Started

Clone this repository and install the requirements:

```
git clone https://github.com/Nehlr1/SQL_using_Python_HR_database.git
cd SQL_using_Python_HR_database
py -m pip install --user virtualenv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Database

The HR database contains employee data such as employee id, name, salary, department etc. The database file hr.sql is included which contains the table structures and sample data.

## Organization of database
This database is organized for HR management with tables for countries, departments, dependents, employees, jobs, locations, and regions. Key relationships and foreign key constraints maintain data integrity. The database is normalized, uses InnoDB storage engine, and employs auto-incrementing primary keys. Character sets are set to `utf8mb4` with case-insensitive collation. Timestamps and time zones are considered for date information. The structure reflects best practices for data organization and relational integrity.

## Jupyter Notebook

The Jupyter Notebook hr_sql.ipynb contains examples of querying the database using Python with SQLAlchemy and performing CRUD operations.

## Python Script 

The Python script hr_sql.py shows how to connect to the database and execute queries programmatically without a notebook.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.