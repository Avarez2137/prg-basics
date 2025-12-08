# tv_show.py file
# main program
import tv

def main():
    # object creation
    TVset = tv.TV()

    # object usage
    TVset.show_status()
    TVset.turn_on()
    TVset.show_status()
    TVset.show_channels()
    TVset.set_channels(["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
    TVset.show_channels()
    TVset.set_channel(5)
    TVset.show_status()
    TVset.set_channel(2)
    TVset.show_status()
    TVset.set_channel(7)
    TVset.show_status()
    TVset.turn_off()
    TVset.show_status()


if __name__ == "__main__":
   main() 