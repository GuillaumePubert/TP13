class Node :
    def __init__(self,val,left,right):
        self.__val=val
        self.__left=left
        self.__right=right

    def GetVal(self):
        return self.__val
    def GetLeft(self):
        return self.__left
    def GetRight(self):
        return self.__right
    def SetLeft(self,a):
        self.__left=a
    def SetRight(self,a):
        self.__right=a
    def __str__(node):
        return "Node :"+str(node.GetVal())

class BinaryTree:
    def __init__(self,root):
        self.__root=root
    def GetRoot(self):
        return self.__root
    def SetRoot(self,a):
        self.__root=a
    def isRoot(self,node):
        if node==self.__root:
            return True
        else:
            return False

    def size(self,node):
        if node==None:
            return 0
        if node.GetLeft()==None and node.GetRight()==None:
            return 1
        else:
            return 1+ self.size(node.GetLeft()) + self.size(node.GetRight())




    def printValues(self,node):
        if node is None:
            return ""
        else:
            return self.printValues(node.GetLeft()) + self.printValues(node.GetRight()) + " " + str(node.GetVal())
    def sumValues(self,node):
        if node==None:
            return 0
        else:
            return node.GetVal()+self.sumValues(node.GetLeft())+self.sumValues(node.GetRight())

    def numberInternalNodes(self, node):
        if node==None:
            return 0
        if node.GetRight()==None and node.GetLeft()==None:
            return 0
        else:
            return 1+self.numberInternalNodes(node.GetLeft())+self.numberInternalNodes(node.GetRight())

    def height(self, node):
        if node==None:
            return 0
        if node.GetRight()==None and node.GetLeft()==None:
            return 0
        else :
            a=1+self.height(node.GetLeft())
            b=1+self.height(node.GetRight())
            return max(a,b)

    def belongs(self, node, val):
        if node is None:
            return
        else:
            a=False
            if node.GetVal()==val:
                a=True
            if a==False:
                self.belongs(node.GetLeft(),val),self.belongs(node.GetRight(),val)
            else:
                print("True")


    def descendants(self, node, val) :
        if node is None :
            return""
        if node.GetVal()== val :
            print(node.GetRight(),node.GetLeft())
        else :
            self.descendants(node.GetRight(),val)
            self.descendants(node.GetLeft(),val)



n6=Node(6,None,None)
n3=Node(3,None,None)
n18=Node(18,None,None)
n21=Node(21,None,None)
n4=Node(4,n3,None)
n19=Node(19,n18,n21)
n17=Node(17,None,n19)
n5=Node(5,n4,n6)
racine=Node(12,n5,n17)
arbre=BinaryTree(racine)

# print(arbre.size(racine))
# print(arbre.printValues(racine))
# print(arbre.sumValues(racine))
# print(arbre.numberInternalNodes(racine))
# print(arbre.height(racine))
# print(arbre.belongs(racine,18))
print(arbre.descendants(racine,5))
