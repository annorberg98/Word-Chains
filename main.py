'''
Grafens utrymmeskomplexitet: O(V + E)
Bygga grafen tidskomplexitet: O(N^2)
Sökning tidskomplexitet: O(V+E)
'''

import networkx as nx
import matplotlib.pyplot as plt

def load_data(fileName):
    '''
    Läser in data från fil.
    '''

    file = open(fileName,"r")
    words = file.readlines()
    file.close()

    words = [x[:-1] for x in words]

    return words


def load_test_file(filename):
    '''
    Läser in testfil
    '''
    with open(filename, "r") as f:
        words = f.readline().replace("\n", "").split(" ")
    
    return words

def check_letters(word1, word2):
    '''
    Controll if each of the 4 last letters in word 1 exists in word 2
    and then add the matched letter to matches-list.
    '''
    if(word1 == word2):
        return False
    matches = [] 
    letters = word1[-4:]
    for char in letters:
        if char in word2:
            matches.append(char)
    
    result =  all(elem in matches for elem in letters)
    matches = None
    return result

def draw_graph(words):
    '''
    O(N^2)
    
    '''
    G = nx.DiGraph()
    G.add_nodes_from(words)

    for word1 in words:
        for word2 in words: 
            if(check_letters(word1, word2)):
                    G.add_edge(word1, word2)
    nx.draw_networkx(G)
    return G

if __name__ == "__main__":
    datafile = "words-250/words-250-data.txt"   
    testfile = "words-250/words-250-test.txt"

    words = load_data(datafile)
    G = draw_graph(words)   

    with open(testfile) as f:
        for line in f.readlines():
            start = line[0:5]
            goal = line[6:11]

            try:
                result = nx.shortest_path(G, source=start, target=goal)
                print(len(result)-1)
            except nx.NodeNotFound:
                print("-1")
            except nx.exception.NetworkXNoPath:
                print("-1")

        plt.show()
    
