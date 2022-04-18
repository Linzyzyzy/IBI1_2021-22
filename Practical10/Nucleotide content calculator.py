#sequence = input('input a DNA sequence: ').upper()
sequence = 'aactgggattcggACGTTAtgatcgtcgATCATTTTTTTT'.upper()
ratio = {'A':0,'T':0,'C':0,"G":0}
def calculator(sequence):
    allnumber = 0
    for i in sequence:
        ratio[i] += 1
        allnumber += 1
    for i in 'ATCG':
        ratio[i] /= allnumber
calculator(sequence)
print(ratio)