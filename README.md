# python-html
Create WEB HTML pages in Python

## About
Framework written in Python 3 to simplify the making of HTML files.

## Get Starting
Installing
```python
pip install pythml
```  

Simplest html page with pytml
```python
from pytml.essential.page import Page
from pytml.tags import *

with Page('./index.html') as page:
    page.register('head', META('utf-8'))
    page.register('head', TITLE('my first web page'))

    page.register('body', H1('Hello World!'))
```
