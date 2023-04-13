from donationalerts import Alert
from config import da_alert_widget_token 

alert = Alert(da_alert_widget_token)
@alert.event()
def new_donation(event): 
    print(event.username)
