# Whats the plan

figure out how irc works with sockets and/or requests

make a list of things one would be able to do in an irc object

make simple irc object to load modules

  One person should work on the actual irc connecting of the object

  another should work on loading all modules in a directory and figuring out
  how to reload if changed


# Architecture / Design

There should be an object that is everything details that gets sent to all
module functions whenever anything happens

This object would include server address, channel, nick of who said it and
stuff like that

We should figure out some standard way to represent everything
