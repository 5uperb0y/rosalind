def calculate_gc_content(dna_sequence):
    """Calculate the GC content of a DNA sequence as a percentage."""
    if not dna_sequence:
        return 0.0
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

def test_gc_content():
    assert calculate_gc_content("GCGC") == 100.0
    assert calculate_gc_content("ATGC") == 50.0
    assert calculate_gc_content("") == 0.0
