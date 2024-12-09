Below is a consolidated list of all the advanced row-wise formulas created so far for the Reg Z use case, along with detailed explanations of their relevance in detecting anomalies. This includes both earlier and newly developed features. These features leverage only the dataset variables you provided.


---

1. APR-Rebalancing Effectiveness Ratio (ARER)

Formula:

ARER = \frac{(current\_pure\_purch\_trans\_bal\_amt - previous\_pure\_purch\_trans\_bal\_amt) \times (current\_bk3\_score\_val - previous\_bk3\_score\_val)}{(current\_interest - previous\_interest)}

Explanation:

Measures how changes in APR influence balances and risk scores.

Anomalies indicate ineffective or inconsistent rebalancing efforts, potentially violating Reg Z requirements.



---

2. Multi-Period APR Adjustment Stability Index (MPASI)

Formula:

MPASI = \frac{\sqrt{\sum_{i=1}^{N}(APR_i - \bar{APR})^2 / N}}{\bar{APR}}

Explanation:

Detects variability in APR adjustments over time.

High MPASI indicates erratic changes, suggesting potential systemic issues or unfair practices.



---

3. Delinquency-Adjusted APR Pressure Index (DAPI)

Formula:

DAPI = \frac{delnq\_stat\_cur\_mon \times (late\_fees + total\_all\_fee\_amt)}{interest}

Explanation:

Captures whether APR changes are effectively addressing delinquency-related risks.

High DAPI values suggest accounts where APR adjustments have been insufficient.



---

4. APR-Driven Fee Recovery Efficiency (ADFRE)

Formula:

ADFRE = \frac{(net\_interest\_amt - (cost\_fix\_epymt\_amt + cost\_dlnq\_coll\_amt))}{interest}

Explanation:

Measures whether APR adjustments successfully recover fees and delinquency costs.

Low ADFRE values highlight inefficiencies or non-compliance.



---

5. Dynamic APR-Balance Sensitivity Index (DABSI)

Formula:

DABSI = \frac{(current\_amort\_balcon\_fee\_amt - previous\_amort\_balcon\_fee\_amt)}{(current\_interest - previous\_interest)}

Explanation:

Assesses the sensitivity of balance changes to APR adjustments.

Anomalies in DABSI could point to systematic inefficiencies in APR impact.



---

6. Hidden APR Utilization Velocity (HAUV)

Formula:

HAUV = \frac{(current\_util\_ncc\_brt\_cl - previous\_util\_ncc\_brt\_cl)}{(current\_days\_since\_last\_payment - previous\_days\_since\_last\_payment)}

Explanation:

Tracks credit utilization rate in response to APR changes.

High HAUV values may indicate customer distress or anomalies in APR effectiveness.



---

7. Tiered APR Misalignment Index (TAMI)

Formula:

TAMI = |interest - expected\_APR|

Explanation:

Identifies misalignments between APRs and product tiers.

Significant deviations can highlight systemic flaws or manual errors in APR assignments.



---

8. APR Shock Transition Probability (ASTP)

Formula:

ASTP = P(APR_t | APR_{t-1})

Explanation:

Evaluates sudden or unexpected APR changes.

High ASTP values suggest deviations from standard policies or potential anomalies.



---

9. Relative APR Outlier Score (RAOS)

Formula:

RAOS = \frac{(interest - \mu_{\text{interest}})}{\sigma_{\text{interest}}}

Explanation:

Flags APRs that significantly deviate from peers.

Useful for uncovering biases or unfair practices in rate assignments.



---

10. APR-Fee Conflict Index (AFCI)

Formula:

AFCI = \frac{(current\_total\_all\_fee\_amt - previous\_total\_all\_fee\_amt)}{(current\_interest - previous\_interest)}

Explanation:

Checks whether APR changes correspond to expected fee behaviors.

Anomalies in AFCI suggest issues in fee-recovery alignment with APR adjustments.



---

11. Payment-to-APR Sensitivity Index (PASI)

Formula:

PASI = \frac{(purch\_pay\_amt - previous\_purch\_pay\_amt)}{(interest - previous\_interest)}

Explanation:

Captures customer payment behavior in response to APR changes.

Anomalies could indicate disproportionate rate adjustments or customer strain.



---

12. Historical APR Velocity (HAV)

Formula:

HAV = \frac{(APR_t - APR_{t-1})}{days\_elapsed}

Explanation:

Tracks the rate of APR adjustments over time.

High HAV values may signal aggressive rate-setting practices or compliance gaps.



---

13. Interest-to-Credit Limit Utilization Ratio (ICLR)

Formula:

ICLR = \frac{interest}{ca\_credi\_limit}

Explanation:

Evaluates how APR impacts credit limit utilization.

High ICLR values suggest disproportionate interest charges, potentially violating fairness principles.



---

14. Rolling APR Risk Score Correlation (RARC)

Formula:

RARC = corr(\text{bk3\_score\_val}, \text{interest})

Explanation:

Tracks the relationship between risk scores and APRs over time.

Weak or inverse correlations highlight misalignments with risk-based pricing requirements.



---

15. APR Impact on Earned Points (AIEP)

Formula:

AIEP = \frac{(tot\_pts\_amount - previous\_tot\_pts\_amount)}{(interest - previous\_interest)}

Explanation:

Assesses whether APR changes influence earned loyalty points.

Significant anomalies indicate potential misalignments in APR-driven incentives.



---

Summary

These formulas cover a wide range of behavioral, financial, and risk-based insights to capture anomalies tied to Reg Z compliance. Let me know if you'd like further optimization or integration into Python code!











import h2o

# Initialize H2O
h2o.init()

# Sample df (master dataframe)
df = h2o.H2OFrame({
    "ID": [101, 102, 103, 101, 102],
    "Table1": ["A", "B", "C", "A", "B"],
    "Table2": ["X", "Y", "Z", "X", "Y"],
    "Table3": [5, 10, 15, 20, 25]
})

# Sample df1 (lookup dataframe for ID -> Count)
df1 = h2o.H2OFrame({
    "ID": [101, 102],
    "Count": [20, 30]
})

# Sample df2 (lookup dataframe for Table1 -> Xyz)
df2 = h2o.H2OFrame({
    "Table1": ["A", "B"],
    "Xyz": [100, 200]
})

# Convert df1 and df2 to Python dictionaries for fast lookup
count_dict = {row["ID"]: row["Count"] for row in df1.as_data_frame().itertuples()}
xyz_dict = {row["Table1"]: row["Xyz"] for row in df2.as_data_frame().itertuples()}

# Create empty columns for Count and Xyz
df["Count"] = None
df["Xyz"] = None

# Optimized for-loop for mapping based on precomputed dictionaries
for i in range(df.nrows):
    id_val = df[i, "ID"]
    table_val = df[i, "Table1"]
    
    # Assign the corresponding values from the dictionaries
    if id_val in count_dict:
        df[i, "Count"] = count_dict[id_val]
    if table_val in xyz_dict:
        df[i, "Xyz"] = xyz_dict[table_val]

# Show the result
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




