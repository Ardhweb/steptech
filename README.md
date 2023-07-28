# steptech

**1.Install Python on your system.**
**2.Open Visual Studio Code and create a new folder.**
**3.Open the terminal in Visual Studio Code.**
**5.If you are using Windows, type the following command in the terminal:**

**python -m venv venv**

**6.To activate the virtual environment, type the following command in the terminal:**

**venv/scripts/activate**

**7.Download the Django repository and extract it.**
**8.Copy the extracted folder to the current folder where you are.**
**9.In the terminal, type the following command to install the necessary Python packages:**

**pip install -r requirements.txt**

**Once you have completed these steps, you will have successfully installed Django.**

**Here are some additional tips for installing Django:**
**You can use the pip install django command to install Django without creating a virtual environment. 
However, it is recommended to use a virtual environment to isolate your Django project from other Python projects on your system.**

** DATABASE Config before user**

-Open the settings.py file of steptech - steptech/stecptech/settings.py in here Find 
**DATABASE{

}**
sedtion and in this find **password** and add your system mysql root user password becauuse this db host is localhost  and user is root.

-Open Your Mysql in cmd and login

-Now Using Mysql Command make New Database with name **users**

-Now Again In Visual Studio Code Terminal with activated venv with current project directory use this command

**python manage.py makemigrations**

after this 

**python manage.py migrate**

**Now After this **
**use py manage.py runserver**
**and check browser with http://127.0.0.1:8000/home**

For other you can check documention!!!
