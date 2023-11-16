def generate_order(projects, dependencies):
    tree = {}
    for p in projects:
        tree[p] = set()
    order = []
    copy = set(projects)
    for x in dependencies:
        tree[x[1]] = x[0]
    while copy:
        for x in list(copy):
            dependency = tree[x]
            if not copy.intersection(dependency):
                order.append(x)
                copy.remove(x)
        if len(order) == 0:
            raise "Error"
    return order
        

if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [['a', 'd'], ['f', 'b'], ['b','d'], ['f', 'a'], ['d', 'c']]
    print(generate_order(projects, dependencies))