from Queue import Queue

def search_substring_with_queue(a,b):
    q = Queue()

    for el in a:
        q.enqueue(el)

    for el in b:
        if q.peek() == el:
            q.dequeue()

    return q.size()==0


print(search_substring_with_queue('uio', 'quefio'))
