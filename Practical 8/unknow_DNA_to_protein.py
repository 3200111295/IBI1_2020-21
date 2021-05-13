import re
f2=open('unknown_function.fa','r')
file3=open('unknown_protein.fa','w')

#create the gencode dictionary
gencode = {
    "TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
    "TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
    "TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
    "TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
    "CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
    "CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
    "CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
    "CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
    "ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
    "ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
    "AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
    "AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
    "GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
    "GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
    "GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
    "GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',
}


s = 0
a = ''
amino_acid = ''
for line in f2:
    if line.startswith('>'):
        output = re.findall('>(.+?)\s',line)
        output = output[0]
    else:
        seq = re.findall('...',line)
        #calculate the length of amino acids
        for i in range(len(seq)):
            if gencode[seq[i]] != (r'O|U|X'):
                amino_acid = amino_acid + gencode[seq[i]]
            else:
                break
        length = len(amino_acid)
        a = a + ('>' + output + '     ' + str(length) + '\n' + amino_acid + '\n')
        #to let amino_acid come to the primary number:zero
        amino_acid = ''
    
f2.close()
file3.write(a)
file3.close()
file4 = open('unknown_protein.fa','r')
print(file4.read())
