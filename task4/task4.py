import sys


def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - median) # минимальное количество ходов
    return moves

def main():
    if len(sys.argv) != 2:
        print("usage: python3 task4.py numbers.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = []
    with open(file_path, 'r') as file:
        for line in file:
            nums.append(int(line))
    result = min_moves(nums)
    print(result)

main()
