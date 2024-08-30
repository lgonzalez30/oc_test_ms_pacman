
import google

class Config:
    
    def __init__(self,):
        pass
    
    def _cover_dict(self, dict_data):
  
        try:
            for key in dict_data:
                if isinstance(dict_data[key], google.cloud.firestore_v1.document.DocumentReference):
                    dict_data[key] = dict_data[key].path #.get().to_dict()
            return dict_data
        except Exception as e:
            return dict_data
        
    
    def _cover_dict_data(self, dict_data):
     
        try:
            for key in dict_data:
      
                if isinstance(dict_data[key], google.cloud.firestore_v1.document.DocumentReference):
                    dict_data[key] = dict_data[key].get().to_dict()
            return dict_data
        except Exception as e:
        
            return dict_data