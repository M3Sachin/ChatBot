# Library
from tkinter import *

#Create a tkinter object (Parent Window)
root=Tk()

#This give the window a title
root.title('Chatbot')

#Icon
root.iconbitmap("D:\Vs Code Python\chatbot.ico")

lst1 = ['Hello','hello','hi','Hi','Bonjour','bonjour','Hola','hola','hey','Hey']
lst2 = ['Namaste','namaste']
lst3 = ['how are you','How are you','how are you?','How are you?','how are u','How are u','how are u?',
'How are u?','how r you','How r you','how r you?','How r you?',"how's going",
"how's going?","How's going","How's going?","Whats's up","Whats up","whats up","what's up"]

lst4 = ['Im fine',"I'm fine","im fine","i'm fine"," I am fine",'i am fine',"fine",'Fine',"awesome","Awesome",
"good",'Good',"i am good","i'm good","I am good","I'm good","I am happy","i am happy","I'm happy","i'm happy"]

lst5 = ["Are you a robot?","are you a robot?","are you a bot?","are you a bot","Are you a bot?","Are you a bot"]

lst6 = ["Tell me about yourself","Tell me about yourself?","tell me about yourself","tell me about yourself?"]

lst7 = ['Who is your creater?','who is your creater?','Who is your creater','who is your creater',"Who is your owner?","who is your owner?",
"Who is your owner","who is your owner","Who made you?","Who made you","who made you?","who made you","Who is your boss?",
"Who is your boss","who is your boss","who is your boss?","Who is your master?","Who is your master","who is your master",
"who is your master?","Who created you?","Who created you","who created you?","who created you"]

lst8 = ["How can you help me?","How can you help me","how can you help me?","how can you help me"]

lst9 = ["I have a question?","I have a question","i have a question?","i have a question","Can you help me?","Can you help me",
"can you help me?","can you help me","I have some problems?","i have some problems?","I have some problem?","i have some problem?",
"I have some problem","i have some problem","I have a problem","i have a problem"]

lst10 = ["How old are you?","How old are you","how old are you?","how old are you","What is your age?","What is your age",
"what is your age","what is your age?","Are you single?","Are you single","are you single","are you single?"]

lst11 = ["Good morning","Good Morning","good morning","Morning","morning"]
lst12 = ["Good afternoon","Good Afternoon","good afternoon","Afternoon","afternoon"]
lst13 = ["Good Evening","Good evening","good evening","Evening","evening"]
lst14 = ["Good Night","Good night","good night","night","Night"]
lst15 = ["Tell me something","tell me something","tell anything","Tell anything","Say something","say something"]

lst16 = ["Do you know a joke?","Do you know a joke","do you know a joke?","do you know a joke","Tell me a joke?","Tell me a joke",
"tell me a joke","tell me a joke?","Can you tell me a joke?","Can you tell me a joke","can you tell me a joke?","can you tell me a joke"]

lst17 = ["You are funny","you are funny","Thank you","thank you","Thanks","thanks","Thanks a lot","thanks a lot"]
lst18 = ["Do you love me?","Do you love me","do you love me?","do you love me"]
lst19 = ["I love you","i love you"]
lst20 = ["You are clever","you are clever","You are smart","you are smart","You are intelligent","you are intelligent"]
lst21 = ["You are annoying","you are annoying","You are boring","you are boring","You are bad","you are bad","You are crazy","you are crazy"]
lst22 = ["What is your name?","what is your name?","What is your name","what is your name"]
lst23 = ["I'm sad","I am sad","i'm sad","i am sad","feeling sad","Feeling sad","I'm not happy","I am not happy","i am not happy",
"i'm not happy","Not good","not good","Not feeling good","not feeling good"]
lst24 = ["Where are you from?","Where are you from","where are you from?","where are you from","Where do you come from?",
"Where do you come from","where do you come from?","where do you come from"]
lst25 = ["Will you marry me?","Will you marry me","will you marry me?","will you marry me"]


