import choices
import route
import colorama
import location

class Order:
    def __init__(self):
        colorama.init()
        
        self.true = colorama.Fore.GREEN
        self.false = colorama.Fore.RED
        
        #( 0  ,    1     ,       2     ,      3   )
        #(Git , Location , host_online , start_now)

        self.values = ()
        print(f"{self.true}[+]All Files Present" if route.Route().file_check() else "{self.false}[-]All Files Are Not Present")
        

    def get_choices(self):
        x=choices.Choice()
        x.git()
        x.location()
        x.host_online()
        x.start_now()
        self.values = x.get_value()
    
    def location(self):
       location.Location(self.values[1]) 

    
x=Order()
x.get_choices()
x.get_value()
