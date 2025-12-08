class Phone():
    def __init__(self, battery):
        self.battery = battery
        self.torch = False
        self.bluetooth = []

    def charge(self, percent):
        self.battery = percent

    def lightsOn(self):
        if self.torch == True:
            self.torch = False
        else:
            self.torch = True

    def connectBluetooth(self, device):
        self.bluetooth.append(device)

    def showBattery(self):
        print(f"Battery state: {self.battery}%")

myPhone = Phone(78)
myPhone.showBattery()
myPhone.lightsOn()
print(myPhone.torch)
myPhone.lightsOn()
print(myPhone.torch)
myPhone.connectBluetooth("Headphones")
myPhone.connectBluetooth("Speaker")
print(myPhone.bluetooth)
myPhone.charge(92)
myPhone.showBattery()