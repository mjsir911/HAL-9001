class Bot:

    def PRIVMSG(self, msg):
        pass

    def __init__(self, addr, identy, tempdir):
        self.command = {}
        self.command['PRIVMSG'] = self.PRIVMSG
        self.everything = []
        self.channels = []

    def __call__(self):
        pass 

    def step(self):
        for x in self.everything:
            x()

    def addMod(self, com):
        self.everything.append(com(self))
