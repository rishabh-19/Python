from datetime import datetime
hour=int((datetime.now()).strftime("%H"))
if hour  <=12 :
        print("Good Morning")
elif hour  <=18 :
        print("Good Afternoon")
elif hour  <=22 :
        print("Good Evening")
elif hour  <=24 :
        print("Good Night")
