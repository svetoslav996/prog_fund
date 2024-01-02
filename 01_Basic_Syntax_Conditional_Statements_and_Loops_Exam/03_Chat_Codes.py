n = int(input())

for _ in range(n):
  message_number = int(input())

  if message_number == 88:
    print("Hello")
  elif message_number == 86:
    print("How are you?")
  elif message_number < 88:
    print("GREAT!")
  elif message_number > 88:
    print("Bye.")