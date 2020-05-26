import smtplib
import ssl
from email.mime.text import MIMEText  # allows us to send text in html emails
from email.mime.multipart import MIMEMultipart


def send_mail(customer, dealer, rating, comments, startDate, endDate, totalCount):
    # port = 2525
    # # Testing with mailtrap
    # smtp_server = 'smtp.mailtrap.io'
    # login = '45a29469c52c65'  # username
    # password = '607adb3fddff50'
    # message = f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li><li>Start Date:{startDate}</li><li>End Date:{endDate}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</li><li>Total Count:{totalCount}</li></ul>"

    # sender_email = 'email1@example.com'
    # receiver_email = 'email2@example.com'
    # msg = MIMEText(message, 'html')
    # msg['Subject'] = 'Lexus Feedback'
    # msg['From'] = sender_email
    # msg['To'] = receiver_email

    # # Sending email
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.login(login, password)
    #     server.sendmail(sender_email, receiver_email, msg.as_string())

    # Testing with gmail
    mail_content = f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li><li>Start Date:{startDate}</li><li>End Date:{endDate}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</li><li>Total Count:{totalCount}</li></ul>"
    sender_address = 'ongmarcus204@gmail.com'
    sender_pass = 'zakka277()'
    receiver_address = 'ong.marcus@u.nus.edu'
    # Setup MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A Test mail send by Python from my gmail to my nus email, with an attachment'
    message.attach(MIMEText(mail_content, 'html'))
    # Create SMTP session for sending the mail
    port = 465
    context = ssl.create_default_context()


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_address, sender_pass)
            text = message.as_string()
            server.sendmail(sender_address, receiver_address, text)
            server.close()
    except Exception as err:
        print(err)


    print('Email Sent!')

