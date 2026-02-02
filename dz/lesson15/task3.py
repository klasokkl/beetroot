CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0  

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, N):
        self.current_index = N - 1
        return self.channels[self.current_index]

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, arg):
        if isinstance(arg, int):
            return "Yes" if 1 <= arg <= len(self.channels) else "No"
        elif isinstance(arg, str):
            return "Yes" if arg in self.channels else "No"
        return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())     
print(controller.last_channel())      
print(controller.turn_channel(1))     
print(controller.next_channel())      
print(controller.previous_channel()) 
print(controller.current_channel())   
print(controller.exists(4))         
print(controller.exists("BBC"))       
