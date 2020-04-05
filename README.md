# Selenium_Python_Test
testing some google fun tricks with Selenium and Creating HTML Reports

Pycharm Setup In Ubuntu

Download Community Version

Open Terminal --> cd path where pycharm file downloaded --> $ tar -xzf pycharm-community.XX.tar.gz

$ cd pycharm-community.XX --> cd bin --> sh pycharm.sh

After pycharm IDE opens --> File --> Setings --> project interpreter --> 

Add 1. Selenium
    2. pytest
    3. pytest-html
    
Add this test to project

pytest -v -s --html=Final_report.html --self-contained-html Browser.py 

find html report in VENv --> open in respective browser


