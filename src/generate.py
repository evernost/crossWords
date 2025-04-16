# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# SETTINGS
# -----------------------------------------------------------------------------
GRID_SIZE_H = 12
GRID_SIZE_V = 10




valid_lines = []






with open("./src/wordListFrench.txt", "r", encoding = "utf-8") as file :
  for line in file:
    line = line.strip()
    # Check if all characters are ASCII (code points less than 128)
    if all(ord(char) < 128 for char in line):
      valid_lines.append(line)

# Output for testing
print(valid_lines)


