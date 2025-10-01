from flask import Flask, render_template, send_file, request, jsonify
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Using system environment variables only (no .env file dependency)

app = Flask(__name__)

# Email configuration - you'll need to set these as environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'lukeslautterback@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', '')  # Use app password for Gmail

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def download_resume():
    return send_file('Luke Slautterback Resume.pdf', as_attachment=True)

def send_email(name, email, subject, message):
    """Send email notification about contact form submission"""
    try:
        print(f"Attempting to send email to {EMAIL_ADDRESS} via {SMTP_SERVER}:{SMTP_PORT}")
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = f"Contact Form: {subject}"
        
        # Create email body
        body = f"""
New contact form submission from your website:

Name: {name}
Email: {email}
Subject: {subject}
Message: {message}

Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        print("Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        print("Starting TLS...")
        server.starttls()
        print("Logging in...")
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("Sending email...")
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, text)
        server.quit()
        print("Email sent successfully!")
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

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
        
        # Log the message
        print(f"Contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        # Debug: Print email configuration status
        print(f"Email configuration check:")
        print(f"  EMAIL_PASSWORD set: {'Yes' if EMAIL_PASSWORD else 'No'}")
        print(f"  EMAIL_ADDRESS: {EMAIL_ADDRESS}")
        print(f"  SMTP_SERVER: {SMTP_SERVER}")
        print(f"  SMTP_PORT: {SMTP_PORT}")
        
        # Send email if configured
        if EMAIL_PASSWORD:
            print("Attempting to send email...")
            email_sent = send_email(name, email, subject, message)
            if email_sent:
                print("Email sent successfully!")
            else:
                print("Email could not be sent, but form submission was logged")
        else:
            print("Warning: Email not configured - form submission logged only")
        
        return jsonify({'success': True, 'message': 'Thank you for your message! I\'ll get back to you soon.'})
        
    except Exception as e:
        print(f"Error processing contact form: {e}")
        return jsonify({'success': False, 'message': 'Sorry, there was an error sending your message. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
