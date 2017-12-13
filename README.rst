
Installation instructions to run jupyter server locally

Install python 2.7 - On Windows use Anaconda distribution

Create a virtualenv using > virtualenv py27

Activate virtualenv > source py27/bin/activate

Install requirements > py27/bin/pip install -r requirements.txt

Enable widgets > jupyter nbextension enable --py --sys-prefix widgetsnbextension

Start jupyter server > py27/bin/jupyter notebook
