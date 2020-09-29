"""
Instructions
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have a function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
"""
def DNA_strand(dna):
    complementary_strand = ""
    for symbol in dna:
        if symbol == 'A':
            complementary_strand += 'T'
            continue
        if symbol == 'T':
            complementary_strand += 'A'
            continue
        if symbol == 'C':
            complementary_strand += 'G'
            continue
        if symbol == 'G':
            complementary_strand += 'C'
            continue
    return complementary_strand