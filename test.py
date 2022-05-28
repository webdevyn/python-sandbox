places = ['paris', 'montreal', 'london', 'tokyo', 'amsterdam']
print(places)

print('\nThis is the list using sorted - in alpha order:')
print(sorted(places))

print('\nThis is the original list still in original order:')
print(places)

print('\nThis is list using sorted-reverse:')
print(sorted(places, reverse=True))

print('\nThis is the original list still in original order:')
print(places)

print('\nThis is the orig list in reverse order:')
places.reverse()
print(places)

print('\nThis is the prev list reversed:')
places.reverse()
print(places)

print('\nThis is the list sorted in alphabetical order:')
places.sort()
print(places)

print('\nThis is the prev list in reverse alphabetical order:')
places.sort(reverse=True)
print(places)