prefix = ' '
# text = '123drakeet'
text = '123 xiaoyuebot'

m = 'xiaoyuebot'
if (prefix + m) in text:
    text = text.replace(m, '@xiaoyuebot' + ' ')
else:
    text = text.replace(m, prefix + '@xiaoyuebot' + ' ')

print(text)
