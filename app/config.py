class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = ('NEWS_API_KEY')
    SOURCES_BASE_API_URL = "https://newsapi.org/v2/sources?apiKey={}"
    EVERYTHING_BASE_API_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    TOP_HEADLINES_BASE_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    BUSINESS_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}"

    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    #to debug mode
    DEBUG = True