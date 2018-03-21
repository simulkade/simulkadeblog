<!--
.. title: Spell checking in Jupyter notebooks
.. slug: 2015-04-07-spell-checking-in-jupyter-notebooks
.. date: 2015-04-07 21:21:18 UTC+02:00
.. tags: jupyter, spellchecker
.. category:
.. link:
.. description:
.. type: text
-->

# UPDATE
The original post (see below) is terribly out of date now with broken links and deprecated procedures. To install spell checker for Jupyter, go to [this link](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) and follow the procedure.  
Alternatively, you can install the Calico extensions that are now maintained [here](https://github.com/Calysto/notebook-extensions). Open a terminal window and write:

```
git clone https://github.com/Calysto/notebook-extensions.git
cd notebook-extensions
jupyter nbextension install calysto --user
jupyter nbextension enable calysto/spell-check/main

```

# Deprecated!!!

This afternoon I found a nice spellchecker for Jupyter markdown cells [BROKEN LINK](). Here's the step by step procedure for the installation of the spellchecker and two other usefull tools:

  * Open a terminal window and type
```
sudo ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-spell-check-1.0.zip
sudo ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-document-tools-1.0.zip
sudo ipython install-nbextension https://bitbucket.org/ipre/calico/downloads/calico-cell-tools-1.0.zip
```
  * Go to `~/.ipython/profile_default/static/custom`, and add the following line to the end of `custom.js`.

```
IPython.load_extensions('calico-spell-check', 'calico-document-tools', 'calico-cell-tools');
```

  * Start a new `ipython notebook`. If everything goes well, you should see the following addition to the toolbar:

![ipython spellcheck toolbar](/ipython_toolbar_screenshot.png)

## Update (thanks to Henry Schreiner)
In Jupyter, instead of adding the load_extension line, you can run the following code in a notebook cell:

```
%%javascript
Jupyter.notebook.config.update({"load_extensions":{"calico-spell-check":true,
                                                  "calico-document-tools":true,
                                                  "calico-cell-tools":true}})
```

## Update II (thanks to Noam Elfanbaum)
Run the following in a terminal:

```
jupyter nbextension enable calico-spell-check
```
