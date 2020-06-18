# pyhtml

## Sobre
Framework em python para criação de páginas HTML.

## Participantes
- Matheus Sena Vasconcelos
- Thiago Oliveira Costa
- Ygor Oliveira Gonçalves

## Gráfico de Burndown e Burnup

<img src="https://github.com/senavs/py-html/blob/master/images/graph-brundown.png">
<img src="https://github.com/senavs/py-html/blob/master/images/graph-brunup.png">

## Criando uma página HTML
Primeiramente é necessário importar as tags que serão usadas. Elas podem ser encontrada em `pyhtml.usable.tags`. 
Para renderizar essas tags em uma página, a classe Page será utilizada `pyhtml.dtype.page`.
Componentes estão armazenados em `pyhtml.usable.components`

- Imports
```python
from pyhtml.dtype.page import Page
from pyhtml.usable.tags import H1, DIV, P, HR, BR, FORM, INPUT, LABEL, META
from pyhtml.usable.components import BOOTSTRAP4, ORDERED_LIST, UNORDERED_LIST
```

- Página
```python
with Page('./index.html') as page:
    pass
```

- Título e charset
```python
with Page('./index.html') as page:
    page.register(META(charset='utf-8'))
    
    page.register(H1('PyHTML'))
```

- Parágrafo e quebra de linha
```python
with Page('./index.html') as page:
    page.register(P('Framework em python para criação de páginas HTML.', style='color: red;'))
    page.register(BR)
    page.register(HR)
    page.register(BR)
```

- Formulário
```python
with Page('./index.html') as page:
    page.register(H2('Formulário'))
    page.register(FIELDSET(FORM([LABEL('Usuário', for_='usuario'), BR,
                                 INPUT(id_='usuario', type='text'), BR,
                                 LABEL('Senha', for_='senha'), BR,
                                 INPUT(id_='senha', type='password'), BR,
                                 BUTTON('ENVIAR', type='submit')])))
```

- Componentes
```python
with Page('./index.html') as page:
   page.register(BOOTSTRAP4())
   
    page.register(ORDERED_LIST('item 1', 'item 2', 'item 3'))
    
    page.register(UNORDERED_LIST('item 1', 'item 2', 'item 3'))
```

Diversas tags em `pyhtml.usable.tags` para você criar suas telas
