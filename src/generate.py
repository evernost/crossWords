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
import random
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
    self.grid = [[]]

    self.history = []

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
  # [PRIVATE] METHOD: CrosswordGen._test()
  # ---------------------------------------------------------------------------
  def _test(self, reqs = [], size = -1) :
    """
    Checks whether there are any words in the dictionary that satisfy a given 
    set of requirements.
    Returns True if at least one word meets the criteria, False otherwise.

    A requirement is a constraint on the letter at a specific position in a word.

    Requirements must be provided as a list of tuples.
    Each tuple contains an index (1-based) and the letter that must appear at that index.

    EXAMPLE: reqs = [('q', 1), ('t', 4)] would return the list ['quit']

    A word length criteria can be added too (argument 'size') 
    If omitted, words of any size with matching requirements will be returned.

    Also, the list of requirements can be left empty (e.g. you only care 
    about words of a given size)

    NOTE: if you want the actual list of words instead of only a test, use 
    '_list()' instead.
    """

    # Size req exceeds the longest known word
    if (size > self.wordSizeMax) :
      return False
    
    else :
      
      # Find the highest requirement
      highestIndex = max((index for (letter, index) in reqs), default = 1)
      
      
      
      for w in self.wordList :
        valid = True

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



  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._list()
  # ---------------------------------------------------------------------------
  def _list(self, reqs = [], size = -1) :
    """
    Lists the words in the dictionary that satisfy a given set of requirements.
    Returns a list of all matching words.

    A requirement is a constraint on the letter at a specific position in a word.

    Requirements must be provided as a list of tuples.
    Each tuple contains an index (1-based) and the letter that must appear at that index.

    EXAMPLE: reqs = [('q', 1), ('t', 4)] would return the list ['quit']

    A word length criteria can be added too (argument 'size') 
    If omitted, words of any size with matching requirements will be returned.

    Also, the list of requirements can be left empty (e.g. you only care 
    about words of a given size)

    NOTE: if you don't want to list the words but rather check if there
    are solutions, use '_test()' instead (more efficient)
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



  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._pickRow()
  # ---------------------------------------------------------------------------
  def _pickRow(self) :
    """
    Returns a random row number in the grid (between 1 and gridSizeV)
    """

    return random.randint(1, self.gridSizeV)



  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._pickColumn()
  # ---------------------------------------------------------------------------
  def _pickColumn(self) :
    """
    Returns a random column number in the grid (between 1 and gridSizeH)
    """

    return random.randint(1, self.gridSizeH)



  # ---------------------------------------------------------------------------
  # [PRIVATE] METHOD: CrosswordGen._solve()
  # ---------------------------------------------------------------------------
  def _solve(self) :
    """
    Proposes content for a row/column satisfying the given requirements.

    Multiple strategies:
    - Fill the entire line with 
    """

    pass





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
  print(cwg._list([("q", 1), ("u", 2)], size = 4))
  print(cwg._list([], size = 19))
  print(cwg._list([], size = 13))
  print(cwg._list([("n", 5)], size = 12))
  print(cwg._list([("l", 3), ("b", 11)], size = 13))

