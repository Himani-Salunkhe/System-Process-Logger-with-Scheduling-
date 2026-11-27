import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = os.getenv("SMTP_EMAIL")
SENDER_PASSWORD = os.getenv("SMTP_PASSWORD")


def SendMail(ReceiverEmail, FileName):
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Set SMTP_EMAIL and SMTP_PASSWORD environment variables.")
        return False
    
    try:
        if not os.path.exists(FileName):
            return False
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = ReceiverEmail
        message["Subject"] = "Running Process Information Log"
        Body = """
                Hello,

                Please find the attached log file containing the running process information.

                This mail is generated automatically using Python Automation Script.

                Thank You.
                """

        message.attach(MIMEText(Body, "plain"))
        attachment = open(FileName, "rb")
        with open(FileName,"rb")as attachment:
            payload = MIMEBase("text", "plain")
            payload.set_payload(attachment.read())
            encoders.encode_base64(payload)
            payload.add_header(
                "Content-Disposition",
                "attachment; filename={}".format(os.path.basename(FileName))
            )
        message.attach(payload)
        #attachment.close()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(
            SENDER_EMAIL,
            ReceiverEmail,
            message.as_string()
        )
        server.quit()
        return True

    except smtplib.SMTPAuthenticationError:
        print("Authentication Failed")
        return False

    except smtplib.SMTPException as e:
        print("SMTP Error :", e)
        return False

    except FileNotFoundError:
        print("Log file not found")
        return False

    except Exception as e:
        print("Error :", e)
        return False