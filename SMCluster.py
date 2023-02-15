# preprocessing, EDA
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

    
    
class smC_v2:
    def __init__(self):
        self.original_data = pd.read_csv('./data/nationalhealth_2010to2021.csv')
        self._20_data = pd.read_csv('./data/national_only20_health_2010to2021.csv')
        self.meta_data = pd.read_excel('./data/meta_data20.xlsx')

        #타겟 + 피쳐 str list
        self.col_li = self.original_data.columns.to_list() 
        #타겟 str list
        self.target_li = self.original_data.columns[-13:].to_list()
        #피쳐 str list
        self.fea_li = self.original_data.columns[:-13].to_list()

        #범주형 자료 str list
        self.temp = list(self.meta_data["variable"][self.meta_data['data type']== "category"].values)
        self.cat_li = [i for i in self.temp if i in self.col_li if i != 'HE_hepaB']
        
        #연속형 자료 str list
        self.temp = list(self.meta_data["variable"][self.meta_data['data type']== "numeric"].values)
        self.expcept = ['ID', 'ID_fam', 'LW_mt_a1', 'age', 'year']

        self.num_li = [i for i in self.temp if i in self.col_li]

    
    def trans(self, val): #변수 번역 input str
        return self.meta_data["variable description"][self.meta_data["variable"] == val].values[0]
    
    def disc(self, val): #설문 내역
            return self.meta_data["option description"][self.meta_data["variable"] == val].values[0]

    def change2None(self, data): #통계량을 측정할 때, 결측값 복원
        for i in data.columns:
            data.replace({i:{-1:None}},inplace = True)
            data.replace({i:{-2:None}},inplace = True)
        return data
    
    
    
    

    
    
