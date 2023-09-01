monthnumber = int(input("Anna kuukauden numero: "))

season = ("talvi", "kevät", "kesä", "syksy",)

index = monthnumber // 3
if index == 4:
    index = 0
seasons = season[index]

print(f"Kuukausi {monthnumber} kuuluu vuodenaikaan {seasons}.")