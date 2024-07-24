# Sets are unordered collections of simple objects. These are used when the existence of an object in a collection is more important than the order or how many times it occurs.
bri = set(['brazil', 'russia', 'india'])

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
bri & bric # OR bri.intersection(bric)
# {'brazil', 'india'}