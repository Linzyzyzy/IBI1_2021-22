import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
n = re.findall('GAATTC',seq)
print(len(n)+1)