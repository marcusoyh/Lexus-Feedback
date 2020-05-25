import smtplib
from email.mime.text import MIMEText  # allows us to send text in html emails


def send_mail(customer, dealer, rating, comments, startDate, endDate):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '45a29469c52c65'  # username
    password = '607adb3fddff50'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li><li>Start Date:{startDate}</li><li>End Date:{endDate}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Sending email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
