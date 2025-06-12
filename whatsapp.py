
import pywhatkit as kit
phone_number = "+919539628147"
message = "Hello! This is a test message."
for _ in range(5):  
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=5)
