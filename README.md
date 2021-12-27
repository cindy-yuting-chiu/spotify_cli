# Spotify Command-line Tool
## Intro
This project is based on the documentation from Spotify Web API. https://developer.spotify.com/documentation/web-api/ The tool is built using Python and click framework. 
The end goal is to create a simple command line tool that user can retrieve the most popular 10 songs for a particular artist listed in Spotify. 
The user can specify the artist name, and the tool will call the Spotify Web API searching query. After finding the most relevant artist, the user can input the country that they're interested in. The default is set to United States. The tool will retrieve the top 10 popular tracks in Spotify with track name and the song duration. The tool will also retrieve the popularity of the artist, including how many users follow the artist on Spotify and the popularity score Spotify calculates (out of 100). 
The user can use the help function under the click framework to see what options they have. 
For demo video of using this command line tool, please refer to this link: https://youtu.be/mgYXYFGlYQ4
