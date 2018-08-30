import sys
import pygame
from collections import defaultdict

class EventEngine():
    def __init__(self):
        #pygame.init()
        self.__handlers =defaultdict(list)
        self.__genneralHandlers =[]

    def register(self,type_,handler):
        handerlist = self.__handlers[type_]
        if handler not in handerlist:
            handerlist.append(handler)


    def unrigister(self,type_,handler):
        handerlist = self.__handlers[type_]
        if handler in handerlist:
            handerlist.remove(handler)
        if handler not in handerlist:
            del self.__handlers[type_]

    def registerGeneralHandler(self,handler):
        if handler not in self.__genneralHandlers:
            self.__genneralHandlers.append(handler)

    def unregisterGeneralHandler(self,handler):
        if handler in self.__genneralHandlers:
            self.__genneralHandlers.remove(handler)


    def put(self,event):
        pygame.event.post(event)

    def process(self,event):
        for e in event:

            if e.type in self.__handlers:
                [handler(e) for handler in self.__handlers[e.type]]

            if self.__genneralHandlers:
                [handler(e) for handler in self.__genneralHandlers]

    def run(self):
        while True:
            event =pygame.event.get()
            self.process(event)



def test(event):
    print 'hello,world',event

def settimer(event):
    print 'print meg per second',event

if __name__=='__main__':
    ee =EventEngine()
    e1 = pygame.event.Event(pygame.USEREVENT+1,{})
    ee.register(e1.type,test)
    ee.put(e1)

    # e2 = pygame.event.Event(pygame.USEREVENT+2,{})
    # ee.register(e2.type,settimer)
    # ee.put(e2)

    pygame.time.set_timer(pygame.USEREVENT+2,200)
    ee.register(pygame.USEREVENT+2,settimer)

    ee.run()

