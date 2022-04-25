import random, string

class Codec:
    
    def __init__(self):
        self.urlsmapped = {}
        self.invertedmap = {}

    def get_Code(self, longUrl: str) -> str:
        return ''.join(random.choice(string.hexdigits) for i in range(6))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        cript = ''
        
        if longUrl not in self.urlsmapped:
            cript = self.get_Code(longUrl)
            while cript in self.invertedmap:
                cript = self.get_Code(longUrl)
            self.urlsmapped[longUrl] = cript
            self.invertedmap[cript] = longUrl
        else:
            cript = self.urlsmapped[longUrl]
        
        return "http://tinyurl.com/" + cript
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split('http://tinyurl.com/')[1]
        
        return self.invertedmap[code]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))