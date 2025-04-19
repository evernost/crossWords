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
import unicodedata



# =============================================================================
# EXTERNAL LIBS
# =============================================================================
class CrosswordGen :
  """
  Class definition for the crossword generator.
  """
  
  def __init__(self, gridSizeH, gridSizeV, language = "fr") :
    self.language = language
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
      print("        Supported dictionaries:")
      print("        - French  ('fr')")
      print("        - English ('en')")
      print("        - German  ('de')")
      quit()

    self.wordSizeMin = 100; self.wordSizeMax = 0
    with open(wordListFile, "r", encoding = "utf-8") as file :
      for line in file :
        
        # TODO: exclude words with hyphen
        # ...

        # Remove trailing '\n'
        line = line.strip()
        
        # Convert letters to their unaccentuated version
        # "NFD" = Normalisation Form Decomposed
        # "Mn" = nonspacing mark
        tmp = "".join(c for c in unicodedata.normalize("NFD", line) if unicodedata.category(c) != "Mn")
        self.wordList.append(tmp)
      
        #if all(ord(char) < 128 for char in line):
        if (len(line) < self.wordSizeMin) :
          self.wordSizeMin = len(line)
        elif (len(line) > self.wordSizeMax) :
          self.wordSizeMax = len(line)

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

    Also, the list of requirements can be left empty (e.g. you only care 
    about words of a given size)
    """

    if (size > self.wordSizeMax) :
      return []
    
    else :
      out = []
      for w in self.wordList :
        valid = True
        
        # TODO: take the max index of all requirements
        # If longer than the size of the word, don't bother.

        # Has the word the right size (if any size constraint)?
        if (((size > -1) and len(w) == size) or (size == -1)) :
          
          # Loop on the requirements 
          for (letter, index) in reqs :
            if (index > len(w)) :
              valid = False
              break
            else :
              if (w[index-1] != letter) :
                valid = False
                break
        else :
          valid = False
        
        # If all tests passed, keep that word.
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
  print(cwg._find([("q", 1), ("u", 2)], size = 4))
  print(cwg._find([], size = 19))
  print(cwg._find([], size = 13))
  print(cwg._find([("n", 5)], size = 12))

