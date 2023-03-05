import sys
import threading

def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    
    def height(node):
        if not tree[node]:
            return 1
        return 1 + max(height(child) for child in tree[node])
    
    return height(root)

def main():
    check = input()
    if "F" in check:
        filename = input().strip()
        with open("test/" + filename) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))

    elif "I" in check:
        n = int(input())
        parent = list(map(int, input().split()))
        print(compute_height(n, parent))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()