def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

# for i in range(5):
#     print(ngrams("salut ça va je vais bien? \n salut ça va et toi ?", i))