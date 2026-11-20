def solution(nums):
    n = len(nums) //2
    pokemon = dict()
    poke_type = set()

    for num in nums:
        pokemon[num] = pokemon.get(num,0)+1
        poke_type.add(num)
    if n <= len(poke_type):
        return n
    else:
        return len(poke_type)
