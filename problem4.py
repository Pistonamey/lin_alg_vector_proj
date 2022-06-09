# import numpy to perform operations on vector
import numpy as np
import matplotlib.pyplot as plt

#Function 'proj' calcultes the projection and plots the graph
def proj(u,v):
    # Task: Project vector u on vector v
    # finding norm of the vector v
    v_norm = np.sqrt(sum(v ** 2))

    # for projecting a vector u onto another vector v
    # find dot product using np.dot()
    proj_of_u_on_v = (np.dot(u, v) / v_norm ** 2) * v

    print("vector u (Blue) : ",u)
    print("vector v (Red) : ", v)
    print("Projection of Vector u on Vector v is (Green) : ", proj_of_u_on_v)

    #plot the graph
    fig=plt.figure()
    ax=plt.axes(projection='3d')
    ax.set_xlim([-1,3])
    ax.set_ylim([-3,3])
    ax.set_zlim([0,1])

    #origin for the vectors
    start=[0,0,0]
    ax.quiver(start[0],start[1],start[2],u[0],u[1],u[2]) #blue vector (u)
    ax.quiver(start[0],start[1],start[2],v[0],v[1],v[2],color='r') #red vector (v)
    ax.quiver(start[0],start[1],start[2],proj_of_u_on_v[0],proj_of_u_on_v[1],proj_of_u_on_v[2],color='g') #green vector (projection of u on v)
    plt.show()

#a) Generate random vectors a & v
u = np.random.rand(3)  # vector u
v = np.random.rand(3)  # vector v

#pass them to the function
proj(u,v)