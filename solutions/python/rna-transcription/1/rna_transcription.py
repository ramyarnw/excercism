def to_rna(dna_strand):
    transcription_map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    # rna = ''
    # for nucleotide in dna_strand:
    #     rna += transcription_map[nucleotide]
    # return rna
    rna = ''.join(transcription_map[nucleotide] for nucleotide in dna_strand)
    return rna
