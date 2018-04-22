#Autor: TANG Kai

BDA数据预处理是main函数：
读取数据、预处理数据


preproc_for_bda有两个函数：
hash函数： 将原始数据HASH，基本是HASH成9位十进制
原数据在14-18位数之间，发生碰撞的概率很低。
sort函数：给不同的数据标注ID，递增。（这应该不是个好的处理方式待改进）
前提： 假设若有数据不同，只在相邻不同。，所以不适用一般情况

数据来源：
https://tianchi.aliyun.com/competition/information.htm?spm=5176.100067.5678.2.6c2e45588WV7JH&raceId=231647
