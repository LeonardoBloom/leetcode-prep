
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
repo2 = ["abbS", "abc", "Abs", "bcs", "bdsa", "cdde", "rgb", "yjmm", "xxmm", "zeee"]
repo3 = ["Abcd", "defr", "zxwd", "rdfvlk", "abc", "abcder", "abccc", "oinadskal", "ksnfls", "abccccdd"]
repo4 = ["abcd", "njsafhsT", "isandabWBB", "hsfnKR", "aBbxkj", "YUGBJK", "NIUHNNN", "nkjndYB", "Abccd", "ABCDE"]
repo5 = ["abcd", "njsafhsT", "isandabWBB", "hsfnKR", "aBbxkj", "YUGBJK", "NIUHNNN", "nkjndYB", "Abccd", "ABCDE"]
customerQuery = "mouse"
cq1 = "abbs"
cq2 = "abcd"
cq3 = "AB"

"""
output max 3
alphabetical sort
all lowercase( case insensitive)

Input:
    m
    mo
    mou
    mous
    mouse

"""

def amazon(repository, customerQuery):

    returnArray = []

    print("query: ", customerQuery)
    for x in repository: # o(n)
        if customerQuery.lower() == x[:len(customerQuery)].lower():
            returnArray.append(x.lower())
    returnArray.sort()

    if len(customerQuery) >= 2:
        return returnArray[:3]

while True:
    print("Type into the keyboard bro:")
    keyword = input()
    if keyword == 'q':
        break
    else:
        print(amazon(repo2, keyword))
        




    