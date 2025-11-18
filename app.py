from flask import Flask, render_template, request, redirect, send_file, jsonify
import mysql.connector
import pandas as pd
import io


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="harish@*)(@))%",
        database="python_db"
    )


app = Flask(__name__)

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM employees_big")
    employees = cur.fetchall()
    conn.close()
    return render_template("index.html", employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age'] or None
        dept = request.form['dept']
        designation = request.form['designation']
        salary = request.form['salary'] or None
        experience = request.form['experience'] or None

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO employees_big (name, age, dept, designation, salary, experience)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, dept, designation, salary, experience))
        conn.commit()
        conn.close()
        return redirect('/')
    
    return render_template("add.html")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age'] or None
        dept = request.form['dept']
        designation = request.form['designation']
        salary = request.form['salary'] or None
        experience = request.form['experience'] or None

        cur.execute("""
            UPDATE employees_big
            SET name=%s, age=%s, dept=%s, designation=%s, salary=%s, experience=%s
            WHERE id=%s
        """, (name, age, dept, designation, salary, experience, id))

        conn.commit()
        conn.close()
        return redirect('/')

    cur.execute("SELECT * FROM employees_big WHERE id=%s", (id,))
    emp = cur.fetchone()
    conn.close()

    return render_template("edit.html", emp=emp)




@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees_big WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/chart-data')
def chart_data():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM employees_big", conn)
    conn.close()

    # Department counts
    dept_counts = df['dept'].value_counts().to_dict()

    # Department average salary
    dept_avg_salary = df.groupby('dept')['salary'].mean().round(2).to_dict()

    # Top 5 salaries
    top5 = df.sort_values('salary', ascending=False).head(5)[['name', 'salary']].to_dict(orient='records')

    # Experience distribution
    exp_bins = df['experience'].value_counts().sort_index().to_dict()

    return jsonify({
        'dept_counts': dept_counts,
        'dept_avg_salary': dept_avg_salary,
        'top5': top5,
        'exp_bins': exp_bins
    })


@app.route('/download/csv')
def download_csv():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM employees_big", conn)
    conn.close()

    buf = io.StringIO()
    df.to_csv(buf, index=False)
    buf.seek(0)

    return send_file(
        io.BytesIO(buf.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='employees_report.csv'
    )

@app.route('/download/excel')
def download_excel():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM employees_big", conn)
    conn.close()

    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Employees')

    buf.seek(0)

    return send_file(
        buf,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='employees_report.xlsx'
    )



@app.route('/charts')
def charts():
    return render_template("charts.html")



if __name__ == "__main__":
    app.run(debug=True)

