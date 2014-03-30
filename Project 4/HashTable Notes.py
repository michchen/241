# Hashing

a = {}
a["cat"] = "a feline friend"
# key on the left value on the right

a= []

a.append(("cat" , "a feline friend"))
# using a list is not quite as convenient because you have to search through the whole list O(n) and it's a waste of time

# first thing for hash is to determine how many buckets you want

class DictionaryEntry:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
ord #converts into a word into a numerical value

numbuckets = 5
key = "cat"
nums = map(ord, key)
bucketindex = sum(nums)%numbuckets