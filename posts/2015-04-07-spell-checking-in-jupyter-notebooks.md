<!--
.. title: Spell checking in Jupyter notebooks
.. slug: 2015-04-07-spell-checking-in-jupyter-notebooks
.. date: 2015-04-07 21:21:18 UTC+02:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

This afternoon I found a nice spellchecker for Jupyter markdown cells [here](http://calicoproject.org/ICalico). Here's the step by step procedure for the installation of the spellchecker and two other usefull tools:

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
