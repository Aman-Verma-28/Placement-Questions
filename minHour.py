def minNumberOfHours( initialEnergy, initialExperience, energy, experience):
    ans = 0
    total = sum(energy)
    ans+=max(total-initialEnergy+1,0)
    for i in experience:
        if i>=initialExperience:
            ans+=i-initialExperience+1
            initialExperience = i+1+i
        else:
            initialExperience += i
    return ans

print(minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))
print(minNumberOfHours(initialEnergy = 1, initialExperience = 4, energy = [1], experience = [3]))