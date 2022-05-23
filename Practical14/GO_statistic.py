from xml.dom.minidom import parse 
import xml.dom.minidom
import matplotlib.pyplot as plt

def recursion(term,path):
    sons = storedic[term]
    for son in sons:
        if childdic[son] == {}:
            path.append(son)
            for i in path:
                childdic[i][son] = 0
            recursion(son,path)
            del path[-1]
        else:
            for i in path:
                childdic[i].update(childdic[son])

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
total_number = 0
storedic = {}
childdic = {}
path = []
translationlist = []
sumlist = []
sumlist_tran = []

for term in terms:
    total_number += 1
    id_ = term.getElementsByTagName('id')[0].childNodes[0].data
    storedic[id_] = []
    childdic[id_] = {}

for term in terms:
    name = term.getElementsByTagName('id')[0].childNodes[0].data
    fathers = term.getElementsByTagName('is_a')
    for father in fathers:
        storedic[father.childNodes[0].data].append(name)
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data.lower():
        translationlist.append(name)

for key in storedic.keys():
    path = [key]
    recursion(key, path)
    sumlist.append(len(childdic[key].keys()))
    if key in translationlist:
        sumlist_tran.append(len(childdic[key].keys()))

print("Total number:")
print(total_number)
print("Average childnode number of all GO terms: ")
print(sum(sumlist)/len(sumlist))
print("Average childnode number of terms associated with ‘translation’: ")
print(sum(sumlist_tran)/len(sumlist_tran))

plt.subplot(1,2,1)
plt.boxplot(sumlist)
plt.title('childnode number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.subplot(1,2,2)
plt.boxplot(sumlist_tran)
plt.title('childnode number of terms associated with ‘translation’')
plt.xlabel("associated with ‘translation’")
plt.ylabel("Number")
plt.show()