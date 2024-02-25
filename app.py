# Loading Libaries
# All Datas of Yearly
import year

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

# Flask
app = Flask(__name__)

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

# Welcome
@app.route('/')
def index():
    return render_template('index.html')

# All The Mini Project Web Page
# Month Name
month_name=""
# Month Page
@app.route('/month')
def month():
    n.show_toast("Ease Expense", "Month Page", duration = 2,icon_path ="/static/logo.ico") 
    return render_template('month.html')

# DashBoard for Monthly
@app.route('/dashboard', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        global month_name
        month_name = request.form['Month']
        
        if month_name is None:
            return redirect('/month')
        else:
            
            sql_query = f'SELECT * FROM {month_name} ORDER BY Date ASC;'
            print(sql_query)
            cursor.execute(sql_query, ())
            # Fetch the results
            result = cursor.fetchall()
            print(len(result))
            if(len(result) == 0 ):

                n.show_toast("Ease Expense", "Add Data/Record of " +month_name+" as it's Empty", duration = 2,icon_path ="/static/logo.ico")
                return redirect("/add-expense")
            else:    
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
                tot_earning = income + side_hustle+ stocks
                # Total Expenses
                tot_expense = food + travel + education + entertainment
                # Total Savings
                tot_savings = tot_earning-tot_expense

                n.show_toast("Ease Expense", "Dashboard Page for "+month_name, duration = 2,icon_path ="/static/logo.ico") 
                # Total Income Pie Chart
                labels = ['Income', 'Side Hustle', 'Stocks']
                values = [income,  side_hustle,stocks]
                fig = px.pie(names=labels, values=values, title='Total Earning Pie Chart')
                chart_html = fig.to_html(full_html=False)

                # Total Expense Pie Chart
                labelss = ['Food', 'Travel', 'Education',"Entertainment"]
                valuess = [food, travel, education,entertainment]
                fig2 = px.pie(names=labelss, values=valuess, title='Total Expense Pie Chart ')
                chart_html2 = fig2.to_html(full_html=False)

                # Date vs Expenses Multi Line Graph
                query = f"SELECT Date,Food,Travel,Education,Entertainment FROM {month_name} ORDER BY Date ASC;"
                df = pd.read_sql(query, db)
                fig = px.line(df, x='Date', y=['Food', "Travel","Education",'Entertainment'], title='Date vs Expenses Multi Line Graph')
                line_html1 = fig.to_html(full_html=False)

                return render_template('dashboard.html',datas=result,earnings=tot_earning,expenses=tot_expense,savings=tot_savings,month=month_name,chart_html=chart_html , line_html1=line_html1, chart_html2=chart_html2)


# DashBoard for Yearly
@app.route('/yearly', methods=['POST'])
def yearly():    
    tot_earning_1,tot_expense_1,tot_savings_1,    tot_earning_2,tot_expense_2,tot_savings_2,    tot_earning_3,tot_expense_3,tot_savings_3,     tot_earning_4,tot_expense_4,tot_savings_4,      tot_earning_5,tot_expense_5,tot_savings_5,       tot_earning_6,tot_expense_6,tot_savings_6,     tot_earning_7,tot_expense_7,tot_savings_7,           tot_earning_8,tot_expense_8,tot_savings_8,       tot_earning_9,tot_expense_9,tot_savings_9,         tot_earning_10,tot_expense_10,tot_savings_10,       tot_earning_11,tot_expense_11,tot_savings_11,           tot_earning_12,tot_expense_12,tot_savings_12=year.data_year()
    return render_template('yearly.html',tot_earning_1=tot_earning_1,tot_expense_1=tot_expense_1,tot_savings_1=tot_savings_1 ,tot_earning_2=tot_earning_2,tot_expense_2=tot_expense_2,tot_savings_2=tot_savings_2,tot_earning_3=tot_earning_3,tot_expense_3=tot_expense_3,tot_savings_3=tot_savings_3 ,tot_earning_4=tot_earning_4,tot_expense_4=tot_expense_4,tot_savings_4=tot_savings_4,tot_earning_5=tot_earning_5,tot_expense_5=tot_expense_5,tot_savings_5=tot_savings_5,tot_earning_6=tot_earning_6,tot_expense_6=tot_expense_6,tot_savings_6=tot_savings_6,tot_earning_7=tot_earning_7,tot_expense_7=tot_expense_7,tot_savings_7=tot_savings_7,tot_earning_8=tot_earning_8,tot_expense_8=tot_expense_8,tot_savings_8=tot_savings_8,tot_earning_9=tot_earning_9,tot_expense_9=tot_expense_9,tot_savings_9=tot_savings_9,tot_earning_10=tot_earning_10,tot_expense_10=tot_expense_10,tot_savings_10=tot_savings_10,tot_earning_11=tot_earning_11,tot_expense_11=tot_expense_11,tot_savings_11=tot_savings_11,tot_earning_12=tot_earning_12,tot_expense_12=tot_expense_12,tot_savings_12=tot_savings_12)

# Contribution Page
@app.route('/contribution')
def conclusion():
    n.show_toast("Ease Expense", "Contribution Page", duration = 2,icon_path ="/static/logo.ico") 
    return render_template('contribution.html')

# Home Page
@app.route('/home')
def home():
    n.show_toast("Ease Expense", "Home Page", duration = 2,icon_path ="/static/logo.ico") 
    return render_template('home.html')

# Add Expense Page
@app.route('/add-expense')
def addexpense():
    if(month_name==""):
        n.show_toast("Ease Expense", "Choose a Month ", duration = 2,icon_path ="/static/logo.ico")
        return redirect("/month")
    elif(month_name is None):
        n.show_toast("Ease Expense", "Choose a Month ", duration = 2,icon_path ="/static/logo.ico")
        return redirect("/month")
    else:
        n.show_toast("Ease Expense", "Add Expense Page for " +month_name, duration = 2,icon_path ="/static/logo.ico") 
        return render_template('add-expense.html' , month_name = month_name)

# Add & Update Expense
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        # Request Post
        count = 0
        option = request.form['option']
        date = request.form['date']
        income = request.form['income']
        sidehustle = request.form['sidehustle']
        stocks = request.form['stocks']
        food = request.form['food']
        travel = request.form['travel']
        education = request.form['education']
        entertainment = request.form['entertainment']
        # Update or Add
        sql_query = f'SELECT * FROM {month_name} ORDER BY Date ASC;'
        print(sql_query)
        cursor.execute(sql_query, ())
        # Fetch the results
        format_string = '%Y-%m-%d'
        result = cursor.fetchall()
        print(result)
        for i in result:
            if(date== i[0].strftime(format_string)):
                count = count+1
            
        if(count==1):
            # AS Count =1 means a record is present
            sql = f"UPDATE {month_name} SET Income = %s, SideHustle = %s , Stocks = %s, Food = %s, Travel = %s, Education = %s,Entertainment = %s WHERE Date = %s"
            values = (income,sidehustle,stocks,food,travel,education,entertainment,date)
            cursor.execute(sql, values)
            # Commit the changes to the database
            db.commit()
            n.show_toast("Ease Expense", "Updated Record of " +date, duration = 2,icon_path ="/static/logo.ico")
            return redirect("/month")

        elif(count==0):
            # Insert as no record is present
            sql = f"INSERT INTO {month_name} (Date,Income,SideHustle,Stocks,Food,Travel,Education,Entertainment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (date,income,sidehustle,stocks,food,travel,education,entertainment)
            cursor.execute(sql, values)
            # Commit the changes to the database
            db.commit()
            n.show_toast("Ease Expense", "Inserted Record of " +date, duration = 2,icon_path ="/static/logo.ico") 
            return redirect("/month")
    
# Dalete Expense Page
@app.route('/delete-expense')
def deleteexpense():
    print(month_name)
    if(month_name==""):
        n.show_toast("Ease Expense", "Choose a Month ", duration = 2,icon_path ="/static/logo.ico")
        return redirect("/month")
    elif(month_name == None):
        n.show_toast("Ease Expense", "Choose a Month ", duration = 2,icon_path ="/static/logo.ico")
        return redirect("/month")
    else:
        print("IN ELSE "+month_name)
        n.show_toast("Ease Expense", "Delete Expense Page for " +month_name, duration = 2,icon_path ="/static/logo.ico") 
        return render_template('delete-expense.html' , month = month_name,month_name = month_name)

# Delete Record
@app.route('/delete', methods=['POST'])
def delete():
    # Add a new user
    if request.method == 'POST':
        # Request Post
        count=0
        option = request.form['option']
        date = request.form['date']
        values=(date,)
        print(option)
        # Delete One or Delete All
        # Delete One
        if option=="one":
            # Execute the SQL DELETE query
            sql_query = f'SELECT * FROM {month_name} ORDER BY Date ASC;'
            print(sql_query)
            cursor.execute(sql_query, ())
            # Fetch the results
            result = cursor.fetchall()
            format_string = '%Y-%m-%d'
            
            for i in result:
                if(date== i[0].strftime(format_string)):
                    count = count+1
                
            if(count==1):
                # Delete with Date as the record is present
                sql = f"DELETE FROM {month_name} WHERE Date = %s"
                cursor.execute(sql,values)
                db.commit()
                n.show_toast("Ease Expense", "Record with " +date+" Deleted", duration = 2,icon_path ="/static/logo.ico")
                return redirect("/month")
            elif(count==0):
                n.show_toast("Ease Expense", "Invalid Date " +date, duration = 2,icon_path ="/static/logo.ico") 
                return redirect("/month")
        # Delete All
        elif option=="all":
            sql = f"TRUNCATE TABLE {month_name} "
            cursor.execute(sql)
            db.commit()
            n.show_toast("Ease Expense", "All Records Deleted ", duration = 2,icon_path ="/static/logo.ico") 
            return redirect("/month")
        else:
            n.show_toast("Ease Expense", "Invalid Option " , duration = 2,icon_path ="/static/logo.ico")
            return redirect("/month")



@app.route('/yearlyy', methods=['POST'])
def yearlyy():

      
    query = "SELECT Date, SUM(Food) AS Food, SUM(Travel) AS Travel, SUM(Education) AS Education, SUM(Entertainment) AS Entertainment FROM your_table_name GROUP BY MONTH(Date) ORDER BY Date ASC;"

    query = f"SELECT Date, Food, Travel, Education, Entertainment FROM {month_name} ORDER BY Date ASC;"

    
    return render_template("yearlyy.html")

# Main Function
if __name__ == '__main__':
    app.run(debug=True)