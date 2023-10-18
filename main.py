# -*- coding:utf-8 -*-
# @Time : 2/5/22 2:15 AM
# @Author: Mack.Ding
# @File : main.py


import sys, GUI_Handle, requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from pprint import pprint
from urllib.parse import quote


def convert(ui):
    # input parameter to replace json value to Encode
    input_login = ui.lineEdit.text()
    input_emails = ui.lineEdit_3.text()
    input_password = ui.lineEdit_2.text()
    json_value = {
        "domain-name": "China",
        "country": "Brazil",
        "firstname": "Q",
        "home-page": "",
        "activity": "",
        "city": "Shenzhen",
        "industry": "Eyewear",
        "login": input_login,
        "emails": input_emails,
        "password": input_password,
        "is-food-inspection": "false",
        "affiliate-id": "",
        "user-ip": "",
        "BU": "AI",
        "billing-salutation": "Mr",
        "fax": "+86 571 8659 3800",
        "turnover": "0",
        "post-code": "518001",
        "company-name": "PPTestCompanyName0321",
        "supplier-company-name": "",
        "address": "Shenzhen",
        "mobile": "+86 571 8659 3800",
        "telephone": "+86 571 8659 3800",
        "is-chb": "false",
        "lastname": "A",
        "refer": "",
        "billing-email": "qateam@qima.com",
        "billing-contact-name": "QA",
        "salutation": "Mr",
        "position": "QA",
        "is-test-account": "false"
    }

    pprint(json_value)
    # Encode
    body = str(quote(str(json_value), 'UTF-8'))

    # Request
    try:
        url = "http://ppservice.qima.com/customer-service/customer-legacy/create-new-account?clientInfo=" + body
        print(url)
        payload = {}
        headers = {}
        response = requests.request("POST", url=url, headers=headers, data=payload)
        result = response.text
        code = response.status_code
        r = str(code) + result
        ui.textBrowser.setText(str(r))
    except Exception as r:
        print('Error %s' % r)
        ui.textBrowser.setText(str(r))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GUI_Handle.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui.pushButton.clicked.connect(click_success)
    ui.pushButton.clicked.connect(partial(convert, ui))
    sys.exit(app.exec_())

# Terminal： pyinstaller main.spec