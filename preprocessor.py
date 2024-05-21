import pandas as pd

def preprocess(ath,cnt):

    #filtering summer olympics dataset
    ath = ath[ath['Season'] == "Summer"]
    # mering noc with region
    ath = ath.merge(cnt, how='left', on='NOC')
    #remove duplicates
    ath.drop_duplicates(inplace=True)
    #creating seprate coloum for gold, silver and bronze
    df = pd.get_dummies(ath['Medal']).astype(int)
    ath = pd.concat([ath, df], axis=1)

    return ath
