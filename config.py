#!/usr/bin/env

CHANGE_NAMES = True    # Change to False if you want filenames to remain unchanged.
RAND_RANGE = 999999    # Generate random nos. upto this number


# Make sure values don't appear as keys.
# e.g.
# 'rar': 'zip',
# 'zip': 'rar'
#
# Don't do that.

transformation = {
    'rar': {'to': 'hlp', 'change_name': True},
    'avi': {'to': 'dat', 'change_name': True},
    'wmv': {'to': 'dmp', 'change_name': True},
    'mov': {'to': 'log', 'change_name': True},
    'mpg': {'to': 'prx', 'change_name': True},
    'mp4': {'to': 'data', 'change_name': True},
    'jpg': {'to': 'ini', 'change_name': False},
    'jpeg': {'to': 'dll', 'change_name': False},
    'png': {'to': 'xml', 'change_name': False},
    'gif': {'to': 'xkcd', 'change_name': False}
}


# Generate heroku-like random names
# https://gist.github.com/1266756
adjs = [
    "autumn", "hidden", "bitter", "misty", "silent", "empty", "dry", "dark",
    "summer", "icy", "delicate", "quiet", "white", "cool", "spring", "winter",
    "patient", "twilight", "dawn", "crimson", "wispy", "weathered", "blue",
    "billowing", "broken", "cold", "damp", "falling", "frosty", "green",
    "long", "late", "lingering", "bold", "little", "morning", "muddy", "old",
    "red", "rough", "still", "small", "sparkling", "throbbing", "shy",
    "wandering", "withered", "wild", "black", "young", "holy", "solitary",
    "fragrant", "aged", "snowy", "proud", "floral", "restless", "divine",
    "polished", "ancient", "purple", "lively", "nameless"
  ]

nouns = [
    "waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning",
    "snow", "lake", "sunset", "pine", "shadow", "leaf", "dawn", "glitter",
    "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook",
    "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly",
    "feather", "grass", "haze", "mountain", "night", "pond", "darkness",
    "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder",
    "violet", "water", "wildflower", "wave", "water", "resonance", "sun",
    "wood", "dream", "cherry", "tree", "fog", "frost", "voice", "paper",
    "frog", "smoke", "star"
  ]

system_folder = [
'컴퓨터_%s.{20D04FE0-3AEA-1069-A2D8-08002B30309D}',
'제어판_%s.{21EC2020-3AEA-1069-A2DD-08002B30309D}',
'휴지통_%s.{645FF040-5081-101B-9F08-00AA002F954E}',
'네트워크설정_%s.{208D2C60-3AEA-1069-A2D7-08002B30309D}',
'프린터및팩스_%s.{2227A280-3AEA-1069-A2DE-08002B30309D}',
'인터넷환경_%s.{DB2112AD-0000-0000-0002-000004281965}',
]