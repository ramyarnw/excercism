def find_anagrams(word, candidates):
    final_candidates = []
    word_lower = word.lower()
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue
        if sorted(candidate_lower) == sorted(word_lower):
            final_candidates.append(candidate)
    return final_candidates
    
        
