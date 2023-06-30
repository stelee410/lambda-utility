from email_sender import send_email
def alert(receiver, msg, proxy=None):
    title = "Instance Alert"
    send_email(receiver, title, msg, proxy_url=proxy)
