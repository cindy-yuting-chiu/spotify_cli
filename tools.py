import requests
import pandas as pd

def get_authentication():
    """
    Get authentication from Spotify API using the credentials we have 
    """
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    cid ="0753888cfb694cf98b9332cd343859a3" 
    secret = "0f47a99eb4bc40eea4f3c9d6b3f1df82"
    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': secret,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)}
    return headers 


def get_artist_id(artistName):
    """
    Return the artist ID by searching for name
    """
    URI = 'https://api.spotify.com/v1/search?query='+ artistName +'&offset=0&limit=1&type=artist'
    response = requests.get(url = URI, headers=get_authentication())
    response = response.json()
    artist_id = response['artists']['items'][0]['id']
    return artist_id

def get_top_track(artist_id, country='US'): 
    """
    Return the top 10 tracks in the country for the specific artist 
    """
    response = requests.get('https://api.spotify.com/v1/' + 'artists/' + artist_id + '/top-tracks?market=' + country
        , headers=get_authentication())
    response = response.json()
    result = {'name':[], "duration_m":[] , "duration_s": []}
    for i in range(len(response['tracks'])):
        result['name'].append(response['tracks'][i]['name'])
        result['duration_m'].append((response['tracks'][i]['duration_ms']/1000)//60)
        result['duration_s'].append(round((response['tracks'][i]['duration_ms']/1000)%60,0))
    df = pd.DataFrame.from_dict(result)
    
    return df


def millify(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


def get_artist_popularity(artist_id): 
    """
    Return the popularity (on scale 1-100) for the artist, and their total follower
    """
    response = requests.get('https://api.spotify.com/v1/artists/'  + artist_id 
        , headers=get_authentication())
    response = response.json()
    #print(response)
    result = {'follower':[millify(response['followers']['total'])] , "popularity": [response['popularity']]}
    #print(result)
    df = pd.DataFrame(result)
    return df