import json

f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-16')

outfile.write('id\tretweet_count\ttext\tlang\n')

output = []

cnt = 0

for line in con:
    cnt+=1
    if (len(line)<=5): continue
    
    obj = json.loads(line.replace('\n',''))

    try:
        id = obj.get('retweeted_status').get('id_str')

    except:
        continue
    try:
        text = obj.get('retweeted_status').get('text')
        text = text.replace('\t', '').replace('\n', '')
        language = obj.get('lang')


        

    except:
        continue
    try:
        retweet_count = obj.get('retweeted_status').get('retweet_count')
    except:
        continue

    if id not in output:
        output.append(id)
        outfile.write(id+'\t'+str(retweet_count)+'\t'+text+'\t'+str(language)+'\n')
#    if (cnt>1500): break

print('done.')
