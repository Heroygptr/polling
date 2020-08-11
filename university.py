responses={}
polling_active=True
while polling_active:
 name=input("\nWhat is your name?")
 response=input("Which university do you prefer?")
 responses[name]=response
 repeat=input("Would you like to let another person respond?(yes/no)")
 if repeat=='no':
  polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
 print(name+" prefer "+response+".")
