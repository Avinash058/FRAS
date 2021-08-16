import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP(user = "avinash.2017.lece@anits.edu.in", password = "Password@123")

# sent the mail
yag.send(
    to="avi.yalamanchili@gmail.com",
    subject= sub, # email subject
    contents= "None",  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
