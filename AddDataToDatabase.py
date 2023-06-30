
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-aba69-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "104004":
        {
            "name":"Divya C",
            "dept":"CSE",
            "starting_year":2019,
            "total_attendance":6,
            "standing":"G",
            "year":"4",
            "last_attendance_time":"2023-04-02 09:36:00"


        },
    "104016":
        {
            "name":"Tamilarasi S",
            "dept":"CSE",
            "starting_year":2019,
            "total_attendance":7,
            "standing":"G",
            "year":"4",
            "last_attendance_time":"2023-04-02 09:36:00"
        },
    "104017":
        {
            "name":"Yuvashri A",
            "dept":"CSE",
            "starting_year":2019,
            "total_attendance":5,
            "standing":"G",
            "year":"4",
            "last_attendance_time":"2023-04-02 09:36:00"
        }

}

for key,value in data.items():
    ref.child(key).set(value)