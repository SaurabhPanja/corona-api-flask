from bs4 import BeautifulSoup
import requests

#cases is the id of div on the website
def scrape_cases_tag():
    html_doc = requests.get("https://www.mohfw.gov.in/").text
    soup = BeautifulSoup(html_doc, 'html.parser')

    cases_table_tbody = soup.find(id = "cases").table.tbody
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
        # corona_dict = {}
        if len(data) > 5:
            province = data[1].lower().replace(" ", "_")
            cases_indian = data[2]
            cases_foreign = data[3]
            cured = data[4]
            death = data[5]

            province_data = {
                'cases_indian' : cases_indian,
                'cases_foreign' : cases_foreign,
                'cured' : cured,
                'death' : death,
            }

            corona_dict[province] = province_data

        elif len(data) > 1:
            cases_indian = data[1].replace("#","")
            cases_foreign = data[2].replace("\n","")
            cured = data[3].replace("\n","")
            death = data[4].replace("\n","")

            total = {
                'cases_indian' : cases_indian,
                'cases_foreign' : cases_foreign,
                'cured' : cured,
                'death' : death, 
            }

            corona_dict['total'] = total
            
    return corona_dict


try:
    tbody_tr = scrape_cases_tag()
    corona_data_arr = get_corona_data_arr(tbody_tr)
    corona_data_api = get_corona_data_api(corona_data_arr)    
except:
    corona_data_api = {
        "message": "Seems Ministry of Health and Family Welfare is not showing data as of now."
    }



    

