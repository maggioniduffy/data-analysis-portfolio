timeStep = 100            # years
waterDepth = 4000        # meters
L = 1350                 # Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8          # W/m2 K4

heat_capacity = waterDepth* 4.2E6
time_list = [0]
TK = [0,]
heat_content = heat_capacity*TK[0]
heat_in = L * (1 - albedo)/4
heat_out = 0
n = int(input(""))

for itime in range(0,n):
  time_list.append(timeStep + time_list[-1])
  heat_out = epsilon * sigma * pow(TK[-1],4)
  #print(time_list[-1], heat_out)
  heat_content = heat_content + (heat_in-heat_out) * timeStep * 3.14e7
  TK.append(heat_content/heat_capacity)

print(TK[-1], heat_out)