# jellyfin-sonarr-webhooker
A small project to facilitate automatically updating jellyfin libraries with new imports from sonarr / radarr


1) Install the dependencies with `pip install -r requirements.txt`
2) Generate an API key in your jellyfin dashboard
3) Modify `config.conf`
  - `host` this is a string of the destination to host the webapp - example values are "localhost", "0.0.0.0", etc.
  - `port` this is an integer of the port to run the webapp on
  - `jellyfin_url` this is the url to access your jellyfin instance - include the protocol and port number
  - `jellyfin_api_key` fill in your generated jellyfin API key here
4) Run the webapp with `python main.py`
5) Create a webhook connection in Sonarr / Radarr
  - Sonarr - (Assuming the app is hosted on localhost:8085) the url is http://localhost:8085/sonarr
  - Radarr - (Assuming the app is hosted on localhost:8085) the url is http://localhost:8085/radarr
