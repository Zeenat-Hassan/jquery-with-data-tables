from flask import Flask, render_template
import mysql.connector
from flask import jsonify
import json
app = Flask(__name__, static_url_path='', static_folder='web/templates', template_folder='web/templates')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="data_analysis"
)

def retrieve_data():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM QA_1")
    rv = mycursor.fetchall()
    payload = []
    content = {}
    for result in rv:
       content ={'Processed_Data': result[0], 'Case_Category': result[1], 'Case_Issues': result[2], 'Data_Type': result[3], 'id': result[4], 'Original_text': result[5]}
       payload.append(content)
    return payload



@app.route('/' )
def get():
  return render_template("table1.html")


@app.route('/api/data', methods=["GET"])
def det_data():
    get_payload_returned_by_function=retrieve_data()
    return jsonify(get_payload_returned_by_function)





if __name__ == '__main__':
   app.run(debug = True)