def percentualize_dataframe(df):
    df = df.copy()
    votes_columns = ['Koalicja Obywatelska', 'Trzecia Droga', 'Prawo i Sprawiedliwość', 'Lewica', 'Konfederacja']
    # Dzielenie każdej komórki przez wartość w kolumnie 'Oddane głosy' dla odpowiedniego wiersza
    df[votes_columns] = df[votes_columns].astype(float)

    # Dzielenie wartości przez całkowitą liczbę głosów w danym wierszu
    df[votes_columns] = df[votes_columns].div(df['Oddane głosy'].astype(float), axis=0)

    df['Frekwencja'] = df['Ważnych kart'].div(df['Uprawnieni do głosowania'].astype(float), axis=0)

    df = df.drop(columns=['Uprawnieni do głosowania', 'Ważnych kart', 'Oddane głosy'])
    return df
