#-----------------------------------------------------------------------------
# Name:        Model.py
# Purpose:     concentrate model related function in a single module
#
# Author:      Flavio Codeco Coelho
#
# Created:     2006/08/20
# RCS-ID:      $Id: Model.py $
# Copyright:   (c) 2004-2006
# Licence:     GPL
# New field:   Whatever
#-----------------------------------------------------------------------------

from scipy import integrate
from numpy import *
from string import *

class Model:
    def __init__(self,equations,pars,inits, trange,):
        """
        Equations: a function with the equations
        inits: sequence of initial conditions
        trange: time range for the simulation
        """
        self.eqs = equations
        self.pars = pars
        self.Inits = inits
        self.Trange = arange(0,trange,0.1)
        pass
    def Run(self):
        """
        Do numeric integration
        """
        t_courseList = []
        t_courseList.append(integrate.odeint(self.Equations,self.Inits,self.Trange, 
        full_output=0, printmessg=0))
        return (t_courseList,self.Trange)
    
    def Equations(self,y,t):
        """
        This function defines the system of differential equations, evaluating
        each line of the equation text box as ydot[i]

        returns ydot
        """
        par = self.pars

    #---Create Parameter Array----------------------------------------------------------------------------
        pars = par.strip().split('\n')
        Npar = len(pars)
        p = zeros((Npar),'d') #initialize p
        if pars[0]: #only if there is at least one parameter
            for j in xrange(len(pars)):
                try:
                    p[j] = eval(pars[j]) #initialize parameter values
                except SyntaxError:
                    dlg = wx.MessageDialog(self, 'There is a syntax error in the parameter Box.\nPlease fix it and try again.',
                      'Syntax Error', wx.OK | wx.ICON_INFORMATION)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                        
    #---Create equation array----------------------------------------------------------------------------
        eqs = strip(self.eqs).split('\n')
        Neq=len(eqs)
        ydot = zeros((Neq),'d') #initialize ydot
        for k in xrange(Neq):
            ydot[k] = eval(eqs[k]) #dy(k)/dt

        return ydot