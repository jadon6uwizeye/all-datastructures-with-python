# # import numpy as np
# # from scipy.integrate import odeint
# # import matplotlib.pyplot as plt

# # g = 9.81 # acceleration due to gravity
# # L = 0.23 # loop radius
# # v = 4.25 # speed downhill
# # m = 0.03 # car mass
# # μ = 0.002 # constant
# # θ0 = 40 # initial angle in degrees
# # ω0 = 0 # initial angular velocity
# # P = 20 # constant force

# # θ0 = θ0 * np.pi/180 # convert initial angle to radians

# # def differential_eqs(y, t, g, L, μ, v, m, P):
# #     θ, ω = y
# #     dθdt = ω
# #     dωdt = -(g/L)*θ + (-μ/(m * L**2))*θ - (P/(m * v * L))*np.cos(θ)
# #     return [dθdt, dωdt]

# # t = np.linspace(0, 0.18, 1000) # time range

# # # solve the ODEs
# # solution = odeint(differential_eqs, [θ0, ω0], t, args=(g, L, μ, v, m, P))
# # θ, ω = solution.T

# # # plot the solution
# # plt.plot(t, θ, label='Angular position (θ)')
# # plt.plot(t, ω, label='Angular velocity (ω)')
# # plt.xlabel('Time (s)')
# # plt.legend()
# # plt.show()

# import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt

# g = 9.81 # acceleration due to gravity
# L = 0.23 # loop radius
# v = 4.25 # speed downhill
# m = 0.03 # car mass
# μ = 0.002 # constant
# k = 20 # constant
# θ0 = 40 # initial angle in degrees
# ω0 = 0 # initial angular velocity
# P = 20 # constant force

# θ0 = θ0 * np.pi/180 # convert initial angle to radians

# def differential_eqs(y, t, g, L, μ, v, m, k, P):
#     θ, ω = y
#     dθdt = ω
#     dωdt = -(g/L)*θ - (k/(v**2 * m * L)) + μ*(ω**2 + (P/(m * L)) * np.cos(θ))
#     return [dθdt, dωdt]

# t = np.linspace(0, 10, 1000) # time range

# # solve the ODEs
# solution = odeint(differential_eqs, [θ0, ω0], t, args=(g, L, μ, v, m, k, P))
# θ, ω = solution.T

# # plot the solution
# plt.plot(t, θ, label='Angular position (θ)')
# plt.xlabel('Time (s)')
# plt.ylabel('Angular position (rad)')
# plt.legend()
# plt.show()


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.81 # acceleration due to gravity
L = 0.23 # loop radius
v = 4.25 # speed downhill
m = 0.03 # car mass
μ = 0.002 # constant
k = 20 # constant
θ0 = 40 # initial angle in degrees
ω0 = 0 # initial angular velocity
P = 20 # constant force

θ0 = θ0 * np.pi/180 # convert initial angle to radians

def differential_eqs(y, t, g, L, μ, v, m, k, P):
    θ, ω = y
    dθdt = ω
    dωdt = -(g/L)*θ - (k/(v**2 * m * L)) + μ*(ω**2 + (P/(m * L)) * np.cos(θ))
    return [dθdt, dωdt]

t = np.linspace(0, 10, 1000) # time range

# solve the ODEs
solution = odeint(differential_eqs, [θ0, ω0], t, args=(g, L, μ, v, m, k, P))
θ, ω = solution.T

# plot the solution
plt.plot(t, θ, label='Angular position (θ)')
plt.xlabel('Time (s)')
plt.ylabel('Angular position (rad)')
plt.legend()
plt.show()