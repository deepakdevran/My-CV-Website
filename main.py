from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qualification')
def qualification():
    return render_template('qualification.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


# ✅ UPDATED CONTACT ROUTE
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        sender_email = "yourgmail@gmail.com"
        sender_password = "your_app_password"   # 🔐 App password here
        receiver_email = "yourgmail@gmail.com"

        msg = MIMEText(f"""
Name: {name}
Email: {email}

Message:
{message}
""")

        msg['Subject'] = "New Message from CV Website"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()

            return "<h2>Message Sent Successfully ✅</h2>"

        except Exception as e:
            return f"<h2>Error: {str(e)}</h2>"

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)