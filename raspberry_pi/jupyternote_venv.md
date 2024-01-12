## Virtual Enviroments for Jupyter Notebooks
These instructions are for setting a virtual enviroment for a jupyter notebook in VS Code.

- Create and activate a new venv

    ```
    python3 -m venv projectname
    source projectname/bin/activate
    ```

- Install ipykernal and a new kernel

    ```
    pip install ipykernel
    python3 -m ipykernel install --user --name=projectname
    conda install jupyter #
    ```


- the conda version 
- conda create -n my_env python=3.9
- oor conda create -p /Users/rafe/path/to_project/env
- conda activate /Users/rafe/full/abs/path/to/my_env
- conda install --file requirements.txt
- conda install -c ipykernel jupyter

conda install -c conda-forge jupyter notebook

- Now all we need to do is restart vs code and select your new kernel (`Ctrl + Shift + P`)
    ```
    >Reload Window
    ```


### Resourse

- [stackoverflow](https://stackoverflow.com/questions/58119823/jupyter-notebooks-in-visual-studio-code-does-not-use-the-active-virtual-environm)
- [Using jupyter notebooks with a virtual env](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/)
