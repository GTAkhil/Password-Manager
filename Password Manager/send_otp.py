# Importing the required libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class SendOTP:
    # Function to send otp through the email
    @staticmethod
    def send_email(email, otp):
        try:
            # Set up the email server
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # Use 465 for SSL
            smtp_username = 'akhilkatare560@gmail.com'
            smtp_password = 'ssql ydqe oxcx djda'

            # Set up the email content
            from_email = 'akhilkatare560@gmail.com'

            message = MIMEMultipart()
            message['From'] = "akhilkatare560@gmail.com"
            message['To'] = email
            message['Subject'] = "OTP"

            # Body
            body = f"This is your otp {otp}. Do not share this with anyone."

            # Attach the body of the email
            message.attach(MIMEText(body, 'plain'))

            # Connect to the server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Use this line if you're using the standard port for TLS
                server.login(smtp_username, smtp_password)
                server.sendmail(from_email, email, message.as_string())

        # if any error occurs
        except Exception as e:
            print(e)