def send():
	send = "You -->"+e.get()
	txt.insert(END,"\n"+send)

	if e.get() in lst1:
		txt.insert(END,"\n"+"Bot -->Hello I'm ZenX your Bot, how can I help you.")

	elif e.get() in lst3:
		txt.insert(END,"\n"+"Bot -->I'm fine, What about you?")

	elif e.get() in lst2:
		txt.insert(END,"\n"+"Bot -->Namaste\n       Sorry to say but I don't understand Hindi.")

	elif e.get() in lst4:
		txt.insert(END,"\n"+"Bot -->Sounds Good.")

	elif e.get() in lst5:
		txt.insert(END,"\n"+"Bot -->Yes I am a robot, but I'm a good one. Let me prove it.\n       How can I help you?")

	elif e.get() in lst6:
		txt.insert(END,"\n"+"Bot -->My name is ZenX and I'm a bot.\n       I was created by Sir Sachin at ZenX House.\n       I'm written in python programming language using tkinter module and\n       some good algorithms.Basically I uses AI for answering your questions.\n       I'm here to help you.\n       You can also simply talk to me.")

	elif e.get() in lst7:#Add instagram link later.
		txt.insert(END,"\n"+"Bot -->I was created by Sachin at ZenX house.\n       You can search him using this link:-https://twitter.com/MrPatmer")

	elif e.get() in lst8:
		txt.insert(END,"\n"+"Bot -->What kind of help do you want from me?")

	elif e.get() in lst9:
		txt.insert(END,"\n"+"Bot -->Yes please, tell me your problem.")

	elif e.get() in lst10:
		txt.insert(END,"\n"+"Bot -->Does it really matters?")

	elif e.get() in lst11:
		txt.insert(END,"\n"+"Bot -->Good Morning")

	elif e.get() in lst12:
		txt.insert(END,"\n"+"Bot -->Good Afternon")

	elif e.get() in lst13:
		txt.insert(END,"\n"+"Bot -->Good Evening")

	elif e.get() in lst14:
		txt.insert(END,"\n"+"Bot -->Good Night")

	elif e.get() in lst15:
		txt.insert(END,"\n"+"Bot -->Corona is never going to end.#bittertruth")

	elif e.get() in lst16:
		txt.insert(END,"\n"+"Bot -->Ok here we go:-\n       I recently decided to sell my vacuum cleaner as all it was doing was\n       gathering dust.")

	elif e.get() in lst17:
		txt.insert(END,"\n"+"Bot -->I'm happy that I made you Happy.")

	elif e.get() in lst18:
		txt.insert(END,"\n"+"Bot -->Well, who doesn't?")

	elif e.get() in lst19:
		txt.insert(END,"\n"+"Bot -->I love me too!")

	elif e.get() in lst20:
		txt.insert(END,"\n"+"Bot -->I Know.")

	elif e.get() in lst21:
		txt.insert(END,"\n"+"Bot -->Look who is saying!")

	elif e.get() in lst22:
		txt.insert(END,"\n"+"Bot -->My name is ZenX")

	elif e.get() in lst23:
		txt.insert(END,"\n"+"Bot -->Why? Ok,let me tell u a joke:-\n       My friend was explaining electricity to me, but I was like,'Watt'?")

	elif e.get() in lst24:
		txt.insert(END,"\n"+"Bot -->Um, Outer Space.")

	elif e.get() in lst25:
		txt.insert(END,"\n"+"Bot -->HAHAHAHA! You just made my day with that joke!")

	else:
		txt.insert(END,"\n"+"Bot -->Sorry I didn't get it.")


	e.delete(0,END)


#To stop the window from resizing.
root.resizable(width=FALSE, height=FALSE)

txt = Text(root)
txt.grid(row = 0,column = 0, columnspan = 2)

e = Entry(root,width = 100)
send = Button(root,text = "Send",command=send).grid(row = 1,column = 1)
e.grid(row = 1,column = 0)

root.mainloop()
