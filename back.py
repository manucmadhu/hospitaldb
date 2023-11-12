import sqlite3

def create():
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS DOCTOR (ID INT PRIMARY KEY, NAME TEXT, DEPARTMENT TEXT, OPDF TIME, OPDT TIME, ROOM_NO INT, PHONE_NO VARCHAR(10));")
    cur.execute("CREATE TABLE IF NOT EXISTS PATIENT(ID INT PRIMARY KEY, NAME TEXT, PH_NO VARCHAR(10), IO VARCHAR(1));")
    cur.execute("CREATE TABLE IF NOT EXISTS APPOINTMENT (ID INT PRIMARY KEY, P_ID INT, D_ID INT, TOKEN INT, FOREIGN KEY (D_ID) REFERENCES DOCTOR(ID), FOREIGN KEY (P_ID) REFERENCES PATIENT(ID));")
    cur.execute("CREATE TABLE IF NOT EXISTS MEDICINE(M_ID INT PRIMARY KEY, NAME TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS PHARMACY (P_ID INT, MED1 INT, MED2 INT, MED3 INT, MED4 INT, FOREIGN KEY(P_ID) REFERENCES PATIENT(ID), FOREIGN KEY (MED1) REFERENCES MEDICINE(M_ID), FOREIGN KEY (MED2) REFERENCES MEDICINE(M_ID), FOREIGN KEY (MED3) REFERENCES MEDICINE(M_ID), FOREIGN KEY (MED4) REFERENCES MEDICINE(M_ID));")
    cur.close()
    conn.commit()
    conn.close()

def addD(a, b, c, d, e, f, g):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO DOCTOR(ID, NAME, DEPARTMENT, OPDF, OPDT, ROOM_NO, PHONE_NO) VALUES(?,?,?,?,?,?,?)", (a, b, c, d, e, f, g))
    cur.close()
    conn.commit()
    conn.close()

def delD(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM DOCTOR WHERE ID=?", (a,))
    cur.close()
    conn.commit()
    conn.close()

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

# Similar functions for other tables (APPOINTMENT, MEDICINE, PHARMACY) can be added following the same pattern.
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
#select for doctor
def selD(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a==-1:
        cur.execute("SELECT * FROM DOCTOR")
    else:
        cur.execute("SELECT * FROM DOCTOR WHERE ID=?",a)
    rows = cur.fetchall()
    return rows
#select for appointment
def selA(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a==-1:
        cur.execute("SELECT * FROM APPOINTMENT")
    else:
        cur.execute("SELECT * FROM APPOINTMENT WHERE ID=?",a)
    rows = cur.fetchall()
    return rows
#select for patient
def selP(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a==-1:
        cur.execute("SELECT * FROM PATIENT")
    else:
        cur.execute("SELECT * FROM PATIENT WHERE ID=?",a)
    rows = cur.fetchall()
    return rows
#select for pharmacy
def selPh(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a==-1:
        cur.execute("SELECT * FROM PHARMACY")
    else:
        cur.execute("SELECT * FROM PHARMACY WHERE ID=?",a)
    rows = cur.fetchall()
    return rows
#select for medicine
def selPh(a):
    create()
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    if a==-1:
        cur.execute("SELECT * FROM MEDICINE")
    else:
        cur.execute("SELECT * FROM MEDICINE WHERE ID=?",a)
    rows = cur.fetchall()
    return rows