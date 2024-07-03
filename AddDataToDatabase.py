import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Admin SDK configuration snippet

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-bb0ee-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "101" : {
        "name":"Swapnali Gawade",
        "major":"CSE",
        "starting_year":2024,
        "total_attendance":6,
        "standing":"Bad",
        "year":4,
        "last_attendance_time":"2024-4-25 00:54:34"

    },
    "102":
        {
            "name": "Elon Musk",
            "major": "Economics",
            "starting_year": 2024,
            "total_attendance": 12,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2024-04-25 00:54:34"
        },
        "103":
        {
            "name": "Sundar Pichai",
            "major": "CSE",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "Average",
            "year": 1,
            "last_attendance_time": "2024-04-25 00:54:34"
        },
        "104":
        {
            "name": "Ananda Mahindra",
            "major": "CSE",
            "starting_year": 2024,
            "total_attendance": 9,
            "standing": "Average",
            "year": 1,
            "last_attendance_time": "2024-04-25 00:54:34"
        },
        "105":
        {
            "name": "Kavya",
            "major": "CSE",
            "starting_year": 2024,
            "total_attendance": 10,
            "standing": "Average",
            "year": 1,
            "last_attendance_time": "2024-04-25 00:54:34"
        }
        
        
}
for key,value in data.items():
    ref.child(key).set(value)