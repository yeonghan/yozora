# yozora Project

### pyenv

* project: https://github.com/pyenv/pyenv
* installation
	```
	$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

	// bash: .bashrc or .bash_profile
	// omyzsh: .zshenv
	$ export RCFILE="~/.zshenv"
	$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $RCFILE
	$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $RCFILE
	$ echo -e 'if command -v pyenv 1>/dev/null 2>$1; then\n eval "$(pyenv init -)"\nfi' >> $RCFILE
	```
### python3.8

* installation
	```
	$ pyenv install -l
	...
	$ pyenv install 3.8.1
	$ pyenv versions
	* system (set by /home/----/.pyenv/version)
	  3.8.1
	$ pyenv global 3.8.1
	$ pyenv rehash
	$ pyenv versions
	  system (set by /home/----/.pyenv/version)
	* 3.8.1
	$ python --version
	Python 3.8.1
	```
