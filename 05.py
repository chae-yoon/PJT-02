import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    API_KEY = os.getenv('API_KEY')
    BASE_URL = 'https://api.themoviedb.org/3/'
    url_search = f'{BASE_URL}search/movie?api_key={API_KEY}&query={title}'
    
    res = requests.get(url=url_search).json()
    results = res['results']
    
    try:
        movie_id = results[0]['id']
        url_recommend = f'{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}&language=ko-KR'
        res2 = requests.get(url=url_recommend).json()
        recommend_results = res2['results']
        recommend_movies = []

        for result in recommend_results:
            recommend_movies.append(result['title'])

        return recommend_movies
    
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
