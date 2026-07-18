class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ''
        print(self.times)
        n = -1
        while n >= -len(self.times[key]):
            time, value = self.times[key][n]
            if time <= timestamp:
                return value
            n -= 1
        return ''
        
        
