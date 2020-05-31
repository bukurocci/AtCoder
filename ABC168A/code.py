def main():
  N = int(input())

  d = N % 10

  hon = [2, 4, 5, 7, 9]
  pon = [0, 1, 6, 8]
  bon = [3]

  if(d in hon):
    print("hon")
  elif(d in pon):
    print("pon")
  elif(d in bon):
    print("bon")
  

if __name__ == "__main__":
  main()