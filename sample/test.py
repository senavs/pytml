from pyhtml.dtype.page import Page
from pyhtml.usable.tags import H1, H2, P, HR, BR, FIELDSET, FORM, BUTTON, INPUT, LABEL, META
from pyhtml.usable.components import BOOTSTRAP4, ORDERED_LIST, UNORDERED_LIST

with Page('index.html') as page:
    # charset
    page.register(META(charset='utf-8'))

    # bootstrap 4
    page.register(BOOTSTRAP4())

    # título
    page.register(H1('PyHTML'))

    # parágrafo
    page.register(P('Framework em python para criação de páginas HTML.', style='color: red;'))
    page.register(BR)
    page.register(HR)
    page.register(BR)

    # formulário
    page.register(H2('Formulário'))
    page.register(FIELDSET(FORM([LABEL('Usuário', for_='usuario'), BR,
                                 INPUT(id_='usuario', type='text'), BR,
                                 LABEL('Senha', for_='senha'), BR,
                                 INPUT(id_='senha', type='password'), BR,
                                 BUTTON('ENVIAR', type='submit')])))

    # componente
    page.register(ORDERED_LIST('item 1', 'item 2', 'item 3'))
    page.register(UNORDERED_LIST('item 1', 'item 2', 'item 3'))
