from flask import Flask, render_template
from myDB import csv_connection

app = Flask(__name__)
df = csv_connection()


#@app.route('/')
#def df_table():
#    return render_template('index.html', tables=[df.to_html(classes='data', header="true")])

@app.route('/')
@app.route('/home')
def html_table():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/attendance')
def attendance_table():
    return render_template('dataframe.html',  tables=[df.to_html(classes='data', header="true")])


@app.route('/contact')
def contact_me():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
