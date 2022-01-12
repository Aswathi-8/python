y=int(input(&quot;Enter the YEAR&quot;))
if((y%100!=0 and y%4==0)or(y%400==0)):
print(&quot;leap year&quot;)
else:
print(&quot;Not leap year&quot;)