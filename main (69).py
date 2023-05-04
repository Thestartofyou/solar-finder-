import pytzwhere
import ephem

# Create a pytzwhere object to look up time zones
tz = pytzwhere.tzwhere()

# Define a list of latitudes and longitudes for locations to check
locations = [
    (40.7128, -74.0060), # New York City
    (34.0522, -118.2437), # Los Angeles
    (41.8781, -87.6298), # Chicago
    (29.7604, -95.3698), # Houston
    (47.6062, -122.3321), # Seattle
    (37.7749, -122.4194), # San Francisco
]

# Loop over each location and calculate sunrise and sunset times
for lat, lon in locations:
    # Look up the time zone for this location
    tz_name = tz.tzNameAt(lat, lon)
    tz_obj = pytz.timezone(tz_name)

    # Create an ephem observer for this location
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.elevation = 0
    obs.pressure = 0
    obs.horizon = '-0:34'

    # Calculate sunrise and sunset times for today
    sunrise = tz_obj.localize(ephem.localtime(obs.next_rising(ephem.Sun())).replace(tzinfo=None))
    sunset = tz_obj.localize(ephem.localtime(obs.next_setting(ephem.Sun())).replace(tzinfo=None))

    # Print the results for this location
    print(f"Location: {lat}, {lon}")
    print(f"Time zone: {tz_name}")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")
