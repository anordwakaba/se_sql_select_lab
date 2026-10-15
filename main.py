# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# Display all employee data
employee_data = pd.read_sql(
    """SELECT * FROM employees""", conn
)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)


# STEP 3
# Select last name first, then employee number
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)


# STEP 4
# Rename employeeNumber to ID using an alias
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)


# STEP 5
# Classify employees as Executive or Not Executive
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)


# STEP 7
# Return the first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)


# Display order details data
order_details = pd.read_sql("""
    SELECT * FROM orderDetails;
""", conn)

print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# STEP 8
# Calculate the sum of rounded priceEach * quantityOrdered
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn).sum()


# STEP 9
# Return order date and extract day, month, and year
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)


# Close the database connection
conn.close()