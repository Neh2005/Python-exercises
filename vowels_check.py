def vowelCounter(text):
  """Count the number of vowels in a text entered as string"""
  vowel = 0
  text=text.casefold()
  for letter in text:
    if letter in "aeiou":
      vowel = vowel + 1
  return vowel

vowelCounter("hello")
vowelCounter("Adios")
