#Autor: TANG Kai
preproc_for_bda有两个函数

hash函数： 将原始数据HASH，基本是HASH成9位十进制
原数据在14-18位数之间，发生碰撞的概率很低。
sort函数：给不同的数据标注ID，递增。（这应该不是个好的处理方式待改进）
前提： 假设若有数据不同，只在相邻不同。，所以不适用一般情况