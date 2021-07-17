import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd


if __name__ == '__main__':

    season = "2020-21"
    seasonTypeParam = "Regular+Season"

    url = "https://stats.nba.com/stats/leaguedashplayerstats?" \
          "College=" \
          "&Conference=" \
          "&Country=" \
          "&DateFrom=" \
          "&DateTo=" \
          "&Division=" \
          "&DraftPick=" \
          "&DraftYear=" \
          "&GameScope=" \
          "&GameSegment=" \
          "&Height=" \
          "&LastNGames=0" \
          "&LeagueID=00" \
          "&Location=" \
          "&MeasureType" \
          "=Base" \
          "&Month=0" \
          "&OpponentTeamID=0" \
          "&Outcome=" \
          "&PORound=0" \
          "&PaceAdjust=N" \
          "&PerMode=PerGame" \
          "&Period=0" \
          "&PlayerExperience=" \
          "&PlayerPosition=" \
          "&PlusMinus=N" \
          "&Rank=N" \
          "&Season=" + season + \
          "&SeasonSegment=" \
          "&SeasonType=" + seasonTypeParam + \
          "&ShotClockRange=" \
          "&StarterBench=" \
          "&TeamID=0" \
          "&TwoWay=0" \
          "&VsConference=" \
          "&VsDivision=" \
          "&Weight= "

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0"
    headers["Accept"] = "application/json, text/plain, */*"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["x-nba-stats-origin"] = "stats"
    headers["x-nba-stats-token"] = "true"
    headers["Origin"] = "https://www.nba.com"
    headers["DNT"] = "1"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = "https://www.nba.com/"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["If-Modified-Since"] = "Fri, 16 Jul 2021 15:05:03 GMT"
    
    resp = requests.get(url, headers=headers)
    data = resp.json()
    columnHeaders = data['resultSets'][0]['headers']
    stats = data['resultSets'][0]['rowSet']

    df = pd.DataFrame(stats, columns=columnHeaders)
    print(df.to_string())
