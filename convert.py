import json


def Readlines(f):
    while True:
        line = f.readline()
        if line == "":
            return
        else:
            yield line

def main():
    outf = open("", 'w', encoding = 'utf-8')
    with open("", 'r', encoding='utf-8') as f:
        batch_size = 128
        i = 0
        Q = {}
        for line in Readlines(f):
            js = json.loads(line)
            if i == 0:
                Q['question'] = js['title']
                Q['answers'] = ['']
                tmp = []
                for j in range(len(js['references'])):
                    ctx = {'title': js['references'][j]['title'], 'text': js['references'][j]['text']}
                    tmp.append(ctx)
                Q['positive_ctxs'] = tmp
            else:
                tmp = []
                for j in range(len(js['references'])):
                    ctx = {'title': js['references'][j]['title'], 'text': js['references'][j]['text']}
                    tmp.append(ctx)
                if not 'negative_ctxs' in Q:
                    Q['negative_ctxs'] = []
                Q['negative_ctxs'] += tmp

            i += 1
            if i >= batch_size:
                i = 0
                outf.write(json.dumps(Q) + '\n')
                Q = {}
                
    outf.close()

if __name__ == "__main__":
    main()
    
