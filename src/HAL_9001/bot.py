class Command(dict):
    def __init__(self):
        @self.register('pass')
        def _(password): pass

        @self.register('nick')
        def _(nickname, hopcount=0): pass

        @self.register('user')
        def _(username, hostname, servername, realname): pass

        @self.register('server')
        def _(servername, hopcount, info): pass

        @self.register('oper')
        def _(user, password): pass

        @self.register('quit')
        def _(quit_message): pass

        @self.register('squit')
        def _(server, comment): pass

        @self.register('join')  #Fix these argument TODO
        def _(channel, key=None): pass

        @self.register('part')
        def _(*channel): pass

        @self.register('mode')
        def _(): pass

        @self.register('topic')
        def _(channel, topic=None): pass

        @self.register('names')
        def _(channel): pass

        @self.register('list')
        def _(): pass

        @self.register('invite')
        def _(nickname, channel): pass

        @self.register('kick')
        def _(channel, user, comment=""): pass

        @self.register('version')
        def _(server=""): pass

        @self.register('stats')
        def _(query, server=""): pass

        @self.register('links')
        def _(): pass

        @self.register('time')
        def _(server=""): pass

        @self.register('connect')
        def _(target_server, port=0, remote_server=""): pass

        @self.register('trace')
        def _(server=""): pass

        @self.register('admin')
        def _(server=""): pass

        @self.register('info')
        def _(server=""): pass

        @self.register('privmsg')
        def _(self, msgtarget, text_to_be_sent): pass

        @self.register('notice')
        def _(nickname, text): pass

        @self.register('who')
        def _(name="", o=""): pass

        @self.register('whois')
        def _(): pass

        @self.register('whowas')
        def _(): pass

        @self.register('kill')
        def _(nickname, comment): pass

        @self.register('ping')
        def _(server, server2=None): pass

        @self.register('pong')
        def _(daemon, daemon2=None): pass

        @self.register('error')
        def _(message): pass

        @self.register('away')
        def _(message=""): pass

        @self.register('rehash')
        def _(): pass

        @self.register('restart')
        def _(): pass

        @self.register('summon')
        def _(user, server=""): pass

        @self.register('users')
        def _(server=""): pass

        @self.register('wallops')
        def _(text): pass

        @self.register('userhost')
        def _(nick, nick2="", nick3="", nick4="", nick5=""): pass

        @self.register('ison')
        def _(): pass

    def register(self, name):
        def wrapper(func):
            self[name.upper()] = func
        return wrapper

class Bot:

    def __init__(self, addr, identy, tempdir):
        self.command = Command() 
        self.everything = []
        self.channels = []

    def __call__(self):
        pass 

    def step(self):
        for x in self.everything:
            x()

    def addMod(self, com):
        self.everything.append(com(self))


x = Bot("idk", "lol", "ttyl")
def z():
    print("Z!")
x.command.__setitem__("Z",z)
#print(x.command)
#x.command["Z"]
print(x.command)
