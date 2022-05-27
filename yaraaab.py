import networkx as nx
import matplotlib.pyplot as plt
# import pydot
# # from networkx.drawing.nx_pydot import graphviz_layout
# from tkinter import *
# from tkinter.ttk import *
# from PIL import Image, ImageTk
# from automata.fa.dfa import DFA
import random
numbers = "0123456789"
operators = "+-*/"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


with open("Output4.txt", "r") as a_file:
    file_contents = a_file.read()
    array_of_actions = file_contents.splitlines()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
def evenchecker(number):
    if number%2 ==0:
        return True
    else:
        return False

def IdentifierChecker(word):
    if word[0] not in letters:
        return False
    for i in word:
        if((i not in letters) and (i not in numbers)):
            return False
    return True

def operatorchecker(word):
    if len(word) > 1:
        return False
    if word[0] not in operators:
        return False
    return True

def numchecker(word):
    if (word.count(".") > 1):
        return False
    if((word[0]==".") or (word[len(word)-1]==".")):
        return False
    for i in word:
        if((i not in numbers) and i!="."):
            return False
    return True

def expressionchecker(sentence):
    splited_sentence=sentence.split()
    if  evenchecker(len(splited_sentence)):
        return "Not accepted"
    for i in range(0, len(splited_sentence), 2):
        if((numchecker(splited_sentence[i])!=True) and(IdentifierChecker(splited_sentence[i])!=True)):
            return "Not accepted"
    for i in range(1, len(splited_sentence), 2):
        if(operatorchecker(splited_sentence[i])!=True):
            return "Not accepted"
    return "Accepted"

def tokenlister(sentence):
    #if expressionchecker(sentence)=="Not accepted":
     #   return "Not a valid expression"
    mylist=[]
    splited_sentence = sentence.split()
    for i in splited_sentence:
        if(IdentifierChecker(i)):
            mylist.append("ID")
        elif(numchecker(i)):
            mylist.append("Number")
        elif(operatorchecker(i)):
            mylist.append("Operator")
        else:
            mylist.append("Unknown_token")
    return mylist

def tokenlister2(sentence):
    return sentence.split()

def Matchedremover(list):
    for i in list:
        if i =='Matched':
            list.remove('Matched')

def Get_parent_children(string):
    x = string.split("->")
    parent = x[0]
    y = x[1]
    children = y.split()
    return parent, children

def Get_All_parent_children(stacktablelist):
    Matchedremover(stacktablelist)
    parent_childrenlist=[]
    for i in stacktablelist:
        parent_childrenlist.append(Get_parent_children(i))
    return parent_childrenlist

def parent_children_orderd_nodes(parent_childrenlist):
    #print(parent_childrenlist)
    parent_childrenlist_copy=parent_childrenlist.copy()
    children=[]
    parents=[]
    nodessortedbyparentchild1 = [parent_childrenlist_copy[0][0]]
    for i in parent_childrenlist_copy:
        parents.append(i[0])
        for j in i[1]:
            children.append(j)
    nodes=children.copy()
    nodes.insert(0, parent_childrenlist_copy[0][0])
    for i in parent_childrenlist_copy[0][1]:

        nodessortedbyparentchild1.append(i)
    #print(nodessortedbyparentchild1)
    i = 1
    while i < len(nodessortedbyparentchild1):
        for j in range(1, len(parent_childrenlist_copy)):
            if nodessortedbyparentchild1[i] == parent_childrenlist_copy[j][0]:
                nodessortedbyparentchild1.extend(parent_childrenlist_copy[j][1])
                parent_childrenlist_copy.pop(j)
                break
            # newtest.pop(i)
        i = i + 1
    return nodessortedbyparentchild1

def Parse_Tree_Drawer(stacktablelist):
    positiondict={}
    parent_childrenlist=Get_All_parent_children(stacktablelist)
    print(parent_childrenlist)
    nodessortedbyparentchild1=parent_children_orderd_nodes(Get_All_parent_children(stacktablelist))
    G = nx.DiGraph()
    dict = {}
    sizelist = []
    for i in range(0, len(nodessortedbyparentchild1)):
        bool = True
        for j in range(0, len(parent_childrenlist)):
            if nodessortedbyparentchild1[i] == parent_childrenlist[j][0]:
                bool = False
                # nodessortedbyparentchild1.extend(newtest22222[j][1])
                # newtest.pop(j)
                sizelist.append(len(parent_childrenlist[j][1]))
                parent_childrenlist.pop(j)
                break
        if bool:
            sizelist.append(0)
    #print(sizelist)
    print(nodessortedbyparentchild1)
    for i in range(0, len(nodessortedbyparentchild1)):
        positiondict[i] = (15-i,38-i)
    for i in range(0, len(nodessortedbyparentchild1)):
        dict[i] = nodessortedbyparentchild1[i]
        G.add_node(i)
    secondcounter = 1
    #print(dict)
    for i in range(0, len(nodessortedbyparentchild1)):
        if sizelist[i] == 0:
            # print("Zero")
            pass
        for j in range(0, sizelist[i]):
            #print(str(i) + ": " + str(secondcounter))
            G.add_edge(i, secondcounter)
            secondcounter += 1
    # pos = nx.nx_agraph.graphviz_layout(G)
    # pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    # # pos = graphviz_layout(G, prog='dot')
    pos = hierarchy_pos(G, 0)
    #pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    nx.draw(G, labels=dict,node_size=1200,pos=pos)
    plt.show()


test = array_of_actions

Parse_Tree_Drawer(test)