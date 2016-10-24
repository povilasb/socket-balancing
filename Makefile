python ?= python2.7
virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip


$(virtualenv_dir):
	virtualenv $@ -p $(python)
	$(pip) install -r requirements.txt
