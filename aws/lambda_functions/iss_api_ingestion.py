import requests

def download_satellite_data(norad_id: int = 25544, units: str = "miles", is_tle:bool = False) -> dict:
    '''_summary_

    Parameters
    ----------
    norad_id : int, optional
        _description_, by default 25544. This is the NORAD ID for the ISS.

    units : str, optional
        _description_,
         by default "miles". Can alternativly be 'kilometers'.

    is_tle : bool, optional
        _description_,
        by default False. TLE data is used for plotting the orbit.
        When this parameter is False we instead return positioning data (lat, long, altitude, etc..)
    '''

    # If we want to return positioning data
    if not is_tle:
        # Get position data from API
        api_url = f'https://api.wheretheiss.at/v1/satellites/{norad_id}?units={units}&?timestamp'
        iss_data = requests.get(api_url).json()
        satellite_data_type = 'position'

    # If we want to return orbital data
    elif is_tle:
        # Get tle data from API
        api_url_tle = f'https://api.wheretheiss.at/v1/satellites/{norad_id}/tles'
        iss_data = requests.get(api_url).json()
        satellite_data_type = 'tle'
        
    print(iss_data)
    return iss_data