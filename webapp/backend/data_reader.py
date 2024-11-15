from datetime import datetime
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.abspath(os.path.join(base_path, '..', '..', 'data', 'acled_data.csv.csv'))
df = pd.read_csv(data_path)



# Filter the DataFrame for each category
political_militia_data = df[df['inter1'] == 'Political militia'][['latitude', 'longitude']].head(5000).values.tolist()
state_forces_data = df[df['inter1'] == 'State forces'][['latitude', 'longitude']].head(5000).values.tolist()
external_forces_data = df[df['inter1'] == 'External/Other forces'][['latitude', 'longitude']].head(5000).values.tolist()


def number_conflict():
    total_conflicts = len(df)

    conflicts_by_country = df.groupby('country')['event_type'].count().sort_values(ascending=False)

    result_df = pd.DataFrame({'Total Conflicts': [total_conflicts]})
    result_df = pd.concat([result_df, conflicts_by_country], axis=1)

    return result_df

def rank_countries():
    crisis_count_by_country = df.groupby('country')['event_type'].count()

    ranked_countries = crisis_count_by_country.sort_values(ascending=False)
    return crisis_count_by_country,ranked_countries

def rank_by_civilian_gatherings():
    country_event_counts = df.groupby(['country', 'event_type'])['event_type'].count()

    country_event_counts = country_event_counts.unstack()

    country_event_counts = country_event_counts.fillna(0)

    country_event_counts['Total'] = country_event_counts.sum(axis=1)

    ranked_countries_by_total = country_event_counts.sort_values('Total', ascending=False)

    print("\nCountries ranked by total civilian gathering events:")
    print(ranked_countries_by_total)

    ranked_countries_by_protests = country_event_counts.sort_values('Protests', ascending=False)
    print("\nCountries ranked by 'Protests' events:")
    ranked_countries_by_protests
    
    return ranked_countries_by_total,ranked_countries_by_protests

