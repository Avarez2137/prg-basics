# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        for channel in channel_list:
            self.channels.append(channel)

    def show_channels(self):
        i = 1
        print("Channel list:")
        for channel in self.channels:
            print(f"{i}. {channel}")
            i+=1

    def show_status(self):
        if self.is_on == True:
            if self.channel_no > len(self.channels):
                print(f"The TV is turned ON, channel {self.channel_no}")
            else:
                print(f"The TV is turned ON, channel {self.channel_no} ({self.channels[self.channel_no]})")
        else:
            print("The TV is turned OFF")
