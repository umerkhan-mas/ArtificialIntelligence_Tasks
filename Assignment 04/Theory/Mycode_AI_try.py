import numpy as np
import queue
import time
class Node:
    def __init__(self,Goal,State,parent,depth,Misplaced,Manhattan,childcount):
        self.Goalstate=Goal
        self.State=State
        self.parent=parent
        self.childcount=childcount
        self.depth=depth
        self.Misplaced=Misplaced
        self.Manhattan=Manhattan

    def HeuristicManhattan(self):
        board = self.State.flatten()
        self.Manhattan=sum(abs((val - 1) % 3 - i % 3) + abs((val - 1) // 3 - i // 3) for i, val in enumerate(board) if val)
        return None


    def HeuristicMisplaced(self):
        State=self.State.flatten()
        Initial=np.array([0,1,2,3,4,5,6,7,8])
        mismatch = len(np.where(State != Initial))
        self.Misplaced=mismatch
        return None

    def NCost(self):
        if(self.parent==None):
            return 0
        else:
            return 1

    def FunctionCost(self,NCost):
        return NCost()+self.Misplaced

        return None
    def Movegen(self,Arrayvalue):
        value = Arrayvalue.flatten()
        center = np.where(value==0)
        if center[0] == 0:
            child1 = Node(self.Goalstate, self.swap(0, 1), self, self.depth+1 , None,None,None)
            self.childcount = self.childcount + 1
            child1.HeuristicManhattan()
            child1.HeuristicMisplaced()
            child2 = Node(self.Goalstate,self.swap(0, 3), self,  self.depth+1 , None,None,None)
            child2.HeuristicManhattan()
            child2.HeuristicMisplaced()
            self.childcount=self.childcount+1
            if child1 not in open:
                frontier.put(child1)
                open.append(child1)
            if child2 not in open:
                frontier.put(child2)
                open.append(child2)



            print(child2.State)


        # if center[0]==1:
        #     child1 = frontier.put(Node(self.Goalstate, self.swap(1, 0), self, self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 =frontier.put(Node(self.Goalstate, self.swap(1, 2), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #     child3 = frontier.put(Node(self.Goalstate,self.swap(1, 4), self,self.depth+1 , None,None,None))
        #     child3.HeuristicManhattan()
        #     child3.HeuristicMisplaced()
        #
        # if center[0]==2:
        #     child1 = frontier.put(Node(self.Goalstate,self.swap(2, 1), self, self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate,self.swap(2, 5), self, self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #
        # if center[0]==3:
        #     child1 =frontier.put(Node(self.Goalstate, self.swap(3, 0), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 =frontier.put( Node(self.Goalstate,self.swap(3, 4), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #     child3 = frontier.put(Node(self.Goalstate,swap(3, 6), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child3.HeuristicManhattan()
        #     child3.HeuristicMisplaced()
        #
        # if center[0]==4:
        #     child1 =frontier.put(Node(self.Goalstate, self.swap(4, 1), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate,self.swap(4, 5), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #     child3 = frontier.put(Node(self.Goalstate,self.swap(4, 7), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child3.HeuristicManhattan()
        #     child3.HeuristicMisplaced()
        #     child4 = frontier.put(Node(self.Goalstate,self.swap(4, 3), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child4.HeuristicManhattan()
        #     child4.HeuristicMisplaced()
        #
        # if center[0] == 5:
        #     child1 =frontier.put(Node(self.Goalstate, self.swap(5, 4), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate,self.swap(5, 2), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #     child3 =frontier.put( Node(self.Goalstate,self.swap(5, 2), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child3.HeuristicManhattan()
        #     child3.HeuristicMisplaced()
        #
        # if center[0]==6:
        #     child1 = frontier.put(Node(self.Goalstate,self.swap(6, 3), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate,self.swap(6, 7), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #
        # if center[0]==7:
        #     child1 = frontier.put(Node(self.Goalstate,self.swap(7, 8), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate,self.swap(7, 6), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()
        #     child3 =frontier.put( Node(self.Goalstate,self.swap(7, 4), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child3.HeuristicManhattan()
        #     child3.HeuristicMisplaced()
        #
        # if center[0]==8:
        #     child1 =frontier.put( Node(self.Goalstate,self.swap(8, 7), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child1.HeuristicManhattan()
        #     child1.HeuristicMisplaced()
        #     child2 = frontier.put(Node(self.Goalstate, self.swap(8, 5), self,self.depth+1 , None,None,None))
        #     self.childcount = self.childcount + 1
        #     child2.HeuristicManhattan()
        #     child2.HeuristicMisplaced()

        return None

    def swap(self, index1, index2):
        new=self.State
        new=new.flatten()
        temp =new[index1]
        new[index1] = new[index2]
        new[index2] = temp
        new=np.array(new).reshape(3,3)
        return new
Goalstate = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
Startstate = np.array([[0,1, 2], [6,7, 5], [4, 5, 8]])
root=Node(Goalstate,Startstate,None,0,None,None,0)
open=[]
open.append(root)
print(open)
closed=[]
frontier=queue.Queue()
frontier.put(root)
k=frontier.empty()
# print(k)
while frontier.empty()==False:
    current=frontier.get()
    current.HeuristicMisplaced()
    current.Movegen(current.State)
    # for i in current.childcount:

    # for i in current.childcount:
    #     if current
    #     functionvalue=current.FunctionCost(current.NCost)
    # print(functionvalue)


print("Happy Ending")