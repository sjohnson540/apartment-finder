import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2800

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["eby", "nby"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "adams_point": [
        [37.80789, -122.25000],
        [37.81589, -122.26081]
    ],
    "piedmont": [
        [37.82240, -122.24768],
        [37.83237, -122.25386]
    ],
    "rockridge": [
        [37.83826, -122.24073],
        [37.84680, -122.25944]
    ],
    "berkeley": [
        [37.86226, -122.25043],
        [37.86781, -122.26502]
    ],
    "north_berkeley": [
        [37.86425, -122.26330],
        [37.87655, -122.28974]
    ],
    "temescal": [
        [37.829362, -122.264142],
        [37.83997, -122.251353]
    ],
    "sausalito": [
        [37.819955, -122.522964],
        [37.866587, -122.470093]
    ],
    "mill_valley": [
        [37.868485, -122.567253],
        [37.921857, -122.497902]
    ],
    "montclair": [
        [37.818727, -122.226279],
        [37.844359,-122.185564]
    ],
    "trestle_glen": [
        [37.804227, -122.242679],
	[37.814027, -122.221779]
    ],
    "emeryville": [
        [37.826895, -122.31547],
        [37.849926, -122.276123]
    ],
    "albany": [
        [37.881355, -122.327856],
        [37.898925, -122.28198]
    ],
    "el_cerrito": [ [37.897825, -122.323581], [37.938224,-122.28108] ],
    "point_richmond": [ [37.908187, -122.401583], [37.932624,-122.371882] ],
    "richmond_view": [ [37.904513, -122.352617], [37.91645, -122.332823] ],
    "richmond_annex": [ [37.897825, -122.317796], [37.919255,-122.30418] ],
    "richmond_north": [ [37.950015, -122.383479], [37.96761,-122.35146] ],
    "richmond_east": [ [37.931224, -122.326783], [37.954147, -122.302294] ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["berkeley north", "berkeley", "rockridge", "adams point",
                 "piedmont", "temescal", "sausalito", "mill valley",
                 "montclair", "trestle glen", "glen view",
                 "trestle glen/glen view", "emeryville", "albany", "el cerrito",
                 "point richmond", "richmond view", "richmond annex", "north richmond",
                 "east richmond", "east richmond heights"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur_bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758],
    "fremont_bart": [37.5574675,-121.9788225,17]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
