from collections import deque, defaultdict
import bisect

class Packet:
    def __init__(self, s, d, t):
        self.source = s
        self.destination = d
        self.timestamp = t
    def __hash__(self):
        return hash((self.source, self.destination, self.timestamp))
    def __eq__(self, other):
        return (self.source, self.destination, self.timestamp) == (other.source, other.destination, other.timestamp)

class Router:
    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # holds Packet objects in insertion order
        self.unique = set()   # to detect duplicates
        self.dest_timestamps = defaultdict(list)  # dest -> list of timestamps
        self.processed_count = defaultdict(int)   # dest -> how many of that destination have been forwarded/removed

    def addPacket(self, source, destination, timestamp):
        pkt = Packet(source, destination, timestamp)
        if pkt in self.unique:
            return False
        # if capacity full, evict oldest
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()
        # add
        self.queue.append(pkt)
        self.unique.add(pkt)
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        pkt = self.queue.popleft()
        self.unique.remove(pkt)
        # record that one more has been removed for this destination
        self.processed_count[pkt.destination] += 1
        return [pkt.source, pkt.destination, pkt.timestamp]

    def getCount(self, destination, startTime, endTime):
        timestamps = self.dest_timestamps.get(destination, [])
        if not timestamps:
            return 0
        # skip all timestamps that correspond to forwarded/evicted packets
        start_index = self.processed_count.get(destination, 0)
        # find lower bound ≥ startTime starting from start_index
        lo = bisect.bisect_left(timestamps, startTime, lo=start_index)
        hi = bisect.bisect_right(timestamps, endTime, lo=start_index)
        return hi - lo


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)