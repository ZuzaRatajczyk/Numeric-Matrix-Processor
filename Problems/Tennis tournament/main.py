num_of_lines = int(input())
list_of_scores = []
for _ in range(num_of_lines):
    list_of_scores.append(input().split())
winners = [data[0] for data in list_of_scores if data[1] == "win"]
print(winners)
print(len(winners))
