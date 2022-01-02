import smtplib
from email.message import EmailMessage


def send_an_email(sender, subject, content, to):

    email = EmailMessage()
    email['from'] = sender
    email['to'] = to
    email['subject'] = subject
    email.set_content(content)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("user@domain.com", "password")
        smtp.send_message(email)
        print(f"mail with subject, {subject}, sent")
    return 1


if __name__ == "__main__":
    send_an_email("Sender", "test",
                  "This is a test", "user@domain.com")
