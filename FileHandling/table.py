
for i in range(3, 21):
    with open(f"Tables/Multiplication_table of_{i}.txt", 'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
            if j!=10:
                f.write("\n")
