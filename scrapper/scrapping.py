import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

df=pd.read_csv('my_data_set.csv')

productNames = np.array(df['ProductName'])
i=0
numOfRecords=0
urls1=[]
urls2=[]
urls3=[]
try:
    urlDf=pd.read_csv('urls.csv')
    

    urlsNp=np.array(urlDf['Urls'])

    numOfRecords=len(urlsNp)
    urls=urlsNp.tolist()
except:
    print('hola')
    
finally:
    try:
        for productName in productNames:
            i=i+1
            print(i)
            if i <= numOfRecords:
                continue
            
            api='https://www.google.com/search?q={{%s}}&tbm=isch'
            # print(api%(productName))
            try:
                r=requests.get(api%(productName))

                soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())

    # image=soup.img
                images=[]
                for image in soup.find_all('img'):
                    images.append(image.get('src'))
                if len(images)==1:
                    urls1.append(images[0])
                    urls2.append("Image not found")
                    urls3.append("Image not found")
                elif len(images)==2:
                    urls1.append(images[0])
                    urls2.append(images[1])
                    urls3.append("Image not found")
                elif len(images)>2:
                    urls1.append(images[0])
                    urls2.append(images[1])
                    urls2.append(images[2])

                else:
                    urls1.append("Image not found")
                    urls2.append("Image not found")
                    urls3.append("Image not found")
               
            except:
                urls1.append("Image not found")
                urls2.append("Image not found")
                urls3.append("Image not found")
                continue
        df['Url_new_1']=pd.Series(urls1)
        df['Url_new_2']=pd.Series(urls2)
        df['Url_new_3']=pd.Series(urls3)
        df.to_csv('my_data_set.csv', sep=',', encoding='utf-8')
    except Exception as e:
        print("{0} ..{1}...{2}....{3}....{4}".format(e,e.__traceback__,e.with_traceback,e.__cause__,e.__annotations__))
        # print(urls)
        df_new=pd.DataFrame(urls1,columns=['Urls1'])
        df_new=pd.DataFrame(urls2,columns=['Urls2'])
        df_new=pd.DataFrame(urls3,columns=['Urls3'])
        df_new.to_csv("urls.csv")

# for links in soup.find_all('a'):
#     print(links.get('href'))


# output= r.json()
# print(r.text)
# print(image)