import string

def main():
  alpha = input();

  if alpha in string.ascii_lowercase:
    print("a")
  else:
    print("A")

if __name__ == "__main__":
  main();