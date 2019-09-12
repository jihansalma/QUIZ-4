ListGPA = [2.1, 2.5, 4, 3]

def Reward (GPA):
    Bonus = 500000
    Reward = GPA * Bonus
    return Reward

for GPA in ListGPA:
    if GPA > 2.5:
        print('Total Bonus anda adalah : Rp ', Reward (GPA))
    else:
        print('Maaf')