# Another Polymorphism example
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        pass


class Email(Notification):
    def send(self):
        print(f"📧 Emailing: {self.message}")


class SMS(Notification):
    def send(self):
        print(f"📱 Texting: {self.message}")


class Push(Notification):
    def send(self):
        print(f"🔔 Pushing: {self.message}")


# Your core system — never changes, ever.
def notify_user(notification):
    notification.send()


# Today
notify_user(Email("Your order shipped!"))
notify_user(SMS("Your OTP is 1234"))


# 6 months later — just add the class, core system untouched ✅
class WhatsApp(Notification):
    def send(self):
        print(f"💬 WhatsApp: {self.message}")


notify_user(WhatsApp("Your delivery is here!"))
