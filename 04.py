import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    API_KEY = os.getenv('API_KEY')
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}'

    res = requests.get(url=url).json()
    results = res['results']

    try:
        return results[0]['id']
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
