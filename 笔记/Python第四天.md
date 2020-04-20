## Python第四天  

* 编码规范  
* 分支语句 
* 多分支 
* while else
* 循环  
* 多重循环  



## 编码规范  

1.代码编排 

* 缩进4个空格  可以 1个tab键 或者   4个空格   不能tab 和空格键 混用

* 所有行限制的最大字符数是79   

* 添加适当的空行

  

2.空格 

> 二元运算符  需要两个操作数的运算符    比如  3 + 5 

* =   ==  前后有空格 

* 二元运算符  两边要添加一个空格 

  ```python
  res = 1 + 1
  print(res)
  ```

* 逗号，冒号，分号 后边要留一个空格，前面不用留

  ```
  if a == 666: print(888)  :左边不留 右边留
  if a == 666 : print(888)  错误
  ```

  

* 如果紧跟在 小括号 中括号 大括号 的后边 ,那么就不要留空格

  ```
  test(only[1],{egg:888})正确的  
  test( only[ 1],{ egg:888}) 错误的   
  ```

  

## 分支语句  

* 单一分支  

  ```
  if 条件表达式:  #条件表达式的结果肯定是bool类型  
  	[代码块]
  【其它代码】
  当条件表达式的结果为真 执行代码块 否则 执行其它代码  
  
  注意 代码块必须缩进
  ```

  ### 示例

  ```
  a = 66
  b = 88
  if a>b:
      print(a)
  print("="*50)
  
  if b>a:
      print(b)
  ```

  

* 双向分支   if - else  

  ```
  if 表达式:
  	代码块a
  else:
  	代码块b
  后续代码  
  当表达式的结果为真 执行代码块a  然后执行后续代码  如果表达式为假 执行代码块b 然后再执行后续代码  
  代码块a 和 代码块b  肯定是二选一的 不能即执行a 又执行 b  
  
  ```

  ### 示例

  ```python
  # score = 66
  # score1 = 88
  # if score>score1:
  #     print(score)
  # else:
  #     print(score1)
  # 
  # print("%"*50)
  
  text = int(input("请输入一个整数:"))
  if text % 3 == 0:
      print("能整除")
  else:
      print("不能整除")
  ```

  

* 多向分支  

  ```
  if 表达式1:
  	代码块1
  elif 表达式2:
  	代码块2
  elif 表达式3:
  	代码块3
  ...
  else:
  	代码块n
  如果表达式1 为真 执行代码块1 否则 计算表达式2的值 如果表达式2的值为真  那么执行代码块2 否则计算表达式3  如果为真 执行代码块3  如果都不符合 走else  执行代码块n 
  ```

  ### 示例 

  ```python
  # < 18.5 偏瘦
  # 18.5-24.9 正常
  #24.9 -27 偏胖
  # 27以上  肥胖
  
  weight = float(input("请输入体重(kg):"))
  height = float(input("请输入身高(m):"))
  
  bmi = weight/height ** 2
  
  if bmi < 18.5:
      print("需要长点肉了")
  elif bmi < 24.9:
      print("标准身材")
  elif bmi < 27:
      print("标准身材")
  else:
      print("你这样的谁要啊")
  print("~"*30)
  ```

## while  

```python
while 表达式 
	循环体   #当表达式为真执行循环体  为假跳过整个while   
			#循环体结束以后 回来再判断一次循环体是否为真
	
sum = 0

i = 1
while i<= 100:
    sum += i
    i+=1
print(sum,i)#  5050 101
```





## while else  

```python
while 循环条件:
	循环体
else:
	代码块
	
#键盘中输入一个数字  判断是否是素数（大于1的自然数   只能被1和自身整除 那么该数字成为质数也叫素数 ）


#如果循环条件不具备，循环正常结束 会执行else 语句块
#如果循环的过程中break 退出了 则不走else

#大于1的自然数
num = int(input("请输入一个整数:"))
i = 2
while i < num:

    if num % i == 0: # 除尽了,不是素数
        break  #break 退出所有循环   不执行else
    i += 1   # 1 和 本身 之外没有别的除数了 这才是素数
    #从2开始


    #检查从2到它本身 是否有别的除数  如果有 这个数就不是素数

else:
    print("是素数")


# #计算1-100的和
# sum = 0
#
# i = 1
# while i<= 100:
#     sum += i
#     i+=1
# print(sum,i)  5050 101
```

## debug的使用 



## while 和 if 的区别  

```
sum = 0
i = 1
if i<=100:  #这里满足条件执行下面的代码块  就不会再回来判断是否满足条件 
    sum += i
    i+=1
print(sum,i) # 1 2


sum = 0
i = 1
while i<=100:  #这里满足条件执行下面的代码块  回来还会判断一次是否满足条件 
    sum += i
    i+=1  
print(sum,i) # 1 2
```



## 死循环  

> 表达式 永远为真的情况  

```
while True:
	#循环体  
或者  
while 1:
	#循环体


while True:
    print("泽宇老弟")
```



## break  & continue  

```

```

