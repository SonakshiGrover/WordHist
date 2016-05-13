x=readLines("c:/python27/rfile.py")
y=rev(sort(table(x)))
colors = c("red", "yellow", "green", "violet","orange", "blue", "pink", "cyan") 
barplot(y[1:20],col=colors)                
for(n in 1:20)
{
   y[n]=y[n]/length(x)

}
barplot(y[1:15],col=colors)

