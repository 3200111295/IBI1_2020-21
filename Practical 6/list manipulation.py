#import two lists
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#create a empty list
average_exon_length=[]
# calculate average exon length for every gene
for i in range(len(gene_lengths)):
    w = gene_lengths[i]/exon_counts[i]
    average_exon_length.append(w)
print(sorted(average_exon_length))
#start to draw a boxplot
import matplotlib.pyplot as plt
#input the data
data = [51,1142,42,216,25,650,32533,57,1,523]
plt.boxplot(x = data)
#set the length of y-axis
plt.ylim(0,2000)
plt.show()

