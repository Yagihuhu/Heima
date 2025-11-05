i = 0
while i < 10:

    if i ==3:
        i += 1
        #注意，循环中使用continue时，需要确认循环计数是否需要修改
        continue   #某一条件满足时，当次循环，进入下一次循环（这里就是i=3的时候，跳出while不执行 print(i)）000
    print(i)

    i+=1