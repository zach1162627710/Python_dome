import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = pd.read_csv("D:/tmdb-5000-movie-dataset/tmdb_5000_credits.csv")
movies = pd.read_csv("D:/tmdb-5000-movie-dataset/tmdb_5000_movies.csv")

complete = pd.concat([credits,movies],axis = 1)
#complete.info()

movies = complete[['original_title','crew','release_date','genres',
                  'keywords','production_companies','production_countries',
                  'revenue','budget']]

movies['profit'] = movies['revenue'] - movies['budget']

null_date = movies['release_date'].isnull()
location = movies.loc[null_date]
print(location)
movies.loc[4553, 'release_date']='2014-06-01'

# 4.3 数据类型转换（将genres的字符串类型转为字典）
movies['genres'] = movies['genres'].apply(json.loads)
#对movies的genres apply JSON的loads()函数
# 自定义函数解码json数据
def jdecode(column):
    z = []
    for i in column:
        z.append(i['name'])
    return ' '.join(z)

movies['genres'] = movies['genres'].apply(jdecode)
movies.head()

# 4.4 将genres 列表中所包含的类型存入genres_list中

genres_list = set()
#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

for i in movies['genres'].str.split(' '):  #对genres中每一个用‘ ’切片
    genres_list = set().union(i,genres_list) #将i和genres_list进行合并
    genres_list = list(genres_list)  #再将genres_list变成list类型

genres_list.remove('')
#genres_list   #此时genres_list中的内容为无序不重复类型
movies['release_date'] = pd.to_datetime(movies['release_date']).dt.year

columns = {'release_date':'year'}
movies.rename(columns=columns,inplace=True)#将columns赋值给真正的columns
#print(movies['year'].apply(int).head())#展示出year的前5个

for genre in genres_list:
    movies[genre] = movies['genres'].str.contains(genre).apply(lambda x:1 if x else 0)
# movies[genre]应该就是在movies的文件里，按照列属性创建genre（list类型）中每一个列表元素的 一列
# movies['genres'].str.contains(genre)应该是lamdba的x
# if x is true，return 1；else return 0
#print(movies.head())

# 从头到尾按照genres_list进行分组，
# 即将genres_list中每一个元素形成一列,year是index，
# 分组得到1910 - 2021每一个题材对应每年的数目
genre_year = movies.loc[:,genres_list]
genre_year.index=movies['year']
genres = genre_year.groupby('year').sum()
#print(genres.head())

#先将genres的sum和求出，再按倒序进行排列，因为scending=False，所以倒序
genresSum = genres.sum(axis=0).sort_values(ascending=False)

#解决中文显示问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

from pylab import rcParams
params = {'legend.fontsize':12,
         'legend.handlelength':10}
rcParams.update(params)


plt.figure(figsize=(13,8))
plt.plot(genres)#genres是一个dataframe，也就是year和sum的dataframe
plt.xticks(range(1910,2021,5))
plt.legend(genres)  #画图例

plt.title('电影类型随时间的变化趋势',fontsize=15)
plt.xlabel('年份',fontsize=15)
plt.ylabel('数量（部）',fontsize=15)

plt.show()

# 5.6 电影类型随时间的变化趋势（前5名）
# 数列转至
tmp = genres.T
tmp = tmp.loc[:,2005].sort_values(ascending=False)
new_columns = tmp.index[:5]
new_columns

tmp_movies = genres[new_columns]
tmp_movies.tail()

from pylab import rcParams
params = {'legend.fontsize':12,
         'legend.handlelength':10}

rcParams.update(params)

plt.figure(figsize=(10,4))
plt.plot(tmp_movies)

plt.xticks(range(1910,2021,10))
plt.legend(new_columns)
plt.title('1-5名电影类型随时间的变化趋势',fontsize=15)
plt.xlabel('年份',fontsize=15)
plt.ylabel('数量（部）',fontsize=15)
plt.show()


fig = plt.figure(figsize=(10,7))
y = genresSum.sort_values(ascending=True)
rects = y.plot(kind='barh',label='genres')
plt.yticks(np.arange(len(y)),y.index,fontsize=15)
plt.rc('font',family='SimHei',size=15) # 中文编码
plt.title('电影类型的数量图')
plt.xlabel('电影数量（部）',fontsize=15)
plt.ylabel('电影类型',fontsize=15)

for i in range(len(y)):
    plt.text(50,i,'%s'%(y[i]),fontsize=15,color='black')

plt.show()









