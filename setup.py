from distutils.core import setup
setup(
  name = 'topsis_101917050',         
  packages = ['topsis_101917050'],   
  version = '0.1',      
  license='MIT',        
  description = 'Name :Harbir Singh RollNo :101917050 Group:3CSE2 Description :A simple python pakage for calculating topsis score',  
  author = 'Harbir Singh',                   
  author_email = 'harbir066@gmail.com',      
  url = 'https://github.com/Harbir66/topsis_101917050', 
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'ML',],   
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state 
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)