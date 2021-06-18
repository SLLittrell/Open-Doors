import os, time
os.system("rm db.sqlite3")
time.sleep(.5)
os.system("python3 manage.py migrate")
os.system("python3 manage.py loaddata categories posts tokens users open_user ")