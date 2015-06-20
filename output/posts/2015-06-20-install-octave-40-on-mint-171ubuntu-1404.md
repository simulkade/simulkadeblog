<!-- 
.. title: Install Octave 4.0 on Mint 17.1/Ubuntu 14.04
.. slug: 2015-06-20-install-octave-40-on-mint-171ubuntu-1404
.. date: 2015-06-20 12:10:53 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

[Octave](http://www.gnu.org/software/octave/) version 4.0 is out, and the good news is that it has a `classdef` feature similar to Matlab. I will soon use it to update my [FVTool](https://github.com/simulkade/FVTool) so that it can be used with all functionalities in Octave as well.  
The problem is that it takes a while before the new version of Octave comes to the software center of Ubuntu. I decided to compile and build it, although I've never had a good experience with building tools from source. This time however it worked however without any issue on my laptop and my pc. I used the procedure I found [here](https://scivision.co/compiling-octave-4-0-on-ubuntu-14-04/). I had to install some more libraries on my Mint 17.1 operating system.  
First, install these dependencies:
```
sudo apt-get install gawk gfortran gperf flex libbison-dev libqhull-dev libglpk-dev libcurl4-gnutls-dev libfltk1.3-dev librsvg2-dev libqrupdate-dev libgl2ps-dev libosmesa6-dev libarpack2-dev libqscintilla2-dev libreadline-dev bison icontool llvm-dev libfftw3-dev libhdf5-serial-dev openjdk-7-jdk transfig  libgraphicsmagick++1-dev libsndfile1-dev
```

Then, download the [octave source code](ftp://ftp.gnu.org/gnu/octave/) for version 4.0.0 from [here](ftp://ftp.gnu.org/gnu/octave/octave-4.0.0.tar.gz), and extract it. Go to the new octave-4.0.0 forlder, and in a terminal window type
```
./configure --enable-jit
make
sudo make install
```

It takes a while, so go and pour a nice cup of coffee for yourself. If you get any error after running `./configure`, find the missing dependencies [here](http://wiki.octave.org/Octave_for_Debian_systems).  
If the installation is successful, run octave by typing `octave`. It should launch the user interface of octave which is enabled by default in this version.  
One other good news is that now you can run octave in a [Jupyter notebook](https://jupyter.org/), by installing [octave kernel](https://github.com/calysto/octave_kernel) and [oct2py](http://blink1073.github.io/oct2py/source/installation.html):
```
sudo pip install oct2py
sudo pip install octave_kernel
```

It is still not possible to use octave kernel. Go to `/usr/local/bin` and type
```
ls -la
```
You will see that `octave` is linked to the `octave-4.0.0`. You need to unlink `octave` and create a symbolic link to the octave command line interface or `octave-cli`. In the terminal window, type
```
sudo unlink octave
sudo ln -s /usr/local/bin/octave-cli octave
```

Now your octave kernel should start without any problem. Open a Jupyter notebook, and change the kernel to octave.

