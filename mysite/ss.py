import sys
def read_input()
    data = sys.stdin.readline()
    n,m = data[0].strip('\n').split(' ')
    sentence = data[1:n+1]
    query = data[n+1:]
    return n,m,sentence,query

def stat_sent(s,q):
    count = 0
    for i in set([k.upper() for k in q.split(' ')]):
        for j in set([l.upper() for l in s.split(' ')]):
            if i == j :
                count += 1
    return count

def get_res(n,m,sentence,query):
    res_dict = {}
    for i in query:
        res = []
        for j in sentence:
            res.append(stat_sent(j,i))
        res_dict[i] = sentence[res.index(max(res))]
    return '\n'.join(res_dict[k] for k in query)

if __name__ == '__main__':
    n = 5
    m = 2
    sentence = ['a,b,c,d,e','a,b,c,c,e','a,c','a,d','a,c,f']
    query = ['a,d,e','a,c,f']
    n,m,sentence,query = read_input()
    a = get_res(n,m,sentence,query)
    print a