class TVController:
    def __init__(self, chnl):
        self.chann = chnl
        
    def first_channel(self):
        print(self.chann[0])
        return self.chann[0]

    def last_channel(self):
        print(self.chann[-1])
        return self.chann[-1]
        
    def turn_channel(self, turn):
        self.turn = turn - 1
        print(self.chann[0])
        return self.chann[0]
        
    def next_channel(self):
        if self.turn == len(self.chann) - 1:
            self.turn = 0
        else:
            self.turn += 1
        print(self.turn)
        return self.chann[self.turn]
    
    def previous_channel(self):
        self.turn -= 1
        if self.turn < 0:
            self.turn = self.chann[-1]
        print(self.turn)
        return self.chann[self.turn]
        
    def current_channel(self):
        return self.chann[self.turn]
    
    def is_exist(self, num):
        if type(num) == str:
            if num in self.chann:
                return 'Yes'
            else:
                return 'No'
        elif type(num) == int:
            if 0 < num <= len(self.chann):
                return 'Yes'
            else:
                return 'No'
        
        
     
CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
 

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
