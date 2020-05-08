from ..dtypes.factory import BaseFactory

FORM = BaseFactory.create_body_tag_class('form', True)
INPUT = BaseFactory.create_body_tag_class('input', False)
TEXTAREA = BaseFactory.create_body_tag_class('textarea', True)
BUTTON = BaseFactory.create_body_tag_class('button', True)
SELECT = BaseFactory.create_body_tag_class('select', True)
OPTGROUP = BaseFactory.create_body_tag_class('optgroup', True)
OPTION = BaseFactory.create_body_tag_class('option', True)
LABEL = BaseFactory.create_body_tag_class('label', True)
FIELDSET = BaseFactory.create_body_tag_class('fieldset', True)
LEGEND = BaseFactory.create_body_tag_class('legend', True)
DATALIST = BaseFactory.create_body_tag_class('datalist', True)
OUTPUT = BaseFactory.create_body_tag_class('output', True)
