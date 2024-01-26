from flask import Flask,request,jsonify
from flask_cors import CORS
import os
import joblib

#api so that neural style transfer can occur
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/',methods=["POST"])
def model():
    diseases=['Drug Reaction', 'Hypothyroidism', 'Acne', 'Common Cold', 'Pneumonia', 'Peptic ulcer diseae', 'hepatitis A', 'Arthritis', 'Paralysis (brain hemorrhage)', 'Migraine', 'Gastroenteritis', 'Hypoglycemia', 'Hepatitis D', 'Typhoid', 'Hepatitis B', 'Osteoarthristis', 'Hypertension ', 'Dengue', 'Hepatitis C', 'Malaria', 'Allergy', 'Dimorphic hemmorhoids(piles)', 'Bronchial Asthma', 'Hepatitis E', 'AIDS', '(vertigo) Paroymsal  Positional Vertigo', 'Alcoholic hepatitis', 'Heart attack', 'Varicose veins', 'Diabetes ', 'Chicken pox', 'Tuberculosis', 'Fungal infection', 'Hyperthyroidism', 'Impetigo', 'Chronic cholestasis', 'Urinary tract infection', 'Jaundice', 'GERD', 'Cervical spondylosis', 'Psoriasis']
    model = joblib.load('random_forest1.joblib')
    array=request.form.get('array')
    array=array.split(',')
    array= [1 if i == 'true' else 0 for i in array]
    predictions = model.predict([array])
    print(predictions)
    return jsonify({'array':"done","disease":diseases[predictions[0]]})
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)