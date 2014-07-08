# -*- coding: cp1252 -*-
from TwitterAPI import TwitterAPI
import json
api = TwitterAPI('vdNxskxaSxEFaVMdANwQ','C4gcR5ErIdg783ZWQ51TyFuWrb7cxIkPOmIqltlg','18886261-eo39zC2ROMDmUfzd5ZOUjoEiZWkZH7IfdCn2hMCn9','KtfBkiiqW2EsmdQ145ukcuvzwlHSxmCz4cCl8rDYfS6lA')
l =api.request('trends/place', {'id':'1'})

#for item in r.get_iterator():
#    fout.write(r.text+'\n')
trend=l.text
jt=json.loads(trend)
#s= str(jt[0][u'trends'][0][u'name'])
s='infocept'
print s

r=api.request('search/tweets', {'q':'from:aceankit','lang':'en','count':'1','result_type':'recent'})
fout=open('output.txt','w')
fout_formatted=open('output_formatted.txt','w')
fout.write(r.text+'\n')
fout.close()
s=r.text
j=json.loads(s)
i=0
while(i<25):
    ut=j['statuses'][i][u'text']
    ul= j['statuses'][i][u'user'][u'location']
    utz=j['statuses'][i][u'user'][u'time_zone']
    #print ul

    print str(i)+'\t'+ut+'\t'+str(utz)+'\t'+unicode(ul)
    s=str(i)+'\t'+(ut)+('\t')+unicode(utz)+('\t')+unicode(ul)+('\n')
    fout_formatted.write(s.encode('UTF-8'))
    i=i+1
    
fout_formatted.close()
#js=json.loads(st)


   
