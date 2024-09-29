import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://short.url/"

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, long_url):
        if long_url in self.url_map.values():
            return next(short for short, long in self.url_map.items() if long == long_url)
        
        short_code = self.generate_short_code()
        while short_code in self.url_map:
            short_code = self.generate_short_code()
        
        self.url_map[short_code] = long_url
        return self.base_url + short_code

    def get_original_url(self, short_url):
        short_code = short_url.replace(self.base_url, "")
        return self.url_map.get(short_code, "URL not found")

# Example usage
if __name__ == "__main__":
    shortener = URLShortener()

    # Shorten some URLs
    long_url1 = "https://www.example.com/very/long/url/that/needs/shortening"
    long_url2 = "https://another.example.com/with/a/long/path"

    short_url1 = shortener.shorten_url(long_url1)
    short_url2 = shortener.shorten_url(long_url2)

    print(f"Shortened URL 1: {short_url1}")
    print(f"Shortened URL 2: {short_url2}")

    # Retrieve original URLs
    print(f"Original URL 1: {shortener.get_original_url(short_url1)}")
    print(f"Original URL 2: {shortener.get_original_url(short_url2)}")
