import re

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as file:
    seq = file.read()
pattern = re.compile(r'gene:(.*?)gene_.*?Acc:.*?](.*?)>',re.S)
seq_list = pattern.findall(seq)
name = input('input a filename: ')
with open(name,'w')as newfile:
    for i in range(len(seq_list)):
        seq_ = re.sub(r'\n','',seq_list[i][1])
        n = re.findall('GAATTC',seq_)
        if 'GAATTC' in seq_:
            newfile.write(f'>{seq_list[i][0]:10}{len(n)+1}\n{seq_}\n')