user_input = set(input())
numbers = set('0123456789')
result = user_input.intersection(numbers)
print(['No', ' '.join(sorted(result))][len(result) > 0])