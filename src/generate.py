# -*- coding: utf-8 -*-
# =============================================================================
# Project         : crossWords
# Module name     : -
# File name       : generate.py
# File type       : Python script (Python 3.10 or greater)
# Purpose         : crossword generator main script
# Author          : QuBi (nitrogenium@outlook.fr)
# Creation date   : April 17, 2025
# -----------------------------------------------------------------------------
# Best viewed with space indentation (2 spaces)
# =============================================================================

# =============================================================================
# DESCRIPTION
# =============================================================================
# TODO



# =============================================================================
# EXTERNAL LIBS
# =============================================================================
import argparse



# =============================================================================
# EXTERNAL LIBS
# =============================================================================
class CrosswordGen :
  """
  Class definition for the crossword generator.
  """
  
  def __init__(self, gridSizeH, gridSizeV, language = "fr") :
    self.language = "fr"
    self.gridSizeH = gridSizeH
    self.gridSizeV = gridSizeV
    self.wordList = []
    self.wordSizeMin = 0
    self.wordSizeMax = 0

    self._loadWordList()



  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._loadWordList()
  # ---------------------------------------------------------------------------
  def _loadWordList(self) :
    """
    TODO
    """

    if (self.language == "fr") :
      wordListFile = "./src/wordListFrench.txt"
    else :
      print("[ERROR] This language is not supported.")
      quit()


    self.wordSizeMin = 100; self.wordSizeMax = 0
    with open(wordListFile, "r", encoding = "utf-8") as file :
      for line in file :
        
        # Remove '\n'
        line = line.strip()
        
        # Keep unaccentuated chars only
        if all(ord(char) < 128 for char in line):
          if (len(line) < self.wordSizeMin) :
            self.wordSizeMin = len(line)
          elif (len(line) > self.wordSizeMax) :
            self.wordSizeMax = len(line)

          self.wordList.append(line)

    print(f"[INFO] {len(self.wordList)} words loaded.")
    print(f"       Word size range: {self.wordSizeMin} to {self.wordSizeMax}")

 

  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._find()
  # ---------------------------------------------------------------------------
  def _find(self, reqs = [], size = -1) :
    """
    Finds the subset of words in the dictionary satisfying a list of requirements.
    Returns a list with all the solutions found.
    
    The requirements must be provided as a list of tuples.
    Each tuple contains an index (1-indexed) and the letter that must appear
    at this index.
    EXAMPLE: reqs = [('q', 1), ('t', 4)] would return the list ['quit']

    A word length criteria can be added too (argument 'size') 
    If omitted, words of any size with matching requirements will be returned.
    """

    if (size > self.wordSizeMax) :
      return []
    
    else :
      out = []
      for w in self.wordList :
        valid = True
        for (letter, index) in reqs :
          if (index > len(w)) :
            valid = False
            break
          else :
            if (w[index-1] != letter) :
              valid = False
              break
        
        if valid :
          out.append(w)

      return out



# -----------------------------------------------------------------------------
# MAIN (UNIT TESTS)
# -----------------------------------------------------------------------------
if (__name__ == '__main__') :

  # PARSE ARGUMENTS
  parser = argparse.ArgumentParser(description = "Crosswords generator.")
  parser.add_argument(
    "--grid_size_h",
    type = int,
    default = 12,
    help = "Grid horizontal size (default: 12)"
  )

  parser.add_argument(
    "--grid_size_v",
    type = int,
    default = 10,
    help = "Grid vertical size (default: 10)"
  )

  args = parser.parse_args()
  
  
  cwg = CrosswordGen(args.grid_size_h, args.grid_size_v, language = "fr")
  
  print(cwg._find([("q", 1), ("u", 4)]))

  