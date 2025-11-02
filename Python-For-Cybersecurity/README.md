# I did not write any of the scripts in this directory!!!

These scripts were provided to me as part of a specialization on Coursera called Python for Cybersecurity. 

The instructor was [Howard Poston](https://github.com/hposton) of the Infosec Institute. 

The repository associated with this specialization can be found here: [Python for Cybersecurity repo](https://github.com/hposton/python-for-cybersecurity)

Although I created a virtual environment with Python 3 to aid in dependency management, the interpreter threw a bunch of errors at me when I attempted to install libraries from the provided requirements.txt file (shown below).

On my machine, I was able to pinpoint a problem with the [libratom library](https://pypi.org/project/libratom/). The errors didn't appear until the installation of numpy as one of the required dependencies.

I spent several hours trying to resolve the errors, and was ultimately unsuccessful. So, your mileage may vary. I just decided to install the necessary libraries on an ad-hoc basis.

Howard's original README.md file is as follows:

# python-for-cybersecurity

This repository holds the Python scripts discussed in the Infosec Institute's Python for Cybersecurity Learning Path

These scripts are designed to run using Python 3. To use these scripts:

```
# Download repo
git clone https://github.com/hposton/python-for-cybersecurity

# Enter repo
cd python-for-cybersecurity

# Install requirements
python -m pip install -r requirements.txt
```

