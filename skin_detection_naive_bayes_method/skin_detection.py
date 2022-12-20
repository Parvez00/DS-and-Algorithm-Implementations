import cv2
from collections import Counter
import ast

org_img = cv2.imread('org.jpg', 1)
mask = cv2.imread('mask.jpg', 1)

m_height, m_width, m_depth = mask.shape

main_file = []

for i in range(0, m_height):
    for j in range(0, m_width):
        b,g,r = mask[i, j]
        if b >= 245 and g >= 245 and r >= 245:
            o_b,o_g,o_r = org_img[i, j]
            main_file.append([o_b,o_g,o_r,'no'])
        else:
            main_file.append([b,g,r,'yes'])

b_file_init = []
g_file_init = []
r_file_init = []

print(main_file)

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


for i in range(0, m_height):
    for j in range(0, m_width):
        b,g,r = org_img[i, j]
        is_skin = (r_final[r][2] * g_final[g][2] * b_final[b][2] * (total_r_yes+total_g_yes+total_b_yes))
        is_not_skin = (r_final[r][3] * g_final[g][3] * b_final[b][3] * (total_r_no+total_g_no+total_b_no))

        if is_not_skin > is_skin:
            org_img[i,j] = [0,0,0]



cv2.imshow('image',org_img)

cv2.waitKey(0)