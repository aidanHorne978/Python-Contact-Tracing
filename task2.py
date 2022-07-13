
my_file = open("test.txt")
z_file = open("testz.txt")
f = my_file.readlines()
fz = z_file.readlines()
my_answer = []
z_answer = []
for line in f:
    my_answer.append(line.split())

for line in fz:
    z_answer.append(line.rstrip().split(", "))

my_answer = [j for sub in my_answer for j in sub]
z_answer = [j for sub in z_answer for j in sub]

z_answer = sorted(z_answer)
my_answer = sorted(my_answer)

correct = True

for line in z_answer:
    if line not in my_answer:
        correct = False

print(correct)