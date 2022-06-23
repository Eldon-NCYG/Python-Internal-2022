def input_size():
  global size
  sizes = ["xs", "s", "m", "l", "xl"]
  size = input("Size (XS, S, M L, XL): ")
  size = size.lower().strip()
\
  if size not in sizes:
    print("Please input a valid size.")
    input_size()
  else:
    pass

input_size()
print(size)