# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        current_time = request.arrived_at
        req_tp = request.time_to_process

        #flush finished packets from queue
        while self.finish_time and self.finish_time[0] <= current_time:
            self.finish_time.popleft()

        #queue is full
        if len(self.finish_time) >= self.size:
            return Response(True, -1)

        #queue is empty
        if not self.finish_time:
            self.finish_time.append(current_time + req_tp)
            return Response(False, current_time)

        #queue neither empty nor full
        self.finish_time.append(self.finish_time[-1]+req_tp)
        return Response(False,self.finish_time[-2])

def process_requests(requests, buffer):
    responses = []
    for ix,request in enumerate(requests):
        responses.append(buffer.process(request))
    return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    if n_requests > 0:
        buffer = Buffer(buffer_size)
        responses = process_requests(requests, buffer)

        for response in responses:
            print(response.started_at if not response.was_dropped else -1)

def test_main():
    for i in range(1,21):
        with open('tests/{:02}'.format(i),'r') as tf, open('tests/{:02}.a'.format(i),'r') as af:
            print('test {}'.format(i))
            buffer_size, n_requests = map(int, tf.readline().split())
            requests = []
            for _ in range(n_requests):
                arrived_at, time_to_process = map(int, tf.readline().split())
                requests.append(Request(arrived_at, time_to_process))

            if n_requests > 0:
                buffer = Buffer(buffer_size)
                responses = process_requests(requests, buffer)

                for response in responses:
                    result = response.started_at if not response.was_dropped else -1
                    assert str(result) == af.readline().strip()


if __name__ == "__main__":
    main()
    #test_main()
