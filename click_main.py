import click
import requests
import pandas as pd 
from tools import get_artist_id, get_top_track, get_artist_popularity

@click.command()
@click.option('--artist', prompt='The artist you want to know'
    , help='Search for the Artist in Spotify')
@click.option('--country', prompt='The country that the songs are popular in', default='US'
    , help='Search for the most popular tracks in that country for that artist')
def cli(artist,country):
    artist_id = get_artist_id(artist)
    top_tracks = get_top_track(artist_id, country).to_string()
    popularity = get_artist_popularity(artist_id).to_string()
    click.secho("{0}'s most popular ten tracks in {1}: ".format(artist, country),  fg='cyan')
    click.secho(top_tracks)
    click.secho("{0}'s popularity on Spotify: ".format(artist),  fg='green')
    click.secho(popularity)
if __name__ == '__main__':
    cli()