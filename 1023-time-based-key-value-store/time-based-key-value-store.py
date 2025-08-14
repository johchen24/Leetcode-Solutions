class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        left, right = 0, len(values) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            t = values[mid][0]
            if t == timestamp:
                return values[mid][1]
            elif t < timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res