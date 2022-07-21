name = "Byungchan"
print(name) # Byungchan을 출력 
print(name.lower()) # 전부다 소문자로 출력 
print(name.upper()) # 전부다 대문자로 출력 
print(name[0].isupper()) # B가 대문자 인가? ture
print(name[0].islower()) # B가 소문자 인가? fasle
print(len(name)) # name의 문자 길이를 구함 
print(name.replace("Byung" , "U")) # 문자열의 Byung를 U로 바꿈 

index = name.index("n") # n의 위치를 찾음 
print(index)
index = name.index("n" , index + 1) # 다음 n의 위치를 찾음 
print(index)

print(name.find("Hi")) # n의 위치를 찾음, 차이점은 찾는 문자가 없으면 -1을 출력 

print(name.count("n")) # n의 갯수를 카운트

