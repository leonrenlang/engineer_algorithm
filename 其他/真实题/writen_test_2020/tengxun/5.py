

def two_set_merge(lis1, lis2):
    set1, set2 = set(lis1),set(lis2)
    if set1.intersection(set2):
        return list(set1.union(set2))
    else:
        return []

relations = [[1,2],[3,4],[5,6],[1,6]]

for i in range(len(relations)):
    for j in range(i+1, len(relations)):
        res = two_set_merge(relations[i], relations[j])
        if res:
            new_relations.append(res)
        else:
            new_relations.append(relations[i])
            new_relations.append(relations[j])
print(new_relations)
exit()

for idx in range(1, len(relations)):
    union = two_set_merge(relations[idx], relations[idx-1])
    if union:
        new_relations.append(union)
    else:
        new_relations.append(relations[idx])
        new_relations.append(relations[idx-1])
print(new_relations)
print(set(new_relations))

