import pandas as pd

movies = pd.read_csv("ml-100k/ml-100k/u.item", sep='|',encoding="latin-1",header=None)
print(movies.head())
movies.columns = ['movie_id','title','release_date','video_release_date','IMDb_URL','unknown', 'Action', 'Adventure', 'Animation', 'Children’s', 'Comedy',
                  'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
                  'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
