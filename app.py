from flask import Flask, render_template, request, redirect, url_for, jsonify
from back import create, addD, delD, addP, delP, addA, delA, addM, delM, addPh, delPh, selD, selA, selP, selPh, selM
# import Flask
# import back
app = Flask(__name__)

create()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doctors')
def doctors():
    doctors_data = selD(-1)
    return render_template('entity.html', entity_type='Doctor', data=doctors_data)

@app.route('/patients')
def patients():
    patients_data = selP(-1)
    return render_template('entity.html', entity_type='Patient', data=patients_data)

@app.route('/pharmacies')
def pharmacies():
    pharmacies_data = selPh(-1)
    return render_template('entity.html', entity_type='Pharmacy', data=pharmacies_data)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    if request.method == 'POST':
        doc_id = int(request.form['entityId'])
        doc_name = request.form['entityName']
        # Get other form inputs and call the corresponding database function
        addD(doc_id, doc_name, ...)
        return jsonify({'success': True})

# Similar routes for other entities (add_patient, add_appointment, add_medicine, add_pharmacy)

@app.route('/delete_doctor/<int:doc_id>')
def delete_doctor(doc_id):
    delD(doc_id)
    return jsonify({'success': True})
# Similar functions for other tables (addP, delP, addA, delA, addM, delM, addPh, delPh, selD, selA, selP, selPh, selM)

# Add and delete functions for PATIENT table
def addP(a, b, c, d):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO PATIENT(ID, NAME, PH_NO, IO) VALUES(?,?,?,?)", (a, b, c, d))
    cur.close()
    conn.commit()
    conn.close()

def delP(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM PATIENT WHERE ID=?", (a,))
    cur.close()
    conn.commit()
    conn.close()

# Add and delete functions for APPOINTMENT table
def addA(a, b, c, d):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO APPOINTMENT(ID, P_ID, D_ID, TOKEN) VALUES(?,?,?,?)", (a, b, c, d))
    cur.close()
    conn.commit()
    conn.close()

def delA(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM APPOINTMENT WHERE ID=?", (a,))
    cur.close()
    conn.commit()
    conn.close()

# Add and delete functions for MEDICINE table
def addM(a, b):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO MEDICINE(M_ID, NAME) VALUES(?,?)", (a, b))
    cur.close()
    conn.commit()
    conn.close()

def delM(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM MEDICINE WHERE M_ID=?", (a,))
    cur.close()
    conn.commit()
    conn.close()

# Add and delete functions for PHARMACY table
def addPh(a, b, c, d, e):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO PHARMACY(P_ID, MED1, MED2, MED3, MED4) VALUES(?,?,?,?,?)", (a, b, c, d, e))
    cur.close()
    conn.commit()
    conn.close()

def delPh(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM PHARMACY WHERE P_ID=?", (a,))
    cur.close()
    conn.commit()
    conn.close()

# Select functions for each table
def selD(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a == -1:
        cur.execute("SELECT * FROM DOCTOR")
    else:
        cur.execute("SELECT * FROM DOCTOR WHERE ID=?", (a,))
    rows = cur.fetchall()
    return rows

def selP(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a == -1:
        cur.execute("SELECT * FROM PATIENT")
    else:
        cur.execute("SELECT * FROM PATIENT WHERE ID=?", (a,))
    rows = cur.fetchall()
    return rows

def selA(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a == -1:
        cur.execute("SELECT * FROM APPOINTMENT")
    else:
        cur.execute("SELECT * FROM APPOINTMENT WHERE ID=?", (a,))
    rows = cur.fetchall()
    return rows

def selM(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a == -1:
        cur.execute("SELECT * FROM MEDICINE")
    else:
        cur.execute("SELECT * FROM MEDICINE WHERE M_ID=?", (a,))
    rows = cur.fetchall()
    return rows

def selPh(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a == -1:
        cur.execute("SELECT * FROM PHARMACY")
    else:
        cur.execute("SELECT * FROM PHARMACY WHERE P_ID=?", (a,))
    rows = cur.fetchall()
    return rows

# Similar routes for other entities (delete_patient, delete_appointment, delete_medicine, delete_pharmacy)

if __name__ == '__main__':
    app.run(debug=True)
