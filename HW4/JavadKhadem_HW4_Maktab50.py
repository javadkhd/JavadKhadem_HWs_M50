print("##############################")
print("############   1   ###########")
print("##############################")

in_str = "The quick brown fox jumps over the lazy dog"

print( ''.join([ i[1] for i in in_str.split() ]) )

#print("##############################")
#print("############   2   ###########")
#print("##############################")

scores = {'Art':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 2},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 3}]}


print("##############################")
print("###########   2.1   ##########")
print("##############################")
dic1 = dict()

for key, value in scores.items() :
    dic1[key] = [d['score'] for d in value]

print(dic1)

print("##############################")
print("###########   2.3   ##########")
print("##############################")

names = set()
list_dic = []
for key, value in scores.items() :
    dic33 = dict()
    for d in value :
        name = d['first_name'] + ' ' + d['last_name']
        names.add(name)
        dic33.update( { name : {key: d['score'] } } )
    list_dic.append(dic33)
    
    #print(dic2)
    #print('*****')
#print('$$$$$$$')

dic3 = dict()
for name in names:
    asghar_list = [ i[name] for i in list_dic if name in i.keys() ]
    asghar_dic = dict()
    for j in asghar_list:
        asghar_dic.update(j)
    del asghar_list
    dic3[name] = asghar_dic
    
print(dic3)



print("##############################")
print("###########   2.2   ##########")
print("##############################")
dic2 = dict()
for i in dic3:
    dic2[i] = list(dic3[i].values())
    
print(dic2)






