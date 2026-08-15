import os

path = '/home/thinindu/Documents/BintaWedding/index.html'
with open(path, 'r') as f:
    content = f.read()

# 1. Update the actual hex values globally (this hits the SVGs and any hardcoded ones, although we mainly use CSS vars)
content = content.replace('#5c6b56', '#800020') # sage -> burgundy
content = content.replace('#8a9b7a', '#C9A9A6') # sage-light -> dusty rose
content = content.replace('#3d4a38', '#5a0016') # sage-dark -> dark burgundy
content = content.replace('#c4a07a', '#d6b8b5') # accent-rose -> light dusty rose

# 2. Rename the CSS variables
content = content.replace('--sage:', '--burgundy:')
content = content.replace('--sage-dark:', '--burgundy-dark:')
content = content.replace('--sage-light:', '--dusty-rose:')

content = content.replace('var(--sage)', 'var(--burgundy)')
content = content.replace('var(--sage-dark)', 'var(--burgundy-dark)')
content = content.replace('var(--sage-light)', 'var(--dusty-rose)')

with open(path, 'w') as f:
    f.write(content)

print("Colors updated successfully.")
