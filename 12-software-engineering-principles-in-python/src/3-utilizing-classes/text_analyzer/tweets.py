from .social_media import SocialMedia

# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = self._filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)
    
    def _filter_lines(self, text, first_chars):
        return text
