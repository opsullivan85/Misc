#Simple Mail Transfer Protocol
import smtplib

#smtp server creation
conn = smtplib.SMTP('smtp.gmail.com', 587)

#connect to server
conn.ehlo()

#start encription
conn.starttls()

#conn.login('email', 'app_specific_password')
conn.login('opsullivan85@gmail.com', 'ocffqkqpwgmiuypw')

string = '''Subject: Hello Mommieo!\n\n
If all goes well this email will have been sent to you by this little program:

import smtplib
conn = smtplib.SMTP(\'smtp.gmail.com\', 587)
conn.ehlo()
conn.starttls()
conn.login(\'opsullivan85@gmail.com\', \'[my fancy app specific password thing]\')
string = \'[this email]\'
conn.sendmail(\'opsullivan85@gmail.com\', \'grsullivan85@gmail.com\', string)
conn.quit()

 - Owen [I tried to send a <3 emoji but it wont let me D:]'''
         
#print(string)
conn.sendmail('opsullivan85@gmail.com', 'grsullivan85@gmail.com', string)

conn.quit()
