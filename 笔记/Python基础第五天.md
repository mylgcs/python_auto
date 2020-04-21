# Python基础第五天  

* while嵌套  

* break、continue

* for、in   

  

  

## while嵌套  

```
语法:
	while 条件1:   #外层循环 
		[代码块1]
		while 条件2: #内层循环
			[代码块2]
	
  1.判断条件1 如果为真，执行代码块1 执行内层循环 
  2.判断条件2 是否成立 如果成立执行代码块2 内层循环结束
  3.重新判断外层循环条件 
  
  特点:  外层循环走一步 内层循环走一遍 
  		外层和内层循环变量必须是不一样的 
  		内层循环必须完全嵌套到内层循环里边 
		 
```



## break continue 

```
continue 语句用来跳过当前循环的剩余语句，然后重新判断循环条件，开启下一轮循环。continue只能出现在while和for循环中

break用于结束当前循环。只对当前这一重循环起作用。break只能出现在循环中
```





## for循环   

> python中的for循环 指的就是 for..in 



```
for i in range(1,11):
	print(i)

in 后边 必须是可迭代的对象 


```

