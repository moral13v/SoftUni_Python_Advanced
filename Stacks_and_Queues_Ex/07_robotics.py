from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


robots_data = input().split(";")
process_time_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split("-")
    process_time_by_robot[name] = int(process_time)

time = convert_str_to_seconds(input())
items = deque()