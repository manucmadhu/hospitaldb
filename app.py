from flask import Flask, render_template, request, jsonify
from back import create, addD, delD, addP, delP, addA, delA, addM, delM, addPh, delPh, selD, selA, selP, selPh, selM

app = Flask(__name__)

create()

@app.route('/')
def index():
    return render_template('index.html')

# Routes for Doctors
@app.route('/doctors')
def doctors():
    doctors_data = selD(-1)
    return render_template('entity.html', entity_type='Doctor', data=doctors_data)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    if request.method == 'POST':
        try:
            doc_id = int(request.form['entityId'])
            doc_name = request.form['entityName']
            department = request.form['department']
            opdf = request.form['opdf']
            opdt = request.form['opdt']
            room_no = int(request.form['roomNo'])
            phone_no = request.form['phoneNo']

            addD(doc_id, doc_name, department, opdf, opdt, room_no, phone_no)

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_doctor/<int:doc_id>')
def delete_doctor(doc_id):
    delD(doc_id)
    return jsonify({'success': True})

# Routes for Patients
@app.route('/patients')
def patients():
    patients_data = selP(-1)
    return render_template('entity.html', entity_type='Patient', data=patients_data)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        try:
            patient_id = int(request.form['entityId'])
            patient_name = request.form['entityName']
            phone_no = request.form['phoneNo']
            io = request.form['io']

            addP(patient_id, patient_name, phone_no, io)

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_patient/<int:patient_id>')
def delete_patient(patient_id):
    delP(patient_id)
    return jsonify({'success': True})

# Routes for Appointments
@app.route('/appointments')
def appointments():
    appointments_data = selA(-1)
    return render_template('entity.html', entity_type='Appointment', data=appointments_data)

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    if request.method == 'POST':
        try:
            appointment_id = int(request.form['entityId'])
            patient_id = int(request.form['patientId'])
            doctor_id = int(request.form['doctorId'])
            token = int(request.form['token'])

            addA(appointment_id, patient_id, doctor_id, token)

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_appointment/<int:appointment_id>')
def delete_appointment(appointment_id):
    delA(appointment_id)
    return jsonify({'success': True})

# Routes for Medicines
@app.route('/medicines')
def medicines():
    medicines_data = selM(-1)
    return render_template('entity.html', entity_type='Medicine', data=medicines_data)

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    if request.method == 'POST':
        try:
            medicine_id = int(request.form['entityId'])
            medicine_name = request.form['entityName']

            addM(medicine_id, medicine_name)

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_medicine/<int:medicine_id>')
def delete_medicine(medicine_id):
    delM(medicine_id)
    return jsonify({'success': True})

# Routes for Pharmacies
@app.route('/pharmacies')
def pharmacies():
    pharmacies_data = selPh(-1)
    return render_template('entity.html', entity_type='Pharmacy', data=pharmacies_data)

@app.route('/add_pharmacy', methods=['POST'])
def add_pharmacy():
    if request.method == 'POST':
        try:
            pharmacy_id = int(request.form['entityId'])
            med1_id = int(request.form['med1Id'])
            med2_id = int(request.form['med2Id'])
            med3_id = int(request.form['med3Id'])
            med4_id = int(request.form['med4Id'])

            addPh(pharmacy_id, med1_id, med2_id, med3_id, med4_id)

            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_pharmacy/<int:pharmacy_id>')
def delete_pharmacy(pharmacy_id):
    delPh(pharmacy_id)
    return jsonify({'success': True})

@app.route('/select_doctor/<int:doc_id>')
def select_doctor(doc_id):
    doctor_data = selD(doc_id)
    return jsonify({'success': True, 'data': doctor_data})

@app.route('/select_patient/<int:patient_id>')
def select_patient(patient_id):
    patient_data = selP(patient_id)
    return jsonify({'success': True, 'data': patient_data})

@app.route('/select_appointment/<int:appointment_id>')
def select_appointment(appointment_id):
    appointment_data = selA(appointment_id)
    return jsonify({'success': True, 'data': appointment_data})

@app.route('/select_medicine/<int:medicine_id>')
def select_medicine(medicine_id):
    medicine_data = selM(medicine_id)
    return jsonify({'success': True, 'data': medicine_data})

@app.route('/select_pharmacy/<int:pharmacy_id>')
def select_pharmacy(pharmacy_id):
    pharmacy_data = selPh(pharmacy_id)
    return jsonify({'success': True, 'data': pharmacy_data})

if __name__ == '__main__':
    app.run(debug=True)
