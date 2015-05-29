<!-- 
.. title: All I need after a fresh installation of Linux Mint
.. slug: 2015-05-29-all-i-need-after-a-fresh-installation-of-linux-mint
.. date: 2015-05-29 14:02:11 UTC+02:00
.. tags: Linux Mint, Packages
.. category: Reminder
.. link: 
.. description: 
.. type: text
-->

I had some issues with my laptop, so I decided to re-install [linux mint/Mate](http://www.linuxmint.com/edition.php?id=174). This is the sequence of task for making my installation ready for work:

  1. Add `Persian` keyboard layout (start menu -> keyboard ->layouts -> add, and then in Options -> switching to another layout -> alt + shift)
  2. Install `adblock plus` add-on for Firefox
  3. Install latex:
```
sudo apt-get install texlive imagemagick texlive-bibtex-extra texlive-fonts-extra texlive-font-utils texlive-extra-utils texlive-formats-extra texlive-generic-extra texlive-latex-extra texlive-math-extra texlive-pictures texlive-pstricks texlive-publishers texlive-science
```
  4. Install the newest version of [lyx](http://www.lyx.org/):
```
sudo add-apt-repository ppa:lyx-devel/release
sudo apt-get update
sudo apt-get install lyx lyx-common dvipng psutils fonts-lyx elyxer tex4ht hevea tth latex2html
```
  5. Install [inkscape](https://inkscape.org)
```
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt-get install inkscape
```
  6. Install [CoolProp](http://www.simulkade.com/posts/Physical%20properties%20in%20Julia:%20CoolProp.html)
  7. Install [pydicom](http://www.pydicom.org/)
```
sudo pip install pydicom
```
  8. Install [ipython](http://ipython.org/install.html)
```
sudo pip install "ipython[all]"
```
  9. Install [Julia](http://julialang.org/downloads/platform.html)
```
sudo add-apt-repository ppa:staticfloat/juliareleases
sudo add-apt-repository ppa:staticfloat/julia-deps
sudo apt-get update
sudo apt-get install julia
```
  10. Install [matplotlib](http://matplotlib.org/) and [scipy](http://www.scipy.org/)
```
sudo apt-get install python-matplotlib python-scipy python-tk
```
  11. Install [mayavi2](http://code.enthought.com/projects/mayavi/) for 3D visualization
```
sudo apt-get install mayavi2
```
  12. Do this at the beginning: install some compilers:
```
sudo apt-get install build-essential gfortran pkg-config
```
I need them to install [Ipopt](https://projects.coin-or.org/Ipopt)
  13. Install [google chrome](https://www.google.com/intl/en/chrome/browser/desktop/)
  14. Install [Nikola](https://getnikola.com/)
```
sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev python-dev
sudo pip install webassets
sudo pip install ghp-import
sudo pip install markdown
sudo pip install nikola
sudo pip install nikola[extras]
```
  15. Install [dropbox](https://www.dropbox.com/install?os=lnx)
  16. Install some dependencies for linking Matlab to other packages
```
sudo apt-get install csh gcc-4.7 g++-4.7 gfortran-4.7
```
  17. Install and configure [git](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
```
sudo apt-get install git
git config --global user.name "Your Name"
git config --global user.email youremail@something.com
```
  18. Install [Matlab](http://nl.mathworks.com/products/matlab/); I still have a license to do so. Otherwise, install `Octave`
  19. Install [Pinta](http://en.wikipedia.org/wiki/Pinta_%28software%29) for working with images, much easier than `GIMP`
```
sudo apt-get install pinta
```

I have perhaps missed one thing or two here, but this is basically all I need to have my laptop ready.
