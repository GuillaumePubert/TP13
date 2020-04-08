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

class BinaryTree:
    def __init__(self,root):
        self.__root=root
    def GetRoot(self):
        return self.__root
    def SetRoot(self,a):
        self.__root=a

racine=Node(12,5,17)
arbre=BinaryTree(racine)
n5=Node(racine.GetLeft(),4,6)
n4=Node(n5.GetLeft(),3,None)
n3=Node(n4.GetLeft(),None,None)
n17=Node(racine.GetRight(),None,19)
n19=Node(n17.GetRight(),18,21)
n18=Node(n19.GetLeft(),None,None)
n21=Node(n18.GetRight(),None,None)



