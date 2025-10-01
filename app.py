from flask import Flask, render_template, send_file, request, jsonify
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def download_resume():
    return send_file('Luke Slautterback Resume.pdf', as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'Please fill in all fields'}), 400
        
        # For now, just log the message (in production, you'd send an email)
        print(f"Contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        return jsonify({'success': True, 'message': 'Thank you for your message! I\'ll get back to you soon.'})
        
    except Exception as e:
        print(f"Error processing contact form: {e}")
        return jsonify({'success': False, 'message': 'Sorry, there was an error sending your message. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
