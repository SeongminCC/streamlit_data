# Insurance Premium Calculator ver 2.0

# import
import pandas as pd
import numpy as np

# data 불러오기
insurance_premium=pd.read_excel('./data/insurance_premium.xlsx')

# 보험료 계산기
# insurance_premium : data
# disease_risk_li : 입력된 질병별 위험도
# age : 나이
# insurance_premium_max : 이용자가 원하는 보험료
def calculator(insurance_premium, disease_risk_li, age, insurance_premium_max):
    
    # 나이대에 따른 최대 보험료, 최소 보험료 뽑아오기
    if 19<age<30:
        price_min = np.array(insurance_premium.iloc[:,2])
        price_max = np.array(insurance_premium.iloc[:,3])
        price_gap = np.floor(np.array(price_max-price_min))
        
    else :
        price_min = np.array(insurance_premium.iloc[:,4])
        price_max = np.array(insurance_premium.iloc[:,5])
        price_gap = np.floor(np.array(price_max-price_min))
        
    # 기본 특약 계산을 위한 변수
    disease_risk_avg = sum(disease_risk_li)/4
    
    # 특약별 보험료 계산을 위한 리스트
    value_min=[0,0,0,0,0]; value_rate=[0,0,0,0,0]; sum_value_rate=[0,0,0,0,0]
    
    # return을 위한 리스트들
    list_1=['기본특약','심혈관질환','대사질환','뇌혈관질환','간질환']
    list_2=[0,0,0,0,0]; list_3=[0,0,0,0,0]
    
    # 보험료 계산에 필요한 값들 정리
    for i in range(5):
        value_min[i]=sum(price_min*np.array(insurance_premium.iloc[:,i+6]))
    sum_value_min=sum(value_min)
    
    value_rate[0]=price_gap*np.array(insurance_premium['기본특약'])*disease_risk_avg
    for i in range(1,5):
        value_rate[i]=price_gap*np.array(insurance_premium.iloc[:,i+6])*disease_risk_li[i-1]
    sum_value_rate_disease=np.sum(np.array(value_rate[1:5]))
    
    # 보험료 출력을 위한 보험료 재조정과 출력
    if sum_value_min>insurance_premium_max:
        list_3[0]=sum_value_min
        
        return list_1, list_2, list_3

    elif sum_value_min+sum_value_rate_disease>insurance_premium_max:

        # 보험료 예산에 맞춘 보험료 재조정
        for i in range(1,5):
            sum_value_rate[i]=np.floor(sum(value_rate[i]*((insurance_premium_max-sum_value_min)/sum_value_rate_disease)))

        # 보험료 출력을 위한 list 저장
        list_2[0]=value_min[0]; list_3[0]=value_min[0]+int(sum(value_rate[0]))
        for i in range(1,5):
            list_2[i]=int(value_min[i]+sum_value_rate[i]); list_3[i]=value_min[i]+int(sum(value_rate[i]))

        return list_1, list_2, list_3
        
    else:

        # 보험료 예산에 맞춘 보험료 재조정
        tmp=sum_value_min+sum_value_rate_disease
        tmp_value1_rate=value_rate[0]*(insurance_premium_max-tmp)/sum(value_rate[0])

        # 보험료 출력을 위한 list 저장
        if value_min[0]+sum(tmp_value1_rate)>=value_min[0]+sum(value_rate[0]):
            list_2[0]=value_min[0]+sum(value_rate[0]); list_3[0]=value_min[0]+sum(value_rate[0])
        else:
            list_2[0]=value_min[0]+sum(tmp_value1_rate); list_3[0]=value_min[0]+sum(value_rate[0])
        for i in range(1,5):
            list_2[i]=value_min[i]+int(sum(value_rate[i])); list_3[i]=value_min[i]+int(sum(value_rate[i]))
            
        return list_1, list_2, list_3 