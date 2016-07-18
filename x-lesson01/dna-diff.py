def diff(dna1, dna2):
    dna1_list = list(dna1)
    dna2_list = list(dna2)
    diff_count = 0
    for i, d in enumerate(dna1_list):
        if not d == dna2_list[i]:
            diff_count += 1
    print diff_count


diff('GAGCCTACTAACGGGAT', 'FFFFFFFFFFFFFFFFF')
diff('GAGCCTACTAACGGGAT', 'TAGCCTACTAACGGGAG')
diff('GAGCCTACTAACGGGAT', 'GAACCTCCCAAGGGATT')