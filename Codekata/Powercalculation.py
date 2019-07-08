def expo(x, y):
  a = x**y
  return a
n, k = map(int, input().split())
print(expo(n, k))
