import os
import cbbd
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


def create_api_instance():
    api_key = os.getenv("CBBD_API_KEY")

    configuration = cbbd.Configuration(
        access_token=api_key
    )

    api_client = cbbd.ApiClient(configuration)

    return cbbd.StatsApi(api_client)


def get_player_stats_df(api_instance, season):
    response = api_instance.get_player_season_stats(season)

    return pd.json_normalize(
        [player.to_dict() for player in response]
    )


def pull_all_seasons(start_year=2010, end_year=2025):

    api_instance = create_api_instance()

    all_dfs = []

    for season in range(start_year, end_year + 1):
        print(f"Pulling {season}...")

        season_df = get_player_stats_df(
            api_instance,
            season
        )

        all_dfs.append(season_df)

    master_df = pd.concat(
        all_dfs,
        ignore_index=True
    )

    return master_df


def save_player_stats(
    filename="college_player_stats_2010_2025.csv"
):
    df = pull_all_seasons()

    df.to_csv(
        filename,
        index=False
    )

    print(f"Saved {len(df)} rows to {filename}")

    return df


def get_player_stats_df(api_instance, season):
    response = api_instance.get_player_season_stats(season)

    return pd.json_normalize(
        [player.to_dict() for player in response]
    )








if __name__ == "__main__":
    save_player_stats()