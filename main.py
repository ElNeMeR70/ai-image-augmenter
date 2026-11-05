"""Data Augmentation Pipeline"""

def horizontal_flip_2d(matrix):
    return [row[::-1] for row in matrix]

if __name__ == "__main__":
    print("[RUN] Image Augmentation Pipeline...")
    mat = [[1, 2], [3, 4]]
    flipped = horizontal_flip_2d(mat)
    print(f"[OK] Flipped Matrix: {flipped}")
