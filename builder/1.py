text = 'hello'

parts = ['<p>', text, '</p>']

print(''.join(parts))

words = ['hello', 'world']

parts = ['<ul>']

for w in words:
    parts.append(f"\t<li>{w}</li>")

print('\n'.join(parts))
