# if 语句里边嵌套 if 语句
ticket = input('买否Y')
if ticket == 'Y':
    print('买票了,可以进站')
    safe = input('是否通过安检Y/N')
    if safe == 'Y':
        print('欢迎进候车室')
    else:
        print('未通过安检')
else:
    print('思想有多远你就走多远')