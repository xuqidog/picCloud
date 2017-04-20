#encoding=utf-8
import matplotlib.pyplot as plt 
from pylab import *
from wordcloud import WordCloud 
import jieba 

text_from_file_with_apath = open('/Users/xuqidong/picCloud/yhpc.txt').read() 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True) 
wl_space_split = " ".join(wordlist_after_jieba) 
backgroud_Image = plt.imread('1024.jpg')
my_wordcloud = WordCloud(font_path='/Users/xuqidong/picCloud/SimHei.ttf',background_color = 'white',mask = backgroud_Image,)
my_wordcloud.generate(wl_space_split) 
plt.imshow(my_wordcloud) 
plt.axis("off") 
plt.show()

