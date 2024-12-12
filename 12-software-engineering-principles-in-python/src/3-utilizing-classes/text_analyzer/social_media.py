from .document import Document

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return self._filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return self._filter_word_counts(self.word_counts, first_char='@')
    
    def _filter_word_counts(self, word_counts, first_char):
        return word_counts
    
    def plot_counts(self, plot_type):
        if plot_type == 'hashtag_counts':
            print(self.hashtag_counts)
        elif plot_type == 'mention_counts':
            print(self.mention_counts)
        