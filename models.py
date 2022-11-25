from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

from app import db


class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)


class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=True, nullable=False)
    weight = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)

class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    specialization = db.Column(db.String(120), unique=True, nullable=False)
    degree = db.Column(db.String(120), unique=True, nullable=False)

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desease = db.Column(db.String(80), unique=True, nullable=False)
    treatment = db.Column(db.String(120), unique=True, nullable=False)
    BMR = db.Column(db.String(120), unique=True, nullable=False)
    ECG = db.Column(db.String(120), unique=True, nullable=False)
    PE = db.Column(db.String(120), unique=True, nullable=False)
    Date = db.Column(db.String(120), unique=True, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patients', backref=db.backref('medical_record', lazy=True))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'), nullable=False)
    hospital = db.relationship('Hospitals', backref=db.backref('patients', lazy=True))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    doctor = db.relationship('Doctors', backref=db.backref('patients', lazy=True))