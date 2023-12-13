
print('**** ISA CALCULATOR ****')
print('\n 1. Calculate ISA for altitude in meters')
print(' 2. Calculate ISA for altitude in feet')
print(' 3. Calculate ISA for altitude in FL')


mode = int(input("\n Choose mode: "))
mod = ['m','ft','FL']
alt = float(input('Enter altitude [' + mod[mode - 1] + ']: ')) 
if mode == 2:
    alt = alt * 0.3048
if mode == 3:
    alt = alt * 100 * 0.3048
if alt > 86000:
    print('Sorry , I can only do altitudes up to 86000 m')
    exit()
    
P = 101325.0
g_0 = 9.80665
R = 287
e = 2.718281828459045235360
T = [input('\n Determine the temperature at sea level that you would like to use. (Press enter to use standard values): ') , 0 , 0 , 0 , 0 , 0 , 0]

if T[0] == '':
    T[0] = 288.15
else:
    T[0] = float(T[0])

h = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000]
a = [-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002]
num = 0
for i in range(len(h)):
    if alt > h[i]:
        num = i + 1

for i in range (num):
    T[i+1] = T[i] + a[i] * (min(alt, h[i+1])- h[i])
    if a[i] != 0:
        P = P * (T[i+1]/T[i])**(-g_0 / (R * a[i]))
    else:
        P = P * e ** ((-g_0 /(R * T[i+1]))*(min(alt, h[i+1])- h[i]))
rho = P/(R * T[num])
                                          
print('The density is ', rho, '.')
print ('The pressure is ', P, '.')
print('The temperature is ',T[num],'.')
