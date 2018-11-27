def distance(strand_a,strand_b):
    
    # sequence length to be the same
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA sequence not the same length!")

    return sum(1 for i in range(len(strand_a)) if strand_a[i] != strand_b[i])
