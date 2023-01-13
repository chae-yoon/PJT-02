import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    API_KEY = os.getenv('API_KEY')
    BASE_URL = 'https://api.themoviedb.org/3/'
    url_search = f'{BASE_URL}search/movie?api_key={API_KEY}&query={title}'
    
    res = requests.get(url=url_search).json()
    results = res['results']

    try:
        movie_id = results[0]['id']
        url_credits = f'{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}'

        res2 = requests.get(url=url_credits).json()
        casts = res2['cast']
        crews = res2['crew']
        movie_credits = {
            'cast': [],
            'crew': [],
        }

        for cast in casts:
            if cast['cast_id'] < 10:
                movie_credits['cast'].append(cast['name'])

        for crew in crews:
            if crew['department'] == 'Directing':
                movie_credits['crew'].append(crew['name'])
        
        return movie_credits

    except:
        return None
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
