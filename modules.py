# Module = a file containing python code. May contain functions, classes etc
# used with modular programming, which is to seperate a program into parts

#here we have imported the message file of py into current file 
import message as msg # 'as' is used to give a nickname to the import file

#message.hello() (if msg is not declared)

msg.hello()
msg.bye()

#another way of importing file
# from message import hello , bye 
#also be written as 
# from message import * (* means all)

# hello()
# bye()

help("modules")