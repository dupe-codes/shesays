"""
Various settings for company reviews

TODO: Automagically import this and all other settings files
into global django settings module
"""

# Labels a user can use to rate a company
SENTIMENT_LABELS = ['positive', 'neutral', 'negative']

SENTIMENT_SCORES = {
    'positive': 100,
    'neutral': 50,
    'negative': 0,
}
