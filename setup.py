from setuptools import setup

setup(name='PySideFlask',
      version='2.0',
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      long_description_content_type = 'text/markdown',
      description='Create desktop application by using Flask and QtWebEngine',
      url="https://github.com/MadsAndreasen/PySideFlask",
      author='Mads Andreasen',
      author_email='app@andreasen.cc',
      license='MIT',
      install_requires=[
          'flask',
          'pyside2',
      ],
      packages=['pysideflask'],
      zip_safe=False,
      keywords = ['​GUI​', '​Flask​', 'Qt', 'webview'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
      ],
      python_requires='>=3',
      )
