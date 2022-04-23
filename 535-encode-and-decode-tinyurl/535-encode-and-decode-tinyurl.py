class Codec:
    def __init__(self):
        self.dict = {}
        self.key = 0
        
    def encode(self, longUrl: str) -> str:
        self.dict["http://tinyurl.com/" + str(self.key)] = longUrl
        encoded = "http://tinyurl.com/" + str(self.key)
        self.key += 1
        
        return encoded
        

    def decode(self, shortUrl: str) -> str:
        decoded = self.dict[shortUrl]
        
        return decoded
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))