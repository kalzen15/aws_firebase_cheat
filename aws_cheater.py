import pyperclip
name=input("Enter the link >")
number=int(input("Enter no of chapters >"))
# https://blockhead2.s3.amazonaws.com/Class+6/Social+Studies/Social+and+Political+Life/Chapter+(1).pdf
def findBracket(link):
    n=len(link)
    for i in range(len(link)-1,-1,-1):
        if link[i]==')':
            n=i
        if link[i]=='(':
            return i,n
def reLinked(link,index,number):
    for i in range(1,number+1):
        new_link=link[:index[0]+1]+str(i)+link[index[1]:]
        pyperclip.copy(new_link)
        print(new_link,'copied')
        input('Press enter for next')
bracket=findBracket(name)
print(bracket)
print(len(name))
reLinked(name,bracket,number)
print('Completed!!!!')
