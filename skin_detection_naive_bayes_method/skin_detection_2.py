import cv2
from collections import Counter
import ast

import os

import xlsxwriter    

import pandas as pd


org_img_dir = 'skin_detection_naive_bayes_method/images'
mask_img_dir = 'skin_detection_naive_bayes_method/masks'
trainer_data = 'skin_detection_naive_bayes_method/train_data.xlsx'

main_file = []

book = xlsxwriter.Workbook(trainer_data)     
sheet = book.add_worksheet()

sheet.write(0, 0, 'b')    
sheet.write(0, 1, 'g')
sheet.write(0, 2, 'r')
sheet.write(0, 3, 'is_skin')

k = 1
for mask_name in os.listdir(mask_img_dir):
    mask_dir = os.path.join(mask_img_dir, mask_name)
    mask = cv2.imread(mask_dir)

    org_img_name = mask_name.replace('bmp','jpg')
    org_img_dir_s = os.path.join(org_img_dir, org_img_name)

    org_img = cv2.imread(org_img_dir_s)

    m_height, m_width, m_depth = mask.shape
    for i in range(0, m_height):
        for j in range(0, m_width):
            b,g,r = mask[i, j]
            # print(b,g,r)
            o_b,o_g,o_r = org_img[i, j]
            if b > 250 and g > 250 and r > 250:
                sheet.write(k, 0, o_b)    
                sheet.write(k, 1, o_g)
                sheet.write(k, 2, o_r)
                sheet.write(k, 3, 'no')
                # main_file.append([o_b,o_g,o_r,'no'])
            else:
                sheet.write(k, 0, b)
                sheet.write(k, 1, g)
                sheet.write(k, 2, r)
                sheet.write(k, 3, 'yes')
                # main_file.append([b,g,r,'yes'])

            k+=1
        
book.close()     


excel_data_df = pd.read_excel(trainer_data, sheet_name='Sheet1')

print(excel_data_df)

main_file =[]
  
# Iterate over each row
for index, rows in excel_data_df.iterrows():
    # Create list for the current row
    my_list =[rows.b, rows.g, rows.r, rows.is_skin]
      
    # append the list to the final list
    main_file.append(my_list)
  
# Print the list
# print(main_file)

b_file_init = []
g_file_init = []
r_file_init = []

# print(main_file)

for i in main_file:
    b_file_init.append(str([i[0],i[3]]))
    g_file_init.append(str([i[1],i[3]]))
    r_file_init.append(str([i[2],i[3]]))
    

# print(b_file_init)

b_count = Counter(b_file_init)
g_count = Counter(g_file_init)
r_count = Counter(r_file_init)


b_final = {}
g_final = {}
r_final = {}


# print(r_count)
for key, value in b_count.items():
    row = ast.literal_eval(key)
    b_final[row[0]] = [0,0,0,0]

for key, value in g_count.items():
    row = ast.literal_eval(key)
    g_final[row[0]] = [0,0,0,0]
    
for key, value in r_count.items():
    row = ast.literal_eval(key)
    r_final[row[0]] = [0,0,0,0]


total_r_yes = 0
total_r_no = 0

total_g_yes = 0
total_g_no = 0

total_b_yes = 0
total_b_no = 0

for key, value in b_count.items():
    row = ast.literal_eval(key)
    if row[1] == 'yes':
        b_final[row[0]][0] = value
        total_b_yes+=value

    elif row[1] == 'no':
        b_final[row[0]][1] = value
        total_b_no+=value



for key, value in g_count.items():
    row = ast.literal_eval(key)
    if row[1] == 'yes':
        g_final[row[0]][0] = value
        total_g_yes+=value

    elif row[1] == 'no':
        g_final[row[0]][1] = value
        total_g_no+=value


for key, value in r_count.items():
    row = ast.literal_eval(key)
    if row[1] == 'yes':
        r_final[row[0]][0] = value
        total_r_yes+=value

    elif row[1] == 'no':
        r_final[row[0]][1] = value
        total_r_no+=value



for key, value in b_final.items():
    b_final[key][2] = b_final[key][0]/total_b_yes
    b_final[key][3] = b_final[key][1]/total_b_no

for key, value in g_final.items():
    g_final[key][2] = g_final[key][0]/total_g_yes
    g_final[key][3] = g_final[key][1]/total_g_no

for key, value in r_final.items():
    r_final[key][2] = r_final[key][0]/total_r_yes
    r_final[key][3] = r_final[key][1]/total_r_no

# print(b_final)


test_img = cv2.imread('skin_detection_naive_bayes_method/test.jpeg', 1)

t_height, t_width, t_depth = test_img.shape

for i in range(0, t_height):
    for j in range(0, t_width):
        b,g,r = test_img[i, j]
        is_skin = (r_final[r][2] * g_final[g][2] * b_final[b][2] * (total_r_yes+total_g_yes+total_b_yes))
        is_not_skin = (r_final[r][3] * g_final[g][3] * b_final[b][3] * (total_r_no+total_g_no+total_b_no))

        if is_not_skin > is_skin:
            test_img[i,j] = [0,0,0]



cv2.imshow('image',test_img)

cv2.waitKey(0)