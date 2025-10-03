def annotate(garden):
    if not garden: 
        return []
    row_length = len(garden[0])
    for row in garden:
        if len(row) != row_length or any(c not in ' *' for c in row):
            raise ValueError("The board is invalid with current input.")
    rows, cols = len(garden), len(garden[0])
    result = [list(row) for row in garden] 
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for r in range(rows):
        for c in range(cols):
            if garden[r][c] == ' ':
                flower_count = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and garden[nr][nc] == '*':
                        flower_count += 1
                if flower_count > 0:
                    result[r][c] = str(flower_count)
    return [''.join(row) for row in result]     
        
