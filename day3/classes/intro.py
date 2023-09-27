class Led:
    is_on: bool = False

    def turn_on(self):
        if not self.is_on:
            print("Let there be light")
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            print("Time to go to sleep")
            self.is_on = False


l = Led()
l.turn_on()
l.turn_on()
l.turn_on()

g = Led()
g.turn_on()
g.turn_on()

