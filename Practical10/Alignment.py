seq_human = "MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
seq_mouse = "MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
seq_random = "GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP"
edit_distance = 0

letter = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X']
mark = [[4  , -1 , -2 , -2 , 0  , -1 , -1 , 0  , -2 , -1 , -1 , -1 , -1 , -2 , -1 , 1  , 0  , -3 , -2 , 0  , -2 , -1 , 0 ],
        [-1 , 5  , 0  , -2 , -3 , 1  , 0  , -2 , 0  , -3 , -2 , 2  , -1 , -3 , -2 , -1 , -1 , -3 , -2 , -3 , -1 , 0  , -1],
        [-2 , 0  , 6  , 1  , -3 , 0  , 0  , 0  , 1  , -3 , -3 , 0  , -2 , -3 , -2 , 1  , 0  , -4 , -2 , -3 , 3  , 0  , -1],
        [-2 , -2 , 1  , 6  , -3 , 0  , 2  , -1 , -1 , -3 , -4 , -1 , -3 , -3 , -1 , 0  , -1 , -4 , -3 , -3 , 4  , 1  , -1],
        [0  , -3 , -3 , -3 , 9  , -3 , -4 , -3 , -3 , -1 , -1 , -3 , -1 , -2 , -3 , -1 , -1 , -2 , -2 , -1 , -3 , -3 , -2],
        [-1 , 1  , 0  , 0  , -3 , 5  , 2  , -2 , 0  , -3 , -2 , 1  , 0  , -3 , -1 , 0  , -1 , -2 , -1 , -2 , 0  , 3  , -1],
        [-1 , 0  , 0  , 2  , -4 , 2  , 5  , -2 , 0  , -3 , -3 , 1  , -2 , -3 , -1 , 0  , -1 , -3 , -2 , -2 , 1  , 4  , -1],
        [0  , -2 , 0  , -1 , -3 , -2 , -2 , 6  , -2 , -4 , -4 , -2 , -3 , -3 , -2 , 0  , -2 , -2 , -3 , -3 , -1 , -2 , -1],
        [-2 , 0  , 1  , -1 , -3 , 0  , 0  , -2 , 8  , -3 , -3 , -1 , -2 , -1 , -2 , -1 , -2 , -2 , 2  , -3 , 0  , 0  , -1],
        [-1 , -3 , -3 , -3 , -1 , -3 , -3 , -4 , -3 , 4  , 2  , -3 , 1  , 0  , -3 , -2 , -1 , -3 , -1 , 3  , -3 , -3 , -1],
        [-1 , -2 , -3 , -4 , -1 , -2 , -3 , -4 , -3 , 2  , 4  , -2 , 2  , 0  , -3 , -2 , -1 , -2 , -1 , 1  , -4 , -3 , -1],
        [-1 , 2  , 0  , -1 , -3 , 1  , 1  , -2 , -1 , -3 , -2 , 5  , -1 , -3 , -1 , 0  , -1 , -3 , -2 , -2 , 0  , 1  , -1],
        [-1 , -1 , -2 , -3 , -1 , 0  , -2 , -3 , -2 , 1  , 2  , -1 , 5  , 0  , -2 , -1 , -1 , -1 , -1 , 1  , -3 , -1 , -1],
        [-2 , -3 , -3 , -3 , -2 , -3 , -3 , -3 , -1 , 0  , 0  , -3 , 0  , 6  , -4 , -2 , -2 , 1  , 3  , -1 , -3 , -3 , -1],
        [-1 , -2 , -2 , -1 , -3 , -1 , -1 , -2 , -2 , -3 , -3 , -1 , -2 , -4 , 7  , -1 , -1 , -4 , -3 , -2 , -2 , -1 , -2],
        [1  , -1 , 1  , 0  , -1 , 0  , 0  , 0  , -1 , -2 , -2 , 0  , -1 , -2 , -1 , 4  , 1  , -3 , -2 , -2 , 0  , 0  , 0 ],
        [0  , -1 , 0  , -1 , -1 , -1 , -1 , -2 , -2 , -1 , -1 , -1 , -1 , -2 , -1 , 1  , 5  , -2 , -2 , 0  , -1 , -1 , 0 ],
        [-3 , -3 , -4 , -4 , -2 , -2 , -3 , -2 , -2 , -3 , -2 , -3 , -1 , 1  , -4 , -3 , -2 , 11 , 2  , -3 , -4 , -3 , -2],
        [-2 , -2 , -2 , -3 , -2 , -1 , -2 , -3 , 2  , -1 , -1 , -2 , -1 , 3  , -3 , -2 , -2 , 2  , 7  , -1 , -3 , -2 , -1],
        [0  , -3 , -3 , -3 , -1 , -2 , -2 , -3 , -3 , 3  , 1  , -2 , 1  , -1 , -2 , -2 , 0  , -3 , -1 , 4  , -3 , -2 , -1],
        [-2 , -1 , 3  , 4  , -3 , 0  , 1  , -1 , 0  , -3 , -4 , 0  , -3 , -3 , -2 , 0  , -1 , -4 , -3 , -3 , 4  , 1  , -1],
        [-1 , 0  , 0  , 1  , -3 , 3  , 4  , -2 , 0  , -3 , -3 , 1  , -1 , -3 , -1 , 0  , -1 , -3 , -2 , -2 , 1  , 4  , -1],
        [0  , -1 , -1 , -1 , -2 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -2 , 0  , 0  , -2 , -1 , -1 , -1 , -1 , -1]]

edit_distance = 0
for i in range(len(seq_human)):
    score = mark[letter.index(seq_human[i])][letter.index(seq_mouse[i])]
    edit_distance += score
print('human and mouse')
print(edit_distance)

edit_distance = 0
for i in range(len(seq_human)):
    score = mark[letter.index(seq_human[i])][letter.index(seq_random[i])]
    edit_distance += score
print('human and random')
print(edit_distance)

edit_distance = 0
for i in range(len(seq_mouse)):
    score = mark[letter.index(seq_mouse[i])][letter.index(seq_random[i])]
    edit_distance += score
print('mouse and random')
print(edit_distance)


# comparing the edit distance, we can find that the distance between human and mouse is 1490, while human to random and 
# mouse to random are -351 and -348 respectively, so human and mouse are very similar comparing to the random.
# meanwhile, i also write a local alignment program, the results between human and mouse are like below:
'''
MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGS-AGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY
MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAG-YPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY
{22: 'Q => P', 51: 'T => A', 53: 'G => A', 84: '- => A', 87: 'S => -', 97: 'S => G', 101: 'S => P', 117: 'N => S', 124: 'T => A', 262: 'T => P'}

MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSA-GSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY
MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAG-YPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY
{22: 'Q => P', 51: 'T => A', 53: 'G => A', 85: '- => A', 87: 'S => -', 97: 'S => G', 101: 'S => P', 117: 'N => S', 124: 'T => A', 262: 'T => P'}
'''