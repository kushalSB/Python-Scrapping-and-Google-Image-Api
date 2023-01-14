import pandas as pd
import numpy as np


#To search for google images
from google_images_search import GoogleImagesSearch



def generate_random_int(start,stop,row):
    x= np.random.randint(start,stop,(row))
    return x

# Random float generator
def generate_random_float(start,stop,row):
    x= np.random.uniform(start,stop,(row))
    return x

df = pd.read_csv('myntra_products_catalog.csv')
df_result=pd.read_csv('my_data_set.csv')

ROW=12491
print(df.info()) 

# Delete Column
del(df['NumImages'])

# Code to add coloum
df['Stock'] = generate_random_int(0,500,ROW)
print(df.info()) 


# Code to get search specific column data
productNames = np.array(df['ProductName'])

productUrls = [df_result['Url']]




gis = GoogleImagesSearch('AIzaSyAbSg3ejhwgF1kckc34pNdOGci36br8QQc', 'f7e686a667deb497f')

#Method to get url for product name
def imageSearch(product_name):

    _search_params = {
        'q': product_name,
        'num': 1,
        'fileType': 'jpg',
        'safe': 'safeUndefined', ##
        'imgType': 'imgTypeUndefined', ##
        'imgSize': 'imgSizeUndefined', ##
        'imgDominantColor': 'imgDominantColorUndefined', ##
        'imgColorType': 'imgColorTypeUndefined' ##
    }
    gis.search(search_params=_search_params)
    for image in gis.results():
        return image.url

    # return gis.results().url
try:
    for productName in productNames:
        productUrls.append(imageSearch(productName))
except Exception as e:
    print('error: {0} and message: {1}'.format(e.__cause__,e.args))
    recordUrlNum+=len(productUrls)
 
finally:

    df['Url']=pd.Series(productUrls)
    df.fillna(0)

# Saving to csv
df.to_csv('my_data_set.csv', sep=',', encoding='utf-8')

   
