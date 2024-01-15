#例題1:使用print()函數將 人生苦短, 我用python 輸出到文本文件test.txt中
fp=open('text.txt', "w") #打開文件
print("人生苦短, 我用python", file=fp) #內容輸出到文件
fp.close() #關閉文件

#例題2:輸出個人自我介紹，使用input()函數從鍵盤輸入姓名, 年齡, 座右銘, 並使用print()函數輸出到控制台
name=input('請輸入您的姓名')
age=input('請輸入您的年齡')
motto=input('請輸入您的座右銘')
print('姓名'+name)
print('年齡'+age)
print('座右銘'+motto)
#加號, 逗號都可以