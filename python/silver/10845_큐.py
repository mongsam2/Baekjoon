import sys

input = sys.stdin.readline
write = sys.stdout.write

class Que:
    lst = []
    size = 0
    def command(self, comm, x):
        if comm == "push":
            self.lst.append(x)
            self.size += 1
            return
        elif comm == "pop":
            if self.size == 0:
                print(-1)
                return
            print(self.lst.pop(0))
            self.size -= 1
            return
        elif comm == "size":
            print(self.size)
            return
        elif comm == "empty":
            if self.size == 0:
                print(1)
            else:
                print(0)
            return
        elif comm == "front":
            if self.size == 0:
                print(-1)
                return
            print(self.lst[0])
            return
        elif comm == "back":
            if self.size == 0:
                print(-1)
                return
            print(self.lst[-1])
            return
        
n = int(input())
q = Que()
for _ in range(n):
    line = input().split()
    comm = ""
    x = 0
    comm = line[0]
    if len(line) == 2:
        x = line[1]
    q.command(comm, x)