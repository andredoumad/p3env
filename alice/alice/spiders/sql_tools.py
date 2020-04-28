import mysql.connector

mydb = mysql.connector.connect(

        # DATABASE = https://www.udemy.com/course/the-business-intelligence-analyst-course-2018/learn/lecture/10122560#overview 
        host="citadel.blackmesanetwork.com",
        user="demo_remote_user",
        passwd="abcdef1124",
        database="employees",
    )

if __name__ == "__main__":


    print(mydb)
    mycursor = mydb.cursor()
    # sql = "SHOW DATABASES"
    
    # sql = "SELECT * FROM employees ORDER BY first_name DESC;"
    
    # sql = "SELECT first_name, COUNT(first_name) AS names_count FROM employees GROUP BY first_name;"
    
    # sql = "SELECT salary FROM salaries WHERE salary > 80000 GROUP BY salary ORDER BY salary"
    
    # sql = "SELECT first_name, COUNT(first_name) AS names_count FROM employees GROUP BY first_name HAVING COUNT(first_name) > 250 ORDER BY first_name;"
    
    # sql = "SELECT emp_no, AVG(salary) FROM salaries GROUP BY emp_no HAVING AVG(salary) > 120000 ORDER BY emp_no;"

    # sql = 'SELECT first_name, COUNT(first_name) AS names_count FROM employees WHERE hire_date > "1999-01-01" GROUP BY first_name HAVING count(first_name) < 200 order by first_name asc;'

    # sql = "SELECT emp_no FROM dept_emp WHERE from_date > '2000-01-01' GROUP BY emp_no HAVING COUNT(from_date) > 1 ORDER BY emp_no;"
    
    # sql = "select * from salaries order by salary DESC limit 1000;"

    # sql = "SELECT COUNT(DISTINCT from_date) FROM salaries;"

    # sql = "SELECT COUNT(DISTINCT dept_no) FROM dept_emp;"

    # sql = "SELECT sum(salary) FROM salaries;"

    # sql = 'SELECT SUM(salary) FROM salaries WHERE from_date > "1997-01-01" LIMIT 1000;'
    
    # sql = "select max(salary) from salaries;"

    # sql = 'select ROUND(avg(salary),2) from salaries WHERE from_date > "2000-01-01" LIMIT 1000;'

    # sql = "SELECT m.dept_no, m.emp_no, d.dept_name FROM dept_manager_dup m INNER JOIN departments_dup d ON m.dept_no = d.dept_no ORDER BY m.dept_no;"

    # Extract a list containing information about all managers’ employee number, first and last name, department number, and hire date. 
    sql = "SELECT e.emp_no, e.first_name, e.last_name, dm.dept_no, e.hire_date FROM employees e JOIN dept_manager dm ON e.emp_no = dm.emp_no;"

    mycursor.execute(sql)
    for x in mycursor:
        print(x)