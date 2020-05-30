# My nlp playground
in this repo I will try to implement some core algorithems and tasks in the filed on NLP.
for now, I have implemented N-gram model.

language models are the beating heart of NLP. these models are the base of every NLP task that you can imagine.

language modeling gives us the ability to predict the most likely word to follow a given sequence of words(the probability), it gives the computer the ability to "understand" the context of a word(s) in a given sentence or phrase.

so what is n-gram? well, an n-gram is just a sequence of n words, given (n-1)words, we want to predict with the model the most likely to follow word. we can repeat this process and get a human-understandable text! 
so!how does it work?
    1. we take a huge corpus of data and splitting it into n-grams.
    2. then we are taking each n-gram and looking at the following word in the original text.
    3. we count the conditional probability of that word with the chain rule.
    fortunately, because of our good friend Markov and his  
    assumptions we don't need the text that was before the gram!.
    you can see the code for this at the " " file along with  
    a working   example.
  
  this is a good approach but: it's time-consuming and sparse(out-
  of-vocabulary words)!

