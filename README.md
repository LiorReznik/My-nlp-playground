# basic-language-models
in this repo I have implemented to language models:
1. basic n-gram model.
2. deep learning char based language model(in progress).

language models is the beting heart of NLP. these models is the base of evrey NLP task that you can imagnie.

basicly language modeling gives us the ability to predict the most likley word to follow a given sequence of words(the propability), it gives the coputer the ability to "understand" the contex of a word(s) in a given sentence or phrase.

in this repo I have tried to implement two language models:
1. classic n-gram model:
  so what is n-gram? well, n-gram is just a sequence of n words,
  given n-words, we want to predict with the model the most likley   to follow word. we can repeat this process and get human-    understandable text! 
  
  so!how does it work?
    1. we take a huge corpus of data and spliting it into n-grams.
    2. then we are taking each n-gram and loking at the following         word in the original text.
    3. we count the condistinoal propability of that word with the        chain rule.
    fortunately  becuse of our good freind markov and his  
    assamptions we don't need the text that was before the gram!.
    you can see the code for this at the " " file along with  
    working   example.
  
  this is a good approach but: it's time consuming an sparse(out-
  of-vocabulary words)!
