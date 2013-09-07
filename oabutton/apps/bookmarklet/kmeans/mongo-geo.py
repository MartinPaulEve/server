"""
This script computes the kmeans cluster using pure python. 

It's slow, but will work.
"""

from pymongo import MongoClient
from kmeansExample import Point
from kmeansExample import kmeans
import os

uri = os.environ['MONGOLAB_URI']
MONGO_CLIENT = MongoClient(uri)
db = MONGO_CLIENT.heroku_app16748047

points = []
for obj in db.events.find():
    try:
        if obj['coords'].has_key('lat') and obj['coords'].has_key('lng'):
            lat, lng = obj['coords']['lat'], obj['coords']['lng'] 
            points.append(Point([float(lat), float(lng)]))
    except:
        # Skip any bad data for now
        pass


# When do we say the optimization has 'converged' and stop updating clusters
opt_cutoff = 0.01

# Cluster those data!
clusters = kmeans(points, 5, opt_cutoff)

# Print our clusters
for i, c in enumerate(clusters):
    print "%d in cluster %d\n\tCentroid -- %r" % (len(c.points), i, c.calculateCentroid())
    #for p in c.points:
    #    print " Cluster: ", i, "\t Point :", p

