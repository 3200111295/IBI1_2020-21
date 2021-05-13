import re
f1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file=open('unknown_function.fa','w')

#create a dictionary
dictionary={}
for i in f1:
        if re.search('>',i):
            key=i
            dictionary[key]=''
        else:
            i = i.strip()
            j=dictionary[key]
            dictionary[key]=j + i
            
#find unknow function DNA and extract them
a = ''
for key in dictionary.keys():
    if re.search('unknown function',key):
        output = re.findall(r'^>([^ ]+)_',key)
        output = output[0]
        a = a + ('>' + output + '     ' + str(len(dictionary[key])) + '\n' + dictionary[key] + '\n')

#output in unknown_function.fa
f1.close()
file.write(a)
file.close()
file2 = open('unknown_function.fa','r')
print(file2.read())
