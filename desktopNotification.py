import time
from plyer import notification 

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Alert!!!",
            message = "Take a break, life is short",
            timeout = 10
        )
        time.sleep(300)