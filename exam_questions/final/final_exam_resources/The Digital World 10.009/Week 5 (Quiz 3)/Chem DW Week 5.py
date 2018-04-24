# -*- coding: utf-8 -*-

import numpy as np
import scipy.constants as c
from math import factorial,pi
a=c.physical_constants['Bohr radius'][0]

def spherical_to_cartesian(r,theta,phi):
    return np.around(r*np.sin(theta)*np.cos(phi),decimals=5),np.around(r*np.sin(theta)*np.sin(phi),decimals=5),np.around(r*np.cos(theta),decimals=5)
    pass

def cartesian_to_spherical(x, y, z):
    return np.around(np.sqrt(x**2+y**2+z**2),decimals=5),np.around(np.arctan2(np.sqrt(x**2+y**2),z),decimals=5),np.around((np.arctan2(y,x) if x!=0 else (0 if y==0 else pi/2)),decimals=5)
    pass

def absolute(cn):
    return np.sqrt(np.real(cn)**2+np.imag(cn)**2)
    pass

def angular_wave_func(m,l,theta,phi):
    #Get the Legenderre function
    def p_l(l):
        if l==0:
            return lambda x:1
        p=np.poly1d([1,0,-1]).__pow__(l)
        p_der=p.deriv(l)
        p_l=p_der/(2**l*factorial(l))
    
        def get_poly(theta):
            poly=0
            for term_power,term_coeff in enumerate(p_l):
                poly += term_coeff*(np.cos(theta)**term_power)
            return poly
        return p_l
    #Get the associated Legenderre function
    def asso_legend(m,l):
        if l==0 and m==0:
            return lambda x:1
        else:
            legend=p_l(l)
            if m!=0:
                gen_asso_legend=legend.deriv(abs(m))
            else:
                gen_asso_legend=legend
        
        def theta_asso_legend(theta):
            return gen_asso_legend(np.cos(theta))*((1-np.cos(theta)**2)**abs(m/2.0))
        return theta_asso_legend
    if l<0 or abs(m)>l:
        return "Error."
    else:
        #calculate individual terms (inside the square root and the 'lone' theta term)
        if m>0:
            epsilon=(-1)**m
        else:
            epsilon=1
        sq_root_term=np.sqrt(((2*l + 1)/(4*np.pi))*(factorial(l-abs(m))/factorial(l+abs(m))))
        theta_term=asso_legend(m,l)(theta)
        y_n_l=epsilon*sq_root_term*np.exp(1j*m*phi)*theta_term
        return np.round(y_n_l,5)
    pass

def radial_wave_func(n,l,r):
    def l_q(q):
        def binomial(powers):
            for power in range(powers):
                new_value=1
                binom_coeff=[new_value]
                for power_sub in range(power):
                    new_value*=(power-power_sub)*1/(power_sub+1)
                    binom_coeff.append(int(new_value))
            return binom_coeff
        lagurre_coeff=[]
        for power_term in range (q+1):
            l_coeff=((-1)**(q+power_term))*(binomial(q+1)[power_term])*(factorial(q)/factorial(q-power_term))
            lagurre_coeff.append(l_coeff)
        return np.poly1d(lagurre_coeff)

    def l_q__q_p(p, q_p):
        q=q_p+p
        lague=l_q(q)
        lague_der=lague.deriv(p)
        def assoc_value(x):
            value=(-1**p)*lague_der(x)
            return value
        return assoc_value
    p=2*l+1
    q_p=n-l-1
    x=(2*r/(n*a))
    lague_func=l_q__q_p(p,q_p)
    lague_term=lague_func(x)
    #Put everything together
    r_n_l=(np.sqrt(((2/(n*a))**3)*((factorial(q_p)/(2.0*n*(factorial(n+l))**3))))*np.exp(-r/(n*a))*x**l*lague_term)
    norm_r_n_l=r_n_l/(a**(-3/2))
    return np.round(norm_r_n_l,5)
    pass

def linspace(start, stop, num=50):
    return [round(start+i*(stop-start)/(num-1),5) for i in range(num)]
    pass

def meshgrid(x,y,z):
    for i in range(len(x)):
        x[i]=float(x[i])
    for j in range(len(y)):
        y[j]=float(y[j])
    for k in range(len(z)):
        z[k]=float(z[k])
    sub_mesh_list_x=[]
    sub_mesh_list_y=[]
    sub_mesh_list_z=[]
    for b in range(len(y)):
        sub_mesh_list_x.append([])
        sub_mesh_list_y.append([])
        sub_mesh_list_z.append([])
        for a in range(len(x)):
            sub_mesh_list_x[b].append([])
            sub_mesh_list_y[b].append([])
            sub_mesh_list_z[b].append([])
            for d in range(len(z)):
                sub_mesh_list_x[b][a].append(x[a])
                sub_mesh_list_y[b][a].append(y[b])
                sub_mesh_list_z[b][a].append(z[d])
    return sub_mesh_list_x,sub_mesh_list_y,sub_mesh_list_z
    pass

def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    a=c.physical_constants['Bohr radius'][0]
    #Create arrays of x,y,z points
    xx,yy,zz=np.mgrid[-1*roa:roa:(Nx*1j),-1*roa:roa:(Ny*1j),-1*roa:roa:(Nz*1j)]
    #Vectorize cartesian_to_spherical function
    cart_to_spher_vec=np.vectorize(cartesian_to_spherical)
    #Create r,theta,phi arrays through conversion
    r_array,theta_array,phi_array=cart_to_spher_vec(xx,yy,zz)
    #Vectorize radial and angular wave component functions
    radial_func_vec=np.vectorize(radial_wave_func)
    angular_func_vec=np.vectorize(angular_wave_func)
    #Find radial component
    radial_part=radial_func_vec(n,l,r_array*a)
    #Find angular component
    if m<0:
        angular_part=1j/np.sqrt(2)*(angular_func_vec(m,l,theta_array,phi_array)-((-1)**m)*angular_func_vec(-1*m,l,theta_array,phi_array))
    elif m>0:
        angular_part=1/np.sqrt(2)*(angular_func_vec(-1*m,l,theta_array,phi_array)+((-1)**m)*angular_func_vec(m,l,theta_array,phi_array))
    else:
        angular_part=angular_func_vec(m,l,theta_array,phi_array)
    #Vectorize absolute function
    abs_vec=np.vectorize(absolute)
    #Find magnitude of square of wave function
    mag=(abs_vec(radial_part*angular_part))**2
    #Return outputs rounded to 5d.p.
    return np.around(xx,decimals=5),np.around(yy,decimals=5),np.around(zz,decimals=5),np.around(mag,decimals=5)
    pass