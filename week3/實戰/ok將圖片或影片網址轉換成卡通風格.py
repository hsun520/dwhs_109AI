# -*- coding: utf-8 -*-
"""將圖片或影片網址轉換成卡通風格.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1woXkNqIJUi9zntS9fJ1Esq2rcVawVXkf

---

# **下面這儲存格只要執行一次就可以了**


---
"""

import os
repo = "CartoonGan-tensorflow"
!git clone https://github.com/mnicnc404/{repo}.git
os.chdir(os.path.join(repo))
!ls | grep cartoonize.py
from IPython.display import clear_output, display, Image
!git clone https://www.github.com/keras-team/keras-contrib.git \
    && cd keras-contrib \
    && python convert_to_tf_keras.py \
    && USE_TF_KERAS=1 python setup.py install
clear_output()
import tensorflow as tf
tf.__version__

"""---

# 請在這邊把想要使用的網址填入!!!!

---
"""

image_url = 'https://raw.githubusercontent.com/MyFirstSecurity2020/nsjh/main/week3/MAN.png'  #@param {type: "string"}

#範例gif:  https://media.giphy.com/media/o5HKScC1PflLO/giphy.gif
#範例png:  https://n.sinaimg.cn/sinakd10118/341/w650h491/20200821/7923-iyaiihk8459061.png

input_image_dir = "input_images"
output_image_dir = input_image_dir.replace("input_", "output_")

import time
if image_url:
    img_filename = image_url.split("/")[-1]
    name, ext = '.'.join(img_filename.split(".")[:-1]), img_filename.split(".")[-1]
    new_name = '_'.join((name, str(int(time.time()))))
    new_img_filename = '.'.join((new_name, ext))
    image_path = os.path.join(input_image_dir, new_img_filename)
    
    !wget {image_url} \
        && mv {img_filename} {new_img_filename} \
        && mv {new_img_filename} {image_path}
# a trick to show gif in notebook
if ".gif" in new_img_filename:
    png_path = new_img_filename + '.png'
    !cp {image_path} {png_path}
if ".png" in new_img_filename:
    png_path = new_img_filename + '.png'
    !cp {image_path} {png_path}

"""---
# **顯示使用的gif或png**



---
"""

display(Image(png_path))

"""---

# **選擇要轉換的風格種類**

shinkai:新海誠

hayao:宮崎駿

hosoda:細田守

paprika:甜椒花

---
"""

styles = "shinkai" #@param ["shinkai", "hayao", "hosoda", "paprika"]

!python cartoonize.py \
    --styles {styles} \
    --batch_size 1 \
    --comparison_view horizontal
clear_output()

if img_filename:
    if ".gif" in img_filename:
        generated_gif = os.path.join(output_image_dir, "comparison", new_img_filename)
        result_path = generated_gif + '.png'
        !cp {generated_gif} {result_path}
    else:
        result_path = os.path.join(output_image_dir, "comparison", new_img_filename)

"""---

# **顯示成果**



---
"""

display(Image(result_path))