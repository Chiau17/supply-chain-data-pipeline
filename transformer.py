import pandas as pd

pd.set_option('display.max_column',None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',None)

def transform_data():

    df = pd.read_json('raw_test.json')

    print(df.head())
    # print(df.head())
    # df.to_csv('output_test.csv',index=False)

    expensive_coins = df[df['current_price']>10]

    ttl = (df['market_cap']> 100000000).sum()

    avg = (df['current_price'] > 100).mean()

    df['symbol'] = df['symbol'].str.upper()

    df['price_tier'] = df['current_price'].apply(lambda x: 'Expensive' if x>50 else 'Affordable')

    def multiple(row):
        return row['current_price'] *0.8

    df.apply(multiple,axis = 1)

    df['current_price'] = df['current_price']*0.8

    group_df = df.groupby('price_tier')

    summary_df = df.groupby('price_tier').agg({
        'current_price':'sum',
        'market_cap':'sum',
    })

    # print(summary_df.head())

    current_sum = df['current_price'].agg(['mean','max'])

    # print(current_sum.head())


    extra_df1 = pd.DataFrame({
        'id': ['bitcoin','ethereum','tether','ripple'],
        'sum': [23,100,75,23]
    })

    combined_df = df.merge(extra_df1,on='id',how='left')

    extra_df2 = pd.DataFrame({
        'id': ['binancecoin','ethereum','cindy','karim'],
        'sum': [78,12,32,20]
    })

    final_df = pd.concat([extra_df1,extra_df2],ignore_index=True)

    return final_df









