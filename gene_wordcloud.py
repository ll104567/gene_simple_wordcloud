import sys
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#### must set chinese ttf
ttf='./simsun.ttf'

usage = """
    usage:
            python {} filename [output_name]
            [output_name] : defalut x.jpg

""".format(sys.argv[0])

if len(sys.argv) == 3:
    filename = sys.argv[1]
    outputname = sys.argv[2]
elif len(sys.argv) == 2:
    filename = sys.argv[1]
    outputname = 'x.jpg'
else:
    print(usage)
    exit(1)

a = pd.read_csv(filename,sep='[ \t,:"./，。]+',header=None,engine='python')
a.fillna('',inplace=True)
wc = WordCloud(width=800,repeat=True,height=600,font_path=ttf).generate(a.to_string(index=None,header=None))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.savefig(outputname)
print('ok~ output filename:{}'.format(outputname))


