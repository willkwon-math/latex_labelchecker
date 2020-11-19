from TexSoup import TexSoup

a=input("Input the TeX file name:")
#soup으로 파일 부르기
with open(a) as f:
    soup = TexSoup(f)

label_list = soup.find_all('label')
ref_list = soup.find_all('ref')

for i in label_list:
    a=i.string
    count = 0
    for j in ref_list:
        b=j.string
        if a == b:
            count = count +1
    print('label:{}, count:{}'.format(a,count))
        