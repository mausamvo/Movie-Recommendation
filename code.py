import csv

movies = {}
users = {}
genres = {}

def take_f(elem):
    return elem[0]

class Genre:
  def __init__(self, name):
    self.name = name
    self.ratings = []
    self.avg = 0
    #movie objects in the genre
    self.movies = []

  def set_rating(self,r):
    self.ratings.append(r)

  def update_avg(self):
    self.avg = sum(self.ratings)/len(self.ratings)

  def add_movie(self, m):
    self.movies.append(m)

class Movie:
  def __init__(self, index, title, genres):
    self.i = index
    self.title = title
    self.genres = genres
    self.ratings = []
    self.avg = 0

  def set_rating(self,r):
    self.ratings.append(r)

  def update_avg(self):
    if len(self.ratings)==0:
      True
    else:
      self.avg = sum(self.ratings)/len(self.ratings)

class User:
  def __init__(self, id, ratings):
    self.id = id
    self.ratings = ratings
    self.genres = {}
    self.avgs = {}
    self.pref = {}
    self.rec = []

  def set_rating(self,r):
    self.ratings.append(r)

  def set_g_rating(self, g, r):
    if g not in self.genres:
      self.genres[g] = [r]
    else:
      self.genres[g].append(r)
    
  def compute_avgs(self):
    for g in self.genres:
      self.avgs[g] = sum(self.genres[g])/len(self.genres[g])

  def compute_pref(self,genres):
      for g in self.avgs:
        self.pref[g] = self.avgs[g]/genres[g].avg



def set_movies(filename):
  #movies.csv
  with open(filename) as f:
    
    r = csv.reader(f)
    next(r)
    for row in r:
      li = row[2].rsplit("|")  
      movie = Movie(row[0],row[1],li)
      for g in li:
        if g not in genres:
          gen = Genre(g)
          gen.add_movie(movie)
          genres[g] = gen
        else:
          genres[g].add_movie(movie)
      movies[row[0]] = movie

def set_users(filename):
  #ratings.csv
  with open(filename) as f:
    r = csv.reader(f)
    next(r)
    for row in r:
      #add rating to movie
      # print(float(str(row[2])))
      movies[row[1]].set_rating(float(str(row[2])))
      #add rating to users genre rating
      gs = movies[row[1]].genres
      user = User(row[0],[float(str(row[2]))])

      for g in gs:
        user.set_g_rating(g, float(str(row[2])))
        genre = Genre(g)
        if g not in genres:
          genres[g] = genre
          genres[g].set_rating(float(str(row[2])))
        else:
          genres[g].set_rating(float(str(row[2])))

      if row[0] not in users:
        users[row[0]] = user
      else:
        users[row[0]].set_rating(float(str(row[2])))

def compute_avgs():
  #call after set_movies and set_users only!
  for i in movies:
    movies[i].update_avg()
  for u in users:
    users[u].compute_avgs()
  for g in genres:
    genres[g].update_avg()
  for ug in users:
    users[ug].compute_pref(genres)

def finalize():
  for user in users:
    for r in users[user].pref:
      #r is the genre
      for movie_id in genres[r].movies:
        # print(movie_id)
        users[user].rec.append((movie_id.title, movie_id.avg*users[user].pref[r]))
      users[user].rec.sort(key=take_f)