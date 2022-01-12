# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class MinHeap():
    data = []
    n = 0

    def __init__(self,input_array):
        self.n = len(input_array)
        self.data = [list(a) for a in zip(input_array,range(self.n))]
        for i in range(self.n//2-1, -1, -1):
            self.sift_down(i)
    
    @staticmethod
    def parent(i):
        return (i-1)//2

    @staticmethod
    def left_child(i):
        return 2*i+1

    @staticmethod
    def right_child(i):
        return 2*i+2

    def sift_up(self,i):  #min-heap sift up
        while i > 0 and \
                        ( self.data[self.parent(i)][0] > self.data[i][0] or \
                          ( self.data[self.parent(i)][0] == self.data[i][0] and self.data[self.parent(i)][1] > self.data[i][1] ) ):
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def sift_down(self,i):  # min-heap sift down
        minix = i
        lix = self.left_child(i)
        if lix <= self.n-1 and \
                               ( self.data[lix][0] < self.data[minix][0] or \
                                 ( self.data[lix][0] == self.data[minix][0] and self.data[lix][1] < self.data[minix][1] ) ):
            minix = lix
        rix = self.right_child(i)
        if rix <= self.n-1 and \
                               ( self.data[rix][0] < self.data[minix][0] or \
                                 ( self.data[rix][0] == self.data[minix][0] and self.data[rix][1] < self.data[minix][1] ) ):
            minix = rix
        if i != minix:
            self.data[i], self.data[minix] = self.data[minix], self.data[i]
            self.sift_down(minix)

    def change_priority(self,i,p):
        oldp,procid = self.data[i]
        self.data[i][0] = p
        if p < oldp:
            self.sift_up(i)
        else:
            self.sift_down(i)
        return procid,oldp
            

def naive_assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def assign_jobs(n_workers, jobs):
    result = [(i,0) for i in range(min(n_workers,len(jobs)))]
    parpro = MinHeap(jobs[:n_workers])
    n_processed = n_workers
    for job in jobs[n_processed:]:
        result.append(parpro.change_priority(0,job+parpro.data[0][0]))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    #assigned_jobs = naive_assign_jobs(n_workers, jobs)
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
