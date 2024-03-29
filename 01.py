import os
from dotenv import load_dotenv
import requests

load_dotenv()

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    API_KEY = os.getenv('API_KEY')
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}'

    res = requests.get(url=url).json()
    results = res['results']

    return len(results)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
