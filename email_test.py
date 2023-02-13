from email.mime.text import MIMEText 
from smtplib import SMTP

  
# Add the From: and To: headers at the start!
# fromaddr =  "happyday.mjohnson@gmail.com"
# toaddrs = fromaddr
# msg = ("From: %s\r\nTo: %s\r\n\r\n"
#        % (fromaddr, ", ".join(toaddrs)))
# print(f"{msg}")
# Prepare the message
message = "Your recent toot was found to contain inappropriate content and has been removed."
from_addr = "happyday.mjohnson@gmail.com"
to_addr = "happyday.mjohnson@gmail.com"
msg = MIMEText(message)
msg['Subject'] = "ALERT! vintageracing.social has inappropriate content!!"
msg['From'] = "happyday.mjohnson@gmail.com"
msg['To'] = "happyday.mjohnson@gmail.com"
# Email the message
server = SMTP('smtp-relay.sendinblue.com')
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

