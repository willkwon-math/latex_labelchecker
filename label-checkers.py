from TexSoup import TexSoup
import pandas as pd

a=input("Input the TeX file name:")
#soup으로 파일 부르기
with open(a) as f: data = f.read() 

reflist = []

soup = TexSoup(data) 

for label in soup.find_all('label'):
    label_str = label.string
    count = 0
    for ref in soup.find_all('ref'):
        ref_str = ref.string
        if label_str == ref_str:
            count = count + 1

    reflist.append([label_str,count])     
        
reflist_pd = pd.DataFrame(reflist,columns=['label','count'])
print("Mission Complete!")

reflist_pd.to_csv('result.csv')
