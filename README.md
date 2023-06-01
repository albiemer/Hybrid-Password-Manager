# Hybrid-Password-Manager

This program can only be use in Linux operating and specifically in debian, this application can also be use in windows with docker or swl2. i will post the windows application version sooner.
before to run the program be sure to install first the steghide with "sudo apt install steghide" and ccrypt with "sudo apt install apt ccrypt" from your terminal.
please see the requirements for addtionall install library for this program to  make it fully functional.

This is a Password manager that created primarily from Python3 with flask framework, implemented with terminal application like steghide and ccrypt to hide the password manager database and to encrypt it. this is created with python3, html, css, javascript or you can considered it as hybrid application.

INSTRUCTION OF INSTALLATION AND USE AFTER YOU DOWNLOAD REPOS:

Step 1:
Install steghide from your terminal

![screen01](https://user-images.githubusercontent.com/36027987/209571309-fd14a68f-4c4c-49b7-9f8d-0f207fb4c498.jpg)


STEP 2:
Install sqlite3 from your terminal

![screen-2022-09-02-02-39-19](https://user-images.githubusercontent.com/36027987/187988923-e4356239-aff7-42fe-9062-afe913f7f7d3.jpg)


STEP 3:
Install ccrypt from your terminal

![screen-2022-09-02-02-43-19](https://user-images.githubusercontent.com/36027987/187989144-dac7c742-c153-4fd4-ac74-7f5e6afe1c9d.jpg)


STEP 4:
go to the directory where the package located

![screen-2022-09-02-02-53-12](https://user-images.githubusercontent.com/36027987/187990983-cebd8600-52a5-4bef-9912-1985a8487a22.jpg)


STEP 5:
Create your own python3 environment

![screen-2022-09-02-02-56-31](https://user-images.githubusercontent.com/36027987/187991610-c2a51716-f59f-4633-9480-a276cda28cfe.jpg)

STEP 6:

Install Flask library from your python environment just type this "pip3 install flask"

STEP 7:
Copy the "gi" folder into the "env" or environment folder library which that "gi" can find from the library directory of python installed from the system or if you are not going to use virtual environment its fine to use directly the "gi library from system and nothing todo as long as you installed also from the system the other required library from requirements.txt" to make this program fully function.

![screen-2022-12-15-18-54-19](https://user-images.githubusercontent.com/36027987/207842753-430af7cf-399d-4950-b288-f52ff5082df4.jpg)

STEP 8:
Install requirements into your python3 environments

![screen-2022-09-02-03-01-21](https://user-images.githubusercontent.com/36027987/187992289-a23c2a6b-cda9-438f-ac1a-7cbff2b0e692.jpg)

STEP 9:
type "python3 main.py -d pstardb.db" it depends on you if where the location of your database but atleast the directory is accurate for target in command.

![screen-2022-09-02-03-09-30](https://user-images.githubusercontent.com/36027987/187993561-cdb5f17d-704b-40bb-93bb-563fc0a2c957.jpg)

USAGE:

STEP 10:
you have the option if you want the password manager accessible on your local network or you want to access it alone from your computer. if accessible this is the default url on the browser "192.168.1.2:5000/mypwdmngr" as long as you know your IP Address.

![screen-2022-09-02-03-11-55](https://user-images.githubusercontent.com/36027987/187993960-9bf8816e-d2b1-4564-a958-546b86bed9a1.jpg)

STEP 11:
Now you are at the login form the default user name is "gwen" and default password is "gw3n".

![screen-2022-09-02-03-12-45](https://user-images.githubusercontent.com/36027987/187994330-bef4612d-58bc-438d-8f78-563e27f6410f.jpg)

then that's it

The Login program

![screen-2022-08-01-12-19-43](https://user-images.githubusercontent.com/36027987/182161491-c7bb2fba-1e3f-4cea-b554-d542a8f0277d.jpg)

The main program which is all password are listed.

![screen-2022-09-16-06-48-55](https://user-images.githubusercontent.com/36027987/190521958-f883f809-133d-4b2f-a97f-eced8305cc38.jpg)

This is the password viewer and edit entry, this form are able to edit, delete, update record.

![screen-2022-12-15-05-19-44](https://user-images.githubusercontent.com/36027987/207717358-6af35a7a-8127-47c5-a322-c7e7574567b3.jpg)



