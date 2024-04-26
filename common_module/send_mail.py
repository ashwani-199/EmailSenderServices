from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, select_autoescape
import time
import smtplib

class SendMail():
    def __init__(self) -> None:
        pass

    @staticmethod
    def send_mail(recipients, smtp_server, smtp_port, sender_details):

        for sender_email, sender_password, subject in sender_details:

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Send the email to each recipient
            for name, email in recipients:

                env = Environment(
                    loader=FileSystemLoader('templates'),
                        autoescape=select_autoescape(['html', 'xml'])
                    )
                template = env.get_template('email_work/email.html')

                context = {
                    'name': name,
                    'email': email,
                    'subject': subject
                }
                html = template.render(data=context)

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = subject

                # Replace {name} with the recipient's name
                msg.attach(MIMEText(html, 'html'))
                server.sendmail(sender_email, email, msg.as_string())
                time.sleep(5) #  Wait 5 seconds between emails to avoid being flag
        


            # Close the SMTP server
            server.quit()