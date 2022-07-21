membership = "gold"
year = 4

if membership == "vip" and year > 4:
    print("이벤트 참여 가능")
elif membership == "gold" and year > 2:
    print("이벤트 참여 3시간 가능")
else :
    print("이벤트 참여 불가능")


