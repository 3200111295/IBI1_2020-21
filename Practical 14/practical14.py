#import some modules
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir("/Users/a1234/Practical 14")

#to get all the element from the file go_obo.xml
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

#create a dictionary which contains all the ids of terms
#define a function to find them
def id_found(terms):
    dict={}
    for term in terms:
        #search all the terms with "is_a", also all the id
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        all_id = term.getElementsByTagName("id")[0].childNodes[0].data
        for id_fa in is_a:
            if id_fa in dict:
                dict[id_fa].append(all_id)
            else:
                dict[id_fa] = [all_id]
    return dict

#define a function which is to search the terms which are related to DNA,RNA or other biomolecules
def related(terms,biomolecule):
    gene = []
    for term in terms:
        defstrs = term.getElementsByTagName("defstr")[0]
        defstr = defstrs.childNodes[0].data
        #find the id which is related to specific molecule
        id_link = term.getElementsByTagName("id")[0].childNodes[0].data
        if not biomolecule.isupper():
            defstr = defstr.lower()
        if biomolecule in defstr:
            gene.append(id_link)
    return set(gene)
        #add "set" to deleted the repeated id

#to get the childnodes
def getnodes(dict,lists):
    allnodes = []
    for i in lists:
        if i in dict:
            a = dict[i]
            allnodes += a
            allnodes += getnodes(dict,a)
    return allnodes

#define a function to calculate all the childnodes
def number(terms,biomolecule):
    dict = id_found(terms)
    b = related(terms,biomolecule)
    #get all chlidnodes
    c = getnodes(dict,b)
    number= len(set(c))
    return number

# the molecules are DNA, RNA, Protein, and Carbohydrate. 
DNA = number(terms,"DNA")
RNA = number(terms,"RNA")
Protein = number(terms,"protein")
Carbohydrate = number(terms,"carbohydrate")

print("The number of childNodes of all DNA-associated terms is:",DNA)
print("The number of childNodes of all RNA-associated terms is:",RNA)
print("The number of childNodes of all protein-associated terms is:",Protein)
print("The number of childNodes of all glycoprotein-associated terms is:",Carbohydrate)


#make a pie chart
labels='DNA', 'RNA', 'Protein', 'Carbohydrate'
sizes=[DNA, RNA, Protein, Carbohydrate]
explode=(0, 0, 0, 0)
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and carbohydrate')
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.show()

