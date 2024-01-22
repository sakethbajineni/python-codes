def first_word_in_dictionary_order(sentence):

  words = sentence.lower().split()
  words.sort()
  return words[0]

input_sentence = input("Enter a sentence: ")
result = first_word_in_dictionary_order(input_sentence)
print("The word that comes first in dictionary order:", result)
sente="saketh is the patel"
print(sente.split())
