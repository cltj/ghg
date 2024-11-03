import os
import requests
import timeit
from datetime import datetime, timedelta
import pandas as pd
import io

# ==== Globals ==== #
all_currencies = ["USD", "GBP", "DKK", "EUR", "CHF", "SEK", "NOK", "JPY", "CAD", "AUD", "NZD", "CNY", "INR"]  # Comprehensive list of supported currencies
foreign_currencies = "USD+GBP+DKK+EUR+CHF+SEK"  # Define initial foreign currencies

# Get the list of additional currencies not included in `foreign_currencies`
foreign_currency_set = set(foreign_currencies.split("+"))
additional_currencies = [currency for currency in all_currencies if currency not in foreign_currency_set]

# Combine the original foreign currencies with additional ones
extended_foreign_currencies = foreign_currencies + "+" + "+".join(additional_currencies)
data_format = "csv"  # json and xml is supported at the source, but involves more complexity
locale = "no"  # setting locale to "no" respects the norwegian holidays // verified date: 2024-05-17 // it also sets precedent for the schema fields 
bom = "exclude"  # byte order mark, including bom is discouraged when using utf-8 
rates_time_interval = "B"  # B = Workday // assume this does not include weekends and holidays
BASE_URL = f"https://data.norges-bank.no/api/data/EXR/{rates_time_interval}.{extended_foreign_currencies}.NOK.SP?format={data_format}&"
HEADERS = None
PAYLOAD = {}

def _get(endpoint: str) -> str:
    url = BASE_URL + endpoint
    response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
    if response.status_code >= 400:
        raise Exception(f"HTTP error {response.status_code} when getting data from {url}")
    data = response.content.decode("utf-8")
    print(type(data))
    return data

def _create_pandas_df(data: str) -> pd.DataFrame:
    pd_df = pd.read_csv(filepath_or_buffer=io.StringIO(data), delimiter=';')
    print(pd_df.shape)
    pd_df = pd_df.drop(columns=['TENOR'])  # drop 'TENOR' col, keep 'tenor'
    print(pd_df.head(5))
    return pd_df

def _write(df, endpoint: str):
    try: 
        print(f"Processed {endpoint} - Written (Col:{len(df.columns)}/Rows:{df.count()}) to source/norgesbank/daily_conversion_rates")
        df.to_csv('src/model_generator/outputs/currency_dim.csv', index=False)
        print("CSV file 'currency_dim.csv' created successfully.")
    except Exception as e:
        print(f"An error occurred while processing {endpoint}: {e}")
        raise e     

def main():
    days = datetime.now() - datetime(2014, 1, 1)
    public_holidays = 1218
    n_observations = days.days - public_holidays
    endpoint = f"lastNObservations={n_observations}&locale={locale}&bom={bom}"
    df = _create_pandas_df(_get(endpoint))
    _write(df, endpoint)

start_time_job = timeit.default_timer()
main()
print(f"=== Data ingested in {timeit.default_timer() - start_time_job} seconds ===")
