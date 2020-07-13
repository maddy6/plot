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




