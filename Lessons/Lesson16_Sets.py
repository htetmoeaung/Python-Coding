# Sets = collection which is unordered, unindexed. No duplicate values

utensils = {'fork','spoon','knife','knife','knife'}
dishes = {'bowl','plate','cup','knife'}

utensils.add('napkin')
utensils.remove('fork')
# utensils.clear()
# dishes.update(utensils)

# dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(dishes.intersection(utensils))


for e in utensils:
    print(e)