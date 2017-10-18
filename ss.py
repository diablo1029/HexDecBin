import random
from random import randint
f_first_names=('Jackie','Jessica','Catherine','Madison')
m_first_names=('John','Andy','Jackson','Jason','Joe','Alex','Richard','Roger','Clark','James','Blake','George','David','Tom','Jay','Barry','Harrison','Cisco','Caitlyn')
last_names=('Johnson','Smith','Williams','Anderson','Rogerson','Richardson','Clarkson','Larson','Davidson','Helms','Teal','Thompson','McClure','McDonald','Wells','Allen','Ramon','Snow','Garrick','McClendon','McLeary')

full_name=random.choice(m_first_names)+" "+random.choice(last_names)


print (full_name)
print(randint(100, 999), "-", randint(10, 99), "-", randint(1000, 9999))
print("(", randint(100, 999), ")", randint(100, 999), "-", randint(1000, 9999))
print(randint(1,12), "/", randint(0, 31), "/", randint(1900, 2017))
