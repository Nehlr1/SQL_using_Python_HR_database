import mysql.connector
import pandas as pd

# Setting for DataBase connection
config = {
    "user": "root",
    "password": "PASSROOT12@",
    "host": "localhost",
    "database": "hr"
}

# Establishing a connection to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Retrieving data from the jobs table
def retrive_data():
    retrive_data_query = "SELECT * FROM jobs"
    cursor.execute(retrive_data_query)
    data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    return data

# Adding data from the jobs table
def add_data(data):
    add_data_query = "INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES (%s, %s, %s, %s)"
    cursor.executemany(add_data_query, data)
    conn.commit()

# Updating data from the jobs table
def update_data(job_id, new_min_salary, new_max_salary):
    update_data_query = "UPDATE jobs SET min_salary = %s, max_salary=%s WHERE job_id = %s"
    cursor.execute(update_data_query, (new_min_salary, new_max_salary, job_id))
    conn.commit()

# Deleting a specific job from the jobs table
def delete_data(job_id):
    delete_data_query = "DELETE FROM jobs WHERE job_id = %s"
    cursor.execute(delete_data_query, (job_id,))
    conn.commit()


# Retrieving and printing data from the jobs table
print("**** Current Data in the jobs table ****")
print(retrive_data())

# Adding data to the jobs's table
new_job = [
    ('20', 'Data Science Manager', 150000, 190000),
    ('21', 'Data Scientist', 80000, 100000),
    ('22', 'Data Analyst', 65000, 80000)
]
add_data(new_job)
print("\n**** Adding Data in the jobs table ****")
print(retrive_data())

# Updating min_salary and max_salary for a job
updated_job_id = 21
update_data(job_id=updated_job_id, new_min_salary=85000, new_max_salary=110000)
print(f"\n**** Data after updating minimum and maximum salary of job_id {updated_job_id} ****")
print(retrive_data())

# Deleting job using job_id
delete_job_id = ["20", "21", "22"]
for job_id in delete_job_id:
    delete_data(job_id=job_id)

print(f"\n**** Deleting Data in the jobs table for job id: {', '.join(delete_job_id)} ****")
print(retrive_data())

# Close the cursor and connection
cursor.close()
conn.close()