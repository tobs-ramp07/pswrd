import fn
pswrd = input("ENTER THE PASSWORD")
flag = 0
while True :
    if( len(pswrd)<8 ):
       flag=-1
        break
    elif not fn.search( '[a-z]', pswrd ):
        flag=-1
        break
    elif not fn.search( '[A-Z]', pswrd ):
        flag=-1
        break
    elif not fn.search( '[0-9]', pswrd ):
        flag=-1
        break
    elif not fn.search( '[~`	!	@	#	$	%	^	&	*]', pswrd ):
        flag=-1
        break
    elif not fn.search('\s',pswrd):
        flag=-1
        break
    else:
        flag=0
        print('INVALID PASSWORD')
        break
if flag==-1:
    print('INVALID PASSWORD')
