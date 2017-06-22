from tempy import H1, H2, H3, Content, Div, P

t = Div()(P()(Content('n')), P()(Content('l')))

x = H1()(H2()(H3()(Content('test', template=t))))
x.inject({'test': [{'n': 1, 'l': 'a'}, {'n': 2, 'l': 'b'}, {'n': 3, 'l': 'c'}]})
print(x.render())
