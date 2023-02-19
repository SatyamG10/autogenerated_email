import pandas as pd
import numpy as np
import smtplib
import warnings
warnings.filterwarnings(action="ignore")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




def send_mail(fromaddr,toaddr,password,day,filename):
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr[0]
        msg['Subject'] = "More_Daily_C2A_"+day.strftime("%Y-%m-%d")
        if True:
            body = """
            
                   """
        else:
            body = """
            
                   """
            
        html = """\
                <html>
                  <head></head>
                  <body>
                        <p>  """  """ <br>
                       <body>""" """</br> <body>
                       <font color = "blue">
                    </p>
                  </body>
                </html>
                """
        
        
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(html, "html"))
        for i in filename:
            attachment = open(i, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % i)
            msg.attach(p)
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(fromaddr, password)
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        
# send_mail(fromaddr,toaddr,pwd,end_date, count,count_miss,filename)
# print('Report Sent at '+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
