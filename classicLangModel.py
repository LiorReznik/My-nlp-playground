# -*- coding: utf-8 -*-
"""
Created on Fri May 29 04:57:43 2020
@author: Lior Reznik
"""


class MyLangModel:
    """
    class that builds a basic n-gram languge model
    """
    def __call__(self,seq,n:int=3):
        """
        method to manage all the procedure

        Parameters
        ----------
        seq : list or tupple
            the sentences to fit our model on, NOTE: it should be pre-tokenized.
        n : int, optional
            the amount of grams to consider. The default is 3.

        Returns
        -------
        None.

        """
        self.seq,self.n,self.model = seq,n,{}
        self.data_validation
        for self.sent in self.seq:
            self.gen = self.split_to_grams
            self.calc_probs
        return self
            
    @property    
    def data_validation(self):
        if type(self.seq) != list and type(self.seq) != tuple:
           raise TypeError("the method supports only list or tuple")

           
    @property
    def split_to_grams(self):
        """
        method to build n-grams from the given corpus

        Yields
        ------
        tuple
            n-gram one at a call.

        """
        def pad():
            n = (self.n-1)
            self.sent = [None]*n+self.sent+[None]*n
            
        def generate():
            for i in range(self.n,len(self.sent)+1):
                yield tuple(self.sent[i-self.n:i])

        pad()
        return generate()
    
    @property
    def calc_probs(self):
        """
        method to calculate the propability of word given n previus words
        Returns
        -------
        None.

        """
        def count_frreq():
            """
            function to calculate the freq of ocournces of each combination of
            n-grams in the text.
            this function is a helper function for the prob calculation.
            Returns
            -------
            None.

            """
            for i in self.gen:
                hist,word = i[:-1],i[-1]
                if not self.model.get(hist):
                    self.model[hist] = {word:1}
                elif not  self.model[hist].get(word):
                    self.model[hist][word] = 1
                else:
                    self.model[hist][word] += 1
                    
        def calc_prob():
            """
            calculate propability of word given it previus words
            for example:
                in 2-grams given previus one word.
                in 3-grams given previus two words.

            Returns
            -------
            None.

            """
            for key,val in self.model.items():
                total = sum(val.values())
                for word in  self.model[key]:
                    self.model[key][word] /= total
        
        count_frreq()
        calc_prob()
      
    def predict(self,words:str)->dict:
        """
        method to predict the following word given n-1 previus words

        Parameters
        ----------
        words : str
              the previus words.

        Raises
        ------
        ValueError
             in case of wrong number of words.

        Returns
        -------
        dict
           the predicted words with propability.

        """
        if len(words) != self.n-1:
            raise ValueError("you must enter {} words".format(self.n-1))
        return self.model[tuple(words)]

if __name__ == "__main__":
    #driver
    #let's get some data!
    from nltk.corpus import brown 
    corpus = list(brown.sents())
    #build the model
    model = MyLangModel()(corpus)
    print( model.predict(["jury","said"]))
    