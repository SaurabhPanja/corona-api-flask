from bs4 import BeautifulSoup
import requests
import traceback
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

#cases is the id of div on the website
def scrape_cases_tag():
    html_doc = requests.get("https://www.mohfw.gov.in/").text
    soup = BeautifulSoup(html_doc, 'html.parser')

    cases_table_tbody = soup.find("table").tbody
    tbody_tr = cases_table_tbody.find_all("tr")
    
    return tbody_tr

def get_corona_data_arr(tbody_tr):
    corona_data = []
    for tr_td in tbody_tr:
        td = tr_td.find_all("td")
        td_data = []
        for text in td:
            td_data.append(text.get_text())
        corona_data.append(td_data)

    return corona_data

def get_corona_data_api(corona_data_arr):

    corona_dict = {}
    for data in corona_data_arr:
        if len(data) > 4:
            province = data[1].lower().replace(" ", "_")
            cases_total = data[2]
            cured = data[3]
            death = data[4]

            province_data = {
                'cases_total': cases_total,
                'cured' : cured,
                'death' : death,
            }

            corona_dict[province] = province_data

        elif len(data) > 1:
            cases_total = data[1].replace("\n","")
            cured = data[2].replace("\n","")
            death = data[3].replace("\n","")

            total = {
                'cases_total': cases_total,
                'cured' : cured,
                'death' : death, 
            }

            corona_dict['total'] = total
            
    return corona_dict


def send_mail(mail_text):
    msg = MIMEText(mail_text)
    msg['Subject'] = "Corona API Stopped Working."
    msg['From']    = "Error@saurabhpanja.com"
    msg['To']      = "panjasaurabh@gmail.com"

    s = smtplib.SMTP('smtp.mailgun.org', 587)
    
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    s.login(USER_NAME,PASSWORD)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()



try:
    tbody_tr = scrape_cases_tag()
    corona_data_arr = get_corona_data_arr(tbody_tr)
    corona_data_api = get_corona_data_api(corona_data_arr) 
except Exception as e:
    error_log = traceback.format_exc()

    send_mail(error_log)

    corona_data_api = {
        "message": "Seems Ministry of Health and Family Welfare is not showing data as of now."
    }



    

