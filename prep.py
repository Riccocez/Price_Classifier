
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd

from Labels import label
import enchant
import nltk
from guess_language import guess_language


# In[2]:

class preprocessing(object):
    
    def __init__(self):
        
        #labels object
        self.lbl= label()
        self.d = enchant.Dict("en_US") 
        pass
    
    def read_data(self):
        """
        * Read all data files
        """
        fb = pd.read_json('data-sample/facebook-rotterdam-20170131.json',lines=True)
        go = pd.read_json('data-sample/google-rotterdam-20170207.json',lines=True)
        fac = pd.read_csv('data-sample/factual-rotterdam-20170207.csv')
        
        return fb,go,fac
    
    def map_fb_loc(self,data,columName,dictName,drop_inst):
        """
        * Map location of facebook into latitude and longitude values
        """
        
        #get location 
        if drop_inst:
            data = data.drop(data.index[drop_inst])
            
        data['longitude'] = [i[dictName][1] for i in data[columName]]
        data['latitude'] = [i[dictName][0] for i in data[columName]]

        
        return data
    
    def dropna(self,data,column_set,how):
        """
        * Drop NAN values from a specific column
        """
        
        data = data.dropna(subset=column_set,how=how)
        data = data.reset_index()
        
        return data
    
    def map_dict(self,data,columnName,dictName):
        """
        * Extract useful values from dictionary
        """
        
        col_set = [data[columnName][i][dictName] for i in range(len(data))]
        
        return col_set
    
    def label_price(self,data):
        """
        * Label price range/level into its corresponding category
        """
        
        data['price'] = np.NaN
        
        for i in range(len(data)):
            if isinstance(data['price_range'][i], str):
                data['price'][i] = data['price_range'][i].count('$')
            elif not np.isnan(data['price_level'][i]):
                data['price'][i] = data['price_level'][i]
            
        return data
    
    def label_category(self,data,columnName):
        """
        * Return a set of labeled data
        """
        
        
        labeled_data = [self.map_label_category(i) for i in data[columnName]]
        
        return labeled_data
    
    def map_label_category(self,category):
        
        """
        * Return label of category based on lexicon
        """
        
        tmp_wrd = nltk.wordpunct_tokenize(category)
        cat_label = np.NaN
    
        for word in tmp_wrd:
            if self.d.check(word):
                unique = 0
            
                for i in range(len(self.lbl.categ)):
                    if word.lower() in self.lbl.categ[i]:
                        if unique != 1:
                            cat_label = i
                            unique = 1
    
        return cat_label  
    
    
    def remove_stop_wds(self,data,columnName):
        """
        * Return key words from columName
        """
    
        reviews = []

        for review in data[columnName]:
            
            review = nltk.wordpunct_tokenize(review)
            text_prosc = [word.lower() for word in review if not word.lower() in self.lbl.stops and word.isalpha()]
            cleaned_text = " ".join(text_prosc)
            reviews.append(cleaned_text)
            
        return reviews
    
    def guess_language(self,data,columnName):
        """
        * Return predicted language of a given columnName
        """
        
        data['language'] = [guess_language(text) for text in data[columnName]]
        
        return data
    


# In[ ]:



