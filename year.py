# Loading Libaries

# Ploting
import pandas as pd
import plotly.express as px
# Database Connector libaries
import mysql.connector
# For Web Development
from flask import Flask, render_template, request, redirect
# For Notification
from win10toast import ToastNotifier 
n = ToastNotifier() 
# .env
import os
from dotenv import load_dotenv
load_dotenv()
import psycopg2



# Configure MySQL connection
# --Here SQL Connection--
db = mysql.connector.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database')
)
# db = psycopg2.connect(os.getenv('DATABASE_URL'))
# Create a cursor
cursor = db.cursor()

def data_year():
    






    # Fetch the results for January
    sql_query = f'SELECT * FROM january ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for January
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_1 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_1 = food + travel + education + entertainment
    # Total Savings
    tot_savings_1 = tot_earning_1-tot_expense_1
    
    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_1,tot_expense_1,tot_savings_1,"January")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()

    # Done

    # February

    sql_query = f'SELECT * FROM february ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for February
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_2 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_2 = food + travel + education + entertainment
    # Total Savings
    tot_savings_2 = tot_earning_2-tot_expense_2

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_2,tot_expense_2,tot_savings_2,"February")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()

    # Done


    # March

    sql_query = f'SELECT * FROM march ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for march
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_3 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_3 = food + travel + education + entertainment
    # Total Savings
    tot_savings_3 = tot_earning_3-tot_expense_3

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_3,tot_expense_3,tot_savings_3,"March")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()

    # Done







    # April



    sql_query = f'SELECT * FROM april ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for may
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_4 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_4 = food + travel + education + entertainment
    # Total Savings
    tot_savings_4 = tot_earning_4-tot_expense_4

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_4,tot_expense_4,tot_savings_4,"April")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()

    # Done

    # May

    sql_query = f'SELECT * FROM may ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for may
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_5 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_5 = food + travel + education + entertainment
    # Total Savings
    tot_savings_5 = tot_earning_5-tot_expense_5

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_5,tot_expense_5,tot_savings_5,"May")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()

    # Done



    # June


    sql_query = f'SELECT * FROM june ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for june
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_6 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_6 = food + travel + education + entertainment
    # Total Savings
    tot_savings_6 = tot_earning_6-tot_expense_6




    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_6,tot_expense_6,tot_savings_6,"June")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done




    # July


    sql_query = f'SELECT * FROM july ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for july
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_7 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_7 = food + travel + education + entertainment
    # Total Savings
    tot_savings_7 = tot_earning_7-tot_expense_7

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_7,tot_expense_7,tot_savings_7,"July")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done



    # August

    sql_query = f'SELECT * FROM august ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for august
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_8 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_8 = food + travel + education + entertainment
    # Total Savings
    tot_savings_8 = tot_earning_8-tot_expense_8

    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_8,tot_expense_8,tot_savings_8,"August")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done

    # September

    sql_query = f'SELECT * FROM september ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for september
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_9 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_9 = food + travel + education + entertainment
    # Total Savings
    tot_savings_9 = tot_earning_9-tot_expense_9
    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_9,tot_expense_9,tot_savings_9,"September")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done

    # October

    sql_query = f'SELECT * FROM october ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for october
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_10 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_10 = food + travel + education + entertainment
    # Total Savings
    tot_savings_10 = tot_earning_10-tot_expense_10
    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_10,tot_expense_10,tot_savings_10,"October")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done



    # November

    sql_query = f'SELECT * FROM november ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for november
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_11 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_11 = food + travel + education + entertainment
    # Total Savings
    tot_savings_11 = tot_earning_11-tot_expense_11
    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_11,tot_expense_11,tot_savings_11,"November")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done


    # December
    sql_query = f'SELECT * FROM december ORDER BY Date ASC;'
    
    cursor.execute(sql_query, ())
    result = cursor.fetchall()
    # Data for december
    # Income
    income = 0
    for i in result:
        income += i[1]
    # Side Hustle
    side_hustle = 0
    for i in result:
        side_hustle += i[2]
    # Stocks
    stocks = 0
    for i in result:
        stocks += i[3]
    # Food
    food = 0
    for i in result:
        food += i[4]
        # Travel
    travel = 0
    for i in result:
        travel += i[5]
    # Education
    education = 0
    for i in result:
        education += i[6]
    # Entertainment
    entertainment = 0
    for i in result:
        entertainment += i[7]
    # Total Earnings
    tot_earning_12 = income + side_hustle+ stocks
    # Total Expenses
    tot_expense_12 = food + travel + education + entertainment
    # Total Savings
    tot_savings_12 = tot_earning_12-tot_expense_12
    # Update
    sql = f"UPDATE year SET   totincome = %s, totexpense = %s, totsavings = %s WHERE monthname = %s"
    values = ( tot_earning_12,tot_expense_12,tot_savings_12,"December")
    cursor.execute(sql, values)
    # Commit the changes to the database
    db.commit()
    # Done

    return tot_earning_1,tot_expense_1,tot_savings_1,    tot_earning_2,tot_expense_2,tot_savings_2,    tot_earning_3,tot_expense_3,tot_savings_3,     tot_earning_4,tot_expense_4,tot_savings_4,      tot_earning_5,tot_expense_5,tot_savings_5,       tot_earning_6,tot_expense_6,tot_savings_6,     tot_earning_7,tot_expense_7,tot_savings_7,           tot_earning_8,tot_expense_8,tot_savings_8,       tot_earning_9,tot_expense_9,tot_savings_9,         tot_earning_10,tot_expense_10,tot_savings_10,       tot_earning_11,tot_expense_11,tot_savings_11,           tot_earning_12,tot_expense_12,tot_savings_12