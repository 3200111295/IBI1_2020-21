def complement(sequence):
#create a dictionary   
    complement = {
      "A":"T","T":"A","G":"C","C":"G",
      "a":"T","t":"A","c":"G","g":"C",
    }
#get the complement of DNA    
    l = list(sequence)
    l = [complement[b] for b in l]
    s = ''.join(l)
    return s
#reverse the DNA sequence
def reverse(sequence):
    return complement(sequence)[::-1]
sequence="agcTgAcG"
print reverse(sequence)
             
