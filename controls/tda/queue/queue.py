from controls.tda.queue.queueOperation import QueueOperation

class Queue():
    def _init_(self, tope):
        self.__queue = QueueOperation(tope)

    def queue(self, data):
        self.__queue.queue(data)

    def dequeue(self):
        return self.__queue.dequeue
    
    def print(self):
        self.__queue.print
    
    def verify(self):
        return self.__queue.verifyTop
    