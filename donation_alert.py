from donationalerts import Alert
da_alert_widget_token = 'Us0Q7Z69fREDrIxizs31'

alert = Alert(da_alert_widget_token)
@alert.event()
def new_donation(event): 
    print(event.username)