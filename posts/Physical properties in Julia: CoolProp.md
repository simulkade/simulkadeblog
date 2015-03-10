<!-- 
.. title: Physical properties in Julia: CoolProp
.. slug: Physical properties in Julia: CoolProp
.. date: 2014-10-25 00:37:54 UTC+01:00
.. tags: CoolProp, Julia
.. category: 
.. link: 
.. description: 
.. type: text
-->

Recently, I was analyzing my core-flooding experimental data in a Julia notebook, when I realize that I don't have access to a few Matlab functions that I have written (or found elsewhere), which I use regularly for the calculation of physical properties of pure components. For instance, viscosity of water (I know that you know it is 0.001 Pa.s) or density of CO2 or nitrogen at different temperatures and pressures. I know that [Professor Wagner](http://www.thermo.ruhr-uni-bochum.de/en/prof-w-wagner.html) and his group have developed a few highly-accurate equations of state for industrial applications and I knew that there is a software called [FPROPS](http://ascend4.org/FPROPS) which is used in [Ascend IV](http://ascend4.org/Main_Page) package. Searching the name in google showed me a fantastic package called [CoolProp](www.coolprop.org/) which is being developed mostly in [thermodynamics laboratory](http://www.labothap.ulg.ac.be/cmsms/) in [Universite de Liege](www.ulg.ac.be/). The code is written in C++ but it supports many languages and environments including Matlab and Python. The Python part was interesting to me because I can call it using [PyCall](https://github.com/stevengj/PyCall.jl) package in Julia. First I installed the `CoolProp` package using the instructions [here](http://www.coolprop.org/HowGetIt.html). You can do it in Ubuntu 14.04 by running the following code in terminal:

```
sudo apt-get install g++
sudo apt-get install cython
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo pip install CoolProp
```

It took around a minute on my computer to compile and install the code. Then I found a reply about using `CoolProp` in Julia google group. I'm too lazy to find the link again, but basically this is what you need to do to run `CoolProp` in Julia.

```jl
Pkg.add("PyCall")
using PyCall
@pyimport CoolProp.CoolProp as CP
mu_w= CP.Props("V","T",273.15+22.0,"P",100,"H2O") # mu [Pa.s], T [K], P [kPa]
```

The code above gives you the viscosity of water at 295.15 K and 100 kPa. You can find more details about the [formulation](http://www.coolprop.org/EOS.html), `CoolProp` [module](http://www.coolprop.org/apidoc/CoolProp.html#module-CoolProp.CoolProp), and `State` [module](http://www.coolprop.org/apidoc/State.html) by consulting the [CoolProp documents](http://www.coolprop.org/apidoc/modules.html).
