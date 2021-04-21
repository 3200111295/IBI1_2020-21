#import the three protein sequences
seq_human = "MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq_mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq_random = "WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL"

#calcultate the percentage identity 
def per(seq1,seq2):
    distance = 0
    #set initial distance as zero
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            distance += 1
            #add a score 1 if amino acids are different
    per=str(distance/len(seq1)*100)+'%'
    return per
print(per(seq_human,seq_mouse))
print(per(seq_human,seq_random))
print(per(seq_mouse,seq_random))
    


from Bio.Align import substitution_matrices
from Bio import pairwise2
#import BLOSUM62 from Biopython
Blosum62 = substitution_matrices.load("BLOSUM62")
#use pairwise2 and BLOSUM62 matrix to get alignement score
human_mouse = pairwise2.align.globalds(seq_human,seq_mouse,Blosum62,-10,-0.5)
human_random =pairwise2.align.globalds(seq_human,seq_random,Blosum62,-10,-0.5)
mouse_random =pairwise2.align.globalds(seq_mouse,seq_random,Blosum62,-10,-0.5)
print(human_mouse)
print(human_random)
print(mouse_random)


