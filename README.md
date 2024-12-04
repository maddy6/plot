import h2o

# Initialize H2O
h2o.init()

# Sample df (master dataframe)

# Function to map "Count" based on "ID"
def map_count(id_val):
    # Look up the value in df1 where "ID" matches
    matching_row = df1[df1["ID"] == id_val, "Count"]
    # If a match exists, return the "Count" value, otherwise return None
    return matching_row[0, 0] if matching_row.nrows > 0 else None

# Use H2O's apply to map the "Count" column from df1 to df based on "ID"
df["Count"] = df["ID"].apply(map_count)

# Show the result
print("After mapping Count from df1:")
df.show()






import h2o

# Initialize H2O
h2o.init()

# Master dataframe (df)
df = h2o.H2OFrame({
    "ID": [101, 102, 103, 101, 102],
    "Table1": ["A", "B", "C", "A", "B"],
    "Table2": ["X", "Y", "Z", "X", "Y"],
    "Table3": [5, 10, 15, 20, 25]
})

# df1 with ID and Count
df1 = h2o.H2OFrame({
    "ID": [101, 102],
    "Count": [20, 30]
})

# Create a dictionary of mapping from df1
count_dict = dict(zip(df1["ID"].as_data_frame()["ID"], df1["Count"].as_data_frame()["Count"]))

# Add the "Count" column to df based on matching IDs
df["Count"] = df["ID"].apply(lambda x: count_dict.get(x, None))

# Show the result
print("After mapping Count from df1:")
df.show()










import h2o

# Initialize H2O
h2o.init()

# Master dataframe (df)
df = h2o.H2OFrame({
    "ID": [101, 102, 103, 101, 102],
    "Table1": ["A", "B", "C", "A", "B"],
    "Table2": ["X", "Y", "Z", "X", "Y"],
    "Table3": [5, 10, 15, 20, 25]
})

# df1 with ID and Count
df1 = h2o.H2OFrame({
    "ID": [101, 102],
    "Count": [20, 30]
})

# Perform left join between df and df1 based on "ID"
df["Count"] = df["ID"].map(dict(zip(df1["ID"].as_data_frame()["ID"], df1["Count"].as_data_frame()["Count"])))
print("After mapping Count from df1:")
df.show()







# Join df with df1 on "ID" (left join to retain all rows in df)
df_with_count = df.cbind(df1[df["ID"] == df1["ID"], "Count"])

# Join df with df2 on "Table1"
df_with_xyz = df_with_count.cbind(df2[df["Table1"] == df2["Table1"], "Xyz"])




# Extract unique IDs from df1 as a Python list
unique_ids = df1["ID"].as_data_frame(use_pandas=False)[1]

# Filter rows in df where ID matches the unique IDs
mask = df["ID"].isin(unique_ids)

# Map "Count" from df1 to df by matching IDs
df["Count"] = mask.ifelse(
    df1[df["ID"] == df1["ID"], "Count"],
    None
)

print("After mapping Count from df1:")
df.show()




# Convert df2 to pandas for easier lookup
df2_pandas = df2.as_data_frame()

# Create a dictionary for Table1-to-Xyz mapping
table1_to_xyz = dict(zip(df2_pandas["Table1"], df2_pandas["Xyz"]))

# Add the "Xyz" column to df
df["Xyz"] = df["Table1"].as_data_frame().apply(lambda x: table1_to_xyz.get(x[0], None), axis=1)

print("After mapping Xyz from df2:")
print(df)







# plot
Data for Plots


[‎16-‎03-‎2018 15:45] Mohanraj Vengadachalam: 
https://github.com/ageitgey/face_recognition 
https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/ 
[‎16-‎03-‎2018 15:47] Mohanraj Vengadachalam: 
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78 
https://www.cs.tau.ac.il/~wolf/ytfaces/ 
[‎16-‎03-‎2018 15:49] Mohanraj Vengadachalam: 
http://www.face-rec.org/databases/ 
[‎16-‎03-‎2018 15:53] Mayur Vishwasrao: 
https://app.faceter.io/auth
We saved this conversation. You'll see it soon in the Conversations tab in Skype for Business and in the Conversation History folder in Outlook.
[‎16-‎03-‎2018 16:07] Mohanraj Vengadachalam: 
https://cs.stanford.edu/people/karpathy/ 
[‎16-‎03-‎2018 16:09] Mohanraj Vengadachalam: 
http://cs231n.stanford.edu/ 



Video Recording

https://github.com/vijayvee/video-captioning

https://github.com/brianhuang1019/Video-Cap

https://github.com/preritj/show_attend_tell

https://github.com/vijayvee/video-captioning

https://github.com/zhegan27/SCN_for_video_captioning

https://github.com/apple2373/chainer_caption_generation

https://github.com/brianhuang1019/Video-Cap

https://github.com/rohit-gupta/Video2Language

https://github.com/ZubairHussain/Video-Paragraph-Captioning---Keras

https://github.com/dongyp13/video-caption

https://github.com/loscheris/VideoCaptioning_att

https://github.com/xiadingZ/video-caption.pytorch

https://github.com/lvapeab/ABiViRNet



s = """The Threat dashboard contains the following dashlets:
• Total Compromised
"""
ans = s.find('Adapter')
print(ans)
#if ans<0:
#    ans = "Index Not Found"
#print(ans)


import docx2txt
import re
#my_text = docx2txt.process("C:/Users/Mayur.v/Documents/test word.docx")
my_text = docx2txt.process("C:/Users/Mayur.v/Documents/Cisco_chapter1.docx")
#my_text = my_text.readline()
test = my_text
#test = my_text[1500:3000]
test = test.strip()
new_string = ''
for line in test.split('\n'):
        if line.strip():
                new_string += line + '\n'
#print old_string,
#print(new_string)

### Remove Special Characters from string
#new_string = re.sub('[^A-Za-z0-9]+', '', new_string)
#new_string = new_string.split()
#new_string = new_string.split(" ")
#new_string = "\n".join(new_string)
#with open("C:/Users/Mayur.v/Documents/hello3.txt") as f:
#new_string = " ".join(new_string.strip() for line in new_string)
#new_string = list(new_string)
new_string = re.sub("\n" , " ", new_string)
new_string1 = re.sub("\s\s+" , " ", new_string)
print(new_string1)
print(type(new_string1))

fh = open("C:/Users/Mayur.v/Documents/hello2.txt", "w") 
fh.write(new_string1) 
fh.close 
### find the index of the Answer
#ans = new_string.find('Wireless')
#if ans<0:
#    ans = "Index Not Found"
#print(ans)

#test1 = filter(lambda x: not re.match(r'^\s*$', x), test)
#lines = test.split()
#lines = [line for line in test if line.strip()]
#sentences = re.split(r' *[\.\?!]*', test)
#cleaned = "\n".join(test)
#cleaned = "\n".join(test.split())
#test = '\n'.join(test)
#print(cleaned)
#print(test.find('Overview'))
#print(lines)




