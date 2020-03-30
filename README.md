# corona-data-api

This application is built on **flask** micoframework. 

It scraps data from the official site of **[Ministry of Health and Family Welfare]("https://www.mohfw.gov.in/")** using **Beautifulsoup**.

Here is the link.

https://www.mohfw.gov.in/

## Setup
*Create a .env file for sending error to mailbox when an error occurs.*

**env** variables are:
* USER_NAME
* PASSWORD

These are *[mailgun]('https://www.mailgun.com/') smtp* credentials.

Comment ```send_mail``` function in *corona_api.py* if you do not wish to use it.

---

### Installation
*create a virtual env*

```pip install -r requirements.txt```

---

### To Run

```python3 main.py ```

---

The application should be running on *localhost* at port *5000* by default.

To get data from all the provinces. <br> http://localhost:5000  

To get data from a province. <br> http://localhost:5000/province_name

---

## [Link to the app hosted on heroku.]("https://shrouded-journey-40316.herokuapp.com/")

https://shrouded-journey-40316.herokuapp.com/

