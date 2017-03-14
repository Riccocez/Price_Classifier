
# coding: utf-8

# In[1]:

from nltk.corpus import stopwords


# In[2]:

class label(object):
    
    def __init__(self):
        
        self.set_categories()
        self.set_stop_wrds()
       
        pass
    
    
    
    def set_categories(self):
        
        home = {'home','improvement'}
        web = {'web', 'designer', 'website','personal website'}
        salon = {'hair','nail','salon','fashion'}
        media = {'media','news','telecom'}
        school = {'school','education','college','university','library'}
        health = {'medical','hospital','health','clinic', 'doctor'}
        gov = {'government','public services','community','non-profit'}
        public = {'landmark','historical place','geographical','public place','neighborhood','city'}
        fitness = {'fitness','beauty','spa','care','trainer','club','performance','coach'}
        travel = {'traveling','tour','agency','travel','hotel','lodging','attractions','things to do'}
        event = {'event','planning','planner','agency'}
        sport = {'sports','arena','stadium','entertainment'}
        ent = {'arts','recreation','movie','museum','art','gallery','artist'}
        comp = {'local', 'business','professional', 'service','organization',
                'consulting','company','business','professional','finance','religious'}
        shop = {'shopping','retail','grocery','store','book','electronics','jewelry','watches','apparel'}
        bar = {'bar','food','beverage','cafe','nightlife','restaurant','café'}
        others = {'pet','automotive'}
        
        self.categ_set = home | web | salon | media | school | health | gov | public | fitness | travel | event | sport | ent | comp | shop | bar | others
        self.categ = [home, web, salon, media, school, health, gov, public, fitness, travel, event,
                         sport, ent, comp,shop,bar,others]

        return
    
    def set_stop_wrds(self):
        
        stop_du = set(stopwords.words('dutch'))
        stop_en = set(stopwords.words('english'))
        stop_others = {'www','com','visit','rotterdam','netherlands','pagina','welkom','vind','emails', 'based',
                         'kart', 'based', 'info', 'follow','specialist','email','online','airport'}

        self.stops = stop_du | stop_en | stop_others
        
        return
        


# In[ ]:



