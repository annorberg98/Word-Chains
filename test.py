import networkx as nx
import matplotlib.pyplot as plt

#word = ['their', 'moist', 'other', 'blimp', 'limps', 'about', 'there', 'pismo']

fileName = "words-250/words-250-data.txt"

file = open(fileName,"r")
words = file.readlines()
file.close()

words = [x[:-1] for x in words]


G = nx.DiGraph()
G.add_nodes_from(words)

def check(word1, word2):
    matches = []
    letters = word1[-4:]
    for char in letters:
        if char in word2:
            matches.append(char)
    
    result =  all(elem in matches for elem in letters)
    return result

def load_test_file(filename):
    with open(filename, 'r') as f:
        words = f.readline().replace("\n", "").split(" ")
    
    return words

for word1 in words:
    for word2 in words:
        if word1 != word2: 
            if(check(word1, word2)):
                G.add_edge(word1, word2)
nx.draw_networkx(G)
#plt.show()

testfile = 'words-250/words-250-test.txt'

with open(testfile) as f:
    for line in f.readlines():
        start = line[0:5]
        goal = line[6:11]

        try:
            result = nx.shortest_path(G, source=start, target=goal)
            #print(result)
            print(len(result)-1)
        except nx.NodeNotFound:
            print("-1")
        except nx.exception.NetworkXNoPath:
            print("-1")
    


#print(nx.algorithms.dag.dag_longest_path(G))